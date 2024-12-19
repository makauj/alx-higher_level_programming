#!/usr/bin/node

const fs = require('fs');

// Get the file paths from the command-line arguments
const [file1, file2, destFile] = process.argv.slice(2);

// Check if all arguments are provided
if (!file1 || !file2 || !destFile) {
  console.log('Usage: node concat-files.js <source1> <source2> <destination>');
  process.exit(1);
}

// Read the contents of the first source file
fs.readFile(file1, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading ${file1}:`, err);
    return;
  }

  // Read the contents of the second source file
  fs.readFile(file2, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${file2}:`, err);
      return;
    }

    // Concatenate the data from both files
    const concatenatedData = data1 + data2;

    // Write the concatenated data to the destination file
    fs.writeFile(destFile, concatenatedData, (err) => {
      if (err) {
        console.error(`Error writing to ${destFile}:`, err);
        return;
      }
      console.log(`Successfully concatenated ${file1} and ${file2} into ${destFile}`);
    });
  });
});
