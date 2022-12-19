const alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
$(document).ready(function () {

    var csrftoken = $('meta[name=csrf-token]').attr('content')

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken)
            }
        }
    })



    $("#dropdown-id").change(function () {

        chart1.destroy()
        $.getJSON('../static/data/letter_freq_'.concat(this.value).concat( '.json'), function (data) {
            myItems = data;
            letters = Object.keys(data);
            letters_value = []
            letters.forEach(element => {
                letters_value.push(data[element])
            });
            chart1 = new Chart(ctx, {
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
    

    });

    let currentLetter = 1
    let url = window.location.href
    urlSplits = url.split("/")
    let keySize = urlSplits[4]
    const ctx = document.getElementById('freqLetters1');
    const ctx2 = document.getElementById('freqLetters2');
    let chart2;
    let chart1;
    $.getJSON('../static/data/letter_freq_en.json', function (data) {
        myItems = data;
        letters = Object.keys(data);
        letters_value = []
        letters.forEach(element => {
            letters_value.push(data[element])
        });
        chart1 = new Chart(ctx, {
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
                // 2) generate chart
                .done(function (request) {
                    console.log(request)
                    letters2 = Object.keys(request)
                    console.log('letters', letters)
                    letters_value2 = []
                    letters2.forEach(element => {
                        letters_value2.push(request[element])
                    });
                    if (chart2) { chart2.destroy() }
                    letterIndex = 0
                    $("#button-".concat(currentLetter)).html(alfabeto[letterIndex]);

                    chart2 = new Chart(ctx2, {
                        type: 'bar',
                        data: {
                            labels: letters2,
                            datasets: [{
                                label: 'Frequency of Letters',
                                data: letters_value2,
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

    // 3) add shift right and left

    $("#shif-left").click(function () {
        if (letterIndex < 25) { letterIndex = letterIndex + 1 }
        else {
            letterIndex = 0
        }
        $("#button-".concat(currentLetter)).html(alfabeto[letterIndex]);
        chart2.data.labels = rotateLeft(chart2.data.labels)
        chart2.data.datasets.forEach((dataset) => {
            dataset.data = rotateLeft(dataset.data);
        });
        chart2.update();
       
    });
    $("#shif-right").click(function () {
        if (letterIndex > 0) { letterIndex = letterIndex - 1 }
        else {
            letterIndex = 25
        }

        $("#button-".concat(currentLetter)).html(alfabeto[letterIndex]);

        chart2.data.labels = rotateRight(chart2.data.labels)
        chart2.data.datasets.forEach((dataset) => {
            dataset.data = rotateRight(dataset.data);
        });
        chart2.update();
    });

 

});

function rotateLeft(arr) {
    let first = arr.shift();
    arr.push(first);
    return arr;
}

function rotateRight(arr) {
    let last = arr.pop();
    arr.unshift(last);
    return arr;
}