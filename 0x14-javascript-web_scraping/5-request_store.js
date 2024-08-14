#!/usr/bin/node
/* Gets the contents of a webpage and stores it in a file. */
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request(url, function (err, rs, body) {
  if (err) {
    console.error('Error:', err);
  }

  fs.writeFile(file, body, 'utf8', function (err) {
    if (err) {
      console.error('Error:', err);
    }
  });
});
