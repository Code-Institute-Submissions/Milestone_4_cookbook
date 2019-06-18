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


