$(document).ready(function(){
  var opacity_kof = 0.8
  var myMap, myButton;
  
  function map_hidden(){
    $('#overlay_wrap').css({
     'visibility':'hidden'
    })
    $("ymaps").remove()
  }
  
  map_hidden()

  $("#text_adress").click(function(){
    $("#overlay_wrap").css({
      'visibility':'visible'
    }).html("<div id='overlay'></div> <div class='slider_ov' id='slider_cen'><div id='map' style='width:100%;height:100%;'></div></div>")
    $("#overlay").height($(document).height())
    .click(map_hidden)
    .css({
    'opacity':opacity_kof
    })
    
    ymaps.ready(function(){
      myButton = new ymaps.control.Button({
          data: {
            content: "Выбрать текущее местоположение",
          },
          options: {
            maxWidth: 400
          }
        }
      )
      myButton.events
      .add(
        'press',
        function () {
          $("#text_adress").val(myMap.controls.get("searchControl").state.get('request'))
          $("#text_coords").val(myMap.getCenter())
          map_hidden()
        }
      )
      myMap = new ymaps.Map("map", {
        center: [55.76, 37.64],
        zoom: 7,
        controls: ["zoomControl", "searchControl"]
      });
      myMap.controls.add(myButton, {
        float: "left"
      });

      myMap.controls.get("searchControl").search($("#text_adress").val())
    });
  })


 });