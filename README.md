# mongodb-eduhub-project
This is second semester examination project for alt school


clone the repository
'''' bash
project repo: https://github.com/Siddiqalawan/mongodb-eduhub-project
''''

### STEP 01- Create a conda enviroment after opening the repository

### STEP 02: How to Get Started with MongoDB Atlas + PyMongo (Cloud Setup)
 Create a MongoDB Atlas Account and Cluster
 Create a Database User
 Configure Network Access (IP Whitelist)
 Get Your Connection String
 setup Your Python Environment for Atlas
 

### install the requirements 
pip install -r requirements.txt


3. Run `eduhub_queries.py` to populate and test features.

## 🧱 Schema Overview

- **Users**: Includes validation for email, roles, and required fields.
- **Courses**: Text search enabled on title, description, tags. Location data stored as GeoJSON.
- **Assignments**: Index on due_date for timely queries.
- **Enrollments**: Archiving logic for old data after 6 months.

## ⚙️ Key Queries & Features

- Full-text search across course fields.
- Personalized course recommendations (skills → tags).
- Location-based course recommendations (geo queries).
- Enrollment archiving logic.
- Performance-optimized queries with index support.

## 📊 Performance Results

| Query                          | Without Index | With Index |
|--------------------------------|---------------|------------|
| Title + Category Search        | > 0.5s        | < 0.1s     |
| Assignment due_date lookup     | ~ 0.3s        | ~ 0.01s    |
| Enrollments by student_id      | ~ 0.2s        | ~ 0.01s    |

## ❗Challenges Faced

- Case-insensitive matching slowed regex searches — solved via full-text indexing.
- Date-range queries were slow — solved with due_date index.
- Inconsistent schema — solved by enforcing validation rules.
