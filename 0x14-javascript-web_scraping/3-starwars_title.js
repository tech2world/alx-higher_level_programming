#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiEndpoint = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiEndpoint, (err, response, body) => {
  if (err) {
    console.error('Error occurred while making the request:', err);
  } else if (response.statusCode !== 200) {
    console.error('Error:', response.statusCode);
  } else {
    const movieData = JSON.parse(body);
    console.log('Title:', movieData.title);
  }
});
