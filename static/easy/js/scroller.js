$(document).ready(function(){
  var current_page = 0;
  function scroll_up(){
   //  alert("UP")
    $.ajax({
    url: "/bitch",
    data : "json",
    error:function(data){
      alert("ERR")
    },
    success: function(data){
      alert( typeof data );
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