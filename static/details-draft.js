

    $(document).ready(function(){
        $.ajax({
        type: "GET",
        url: "invite",
        success: function(result){
            $("#home-draft").text(result["invitation"])
        },          
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
        });

        $("#submit_correction").click(function(){
            var c = $("#correction").val();
            console.log("hi")
            //window.location.href='details-draft';
            
            $.ajax({
            type: "POST",
            url: "fix",
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify({correction: c}),
            success: function(result){
                setTimeout(function(){window.location.href='details-draft'},5000)
            },          
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
            });

            console.log("bye")
            setTimeout(function(){window.location.href='details-draft'},5000)
            //setTimeout(reload(),5000)
        })
    })