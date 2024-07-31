#!/usr/bin/node

const fs = require('fs');
const fileName = process.argv[2];
const writeData = process.argv[3];

fs.writeFile(fileName, writeData,'utf8', (err, data) => {
  if (err) throw err;
});
