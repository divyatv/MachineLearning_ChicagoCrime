//process the results obtained from doughnut.py (the Flask application)
// Plot a default doughnut plot when the user has not entered any SKU
var ctx = document.getElementById("count-crime");
var myChart = new Chart(ctx, {
type: 'bar',
data: {
 labels: ['Divya', 'Harsha', 'Joe', 'Kevin', 'Ramesh','Frances'],
 datasets: [{
   label: 'Project Team Members',
   data: [25, 25, 25, 25, 25, 25],
   backgroundColor: [
     'rgba(255, 99, 132, 0.5)',
     'rgba(54, 162, 235, 0.2)',
     'rgba(255, 206, 86, 0.2)',
     'rgba(75, 192, 192, 0.2)',
     'rgba(80, 193, 193, 0.2)',
     'rgba(169, 104, 118, 0.2)'
   ],
   borderColor: [
     'rgba(243, 99, 132, 1)',
     'rgba(54, 23, 235, 1)',
     'rgba(254, 204, 86, 1)',
     'rgba(32, 192, 192, 1)',
     'rgba(99, 193, 193, 1)',
     'rgba(99, 193, 193, 1)'
   ],
   borderWidth: 1
 }]
},
options: {
    cutoutPercentage: 60,
 responsive: true,
}
});
// Select the button
var button = d3.select("#filter-btn-crime");
// define a function to process the data and plot when the user enters an SKU and loads the page
function processInputsandPlot() {
  
  myChart.destroy();
     // define a variable url which pulls the value of the user entered sku dynamically
     var url = "/count/"+document.getElementById("selectCrime").value
     d3.json(url).then(function(result) {
     console.log(result);
     // define two arrays to store data obtained from executing the sky in the .py file for plotting
     plot_labels = [];
     plot_data = [];
     result.forEach( x =>  {
        count = Object.entries(x)[0][1];
        year  = Object.entries(x)[1][1];
        plot_labels.push(year);
        plot_data.push(count);
       });
       var ctx = document.getElementById("count-crime");
       var myChart = new Chart(ctx, {
       type: 'bar',
       data: {
         labels: plot_labels,
         datasets: [{
           label: 'Annual ' + name + ' Occurences',
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