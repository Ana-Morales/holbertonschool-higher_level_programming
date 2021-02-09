#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const ans = {};
    const obj = JSON.parse(body);
    for (const i of obj) {
      if (i.completed) {
        if (!ans[i.userId]) {
          ans[i.userId] = 1;
        } else {
          ans[i.userId] += 1;
        }
      }
    }
    console.log(ans);
  }
});
