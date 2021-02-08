#!/usr/bin/node
const dic = require('./101-data').dict;
const newD = {};
for (const key in dic) {
  if (!newD[dic[key]]) {
    newD[dic[key]] = [];
  }
  newD[dic[key]].push(key);
}
console.log(newD);
