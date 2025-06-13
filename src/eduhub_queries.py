
# This Python script contains all MongoDB operations for the EduHub platform using PyMongo.


from pymongo import MongoClient, ASCENDING, TEXT, GEOSPHERE
from pymongo.errors import DuplicateKeyError, WriteError, WriteConcernError
from datetime import datetime, timedelta
import random
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the MongoDB connection string from environment
connection_string = os.getenv("MONGODB_URI")

client = MongoClient(connection_string)
db = client["eduhub"]

# Define collection handles for easy access
users_col = db["users"]
courses_col = db["courses"]
assignments_col = db["assignments"]
enrollments_col = db["enrollments"]




# 1. Find courses priced between $50 and $200

courses = courses_col.find({"price": {"$gte": 50, "$lte": 200}})
print("Courses priced between $50 and $200:")
for course in courses:
    print(f"{course['course_id']} - {course['title']} (${course['price']})")


# 2. Get users who joined in the last 6 months

six_months_ago = datetime.now() - timedelta(days=180)
recent_users = users_col.find({"date_joined": {"$gte": six_months_ago}})
print("\nUsers who joined in the last 6 months:")
for user in recent_users:
    print(f"{user['user_id']} - {user['first_name']} {user['last_name']} (Joined: {user['date_joined']})")


# 3. Find courses with specific tags using $in

target_tags = ["career-ready", "assignment-driven", "interactive"]
courses = courses_col.find({"tags": {"$in": target_tags}})
print("\nCourses with selected tags:")
for course in courses:
    print(f"{course['course_id']} - {course['title']} | Tags: {course['tags']}")


# 4. Retrieve assignments due in the next 7 days

today = datetime.now()
next_week = today + timedelta(days=7)
upcoming_assignments = assignments_col.find({
    "due_date": {"$gte": today, "$lte": next_week}
})
print("\nAssignments due in the next 7 days:")
for assignment in upcoming_assignments:
    print(f"{assignment['assignment_id']} - {assignment['title']} | Due: {assignment['due_date']}")


# 5. Count total enrollments per course

pipeline = [
    {"$group": {"_id": "$course_id", "total_enrollments": {"$sum": 1}}},
    {"$sort": {"total_enrollments": -1}}
]
results = list(enrollments_col.aggregate(pipeline))
print("\nTotal enrollments per course:")
for item in results:
    print(f"Course: {item['_id']} | Enrollments: {item['total_enrollments']}")


# 6. Average rating per course

pipeline = [
    {"$project": {"course_id": 1, "title": 1, "average_rating": {"$avg": "$ratings"}}},
    {"$sort": {"average_rating": -1}}
]
results = list(courses_col.aggregate(pipeline))
print("\nAverage course rating:")
for course in results:
    avg = course.get('average_rating')
    print(f"{course['course_id']} - {course['title']} | Avg Rating: {round(avg, 2) if avg else 'Not Available'}")


# 7. Group courses by category

pipeline = [
    {"$group": {"_id": "$category", "total_courses": {"$sum": 1}}},
    {"$sort": {"total_courses": -1}}
]
results = list(courses_col.aggregate(pipeline))
print("\nTotal courses per category:")
for item in results:
    print(f"{item['_id']} → {item['total_courses']} courses")


# 8. Average grade per student

pipeline = [
    {"$group": {"_id": "$user_id", "average_grade": {"$avg": "$grade"}}},
    {"$sort": {"average_grade": -1}}
]
results = list(submissions_col.aggregate(pipeline))
print("\nAverage grade per student:")
for student in results:
    avg = student.get('average_grade')
    print(f"Student: {student['_id']} → Avg Grade: {round(avg, 2) if avg else 'Not Available'}")


# 9. Completion rate by course

pipeline = [
    {"$match": {"status": "completed"}},
    {"$group": {"_id": "$course_id", "completed_count": {"$sum": 1}}},
    {"$lookup": {
        "from": "enrollments",
        "localField": "_id",
        "foreignField": "course_id",
        "as": "enrollments"
    }},
    {"$project": {
        "course_id": "$_id",
        "completed_count": 1,
        "total_enrolled": {"$size": "$enrollments"},
        "completion_rate": {
            "$cond": [
                {"$eq": [{"$size": "$enrollments"}, 0]},
                0,
                {"$multiply": [{"$divide": ["$completed_count", {"$size": "$enrollments"}]}, 100]}
            ]
        }
    }},
    {"$sort": {"completion_rate": -1}}
]
results = list(submissions_col.aggregate(pipeline))
print("\nCompletion rate by course:")
for item in results:
    print(f"{item['course_id']} → {round(item['completion_rate'], 2)}%")


# 10. Top 5 performing students

