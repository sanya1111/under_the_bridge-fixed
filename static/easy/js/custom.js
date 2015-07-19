$(document).ready(function () {
    function getIntPx(str){
        return parseInt(str.slice(0, str.length - 2))
    }
    function elementMaxWitdth(e){
        // alert($("#content").width())
        return e.parent().width() - getIntPx(e.css('margin-left')) - getIntPx(e.css('margin-right')) - getIntPx(e.css('border-left-width')) - getIntPx(e.css('border-right-width'))-
                                    getIntPx(e.css('padding-left')) - getIntPx(e.css('padding-right'))
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
    $('#text_date').css({    'height' : content_height * 0.03,
                                'width' : elementMaxWitdth($('#text_date'))  })
    $('#text_adress').css({    'height' : content_height * 0.03 ,
                                'width' : elementMaxWitdth($('#text_adress')) })    
    $('#text_content').css({    'height' : content_height * 0.2,
                                'width' : elementMaxWitdth($('#text_content')) })
    $('#create_button').css({
        'width' : elementMaxWitdth($('#create_button'))
    })
    $("#up_arrow").css({
        "left" :$('#have_adverts').offset()["left"] / 3,
        "top" : $("header").height() + 30
    })
    $("#down_arrow").css({
        "right" : ($("#content").height() - $('#have_adverts').offset()["left"]) / 3,
        "bottom" : $("footer").height() + getIntPx($('footer').css('padding-top')) + getIntPx($('footer').css('padding-bottom')) + 30
    })
});
