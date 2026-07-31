/* Accordion sidebar: only one handbook topic open at a time */
(function () {
  const TOPIC_TOGGLE_SELECTOR =
    '.md-nav--primary nav[data-md-level="1"] > .md-nav__list > .md-nav__item--nested > input.md-nav__toggle';

  function getTopicToggles() {
    return Array.from(document.querySelectorAll(TOPIC_TOGGLE_SELECTOR));
  }

  function closeOtherTopics(current) {
    getTopicToggles().forEach((toggle) => {
      if (toggle === current) return;
      toggle.checked = false;
      toggle.classList.remove("md-toggle--indeterminate");
    });
  }

  document.addEventListener("change", (event) => {
    const toggle = event.target;
    if (!(toggle instanceof HTMLInputElement)) return;
    if (!toggle.matches(TOPIC_TOGGLE_SELECTOR)) return;
    if (!toggle.checked) return;

    closeOtherTopics(toggle);
  });
})();
