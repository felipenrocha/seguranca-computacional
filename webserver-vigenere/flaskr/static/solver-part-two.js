$(document).ready(function () {
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
    $( "#button-1" ).click(function() {
        post()
      });

/*
    TODO: get frequency for specific keysize:
    
*/
// 1) api request:
    data = {"currentLetter": currentLetter}
    post(data)
    

});

function post(data)
{
    $.post("/api/frequency", data,
        function (data, textStatus, jqXHR) {
            
        },
        "dataType"
    );
}