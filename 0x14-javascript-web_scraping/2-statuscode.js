#!/usr/bin/node
/* Display the status code of a GET request. */
const request = require('request');
const url = process.argv[2];

request.get(url, function (err, rs, body) {
  if (err) console.log('Error:', err);
  else console.log('code:', rs.statusCode);
});
