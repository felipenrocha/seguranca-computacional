$(document).ready(function () {

    var csrftoken = $('meta[name=csrf-token]').attr('content')

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken)
            }
        }
    })


    let currentLetter = 1
    let url = window.location.href
    urlSplits = url.split("/")
    let keySize = urlSplits[4]
    const ctx = document.getElementById('freqLetters1');
    $.getJSON('../static/data/letter_freq_en.json', function (data) {
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
    // 1) api request for each button:

    for (let index = 1; index <= keySize; index++) {

        $("#button-".concat(index)).click(function () {
            currentLetter = index
            var request = $.ajax({
                url: "/api/frequency",
                type: "POST",
                contentType: "application/json",
                data: JSON.stringify({
                    currentLetter: index,
                    keySize: keySize
                }),
            })
                .done(function (request) {
                    console.log(request)
                    letters = Object.keys(request)
                    console.log('letters', letters)
                    letters_value = []
                    letters.forEach(element => {
                        letters_value.push(request[element])
                    });
                    console.log('lettersvalue', letters_value)

                    const ctx2 = document.getElementById('freqLetters2');
                    new Chart(ctx2, {
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

                })
        });
    }




});
