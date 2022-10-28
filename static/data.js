function home(invitation){
    $.ajax({
        type: "POST",
        url: "basic",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(invitation),
        success: function(result){
            $("#home-draft").html(result); 
            console.log(result)
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
    
  });
  