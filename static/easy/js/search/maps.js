$(document).ready(function(){
  var myMap, mySearchControl 
  var content_height = getContentHeight()
  var current_page = 0

  function append_result(id, data){
    $("#results").append('<div class="clearFix edit_border list_item" style="height:120px;">   <div class="col floatLeft back_img round_img" id="back' + id.toString() + '" style="height:100%;width:20%"></div> <div class="col floatLeft back_img round_img" id="user' + id.toString() + '" style="height:100%;width:10%"></div> <div class="col floatRight list_content" style="width:65%;height:100%;word-wrap: break-word;overflow:hidden;text-overflow: ellipsis;"><p id="text_content' + id.toString() + '"><strong>Адрес </strong><br><br><strong>Описание </strong><br> </p></div></div>')   
    $('#user' + id.toString()).css({
      'background-image':  'url(' + data["user_img"] + ')'
    })
    $('#text_content' + id.toString()).html('<strong>Адрес </strong><br>' + data["adress"] + '<br><strong>Описание </strong><br>' + data["content"])
  }

  function refresh_objects(){
    var m_bounds = myMap.getBounds()
      // alert(m_bounds)
        var url =  "/ajax/?search=1" + "&bounds=[" + m_bounds.toString() + "]" + "&page=" + current_page.toString()
       $.ajax({
        url: "/ajax/?search=1" + "&bounds=[" + m_bounds.toString() + "]" + "&page=" + current_page.toString() + "&type=" + document.search_type.toString(),
        dataType : "json",  
        error:function(data){
          console.log("ERR")
        },
        success: function(data){
          myMap.geoObjects.removeAll()
          $("#results").html('')
          if (data["prev"]) {
             $("#results").append('<div class="button" id="prev_page"><=PREV</div>')
             $("#prev_page").click(function(){
                current_page = current_page - 1
                refresh_objects()
             })
          }
          if (data["next"]) {
             $("#results").append('<div class="button" id="next_page">NEXT=></div>')
             $("#next_page").click(function(){
                current_page = current_page + 1
                refresh_objects()
             })
          }
          data = data["response"]
          for(var i = 0; i < data.length; i++){
              append_result(i, data[i])
              var myPlacemark = new ymaps.GeoObject({
                    geometry: {
                    type: "Point",
                   coordinates: data[i]["coords"]
                },
                  properties: {
                     iconContent: (i + 1).toString()
                  } 
                },
                {    preset : "islands#redIcon",
                }
              );
              myMap.geoObjects.add(myPlacemark);

          }
          $(".list_item").css({
              'height' : content_height / 6,
          }) 
        } 
      })
  }

  $("#params").append("<div id='map' style='width:100%;height:50%;'></div>")  
  ymaps.ready(function(){

    var mySearchControl = new ymaps.control.SearchControl({
         options: {
             float: 'right',
             floatIndex: 100,
             noPlacemark: true
         }
    });
    myMap = new ymaps.Map("map", {
      center: [59.93883244868871,30.308324582031215],
      zoom: 7,
      controls: ["zoomControl"]
    });

    myMap.controls.add(mySearchControl)
    myMap.events.add("actionend", function(e){
      current_page = 0
      refresh_objects()
    })
    refresh_objects()
  });


 });