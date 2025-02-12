#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const film = process.argv[2];
if (process.argv.length > 2) {
  request(`${url}/films/${film}/`, function (error, response, body) {
    if (error) {
      console.log(error);
      return;
    }

    if (response.statusCode === 200) {
      const data = JSON.parse(body).characters;

      data.forEach(element => {
        request(element, function (error, response, body) {
          if (error) {
            console.log(error);
            return;
          }

          if (response.statusCode === 200) {
            const character = JSON.parse(body);
            console.log(character.name);
          }
        });
      });
    } else {
      console.log('Error: Could not retrieve film data.');
    }
  });
}
