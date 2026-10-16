#!/usr/bin/env node
// Bounded checks of actual upstream excerpts; no browser/Flutter-runtime claim.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const root = path.resolve(__dirname, '../docs/examples');
const manifest = JSON.parse(fs.readFileSync(path.join(root, 'public-provenance.json')));
for (const c of manifest.cases) {
  for (const side of ['before', 'after']) {
    const data = fs.readFileSync(path.join(root, `${c.id}.${side}.txt`));
    assert.equal(crypto.createHash('sha256').update(data).digest('hex'), c[`${side}_excerpt_sha256`]);
  }
}
const text = (id, side) => fs.readFileSync(path.join(root, `${id}.${side}.txt`), 'utf8');
function compare(id, check, expectedBeforeFailures) {
  for (const side of ['before', 'after']) {
    const results = check(text(id, side));
    const failed = results.filter(x => !x).length;
    assert.equal(failed, side === 'before' ? expectedBeforeFailures : 0, `${id}/${side}`);
    console.log(`${id}/${side}: ${results.length - failed}/${results.length} checks; ${failed} failures`);
  }
}
compare('press-capture', code => [true, false, undefined, 'no-release'].map(state => {
  const calls = [];
  const target = {};
  if (state !== 'no-release') target.releasePointerCapture = id => calls.push(id);
  if (typeof state === 'boolean') target.hasPointerCapture = () => state;
  // Only erase the TypeScript assertion; keep the excerpt's control flow intact.
  vm.runInNewContext(code.replace('(target as Element)', 'target'), {target, e: {pointerId: 17}});
  const expected = state === true || state === undefined ? [17] : [];
  return JSON.stringify(calls) === JSON.stringify(expected);
}), 1);
compare('slider-commit', code => [
  {prev: [105, 107], next: [105, 105], index: 0, commits: 1},
  {prev: [105, 107], next: [105, 108], index: 1, commits: 1},
  {prev: [105, 107], next: [105, 107], index: 1, commits: 0},
  {prev: [105, 107], next: [104, 107], index: 0, commits: 1},
].map(c => {
  const calls = [];
  vm.runInNewContext(code + '\nhandleSlideEnd();', {
    valuesBeforeSlideStartRef: {current: c.prev}, valueIndexToChangeRef: {current: c.index},
    values: c.next, onValueCommit: values => calls.push(values)
  });
  return calls.length === c.commits && calls.every(values => values === c.next);
}), 1);
compare('navigation-theme', code => ['selectedState', 'unselectedState', 'disabledState'].map(state => {
  const expression = code.split(';').find(s => s.includes(`navigationBarTheme.labelTextStyle?.resolve(${state})`));
  assert.ok(expression, `missing theme branch: ${state}`);
  const widget = expression.indexOf(`info.labelTextStyle?.resolve(${state})`);
  const theme = expression.indexOf(`navigationBarTheme.labelTextStyle?.resolve(${state})`);
  const fallback = expression.indexOf(`defaults.labelTextStyle!.resolve(${state})`);
  return widget >= 0 && widget < theme && theme < fallback;
}), 3);
console.log('PASS: excerpt fingerprints, 8 JS contract cases and 3 static Dart precedence checks; not full upstream suites.');
