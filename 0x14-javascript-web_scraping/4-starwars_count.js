#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterID = 18;

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error('Error occurred while making the request:', err);
  } else if (response.statusCode !== 200) {
    console.error('Error:', response.statusCode);
  } else {
    const data = JSON.parse(body).results;
    const moviesWithWedgeAntilles = data.filter((film) => {
      return film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterID}/`);
    });

    console.log(moviesWithWedgeAntilles.length);
  }
});
