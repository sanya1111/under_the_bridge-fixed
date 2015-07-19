$(document).ready(function(){
  var myMap; 
  $("#params").append("<div id='map' style='width:100%;height:50%;'></div>")  
  ymaps.ready(function(){
    myMap = new ymaps.Map("map", {
      center: [55.76, 37.64],
      zoom: 7,
      controls: ["zoomControl", "searchControl"]
    });
    myMap.controls.get("searchControl").events.add("submit", function(){
      var m_bounds = myMap.getBounds()
       $.ajax({
        url: "/ajax/?search=1" + "&bounds=[" + m_bounds.toString() + "]",
        dataType : "html",  
        error:function(data){
          console.log("ERR")
        },
        success: function(data){
          
        }
      })
    })
  });


 });