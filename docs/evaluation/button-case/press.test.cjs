const test = require('node:test');
const assert = require('node:assert/strict');
const {attachPress} = require('./press.cjs');
const {mount} = require('./app.cjs');

class Target extends EventTarget {
  constructor() { super(); this.listeners = new Map(); }
  addEventListener(type, callback, options) {
    super.addEventListener(type, callback, options);
    const key = `${type}/${options === true || options?.capture === true}`;
    if (!this.listeners.has(key)) this.listeners.set(key, new Set());
    this.listeners.get(key).add(callback);
  }
  removeEventListener(type, callback, options) {
    super.removeEventListener(type, callback, options);
    this.listeners.get(`${type}/${options === true || options?.capture === true}`)?.delete(callback);
  }
  listenerCount() { return [...this.listeners.values()].reduce((sum, callbacks) => sum + callbacks.size, 0); }
  emit(type, properties = {}) {
    const event = new Event(type);
    Object.assign(event, properties);
    this.dispatchEvent(event);
  }
}

function fixture() {
  const observers = new Set();
  const window = new Target();
  window.MutationObserver = class {
    constructor(callback) { this.callback = callback; }
    observe() { observers.add(this); }
    disconnect() { observers.delete(this); }
  };
  const document = new Target();
  document.defaultView = window;
  document.hidden = false;
  function button() {
    const element = new Target();
    Object.assign(element, {ownerDocument: document, dataset: {}, disabled: false, isConnected: true});
    element.setPointerCapture = () => assert.fail('preserve native button click targeting');
    return element;
  }
  return {
    document, window, button,
    mutate() { for (const observer of [...observers]) observer.callback(); },
    observerCount() { return observers.size; }
  };
}

function down(element, pointerId = 1, extra = {}) {
  element.emit('pointerdown', {button: 0, pointerId, isPrimary: true, ...extra});
}

for (const interruption of ['pointerup', 'pointercancel', 'lostpointercapture', 'document exit', 'element blur', 'window blur', 'pagehide', 'hidden', 'disabled', 'removed', 'dispose']) {
  test(`press resets and releases resources after ${interruption}`, () => {
    const f = fixture();
    const element = f.button();
    const dispose = attachPress(element);
    let clicks = 0;
    element.addEventListener('click', () => clicks++);
    down(element);
    assert.equal(element.dataset.pressed, 'true');
    if (interruption === 'pointerup' || interruption === 'pointercancel') f.document.emit(interruption, {pointerId: 1});
    if (interruption === 'lostpointercapture') element.emit(interruption, {pointerId: 1});
    if (interruption === 'document exit') f.document.emit('pointerout', {pointerId: 1, relatedTarget: null});
    if (interruption === 'element blur') element.emit('blur');
    if (interruption === 'window blur') f.window.emit('blur');
    if (interruption === 'pagehide') f.window.emit('pagehide');
    if (interruption === 'hidden') { f.document.hidden = true; f.document.emit('visibilitychange'); }
    if (interruption === 'disabled') { element.disabled = true; f.mutate(); element.disabled = false; }
    if (interruption === 'removed') { element.isConnected = false; f.mutate(); element.isConnected = true; }
    if (interruption === 'dispose') dispose();
    assert.equal(element.dataset.pressed, undefined);
    assert.equal(f.observerCount(), 0);
    assert.equal(f.document.listenerCount(), 0);
    assert.equal(f.window.listenerCount(), 0);
    assert.equal(clicks, 0, 'cleanup must not activate the action');
    down(element, 2);
    assert.equal(element.dataset.pressed, interruption === 'dispose' ? undefined : 'true');
    dispose();
  });
}

test('unrelated and non-primary pointers cannot change the active press', () => {
  const f = fixture();
  const element = f.button();
  const dispose = attachPress(element);
  down(element, 1, {button: 2});
  down(element, 1, {isPrimary: false});
  element.disabled = true;
  down(element);
  assert.equal(element.dataset.pressed, undefined);
  element.disabled = false;
  down(element);
  down(element, 2);
  f.document.emit('pointerup', {pointerId: 2});
  f.document.emit('pointerout', {pointerId: 2, relatedTarget: null});
  f.document.emit('pointerout', {pointerId: 1, relatedTarget: f.button()});
  element.emit('lostpointercapture', {pointerId: 2});
  assert.equal(element.dataset.pressed, 'true');
  f.document.emit('pointerup', {pointerId: 1});
  assert.equal(element.dataset.pressed, undefined);
  dispose();
});

test('outside release resets without taking pointer capture', () => {
  const f = fixture();
  const element = f.button();
  const dispose = attachPress(element);
  down(element);
  f.document.emit('pointerup', {pointerId: 1});
  assert.equal(element.dataset.pressed, undefined);
  dispose();
});

test('all mounted buttons recover independently; native click and range input retain their behavior', () => {
  const f = fixture();
  const refresh = f.button();
  const archive = f.button();
  const amount = new Target();
  const count = {textContent: '0'};
  const value = {textContent: '25'};
  const elements = {'#refresh': refresh, '#archive': archive, '#count': count, '#amount': amount, '#value': value};
  f.document.querySelectorAll = selector => { assert.equal(selector, 'button'); return [refresh, archive]; };
  f.document.querySelector = selector => elements[selector];
  mount(f.document);
  for (let i = 0; i < 5; i++) {
    down(refresh, i + 1);
    f.document.emit('pointercancel', {pointerId: i + 1});
    assert.equal(refresh.dataset.pressed, undefined);
  }
  assert.equal(count.textContent, '0');
  down(refresh, 10);
  down(archive, 11);
  f.document.emit('pointerup', {pointerId: 10});
  assert.equal(refresh.dataset.pressed, undefined);
  assert.equal(archive.dataset.pressed, 'true');
  refresh.emit('click');
  assert.equal(count.textContent, '1');
  refresh.emit('click');
  assert.equal(count.textContent, '2', 'keyboard/native click remains the sole action path');
  f.document.emit('pointercancel', {pointerId: 11});
  assert.equal(archive.dataset.pressed, undefined);
  amount.value = '73';
  amount.emit('input');
  assert.equal(value.textContent, '73');
});
