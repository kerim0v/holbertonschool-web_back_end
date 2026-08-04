import fs from 'fs';

const readDatabase = (filePath) => new Promise((resolve, reject) => {
  fs.readFile(filePath, (err, data) => {
    if (err) {
      reject(new Error(err.message));
      return;
    }

    const fileLines = data.toString('utf-8').trim().split('\n');
    const studentGroups = {};

    for (const line of fileLines.slice(1)) {
      const studentRecord = line.split(',');
      const firstName = studentRecord[0];
      const field = studentRecord[studentRecord.length - 1];

      if (!studentGroups[field]) {
        studentGroups[field] = [];
      }
      studentGroups[field].push(firstName);
    }

    resolve(studentGroups);
  });
});

export default readDatabase;
