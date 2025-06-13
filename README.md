## Overview
The EduHub project is a backend database solution built with MongoDB for an online e-learning platform. Developed as part of the AltSchool of Data Engineering Tinyuka 2024 Second Semester Project Exam, this project showcases key MongoDB skills such as data modeling, database structuring, CRUD operations, aggregation, query performance tuning, and optimization techniques. It includes core functionalities like managing users, courses, enrollments, assessments, data analysis, and advanced search features.

## Project Goals
Design a scalable NoSQL database architecture tailored for an online learning platform.
Ensure data accuracy through validation rules and support high-performance querying.
Deliver clear documentation along with hands-on code demonstrations for practical understanding.

## Key Features
User Accounts: Supports user registration, login, and profile management for both learners and instructors.
Course Administration: Allows creation, structuring, and publishing of educational courses.
Enrollment Tracking: Monitors which students are enrolled in which courses and their learning progress.
Assignment Management: Handles assignment creation, student submissions, and grading workflows.
Data Insights & Reporting: Produces performance analytics and key learning statistics.
Smart Search & Filters: Enables users to search for courses using keyword filters and sorting options.

## Setup Instructions
Prerequisites
MongoDB v8.0 or higher 
Python 3.8+
Required Python libraries: pymongo, pandas, datetime

##  Installation
#### 1. Clone the Repository
git clone https://github.com/Siddiqalawan/mongodb-eduhub-project
cd mongodb-eduhub-project

#### 2. Set Up MongoDB
Install MongoDB and start the service.
Ensure it runs on "mongodb+srv://siddiqalawan:QHTmw1FYbuH4G9BT@alt-cluster.jjgozve.mongodb.net/?retryWrites=true&w=majority&appName=Alt-cluster"

#### 3. Install Dependencies
setup the requirement.txt file
pymongo



#### 4. Run the Jupyter Notebook
Open notebooks/eduhub_mongodb_project.ipynb in Jupyter Notebook.
Execute all cells to set up the database and run queries.

#### 5. Import Sample Data
Data imported in data/sample_data.json.





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
