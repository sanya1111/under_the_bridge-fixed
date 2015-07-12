$(document).ready(function () {
    function getIntPx(str){
        return parseInt(str.slice(0, str.length - 2))
    }
    $('li.parent').hover(function () {
        if ($(this).find('> ul').css('display') == "none") {
            $(this).find('> ul').slideDown(200);
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
    // alesrt("fcuk")
    var content_height = $(window).height() - $("header").height() - $("footer").height() -  getIntPx($('#content').css('padding-top')) - getIntPx($('#content').css('padding-bottom')) - getIntPx($('footer').css('padding-top')) - getIntPx($('footer').css('padding-bottom'))
    $('#content').css({
        'height' : content_height
    })
});
