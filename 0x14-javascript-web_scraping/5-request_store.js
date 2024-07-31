#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const URL = process.argv[2];
const fileName = process.argv[3];

request(URL, { json: true }, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  fs.writeFile(fileName, body, 'utf8', (err) => {
    if (err) throw err;
  });
});
