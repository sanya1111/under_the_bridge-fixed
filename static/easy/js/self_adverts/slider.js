$(document).ready(function(){
  var opacity_kof = 0.8

  $('#overlay_wrap').css({
     'visibility':'hidden'
  })
  
  
  $("#slider").click(function(){
    $("#overlay_wrap").css({
      'visibility':'visible'
    }).html("<div id='overlay'></div> <img src='http://cs624731.vk.me/v624731845/3606f/1AJQqER7pDE.jpg' class='slider_ov' id='slider_cen'>  <img src='/static/easy/images/left_arrow.png' class='slider_ov' id='slider_l'><img src='/static/easy/images/right_arrow.png' class='slider_ov' id='slider_r'>")
      $("#slider_l").css({
    'width':'40px',
    'height':'40px',
    'left' :'-70%'
  })
  $("#slider_r").css({
    'width':'40px',
    'height':'40px',
    'left' :'70%'
  })
  $("#overlay").height($(document).height())
  .click(function(){
      $("#overlay_wrap").css({
        'visibility': 'hidden'
      })
  }).css({
    'opacity':opacity_kof
  })
  })
 });