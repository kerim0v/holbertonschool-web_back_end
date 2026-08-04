import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    const dbPath = process.argv[2];

    readDatabase(dbPath)
      .then((studentGroups) => {
        const lines = ['This is the list of our students'];
        const fields = Object.keys(studentGroups)
          .sort((a, b) => a.localeCompare(b, 'en', { sensitivity: 'base' }));

        for (const field of fields) {
          const students = studentGroups[field];
          lines.push(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
        }

        response.status(200).send(lines.join('\n'));
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    const dbPath = process.argv[2];
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(dbPath)
      .then((studentGroups) => {
        const students = studentGroups[major] || [];
        response.status(200).send(`List: ${students.join(', ')}`);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
