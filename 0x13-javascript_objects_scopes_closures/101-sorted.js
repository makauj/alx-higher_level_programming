#!/usr/bin/node
const dict = require('./101-data.js').dict;

const newDict = {};

Object.getOwnPropertyNames(dict).forEach(occurences => {
  const occurences = dict[userId].length;
  if (newDict[dict[occurences]] === undefined) {
    newDict[occurences] = [parseInt(userId)];
  } else {
    newDict[occurences].push(parseInt(userId));
  }
});
console.log(newDict);