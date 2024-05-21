#!/usr/bin/node
const fs = require('fs');
function writeToFile (filePath, content) {
  try {
    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`Written to file: ${filePath}`);
  } catch (error) {
    console.error(`Error: ${error}`);
  }
}
if (process.argv.length < 4) {
  console.log('Usage: node script.js <file_path> <content>');
} else {
  const filePath = process.argv[2];
  const content = process.argv[3];
  writeToFile(filePath, content);
}
