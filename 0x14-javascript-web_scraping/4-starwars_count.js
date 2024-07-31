#!/usr/bin/node
const request = require('request');

const URL = process.argv[2];
const character = 'https://swapi-api.alx-tools.com/api/people/18/';
let charactersArray = [];

request(URL, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  const data = body.results;
  data.map(x => {
    const result = x.characters.filter(link => link === character);
    charactersArray = charactersArray.concat(result);
    return charactersArray.length;
  });
  console.log(charactersArray.length);
});
