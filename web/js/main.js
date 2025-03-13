document.addEventListener('contextmenu', function(event) {
    event.preventDefault();  // Блокує контекстне меню
    return false;  // Додаткове запобігання за замовчуванням
});