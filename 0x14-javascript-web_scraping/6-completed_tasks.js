#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];

let tasks = [
];
const completedTasksByUser = {};

request(URL, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }

  tasks = body;

  tasks.forEach(task => {
    if (task.completed) {
      if (completedTasksByUser[task.userId]) {
        completedTasksByUser[task.userId] += 1;
      } else {
        completedTasksByUser[task.userId] = 1;
      }
    }
  });

  console.log(completedTasksByUser);
});
