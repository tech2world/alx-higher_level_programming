#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const urlToRequest = process.argv[2];
const filePath = process.argv[3];

request.get({ url: urlToRequest, encoding: 'utf-8' }, (error, _response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
