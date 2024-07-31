#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];

const URL = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(URL, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  console.log(body.title);
});
