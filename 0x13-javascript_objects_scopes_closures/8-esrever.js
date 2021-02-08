#!/usr/bin/node
exports.esrever = function (list) {
  const arr = [];
  while (list.length) {
    arr.push(list.pop());
  }
  return arr;
};
