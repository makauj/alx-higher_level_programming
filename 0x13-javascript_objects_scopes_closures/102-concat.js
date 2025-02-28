#!/usr/bin/node

const fs = require('fs');

// Get the file paths from the command-line arguments
const [fileA, fileB, fileC] = process.argv.slice(2);

// Check if the files exist and are files
if (
  fs.existsSync(fileA) &&
  fs.statSync(fileA).isFile() &&
  fs.existsSync(fileB) &&
  fs.statSync(fileB).isFile() &&
  fileC !== undefined
) {
  // Read the contents of the files and write them to the third file
  const dataA = fs.readFileSync(fileA, 'utf8');
  const dataB = fs.readFileSync(fileB, 'utf8');
  const stream = fs.createWriteStream(fileC);

  // Write the contents of the files to the third file
  stream.write(dataA);
  stream.write(dataB);
  stream.end();
}
