#!/usr/bin/node
const arr = require('./100-data').list;
console.log(arr);
const map1 = arr.map((x, index) => x * index);
console.log(map1);
