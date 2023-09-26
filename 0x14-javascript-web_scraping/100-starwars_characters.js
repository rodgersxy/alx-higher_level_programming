#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const urlApi = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(urlApi, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const film = JSON.parse(body);
    for (let i = 0; i < film.characters.length; i++) {
      request(film.characters[i], function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          const actor = JSON.parse(body);
          console.log(actor.name);
        }
      });
    }
  }
});
