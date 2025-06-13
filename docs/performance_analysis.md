# PERFORMANCE ANALYSIS RESULTS

## Task 4.1: Complex Queries

### Courses with price between $50 and $200
| Course ID | Course Title                    | Price (USD) |
| --------- | ------------------------------- | ----------- |
| C003      | Unit Testing in Python          | \$100       |
| C005      | Computer Vision with OpenCV     | \$150       |
| C006      | Deep Learning with TensorFlow   | \$150       |
| C007      | Data Visualization with Seaborn | \$50        |
| C008      | Unit Testing in Python          | \$50        |
| C701      | Machine Learning Foundation     | \$150       |

## There are six courses within the specified price range, with prices ranging from $50 to $150. Notably, "Unit Testing in Python" appears twice at different price points, likely indicating different course levels like beginner and advanced.


### Users who joined in the last 6 months
| User ID | Name               | Date Joined         |
| ------- | ------------------ | ------------------- |
| U003    | Laura Davis        | 2024-12-17 15:39:44 |
| U004    | Luis Maxwell       | 2024-12-20 20:22:25 |
| U008    | Sharon Kent        | 2025-03-17 11:56:22 |
| U011    | Michelle Jones     | 2025-05-22 19:14:53 |
| U012    | David Weber        | 2025-04-02 03:02:00 |
| U013    | Heather Herrera    | 2025-01-29 01:26:34 |
| U015    | Emily Nixon        | 2025-02-02 06:50:52 |
| U016    | Barbara Sanders    | 2025-04-15 12:32:10 |
| U017    | Luke Suarez        | 2025-03-06 12:33:41 |
| U018    | Thomas Sanchez     | 2024-12-18 07:43:40 |
| U020    | Whitney Russo      | 2025-02-05 15:51:52 |
| U001    | Christine Williams | 2025-04-18 18:26:19 |
| U002    | Brian Fisher       | 2025-01-18 07:58:31 |
| U004    | Brandon Soto       | 2025-03-26 21:03:49 |
| U005    | Sarah Grant        | 2025-01-17 07:44:12 |
| U007    | Christopher Cross  | 2025-05-14 02:10:04 |
| U008    | James Owen         | 2025-03-22 00:39:40 |
| U010    | Noah Oconnor       | 2025-02-17 08:59:22 |

## This table shows 17 user records with their join dates, but some `User ID`s (e.g., U004, U008) appear more than once, indicating possible duplicates in the user data.


### Courses that have specific tags using $in operator
| Course ID | Course Title                | Tags                                              |
| --------- | --------------------------- | ------------------------------------------------- |
| C701      | Machine Learning Foundation | \['project-based', 'career-ready', 'interactive'] |


### Assignments with due dates in the next week.
| Assignment ID | Title                                         | Due Date                   |
| ------------- | --------------------------------------------- | -------------------------- |
| A001          | Assignment 1: Computer Vision with OpenCV     | 2025-06-18 14:26:57.405000 |
| A006          | Assignment 6: Unit Testing in Python          | 2025-06-16 14:26:57.411000 |
| A007          | Assignment 7: Building REST APIs with FastAPI | 2025-06-19 14:26:57.411000 |

### Three assignments are scheduled with due dates between June 16 and June 19, 2025. 

## Task 4.2: Aggregation Pipeline

#### Total enrollments per course
| Course ID | Total Enrollments |
| --------- | ----------------- |
| C006      | 4                 |
| C701      | 3                 |
| C001      | 3                 |
| C007      | 2                 |
| C004      | 2                 |
| C008      | 1                 |
| C005      | 1                 |
| C002      | 1                 |

### The course with the highest enrollment is C006 with 4 enrollments, followed by C701 and C001 with 3 enrollments each.


#### Average course rating.
| Course ID | Course Title                       | Avg Rating    |
| --------- | ---------------------------------- | ------------- |
| C001      | Kubernetes for Developers          | Not Available |
| C002      | Machine Learning with scikit-learn | Not Available |
| C003      | Unit Testing in Python             | Not Available |
| C004      | Kubernetes for Developers          | Not Available |
| C005      | Computer Vision with OpenCV        | Not Available |
| C006      | Deep Learning with TensorFlow      | Not Available |
| C007      | Data Visualization with Seaborn    | Not Available |
| C008      | Unit Testing in Python             | Not Available |
| C701      | Machine Learning Foundation        | Not Available |

### Data for average rating not available 

