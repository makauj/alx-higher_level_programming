#!/usr/bin/node
// import a dictionary of occurrences by userid and compute a new dictionary
// of user ids by occurrences
const dict = require('./101-data.js').dict;

const newDict = {};

Object.getOwnPropertyNames(dict).forEach((key) => {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [key];
  }
  newDict[dict[key]].push(key);
});
