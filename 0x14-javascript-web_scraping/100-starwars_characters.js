#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const i of characters) {
      request(i, function (err, resp, b) {
        if (err) {
          console.error('error:', err);
        } else {
          console.log(JSON.parse(b).name);
        }
      });
    }
  }
});