#### Total courses per category:
| Category         | Total Courses |
| ---------------- | ------------- |
| Web Development  | 4             |
| AI               | 2             |
| DevOps           | 1             |
| Cloud Computing  | 1             |
| Machine Learning | 1             |

### Web Development has the highest number of courses (4), indicating a strong focus in that category, followed by AI with 2 courses, while DevOps, Cloud Computing, and Machine Learning each have one course.


#### Average grade per student:
| Student ID | Average Grade |
| ---------- | ------------- |
| U013       | 85.0          |
| U016       | Not Available |

### Two students have an average grade of 85.0, while the rest have no available grade data.


#### Top Performing Student:
| Student ID | Average Grade | Total Submissions |
| ---------- | ------------- | ----------------- |
| U013       | 85.0          | 6                 |


#### Total student taught by each instructor
| Instructor ID | Students Taught |
| ------------- | --------------- |
| U007          | 1               |
| U008          | 1               |
| U001          | 2               |
| U003          | 2               |
| U012          | 2               |

### Instructor U001, U003, and U012 each taught 2 students, while U007 and U008 taught 1 student each.


#### Average course rating per instructor
| Instructor ID | Average Rating |
| ------------- | -------------- |
| U008          | Not Available  |
| U012          | Not Available  |
| U003          | Not Available  |
| U007          | Not Available  |
| U001          | Not Available  |

### Data not available

#### Revenue generated per instructor 
| Instructor ID | Total Revenue (USD) |
| ------------- | ------------------- |
| U012          | 600 USD             |
| U003          | 1050 USD            |
| U001          | 150 USD             |
| U008          | 600 USD             |
| U007          | 450 USD             |

### Instructor U003 has generated the highest revenue at \$1050, followed by U012 and U007 with \$600.

#### Most popular course categories
| Category         | Total Enrollments |
| ---------------- | ----------------- |
| AI               | 6                 |
| Web Development  | 5                 |
| Machine Learning | 3                 |
| DevOps           | 3                 |

### AI has the highest number of enrollment followed by web development whle machine leraning and devops has the least.

#### Student metrics engagement 
| User ID | Courses Enrolled | Submissions Made |
| ------- | ---------------- | ---------------- |
| U013    | 10               | 6                |
| U016    | 4                | 6                |
| U600    | 3                | 0                |


## Summary: Query Optimization & Execution Stats
| Metric                   | Details                                                                |
| ---------------------------- | -------------------------------------------------------------------------- |
| Execution Time           | `0 ms` – Query executed very quickly.                                      |
| Total Documents Examined | `2` – MongoDB only scanned 2 documents to find the result.                 |
| Index Used               | `title_1_category_1` – A compound index on `title` and `category` fields.  |
| Query Type               | `Regex search` on title + `Equality match` on category.                    |
| Winning Plan             | `IXSCAN` (Index Scan) → `FETCH` – Efficient use of index to retrieve docs. |
| Index Efficiency         | High – Query used the appropriate compound index and avoided full scan.    |

## Key Takeaways
Efficient Query: The index on title and category was effectively used, avoiding a collection scan.
Low Document Scan Count: Only 2 documents examined means minimal resource usage.
Fast Execution: With 0 ms runtime, this is a highly optimized query.
Regex Support in Index: The query used a case-insensitive regex on the title field, which was still index-supported thanks to the regex's nature and index ordering.


## Summary: Query Optimization on enrollments Collection
| Metric               | Details                                                 |
| ------------------------ | ----------------------------------------------------------- |
| Query Target         | `enrollments` collection                                    |
| Query Condition      | `student_id = "U004"`                                       |
| Execution Plan       | Index Scan (`IXSCAN`) followed by Fetch (`FETCH`)   |
| Index Used           | `student_id_1`                                              |
| Index Bounds         | `["U004", "U004"]` – Narrow scan using equality match       |
| Documents Examined   | Not shown, but very likely minimal due to index use     |
| Query Execution Time | Fast (exact time not specified, but near-instant)           |
| Optimization Flags   | All optimization limits (`maxScansToExplode`, etc.) avoided |


## Key Points
Efficient Index Use: The query used the student_id_1 index to quickly locate matching enrollment documents.
Precise Bounds: The bounds show that it searched exactly for "U004" with no range or full scan.
Minimal Cost: Since student_id is likely a low-cardinality field and the query is exact-match, MongoDB didn't need to scan many documents.

## Reference:
Optimization implementation can be found in the eduhub_mongodb_project.ipynb, under Task 5.

