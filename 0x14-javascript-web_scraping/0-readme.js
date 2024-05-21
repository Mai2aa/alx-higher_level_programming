#!/usr/bin/node
const fs = require('fs');
function readFile (filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf8');
    console.log(content);
  } catch (error) {
    console.error(`Error: ${error}`);
  }
}
if (process.argv.length < 3) {
  console.log('Usage: node script.js <file_path>');
} else {
  const filePath = process.argv[2];
  readFile(filePath);
}
