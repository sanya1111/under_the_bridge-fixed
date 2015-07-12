$(document).ready(function(){
  var opacity_kof = 0.8

  $('#overlay_wrap').css({
     'visibility':'hidden'
  })
  $("#overlay").height($(document).height())
  .click(function(){
      $("#overlay_wrap").css({
        'visibility': 'hidden'
      })
  }).css({
    'opacity':opacity_kof
  })
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
  
  $("#slider").click(function(){
    $("#overlay_wrap").css({
      'visibility':'visible'
    })
  })
 });