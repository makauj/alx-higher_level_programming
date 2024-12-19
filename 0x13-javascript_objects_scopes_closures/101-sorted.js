#!/usr/bin/node

const { dict } = require('./101-data.js');

const invertedDict = {};

for (const userId in dict) {
  const occurrences = dict[userId].length;

  if (invertedDict[occurrences]) {
    invertedDict[occurrences].push(Number(userId));
  } else {
    invertedDict[occurrences] = [Number(userId)];
  }
}

console.log(invertedDict);
