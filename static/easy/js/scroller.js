$(document).ready(function(){
  var current_page = 0;
  function next(page){
    $.ajax({
      url: "/ajax/?next=" + page.toString(),
      dataType : "json",  
      error:function(data){
        console.log("ERR")
      },
      success: function(data){
        var h = $("#have_adverts")
        var nh = $("#not_have_adverts")
        if("none" in data){
          h.css({ 'visibility' : 'hidden'})
          nh.css({ 'visibility' : 'visible'})
          return
        }
        h.css({ 'visibility' : 'visible'})
        nh.css({ 'visibility' : 'hidden'})
        $(".round_img").attr('src', data["face_img"])
        $("#text_adress").val(data["adress"])
        $("#text_date").val(data["date"])
        $("#text_content").val(data["content"])
        current_page = parseInt(data["page"])
      }
    })
  }

  function scroll_up(){
    next(current_page - 1)
    //какая нибудь анимация
  }


  function scroll_down(){
    next(current_page + 1)
    //аналогично
  }

  $(window).bind('mousewheel DOMMouseScroll', function(event){
    if (event.originalEvent.wheelDelta > 0 || event.originalEvent.detail < 0) {
        scroll_up()
    }
    else {
      scroll_down()
    }
  });

  $(window).keydown(function(e){
       if(e.which == 38){
        scroll_up()
      }
       if (e.which == 40){
        scroll_down()
       }
  })

  next(0);
});