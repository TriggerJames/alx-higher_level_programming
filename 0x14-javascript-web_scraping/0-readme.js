#!/usr/bin/node

const fs = require('fs');

// Import the built-in Node.js 'fs' module.

fs.readFile(process.argv[2], 'utf8', function (error, content) {
 
  if (error) {
    console.error('Error reading the file:', error);
  } else {
    console.log(content);
  }
});
