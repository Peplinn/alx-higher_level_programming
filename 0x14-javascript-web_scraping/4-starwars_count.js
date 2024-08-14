#!/usr/bin/node
/* Prints the number of movies where the character “Wedge Antilles” is present. */
const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18/';

request(apiUrl, function (err, rs, body) {
  if (err) {
    console.error('Error:', err);
    return;
  }

  const films = JSON.parse(body).results;
  let count = 0;
  films.forEach(film => {
    film.characters.forEach(character => {
      if (character.endsWith(characterId)) {
        count++;
      }
    });
  });
  console.log(count);
});
