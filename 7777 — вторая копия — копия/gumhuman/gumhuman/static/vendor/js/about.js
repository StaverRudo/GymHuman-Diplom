document.addEventListener('DOMContentLoaded', function() {

    document.getElementById('burger').addEventListener('click', function(){
 
     document.querySelector('header').classList.toggle('open')
 
    })
 
 })
 
 
 document.addEventListener('DOMContentLoaded', function() {
 
    document.getElementById('sidebarburger').addEventListener('click', function(){
 
     document.querySelector('main').classList.toggle('opens')
 
    })
 
 })
 
 var button = document.getElementById("my-button");
 var block = document.getElementById("my-block");
 var strelka = document.getElementById("strelka");
 var isVisible = false; // Флаг текущего состояния блока
 

button.addEventListener("click", function() {
if (isVisible) {
  block.style.display = "none"; // Если блок видим, скрываем его
  strelka.style.display = "block";
  isVisible = false; // Устанавливаем флаг в false
  
} else {
  block.style.display = "block"; // Если блок скрыт, показываем его
  strelka.style.display = "none";
  isVisible = true; // Устанавливаем флаг в true
  
}
});
var imageLink = document.getElementById("my-button");

imageLink.addEventListener("click", function(e) {
e.preventDefault(); // Отменяем переход по ссылке

imageLink.classList.toggle("expanded"); // Добавляем/удаляем класс "expanded" для разворачивания/сворачивания изображения
});

var buttonn = document.getElementById("profile__link-clickimages");
var blockk = document.getElementById("profile");
var isVisible = false; // Флаг текущего состояния блока

buttonn.addEventListener("click", function() {
  if (isVisible) {
    blockk.style.display = "none"; // Если блок видим, скрываем его
    isVisible = false; // Устанавливаем флаг в false
  } else {
    blockk.style.display = "block"; // Если блок скрыт, показываем его
    isVisible = true; // Устанавливаем флаг в true
  }
});
 