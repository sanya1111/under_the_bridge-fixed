$(document).ready(function () {
    content_height = getContentHeight()
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
