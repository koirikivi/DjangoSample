$(document).ready(function(){
    $("#login").click(function(e){
        e.preventDefault()
        username=$("#name").val();
        password=$("#word").val();
        $.ajax({
            type: "POST",
            url: "/login_ajax/",
            data: {
                'name': username,
                'pwd': password,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'html',
            success: clickSuccess,
            error: clickError,
        });
    });
});

function clickSuccess(data, textStatus, jqXHR){
    window.location.href = data;
}

function clickError(data, textStatus, jqXHR){
    $("#status").html(data.responseText);
}
