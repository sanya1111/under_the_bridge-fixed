$(document).ready(function () {
    
    var content_height = getContentHeight()
    var w = $("#content").width()
    $("#params").css({
        'height' : content_height,
        'width' : w * 0.5
    })
    $("#results").css({
        'height' : content_height,
        'width' : w * 0.49
    })
});
