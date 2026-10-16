function attachPress(element) {
  const document = element.ownerDocument;
  const window = document.defaultView;
  let pointerId = null;
  let observer;

  function reset() {
    pointerId = null;
    delete element.dataset.pressed;
    document.removeEventListener('pointerup', endPress, true);
    document.removeEventListener('pointercancel', endPress, true);
    document.removeEventListener('pointerout', leaveDocument, true);
    document.removeEventListener('visibilitychange', visibilityChanged);
    window?.removeEventListener('blur', reset);
    window?.removeEventListener('pagehide', reset);
    observer?.disconnect();
    observer = undefined;
  }

  function endPress(event) {
    if (event.pointerId === pointerId) reset();
  }

  function visibilityChanged() {
    if (document.hidden) reset();
  }

  function leaveDocument(event) {
    if (event.relatedTarget === null) endPress(event);
  }

  function startPress(event) {
    if (event.button !== 0 || event.isPrimary === false || element.disabled || pointerId !== null) return;
    pointerId = event.pointerId;
    element.dataset.pressed = 'true';
    // Observe release globally without capturing the pointer or changing native click targeting.
    document.addEventListener('pointerup', endPress, true);
    document.addEventListener('pointercancel', endPress, true);
    document.addEventListener('pointerout', leaveDocument, true);
    document.addEventListener('visibilitychange', visibilityChanged);
    window?.addEventListener('blur', reset);
    window?.addEventListener('pagehide', reset);
    if (window?.MutationObserver) {
      observer = new window.MutationObserver(() => {
        if (element.disabled || !element.isConnected) reset();
      });
      observer.observe(element, {attributes: true, attributeFilter: ['disabled']});
      observer.observe(document, {childList: true, subtree: true});
    }
  }

  element.addEventListener('pointerdown', startPress);
  element.addEventListener('lostpointercapture', endPress);
  element.addEventListener('blur', reset);
  return () => {
    reset();
    element.removeEventListener('pointerdown', startPress);
    element.removeEventListener('lostpointercapture', endPress);
    element.removeEventListener('blur', reset);
  };
}
module.exports = {attachPress};
