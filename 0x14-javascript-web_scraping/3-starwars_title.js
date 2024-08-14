#!/usr/bin/node
/* Prints the title of a Star Wars movie where the episode number matches a given integer. */
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, function (err, rs, body) {
  if (err) console.error('Error:', err);
  else console.log(JSON.parse(body).title);
});
