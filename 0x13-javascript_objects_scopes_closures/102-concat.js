#!/usr/bin/node

const fs = require('fs');

// Get the file paths from the command-line arguments
const [fileA, fileB, fileC] = process.argv.slice(2);

// Check if all arguments are provided
if (!fileA || !fileB || !fileC) {
  console.log('Usage: node concat-files.js <source1> <source2> <destination>');
  process.exit(1);
}

// Read the contents of the first source file
fs.readFile(fileA, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading ${fileA}:`, err);
    return;
  }

  // Read the contents of the second source file
  fs.readFile(fileB, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${fileB}:`, err);
      return;
    }

    // Concatenate the data from both files
    const concatenatedData = data1 + data2;

    // Write the concatenated data to the destination file
    fs.writeFile(fileC, concatenatedData, (err) => {
      if (err) {
        console.error(`Error writing to ${fileC}:`, err);
        return;
      }
      console.log(`Successfully concatenated ${fileA} and ${fileB} into ${fileC}`);
    });
  });
});
