# Contact

If you spot an error, disagree with an approach, or have a better idea, send me a message.

<form class="contact-form" action="https://formsubmit.co/contact@milenageorgieva.tech" method="POST">
  <input type="hidden" name="_subject" value="AI Engineering Handbook — new message">
  <input type="hidden" name="_captcha" value="false">
  <input type="hidden" name="_next" id="contact-form-next" value="">

  <label class="contact-form__label" for="contact-name">Name</label>
  <input class="contact-form__input" id="contact-name" type="text" name="name" required autocomplete="name">

  <label class="contact-form__label" for="contact-email">Email</label>
  <input class="contact-form__input" id="contact-email" type="email" name="email" required autocomplete="email">

  <label class="contact-form__label" for="contact-message">Message</label>
  <textarea class="contact-form__input contact-form__textarea" id="contact-message" name="message" rows="6" required></textarea>

  <button class="contact-form__submit md-button md-button--primary" type="submit">Send message</button>
</form>

<script>
  const contactNext = document.getElementById("contact-form-next");
  if (contactNext) {
    contactNext.value = `${window.location.origin}/contact/?sent=1`;
  }

  if (new URLSearchParams(window.location.search).get("sent") === "1") {
    const notice = document.createElement("p");
    notice.className = "contact-form__notice";
    notice.textContent = "Thank you — your message was sent.";
    document.querySelector(".contact-form")?.prepend(notice);
  }
</script>
