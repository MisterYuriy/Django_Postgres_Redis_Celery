//validate url on Frontend
function validURL(myURL) {
    var pattern = new RegExp('^(https?:\\/\\/)?'+ // protocol
    '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.?)+[a-z]{2,}|'+ // domain name
    '((\\d{1,3}\\.){3}\\d{1,3}))'+ // ip (v4) address
    '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ //port
    '(\\?[;&amp;a-z\\d%_.~+=-]*)?'+ // query string
    '(\\#[-a-z\\d_]*)?$','i');
    return pattern.test(myURL);
    }

//send ajax post request
function updateButton() {
    let user_url = $('#urlinput').val();
    if (!validURL(user_url)) {
        alert('Url is not valid, Front');
        return
    }
    $.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
       } 
    });

    $.ajax({
        type: 'POST',
        url: '/myapp/calculate/',
        data: JSON.stringify({'users_url': user_url}),
        success: function(response){
                    if (response['status'] == 200) {
                        drawTagsPie(response['data']);
                    } else {
                        alert(response['message']);
                    }
                },
        dataType : 'json',
        contentType: 'application/json; charset=utf-8',
        failure: function(errMsg) {
            alert(errMsg);
        }
    });
};

//print pie diagram
function drawTagsPie(array) {
    google.charts.load("current", {packages:["corechart"]});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = google.visualization.arrayToDataTable(array);
        var options = {
                title: 'Теги на странице ',
                is3D: true,
            };
        var chart = new google.visualization.PieChart(document.getElementById('piechart_3d'));
        chart.draw(data, options);
    };
};
