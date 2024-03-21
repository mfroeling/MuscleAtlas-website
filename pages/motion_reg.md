---

layout: page
permalink: /motion/registratie/
header: no

title: "Registratie"
subheadline: 'Ja ik doe mee!!'

tags: motion

---

Leuk dat je interesse hebt om deel te nemen aan de studie! Omdat het voor de studie belangrijk is dat we een goede verdeling hebben van de deelnemers over verschillende leeftijden, gewicht en lengte vragen we je vast deze gegeven in te vullen. Tijdens het onderzoek worden deze exact gemeten. Je telefoon nummer achter laten hoeft niet maar is wel zo makkelijk voor ons.

Als je je gegevens achter laat krijg je een email ter bevestiging en nemen we zo snel mogelijk contact met je op. Je hier aanmelden is geheel vrijblijvend. Als we binnen jouw leeftijdscategorie al genoeg deelnemers hebben kan het ook zijn dat je helaas niet meer hoeft deel te nemen.

De plannnig voor scandagen is:

- ***dag 7: zondag 26 mei 2024***
- dag 8: zondag 14 juli 2024
- dag 9: zondag 1 september 204
- dag 10: zondag 20 oktober 2024
- dag 11: zondag 15 december 2024
- dag 12: zondag 12 januari 2025

Mocht je op deze dagen niet kunnnen kan je je toch gewoon inschrijven en kunnen we samen kijken naar een ander moment.

<form
  name="RegistrationForm"
  method="POST"
  id="contact-form"
  class="contact-form"
  data-netlify="true"
  action="/motion/bedankt"
>
  <input type="hidden" name="subject" value="Motion Registratie" />
  <p class="form-row">
    <label id="contact-form-name-label" for="contact-form-name" class="form-label">Naam &ast;</label>
    <input type="text" name="name" id="contact-form-name" aria-labelledby="contact-form-name-label" class="form-input"/>
  </p>
  <p class="form-row">
    <label id="contact-form-email-label" for="contact-form-email" class="form-label">Email adres &ast;</label>
    <input type="email" name="email" id="contact-form-email" aria-labelledby="contact-form-email-label" class="form-input" required/>
  </p>
  <p class="form-row">
    <label id="contact-form-phone-label" for="contact-form-phone" class="form-label">Telefoon nummer</label>
    <input type="phone" name="phone" id="contact-form-phone" aria-labelledby="contact-form-phone-label" class="form-input"/>
  </p>
  <p class="form-row">
    <label id="contact-form-gender-label" for="contact-form-gender" class="form-label">Geslacht &ast;</label>
    <select name="gender" id="contact-form-gender" aria-labelledby="contact-form-gender-label" class="form-input" required>
      <option value="">Maak een keuze</option>
      <option value="Man">Man</option>
      <option value="Vrouw">Vrouw</option>
    </select>
  </p>
  <p class="form-row">
    <label id="contact-form-age-label" for="contact-form-age" class="form-label">Leeftijdscategorie &ast;</label>
    <select name="age" id="contact-form-age" aria-labelledby="contact-form-age-label" class="form-input" required>
      <option value="">Maak een keuze</option>
      <option value="16-20">16-20</option>
      <option value="21-25">21-25</option>
      <option value="26-30">26-30</option>
      <option value="31-35">31-35</option>
      <option value="36-40">36-40</option>
      <option value="41-45">41-45</option>
      <option value="46-50">46-50</option>
      <option value="51-55">51-55</option>
      <option value="56-60">56-60</option>
    </select>
  </p>
  <p class="form-row">
    <label id="contact-form-weight-label" for="contact-form-weight" class="form-label">Gewichts categorie &ast; </label>
    <select name="weight" id="contact-form-weight" aria-labelledby="contact-form-weight-label" class="form-input" required>
      <option value="">Maak een keuze</option>
      <option value="< 50">50- kg</option>
      <option value="50-55">50-55 kg</option>
      <option value="55-60">55-60 kg</option>
      <option value="60-65">60-65 kg</option>
      <option value="65-70">65-70 kg</option>
      <option value="70-75">70-75 kg</option>
      <option value="75-80">75-80 kg</option>
      <option value="80-85">80-85 kg</option>
      <option value="85-90">85-90 kg</option>
      <option value="90-95">90-95 kg</option>
      <option value="95-100">95-100 kg</option>
      <option value="100-105">100-105 kg</option>
      <option value="105-110">105-110 kg</option>
      <option value="110-115">110-115 kg</option>
      <option value="115-120">115-120 kg</option>
      <option value="120 <">120+ kg</option>
    </select>
  </p>
  <p class="form-row">
    <label id="contact-form-height-label" for="contact-form-height" class="form-label">Lengte categorie &ast; </label>
    <select name="height" id="contact-form-height" aria-labelledby="contact-form-height-label" class="form-input" required>
      <option value="">Maak een keuze</option>
      <option value="< 150">150- cm</option>
      <option value="150-155">150-155 cm</option>
      <option value="155-160">155-160 cm</option>
      <option value="160-165">160-165 cm</option>
      <option value="165-170">165-170 cm</option>
      <option value="170-175">170-175 cm</option>
      <option value="175-180">175-180 cm</option>
      <option value="180-185">180-185 cm</option>
      <option value="185-190">185-190 cm</option>
      <option value="190-195">190-195 cm</option>
      <option value="195-200">195-200 cm</option>
      <option value="200 <">200+ cm</option>
    </select>
  </p>
  <p class="form-row">
    <label id="contact-form-message-label" for="contact-form-message" class="form-label">Opmerkingen</label>
    <textarea name="message" id="contact-form-message" aria-labelledby="contact-form-message-label" class="form-textarea" rows="2"></textarea>
  </p>
  <p class="form-row"><div data-netlify-recaptcha="true" class="form-row"></div></p>
  <p class="hidden" style="visibility: hidden; height: 0;">
    <label id="contact-form-bot-label">Don't fill this out if you're human: <input name="" aria-labelledby="contact-form-bot-label" /></label>
  </p>
  <p class="form-row form-submit">
    <button type="submit" class="button">Registreer mij</button>
  </p>
</form>

{% include list-pages tag="motion" %}
