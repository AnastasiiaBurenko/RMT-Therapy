# Звіт з лабораторної роботи №2

**Тема:** Семантична розмітка та форми: каркас вебзастосунку  
**Студентка:** Буренко Анастасія  
**Назва проєкту:** RMT-Therapy  
**Посилання на репозиторій GitHub:** [https://github.com/AnastasiiaBurenko/RMT-Therapy](https://github.com/AnastasiiaBurenko/RMT-Therapy)  
**Посилання на опубліковані сторінки (GitHub Pages):**  
* [Головна сторінка](https://anastasiiaburenko.github.io/RMT-Therapy/index.html)  
* [Перелік вправ](anastasiiaburenko.github.io/RMT-Therapy/exercises.html)  
* [Форма запису](anastasiiaburenko.github.io/RMT-Therapy/contact.html)  

---


## 1. Опис виконаної роботи та структури сторінок

В рамках лабораторної роботи було створено три сторінки проєкту RMT Therapy із дотриманням семантики HTML5:
1. `index.html` — Головна сторінка з описом предметної області RMT, графічною схемою (SVG з `role="img"` та `aria-label`) та переліком переваг.
2. `exercises.html` — Перелік вправ у формі семантичної доступної таблиці з елементами `<caption>`, `<thead>`, `<tbody>` та атрибутами `scope="col"` / `scope="row"`.
3. `contact.html` — Форма запису на діагностику з 6 типами полів, групуванням у `fieldset` / `legend` та валідацією.

На всіх сторінках присутнє посилання «Перейти до основного вмісту» (`<a href="#main-content">`), присутній рівно один заголовок `<h1>` та єдина навігація `<nav>`.

### Перелік полів форми та обґрунтування типів:
* `parent-name` (`type="text"`): Для введення текстового ПІБ. Використано `minlength="3"`, `required` та `autocomplete="name"`.
* `email` (`type="email"`): Забезпечує автоматичну перевірку формату email браузером.
* `phone` (`type="tel"`): Викликає відповідну цифрове клавіатуру на мобільних пристроях. Додано regex-валідацію за атрибутом `pattern="^\+380\d{9}$"`.
* `child-age` (`type="number"`): Дозволяє обмежити значення діапазоном від 3 до 18 років за допомогою атрибутів `min` та `max`.
* `preferred-date` (`type="date"`): Надає зручний календарний віджет для вибору дати.
* `exercise-select` (`<select>`): Вибір опції із заздалегідь визначеного списку.
* `comments` (`<textarea>`): Багаторядкове текстове поле для довільних приміток.

---

## 2. Результати перевірки валідатором розмітки (W3C Nu HTML Validator)

Усі три сторінки було перевірено онлайн-валідатором [W3C Nu HTML Validator].

* **`index.html`:** Document checking completed. No errors or warnings to show.
* **`exercises.html`:** Document checking completed. No errors or warnings to show.
* **`contact.html`:** Document checking completed. No errors or warnings to show.

## 3. Перевірка доступності (Accessibility Audit)

1. **Клавіатурна навігація (Tab/Shift+Tab):**
   * Пройдено всі сторінки клавішею `Tab`.
   * Усі інтерактивні елементи (посилання, поля форми, кнопки) отримують чіткий системний фокус.
   * Порядок переходу логічний та відповідає візуальній структурі документа.
   * Посилання «Перейти до основного вмісту» працює коректно, переміщуючи фокус на `<main id="main-content">`.

2. **Автоматичний аудит (Lighthouse Accessibility Audit):**
   * Оцінка доступності за шкалою Lighthouse склала **100/100** для всіх трьох сторінок.
   * Усі змістовні зображення мають чіткі `alt` підписи, декоративні — `alt=""`.
   * Усі поля форми зв'язані з відповідними `label`.