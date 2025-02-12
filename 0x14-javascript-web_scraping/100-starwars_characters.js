#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

if (process.argv.length > 2) {
  request('${url}/films/${process.argv[2]}/', function (error, response, body) {
    if (error) {
      console.log(error);
    }
    const data = JSON.parse(body).characters;
    charURL.forEach(element => {
      request(element, function (error, response, body) {
        if (error) {
          console.log(error);
        }
        console.log(JSON.parse(body).name);
      });
    });
});
}
