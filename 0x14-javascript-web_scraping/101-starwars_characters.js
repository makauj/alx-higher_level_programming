#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api';
const film = process.argv[2];

if (process.argv.length > 2) {
  request(`${url}/films/${film}/`, (error, response, body) => {
    if (error) {
      console.log(error);
    }
    const charactersURL = JSON.parse(body).characters;
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (error, res, body) => {
          if (error) {
            reject(error);
          }
          resolve(JSON.parse(body).name);
        });
      }));

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(error => console.log(error));
  });
}
