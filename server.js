

const PORT = 5000;

// var gpio = require("pi-gpio");
var pin = 8;
// Requires
var express = require('express');
var app = express();
var bodyParser = require('body-parser');
app.use(bodyParser.json());       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
  extended: true
}));
var PythonShell = require('python-shell');



app.get('/', function(res) {
	// res.sendfile("public/index.html");
});

// var options = {
//   mode: 'text',
//   pythonPath: 'path/to/python',
//   pythonOptions: ['-u'],
//   scriptPath: 'path/to/my/scripts',
//   args: ['value1', 'value2', 'value3']
// };

app.post('/change-val', function(req, res) {
	res.status(200).end();
	console.log("TURN ON");
	var red = req.body.redVal;
	var green = req.body.greenVal;
	var blue = req.body.blueVal;
	var options = {
		//pythonPath: 'path/to/python',
		//scriptPath: 'path/to/my/scripts',
		args: [red, green, blue];
	};

	PythonShell.run('makePipe.py', options, function (err, results) {
		if (err) throw err;
		// results is an array consisting of messages collected during execution
		console.log('results: %j', results);
	});


	/*gpio.open(pin, "output", function(err) {		// Open pin 16 for output 
		gpio.write(pin, 1, function() {			// Set pin 16 high (1) 
		    gpio.close(pin);
		    console.log("ON!");						// Close pin 16 
		});
	});*/
});


app.post('/turn-off', function(req, res) {
	res.status(200).end();
	// console.log(req);
	console.log(req.body);

	gpio.open(pin, "output", function(err) {		// Open pin 16 for output 
		gpio.write(pin, 0, function() {			// Set pin 16 high (1) 
		    gpio.close(pin);	
		    console.log("off");					// Close pin 16 
		});
	});
});


// Serve files from public
app.use(express.static(__dirname + '/public'));

//Start server
app.listen(PORT);
console.log('server is live on port ' + PORT);