pipeline = [
    {"$group": {"_id": "$user_id", "average_grade": {"$avg": "$grade"}, "total_submissions": {"$sum": 1}}},
    {"$sort": {"average_grade": -1}},
    {"$limit": 5}
]
results = list(submissions_col.aggregate(pipeline))
print("\nTop Performing Students:")
for student in results:
    avg = student.get('average_grade')
    print(f"Student: {student['_id']} → Avg Grade: {round(avg, 2)} | Submissions: {student['total_submissions']}")


# 11. Instructor analysis – total students taught

pipeline = [
    {"$lookup": {
        "from": "courses",
        "localField": "course_id",
        "foreignField": "course_id",
        "as": "course_info"
    }},
    {"$unwind": "$course_info"},
    {"$group": {
        "_id": "$course_info.instructor_id",
        "total_students": {"$addToSet": "$user_id"}
    }},
    {"$project": {
        "instructor_id": "$_id",
        "total_students": {"$size": "$total_students"},
        "_id": 0
    }}
]
results = list(enrollments_col.aggregate(pipeline))
print("\nInstructor analysis – students taught:")
for item in results:
    print(f"Instructor: {item['instructor_id']} → Students Taught: {item['total_students']}")


# 12. Average course rating per instructor

pipeline = [
    {"$group": {"_id": "$instructor_id", "average_rating": {"$avg": "$rating"}}},
    {"$project": {"instructor_id": "$_id", "average_rating": 1, "_id": 0}}
]
results = list(courses_col.aggregate(pipeline))
print("\nAverage course rating per instructor:")
for item in results:
    rating = item.get('average_rating')
    print(f"{item['instructor_id']} → {round(rating, 2) if rating else 'Not Available'}")


# 13. Revenue generated per instructor

pipeline = [
    {"$lookup": {
        "from": "courses",
        "localField": "course_id",
        "foreignField": "course_id",
        "as": "course_info"
    }},
    {"$unwind": "$course_info"},
    {"$group": {
        "_id": "$course_info.instructor_id",
        "total_revenue": {"$sum": "$course_info.price"}
    }},
    {"$project": {"instructor_id": "$_id", "total_revenue": 1, "_id": 0}}
]
results = list(enrollments_col.aggregate(pipeline))
print("\nRevenue generated per instructor:")
for item in results:
    print(f"{item['instructor_id']} → {round(item['total_revenue'], 2)} USD")


# 14. Monthly enrollment trends

pipeline = [
    {"$group": {
        "_id": {"year": {"$year": "$enrolled_at"}, "month": {"$month": "$enrolled_at"}},
        "total_enrollments": {"$sum": 1}
    }},
    {"$sort": {"_id.year": 1, "_id.month": 1}}
]
results = list(enrollments_col.aggregate(pipeline))
print("\nMonthly enrollment trends:")
for item in results:
    year = item['_id']['year']
    month = item['_id']['month']
    total = item['total_enrollments']
    print(f"{year}-{str(month).zfill(2)} → {total} enrollments")


# 15. Most popular course categories

pipeline = [
    {"$lookup": {
        "from": "courses",
        "localField": "course_id",
        "foreignField": "course_id",
        "as": "course_info"
    }},
    {"$unwind": "$course_info"},
    {"$group": {
        "_id": "$course_info.category",
        "total_enrollments": {"$sum": 1}
    }},
    {"$sort": {"total_enrollments": -1}}
]
results = list(enrollments_col.aggregate(pipeline))
print("\nMost popular course categories:")
for item in results:
    print(f"Category: {item['_id']} → Enrollments: {item['total_enrollments']}")


# 16. Student engagement metrics


# 1. Number of courses enrolled per student
pipeline = [
    {"$group": {"_id": "$user_id", "courses_enrolled": {"$sum": 1}}},
    {"$project": {"user_id": "$_id", "courses_enrolled": 1, "_id": 0}}
]
courses_enrolled = list(enrollments_col.aggregate(pipeline))

# 2. Number of assignments submitted per student
pipeline = [
    {"$group": {"_id": "$user_id", "assignments_submitted": {"$sum": 1}}},
    {"$project": {"user_id": "$_id", "assignments_submitted": 1, "_id": 0}}
]
assignments_done = list(submissions_col.aggregate(pipeline))

# Combine engagement data
engagement = defaultdict(lambda: {"courses_enrolled": 0, "assignments_submitted": 0})
for item in courses_enrolled:
    uid = item["user_id"]
    engagement[uid]["courses_enrolled"] = item["courses_enrolled"]
for item in assignments_done:
    uid = item["user_id"]
    engagement[uid]["assignments_submitted"] = item["assignments_submitted"]

print("\nStudent Engagement Metrics:")
for user_id, metrics in engagement.items():
    print(f"User: {user_id} → Courses: {metrics['courses_enrolled']} | Submissions: {metrics['assignments_submitted']}")
