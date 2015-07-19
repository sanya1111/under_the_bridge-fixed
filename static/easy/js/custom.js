 function getIntPx(str){
        return parseInt(str.slice(0, str.length - 2))
}

function elementMaxWitdth(e){
    return e.parent().width() - getIntPx(e.css('margin-left')) - getIntPx(e.css('margin-right')) - getIntPx(e.css('border-left-width')) - getIntPx(e.css('border-right-width'))-
                            getIntPx(e.css('padding-left')) - getIntPx(e.css('padding-right'))
}

function getContentHeight(){
    return $(window).height() - $("header").height() - $("footer").height() -  getIntPx($('#content').css('padding-top')) - getIntPx($('#content').css('padding-bottom')) - getIntPx($('footer').css('padding-top')) - getIntPx($('footer').css('padding-bottom'))
}

$(document).ready(function () {
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
    var content_height = getContentHeight()
    $('#content').css({
        'height' : content_height
    })
});
