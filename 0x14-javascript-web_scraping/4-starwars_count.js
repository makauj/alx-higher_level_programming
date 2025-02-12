#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  request(process.argv[2], function (error, response, body) {
    if (error) {
      console.log(error);
    } else if (body) {
      const filmsChar = JSON.parse(body).results.filter(
        x => x.characters.find(y => y.match(/\18\/?$/))
      );
      console.log(filmsChar.length);
    }
  });
}
