

const PORT = 5000;

var gpio = require("pi-gpio");

// Requires
var express = require('express');
var app = express();
var bodyParser = require('body-parser');
app.use(bodyParser.json());       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
  extended: true
}));

app.get('/', function(res) {
	// res.sendfile("public/index.html");
});


app.post('/turn-on', function(req, res) {
	res.status(200).end();
	// console.log(req);
	console.log(req.body);

	gpio.open(8, "output", function(err) {		// Open pin 16 for output 
		gpio.write(8, 1, function() {			// Set pin 16 high (1) 
		    gpio.close(8);
		    console.log("ON!");						// Close pin 16 
		});
	});
});


app.post('/turn-off', function(req, res) {
	res.status(200).end();
	// console.log(req);
	console.log(req.body);

	gpio.open(8, "output", function(err) {		// Open pin 16 for output 
		gpio.write(8, 0, function() {			// Set pin 16 high (1) 
		    gpio.close(8);	
		    console.log("off");					// Close pin 16 
		});
	});
});


// Serve files from public
app.use(express.static(__dirname + '/public'));

//Start server
app.listen(PORT);
console.log('server is live on port ' + PORT);
