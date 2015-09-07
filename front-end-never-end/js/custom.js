$(document).ready(function () {
    var slide = false;
    $('li.parent').hover(function () {
        if ($(this).find('> ul').css('display') == "none") {
            $(this).find('> ul').slideDown(150);
            slide = true;
        }
    }, function () {
        if (slide == true) {
            $(this).find('> ul').slideUp();
            slide = false;
        }
    });
    $('nav strong').click(function () {
        $('nav ul').toggle();
    });
});
