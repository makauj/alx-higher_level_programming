#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const tasks = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (tasks[todo.userId]) {
        tasks[todo.userId] += 1;
      } else {
        tasks[todo.userId] = 1;
      }
    }
  });
  console.log(tasks);
});
