$(document).ready(function() {
    //Materialize function
    $('select').formSelect();
    $('select').not('.disabled').formSelect();
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    //End of Materialize functions
    
    //My functions
    $('#alert_close').click(function() {
        $("#alert_box").fadeOut("fast", function() {});
    });
    //End of my functions

});


/*Back to the top button*/

// Code taken from WS Schools - https://www.w3schools.com/howto/howto_js_scroll_to_top.asp

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("mytop").style.display = "block";
  } else {
    document.getElementById("mytop").style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
} 

// End of Scroll to the top button -Code taken from WS Schools - https://www.w3schools.com/howto/howto_js_scroll_to_top.asp