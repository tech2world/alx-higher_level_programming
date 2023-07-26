#!/usr/bin/node
const request = require('request');

// get url from command line
const url = process.argv[2];

request.get(url, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
