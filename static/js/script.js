function clMenu1() {
  document.getElementById("tab1").classList.toggle("show");
  $('#tab1').slideToggle(500);
}
function clMenu2() {
  document.getElementById("tab2").classList.toggle("show");
  $('#tab2').slideToggle(500);
}
function clMenu3() {
  document.getElementById("tab3").classList.toggle("show");
  $('#tab3').slideToggle(500);
}
function clMenu4() {
  document.getElementById("tab4").classList.toggle("show");
  $('#tab4').slideToggle(500);
}
function clMenu5() {
  document.getElementById("tab5").classList.toggle("show");
  $('#tab5').slideToggle(500);
}
function clMenu6() {
  document.getElementById("tab6").classList.toggle("show");
  $('#tab6').slideToggle(500);
}

// Закрытие выпадающего меню, если пользователь щелкает за его пределами
window.onclick = function(event) {
if (!event.target.matches('.CATEGORIES')) {
    var dropdowns = document.getElementsByClassName("menu");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
} 
$(document).ready(function(){
	$(".owl-carousel").owlCarousel({
	margin: 10, //отступ
	loop: true, //зацикливание
	nav: true,
	navText: ['&#9668;','&#9658;'],
	responsive:{ //адаптивность блока к размеру экрана
		0:{items:1},
		600:{items:3},
		1000:{items:5},
		},
	autoplayTimeout: 8500, //смена кадра (время в милисекндах)
	autoplay: true, //автопроигрывание
	center: true, //центрирование
	smartSpeed: 2000 //скорость смены кадра (время в милисекндах)
		});
	})














