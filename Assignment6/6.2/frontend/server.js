// server.js

// BASE SETUP
// =============================================================================

// call the packages we need
var express = require('express');        // call express
var app = express();                 // define our app using express
var bodyParser = require('body-parser');
var cors = require('cors');// call express
var superagent = require('superagent');

// configure app to use bodyParser()
// this will let us get the data from a POST
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(cors());

var port = process.env.PORT || 8080;        // set our port

var moment = require('moment');

// ROUTES FOR OUR API
// =============================================================================
var router = express.Router();              // get an instance of the express Router


router.use(function (req, res, next) {
    // do logging
    console.log('Something is happening.');
    next(); // make sure we go to the next routes and don't stop here
});

// test route to make sure everything is working (accessed at GET http://localhost:8080/api)
router.get('/serverConfig', function (req, res) {
    superagent.get('https://chat.berg-hansen.no/I3Root/websvcs/serverConfiguration')
        .end((error, response) => {
            if (!error && response) {
                res.json(response.body);
            } else {
                console.log('There was an error fetching from the api', error);
            }
        }
        );
});

router.post('/initChat', function (req, res) {
    var data = (req.body)
    superagent.post('https://chat.berg-hansen.no/I3Root/websvcs/chat/start').set('Content-Type', 'application/json').send(data).end((error, response) => {
        if (!error && response) {
            res.json({ message: response.body });
        } else {
            console.log('There was an error fetching from the api', error);
        }
    });//endof superagent
});//endof post


router.get('/pollChat/:id', function (req, res) {

    console.log(req.params.id)

    superagent.get('https://chat.berg-hansen.no/I3Root/websvcs/chat/poll/' + req.params.id).set('Content-Type', 'application/json').end((error, response) => {
        if (!error && response) {
            res.json({ message: response.body });
        } else {
            console.log('There was an error fetching from the api', error);
        }
    });//endof superagent
});//endof post

router.post('/sendMessage/:id', function (req, res) {
    var data = (req.body)
    superagent.post('https://chat.berg-hansen.no/I3Root/websvcs/chat/sendMessage/'  + req.params.id).set('Content-Type', 'application/json').send(data).end((error, response) => {
        if (!error && response) {
            res.json({ message: response.body });
        } else {
            console.log('There was an error fetching from the api', error);
        }
    });//endof superagent
});//endof post



// more routes for our API will happen here

// REGISTER OUR ROUTES -------------------------------
// all of our routes will be prefixed with /api
app.use('/api', router);

// START THE SERVER
// =============================================================================
app.listen(port);
console.log('Magic happens on port ' + port);