
// controller
var app = {
init: function(){
	console.log('init');

// The radius scale for the centroids.
var r = d3.scale.sqrt()
    .domain([0, 1e6])
    .range([0, 10]);

// Our projection.

var xy = d3.geo.albersUsa();
$('body').click(function() {
  console.log('click');
  $('body').load('/');
});
var svg = d3.select("body").append("svg");
svg.append("g").attr("id", "states");
svg.append("g").attr("id", "state-centroids");

d3.json("../static/data/us-states.json", function(collection) {
  svg.select("#states")
    .selectAll("path")
      .data(collection.features)
    .enter().append("path")
      .attr("d", d3.geo.path().projection(xy));
});


// for every feature in the collection, plot it on the us map.
d3.json("../static/data/categories.json", function(collection) {
  svg.select("#state-centroids")
    .selectAll("circle")
      .data(collection.features
      .sort(function(a, b) { return b.properties.venues - a.properties.venues; }))

    .enter()
    .append("circle")

     
      .attr("transform", function(d) { return "translate(" + xy(d.geometry.coordinates) + ")"; })
      .attr("r", 10)

    .transition()
      .duration(1000)
     .delay(function(d, i) { return i * 50; })
      .attr("r", function(d) { return 10; }); // change total classes
});


// for every feature in the collection, plot it on the us map.
d3.json("../static/data/categories.json", function(collection) {
  svg.select("#state-centroids")
    .selectAll("circle")
    
     
      .attr('class', function(d) { return d.properties.skillset;  })

});
}
}
app.init();



