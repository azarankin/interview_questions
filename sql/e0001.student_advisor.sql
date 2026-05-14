/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/
SELECT si.roll_number as roll_number , si.name as name
FROM student_information si
JOIN faculty_information fi on si.advisor=fi.employee_id
WHERE (fi.gender LIKE('F') and fi.salary > 20000) or (fi.gender LIKE('M') and fi.salary > 15000)