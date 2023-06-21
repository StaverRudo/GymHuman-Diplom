
const btn = document.querySelector('.content-buttonblock__button');
const paginator = document.querySelector('.content-paginations')
const cards = document.querySelectorAll('.card');

btn.addEventListener('click', function() {
    for(let card of cards) {
        card.style.display = 'flex'
        
    }
    btn.style.display = 'none';
    paginator.style.display = 'block'
})



document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Предотвращаем отправку формы по умолчанию

    // Получаем значения полей формы
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var subject = document.getElementById('subject').value;
    var message = document.getElementById('message').value;

    // Формируем текст сообщения
    var emailBody = 'Имя: ' + name + '\n' +
                    'Email: ' + email + '\n' +
                    'Заголовок: ' + subject + '\n' +
                    'Сообщение: ' + message;

    // Отправка сообщения на почту
    window.location.href = 'vlstavervl@gmail.com?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(emailBody);
});
