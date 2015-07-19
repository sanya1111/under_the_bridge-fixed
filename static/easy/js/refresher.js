$(document).ready(function(){
  $("#refresh_button").click(function(){
    var old_text = $("#refresh_button").html()
    $("#refresh_button").html("...Загрузка...")
    setTimeout(function(){
      $("#refresh_button").html(old_text)
    }, 500)
    $.ajax({
      url: "/ajax/?update=1" + "&advert_id=" + current_page.toString() + "&adress=" + $("#text_adress").val() + "&content=" + $("#text_content").val(),
      dataType : "html",  
      error:function(data){
        console.log("ERR" )
      },
      success: function(data){
        console.log("update successfull" + data)
        // $("#refresh_button").html(old_text)
        next(current_page)
      }
    })
  })
  $(".create_new").click(function(){
    $.ajax({
      url: "/ajax/?create=1",
      dataType : "html",  
      error:function(data){
        console.log("ERR" )
      },
      success: function(data){
        console.log("create successfull" + data)
        next(current_page + 1)
      }
    })
  })
   $("#remove_button").click(function(){
    $.ajax({
      url: "/ajax/?remove=1" + "&advert_id=" + current_page.toString() ,
      dataType : "html",  
      error:function(data){
        console.log("ERR" )
      },
      success: function(data){
        console.log("update successfull" + data)
        next(current_page)
      }
    })
  })
});