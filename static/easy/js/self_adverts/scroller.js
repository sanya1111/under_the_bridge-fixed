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
        $("#text_date").html(data["date"])
        $("#text_content").val(data["content"])
        $("#text_coords").val(data["coords"])
        current_page = parseInt(data["page"])
      }
    })
}

$(document).ready(function(){
  var can = 1
  function scroll_up(){
    if (can == 1){
      next(current_page - 1)
    }
    
    //какая нибудь анимация
  }


  function scroll_down(){
    if(can ==1 ){
      next(current_page + 1)
    }
  
    //аналогично
  }

  $(window).bind('mousewheel DOMMouseScroll', function(event){  
      if (event.originalEvent.wheelDelta > 0 || event.originalEvent.detail < 0) {
          scroll_up()
      }
      else {
        scroll_down()
      }
      // can = 0
      // setTimeout(function(){
      //   can = 1
      // }, 2000)    
  });

  $("#up_arrow").click(function(){
    scroll_up()
  })

  $("#down_arrow").click(function(){
    scroll_down()
  })

  // $(window).keydown(function(e){
  //      if(e.which == 38){
  //       scroll_up()
  //     }
  //      if (e.which == 40){
  //       scroll_down()
  //      }
  // })

  next(0);
});