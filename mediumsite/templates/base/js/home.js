$(document).ready(function() {
	$(function(){
		$("#typed").typed({
			strings: ["Dialogue through Design", "Building Design at Cornell", "What's your Medium?"],
			backDelay: 3000,
			typeSpeed: 25,
			cursorChar: ""
		});
  });

	$(".hamburger").click(function() {
		if($(this).hasClass("is-active")) {
			$(this).removeClass("is-active");
			$("#nav-screen").fadeOut(100);
		} else {
			$(this).addClass("is-active");
			$("#nav-screen").fadeIn(100);
		}
	});
});