// Creating map object
var myMap = L.map("map", {
    center: [41.8781, -87.6298],
    zoom: 11
  });
  
  // Adding tile layer to the map
  L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 15,
    id: "mapbox.streets",
    accessToken: API_KEY
  }).addTo(myMap);
    
  console.log(graphData)
   // Create a new marker cluster group
   var markers = L.markerClusterGroup();
  
   // Loop through data
   for (var i = 0; i < graphData.length; i++) {
  
     // Set the data location property to a variable
     var latitude = graphData[i].Latitude;
     var longitude = graphData[i].Longitude;
  
     // Check for location property
     if (latitude && longitude) {
  
       // Add a new marker to the cluster group and bind a pop-up
       markers.addLayer(L.marker([latitude, longitude])
         .bindPopup("Primary Type: " + graphData[i].Primary_Type + "<br> Ward: " + graphData[i].Ward + "<br> Police District: " + graphData[i].Police_Districts + " | Police Beats: " + graphData[i].Police_Beats)).on('mouseover',function(ev) {
          ev.target.openPopup(graphData[i].Primary_Type);
      //  markers.on('mouseover',function(ev) {
      //     ev.target.openPopup(graphData[i].priceoff);
       });
     }
  
   }
  
   // Add our marker cluster layer to the map
   myMap.addLayer(markers);
   
   // Load kml file
   var runLayer = omnivore.kml('/static/doc.kml')
   .on('ready', function() {
       map.fitBounds(runLayer.getBounds());
       if (layer.feature.properties.styleUrl === '#PolyStyle00') {
        // See Leaflet path layers options
        // http://leafletjs.com/reference-1.0.3.html#path
        layer.setStyle({
          color: '#ff6e6e6e', // More red than green and blue => redish color
          weight: 4 
        });
    }
   })
   .addTo(myMap);


    