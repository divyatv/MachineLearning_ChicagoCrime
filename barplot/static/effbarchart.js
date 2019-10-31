//process the results obtained from  app.py (the Flask application)
// Select the button
var button = d3.select("#filter-btn-type");
// define a function to process the police eff data
function processInputsandPlot() {
     // define a variable url which pulls the value of the user entered sku dynamically
     var url = "/count/"+document.getElementById("selectType").value
     d3.json(url).then(function(result) {
     console.log(result);
     // define two arrays to store data obtained from executing the sky in the .py file for plotting
     plot_labels = [];
     plot_data = [];
     result.forEach( x =>  {
        beat = Object.entries(x)[0][1];
        efficiency  = Object.entries(x)[1][1];
        plot_labels.push(beat);
        plot_data.push(efficiency);
       });
       var ctx = document.getElementById("count-type");
       var myChart = new Chart(ctx, {
       type: 'bar',
       data: {
         labels: plot_labels,
         datasets: [{
           label: 'Beat Efficiency for' + name + ' Crime',
           data : plot_data,
           backgroundColor: [
             'rgba(202, 45, 11, 1)',
             'rgba( 73, 202, 11, 1 )',
             'rgba( 11, 69, 202, 1)',
             'rgba(205,92,92, 0.2)',
             'rgba(202, 45, 11, 1)',
             'rgba(250,128,114, 1 )',
             'rgba(255,69,0, 1)',
             'rgba(255,215,0, 0.2)',
             'rgba(128,128,0, 1)',
             'rgba(47,79,79, 1 )',
             'rgba(25,25,112, 1)',
             'rgba(139,0,139, 0.2)'

           ],
           borderColor: [
            'rgba(202, 45, 11, 1)',
            'rgba( 73, 202, 11, 1 )',
            'rgba( 11, 69, 202, 1)',
            'rgba(205,92,92, 0.2)',
            'rgba(202, 45, 11, 1)',
            'rgba(250,128,114, 1 )',
            'rgba(255,69,0, 1)',
            'rgba(255,215,0, 0.2)',
            'rgba(128,128,0, 1)',
            'rgba(47,79,79, 1 )',
            'rgba(25,25,112, 1)',
            'rgba(139,0,139, 0.2)'
           ],
           borderWidth: 1
         }]
       },
       options: {
            cutoutPercentage: 60,
         responsive: true,
       }
     });
   });
};

var name;

function optionChanged(newCrime) {
  name = newCrime
  // Fetch new data each time a new crime is selected
  // processInputsandPlot(newCrime);
}

// define the function call when the "Display Stock Status" button is clicked
button.on("click",processInputsandPlot);