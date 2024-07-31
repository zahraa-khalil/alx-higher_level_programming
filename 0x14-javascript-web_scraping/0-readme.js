#!/usr/bin/node

const fs = require('fs');
const argument = process.argv[2];

fs.readFile(argument, 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
