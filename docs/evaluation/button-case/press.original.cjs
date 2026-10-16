function attachPress(element) {
  element.addEventListener('pointerdown', event => {
    if (event.button === 0 && !element.disabled) element.dataset.pressed = 'true';
  });
  element.addEventListener('pointerup', () => { delete element.dataset.pressed; });
}
module.exports = {attachPress};
