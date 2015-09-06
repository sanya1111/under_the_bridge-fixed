function refresh_incomings(){
   $.ajax({
        url: "/ajax/?search=1&incomings=1",
        dataType : "json",  
        error:function(data){
          console.log("ERR")
        },
        success: function(data){
            $("#incomings").css({'visibility' : (data["incomings"] == false ? "visible" : "hidden")})      
        } 
  })
}

function switch_radio(e){
    to = e.data.to
    if(document.search_type != to){
        $("#radio_" + document.search_type.toString()).removeClass("button_active")
        $("#radio_" + to.toString()).addClass("button_active")
        document.search_type = to
    }

}


$(document).ready(function () {
    document.search_type = 2
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
    $(".create_incomings").click(function(){
        window.location.replace("/incomings");
    })
    $("#incomings").css({"visibility":"hidden"})
    $("#radio_1").bind('click', {to : 1}, switch_radio)
    $("#radio_2").bind('click', {to : 2}, switch_radio)
    refresh_incomings()
  
});
