$(document).ready(function() {
    $('.collapsible').collapsible();
    $('select').material_select();
    $(".button-collapse").sideNav({
        edge: 'right',
        menuWidth: 200
    });
    $('.materialize-textarea').trigger('autoresize');
    $('textarea#recipe_description').characterCounter();
    $('.dropdown-button').dropdown({
        inDuration: 300,
        outDuration: 225,
        constrainWidth: false, // Does not change width of dropdown to that of the activator
        hover: false, // Activate on hover
        gutter: 0, // Spacing from edge
        belowOrigin: true, // Displays dropdown below the button
        alignment: 'right', // Displays dropdown with edge aligned to the left of button
        stopPropagation: false // Stops event propagation
    });
});

// Back-to-top functionality
if ($('#back-to-top').length) {
    var scrollTrigger = 100, // px
        backToTop = function() {
            var scrollTop = $(window).scrollTop();
            if (scrollTop > scrollTrigger) {
                $('#back-to-top').removeClass('scale-out');
            }
            else {
                $('#back-to-top').addClass('scale-out');
            }
        };
    backToTop();
    $(window).on('scroll', function() {
        backToTop();
    });

    $('#back-to-top').on('click', function(e) {
        e.preventDefault();
        $('html,body').animate({
            scrollTop: 0
        }, 700);
    });
}