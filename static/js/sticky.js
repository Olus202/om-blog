$(document).ready(function() {
   var stickyNavTop = $('#menu').offset().top;

   var stickyNav = function(){
   var scrollTop = $(window).scrollTop();

   if (scrollTop > stickyNavTop) {
      $('#menu').addClass('sticky');
   } else {
      $('#menu').removeClass('sticky');
    }
   };

   stickyNav();

   $(window).scroll(function() {
      stickyNav();
   });
});