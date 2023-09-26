#!/usr/bin/node

/* Import the 'request' module */
const request = require('request');
const movieId = process.argv[2];
const urlApi = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

/* Make an asynchronous HTTP GET request to the Star Wars API */
request(urlApi, async function (error, response, body) {
  const arr = [];

  if (error) {
    console.log(error);
  } else {
    const film = JSON.parse(body);
    /* Iterate through the 'characters' array in the movie data */
    for (let i = 0; i < film.characters.length; i++) {
      arr.push(myCharacter(film.characters[i]));
    }
  }
  /* Use Promise.all to wait for all promises to resolve */
  let actors = await Promise.all(arr);

  actors = actors.map((actor) => JSON.parse(actor).name);
  actors.forEach((actor) => console.log(actor));
});

function myCharacter (thisCharacter) {
  return new Promise((resolve, reject) => {
    request(thisCharacter, function (error, response, body) {
      if (error) {
        reject(error);
      }
      resolve(body);
    });
  });
}
