$(document).ready(function () {

    var csrftoken = $('meta[name=csrf-token]').attr('content')

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken)
            }
        }
    })


    let currentLetter = 1
    let url =  window.location.href
    urlSplits = url.split("/")
    let keySize = urlSplits[4] 
    const ctx = document.getElementById('myChart');
    $.getJSON('../static/data/letter_freq_en.json', function(data) {
        myItems = data;
         letters = Object.keys(data);
        letters_value = []
        letters.forEach(element => {
            letters_value.push(data[element])
        });
        new Chart(ctx, {
        type: 'bar',
        data: {
            labels: letters,
            datasets: [{
                label: 'Frequency of Letters',
                data: letters_value,
                borderWidth: 1,
                backgroundColor: "purple"
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
    });

    /*
    TODO: get frequency for specific keysize:
    
*/
// 1) api request:


    $( "#button-1" ).click(function() {
        var request = $.ajax({
            url: "/api/frequency",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({
              currentLetter: currentLetter, 
              known: 2
            }),  
         })  
           .done( function (request) {
         })
      });



});
