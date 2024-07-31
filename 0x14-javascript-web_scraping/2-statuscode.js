#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];

request(URL, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  console.log('code:', res.statusCode);
});
