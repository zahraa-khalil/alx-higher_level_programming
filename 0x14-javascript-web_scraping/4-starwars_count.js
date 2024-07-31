#!/usr/bin/node
const request = require('request');

const URL = process.argv[2];
const character = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;

request(URL, (err, res, body) => {
  if (err) { return console.log(err); }

  if (!body.results || !Array.isArray(body.results)) {
    return console.log('Invalid or empty results.');
  }

  body.results.forEach(item => {
    if (item.characters.includes(character)) {
      count++;
    }
  });
  console.log(count);
});
