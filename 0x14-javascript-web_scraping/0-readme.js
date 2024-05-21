#!/usr/bin/node
const fs = require('fs');
function read_file(file_path) {
	try {
		const content = fs.readFileSync(file_path, 'utf8');
		console.log(content);
	}
	catch(error) {
		console.error(`Error: ${error}`);
	}
}
if (process.argv.length < 3) {
	console.log('Usage: node script.js <file_path>');
}
else {
	const file_path = process.argv[2];
	read_file(file_path);
}
