$(document).ready(function(){
    console.log('document is ready')

    $('#inference').click(async function(){  //when button is clicked
        console.log('button was clicked!')
        const cylinders = parseFloat($('#cylinders').val());
        const horsepower = parseFloat($('#horsepower').val());
        const weight = parseFloat($('#weight').val());
        const data = { // object? of 3 vars
            cylinders,
            horsepower,
            weight
        } 
        console.log(data)
        const response = await $.ajax('/inference',{  
            data: JSON.stringify(data),
            method:'post',
            contentType: 'application/json'
        })
        console.log('response')  //prints response
        $('#mpg').val(response.prediction) //gets prediction from response
    })

    $('#scatter-plot').click(async function(){  //when button is clicked
        console.log('scatter button was clicked!')
        const response = await $.ajax('/plot')
        console.log('response')
        const mpg = reponse.map(a => a[0])  
        const weight = reponse.map(a => a[1])
        console.log(mpg)
        
        // create the trace
        const trace =[{
            x:weight,
            y:mpg,
            mode: 'markers',
            type: 'scatter'
        }]
        //create the layout

        const layout = {
            xaxis:{
                title:'Weight'
            },
            yaxis:{
                title:'mpg'
            },
            title: 'Scatter MPG vs weight',
            width: 700,
            height: 300
        }

    })
})