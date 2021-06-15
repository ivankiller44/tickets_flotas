var express = require('express');

var app = express();

// Rewrite rule for angular
// app.use('/', express.static(__dirname + '/public'));
app.use(express.static(__dirname + '/dist'));
app.get('/assets', function(req, res){
    res.sendFile(__dirname + '/dist/assets');
});
app.get('/*', function(req, res){
    res.sendFile(__dirname + '/dist/angular-tickets-flotas/index.html');
});

var port = process.env.PORT || 4200;
app.listen(port, function(){
    console.log('server running on port ' + port + '.');
})
