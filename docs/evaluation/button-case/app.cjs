const {attachPress} = require('./press.cjs');
function mount(document) {
  for (const element of document.querySelectorAll('button')) attachPress(element);
  document.querySelector('#refresh').addEventListener('click', () => {
    document.querySelector('#count').textContent =
      String(Number(document.querySelector('#count').textContent) + 1);
  });
  document.querySelector('#amount').addEventListener('input', event => {
    document.querySelector('#value').textContent = event.target.value;
  });
}
module.exports = {mount};
