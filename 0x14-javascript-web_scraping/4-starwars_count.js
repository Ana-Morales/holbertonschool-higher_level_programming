#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    let count = 0;
    const movies = JSON.parse(body).results;
    for (const i in movies) {
      for (const j in movies[i].characters) {
        if (movies[i].characters[j].search('18') > 0) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
