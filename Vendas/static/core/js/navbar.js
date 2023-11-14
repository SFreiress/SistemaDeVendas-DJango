$(document).ready(function() {
    const barsButton = $('.navbar-bars-button');
    const navbarContent = $('.navbar-content');
    const navbarFooter = $('.navbar-footer');

    barsButton.on('click', function() {
        if (navbarContent.hasClass('hidden')) {
            navbarContent.removeClass('hidden');
            navbarFooter.removeClass('hidden');
        } else {
            navbarContent.addClass('hidden');
            navbarFooter.addClass('hidden');
        }
    });
});
