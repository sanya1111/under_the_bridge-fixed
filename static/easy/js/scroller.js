$(document).ready(function(){
  var current_page = 0;
  function scroll_up(){
   //  alert("UP")
    current_page = 1 - current_page
    $.ajax({
    url: "/ajax/?next=" + current_page.toString(),
    dataType : "json",  
    error:function(data){
      alert("ERR")
    },
    success: function(data){
      $(".round_img").attr('src', data["src"]);
      console.log(data["src"])
    }
   });
    //  $.get("/", function(data) {
    //     alert(data);
    // });
  }


  function scroll_down(){

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
 });