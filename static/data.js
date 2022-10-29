function home(date, time, location) {
    $.ajax({
        type: "POST",
        url: "basic",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify({date:date, time:time, location: location}),
        success: function(result){

        },          
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}


$(document).ready(function () {
    $("form#home-form").submit(function(event) {
        event.preventDefault();
        var date = $("#date").val();
        var time = $("#time").val();
        var location = $("#location").val();
        home(date, time, location)
        setTimeout(function(){window.location.href='details-draft'},5000)

    })
  });

  