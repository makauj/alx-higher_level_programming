#!/usr/bin/node

const fs = require('fs');
const filename = ProcessingInstruction.argv(2);
fs.readFile(filename, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
