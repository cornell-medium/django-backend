$(document).ready(function() {
  var end = new Date('December 15, 2019 12:00:00').getTime();
  var countdown = setInterval(function() {
    var now = new Date().getTime();

    var distance = end - now;
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);


    $('.narrative__countdown__days').html(days);
    $('.narrative__countdown__hours').html(hours);
    $('.narrative__countdown__minutes').html(minutes);
    $('.narrative__countdown__seconds').html(seconds)

    if (distance < 0) {
     clearInterval(x);
     document.getElementById("demo").innerHTML = "EXPIRED";
   }
 }, 1000);
});


$(function(){  // $(document).ready shorthand
  // $('.monster').fadeIn('slow');
});

$(document).ready(function() {

    /* Every time the window is scrolled ... */
    $(window).scroll( function(){

        /* Check the location of each desired element */
        $('.fade_in').each( function(i){

            var bottom_of_object = $(this).position().top + $(this).outerHeight();
            var bottom_of_window = $(window).scrollTop() + $(window).height();

            /* If the object is completely visible in the window, fade it it */
            if( bottom_of_window > bottom_of_object ){

                $(this).animate({'opacity':'1'},2000);

            }

        });

    });

});
