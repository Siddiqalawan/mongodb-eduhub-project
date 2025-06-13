
# This Python script contains all MongoDB operations for the EduHub platform using PyMongo.
# It includes CRUD operations, performance tuning, error handling, text and geospatial search,
# recommendations, and data archiving functionalities.

from pymongo import MongoClient, ASCENDING, TEXT, GEOSPHERE
from pymongo.errors import DuplicateKeyError, WriteError, WriteConcernError
from datetime import datetime, timedelta
import random
import time


# Connect to MongoDB instance running locally

client = MongoClient("mongodb://localhost:27017/")
db = client["eduhub"]

# Define collection handles for easy access
users_col = db["users"]
courses_col = db["courses"]
assignments_col = db["assignments"]
enrollments_col = db["enrollments"]


# TEXT SEARCH FUNCTIONALITY - Create Text Index
# Enables full-text search across multiple fields

courses_col.create_index([
    ("title", TEXT),
    ("description", TEXT),
    ("tags", TEXT)
])

def search_courses_by_text(keyword):
    """Perform a full-text search on title, description, or tags."""
    results = courses_col.find({ "$text": { "$search": keyword } })
    for course in results:
        print(f"{course['title']} - {course['description'][:50]}...")


# RECOMMENDATION ENGINE - Based on user's skill match
# Uses aggregation to calculate matching tags

def recommend_courses(user_id):
    """Recommend courses based on intersection of user skills and course tags."""
    user = users_col.find_one({"user_id": user_id})
    if not user:
        print("User not found.")
        return

    user_skills = user["profile"]["skills"]

    # Aggregation pipeline to match and rank relevant courses
    pipeline = [
        { "$match": { "tags": {"$in": user_skills}, "is_published": True }},
        { "$addFields": {
            "matched_skills": { "$size": { "$setIntersection": ["$tags", user_skills] }}
        }},
        { "$sort": { "matched_skills": -1, "price": 1 }},
        { "$limit": 5 }
    ]

    recommendations = courses_col.aggregate(pipeline)
    for course in recommendations:
        print(f"{course['title']} (Matched Skills: {course['matched_skills']})")


# ARCHIVING OLD ENROLLMENTS
# Moves enrollments older than 6 months to archive

archived_col = db["archived_enrollments"]

def archive_old_enrollments():
    """Archive enrollments that were created more than 6 months ago."""
    six_months_ago = datetime.now() - timedelta(days=180)
    old_enrollments = list(enrollments_col.find({ "enrolled_on": { "$lt": six_months_ago } }))
    if old_enrollments:
        archived_col.insert_many(old_enrollments)
        ids = [e["_id"] for e in old_enrollments]
        enrollments_col.delete_many({ "_id": { "$in": ids } })
        print(f"Archived {len(old_enrollments)} records.")
    else:
        print("No records to archive.")


# GEOSPATIAL QUERIES - Course recommendations by location
# Updates course documents with random Abuja coordinates
# and creates a 2dsphere index to support geospatial search

courses_col.update_many(
    {},
    [{
        "$set": {
            "location": {
                "type": "Point",
                "coordinates": [
                    random.uniform(7.40, 7.60),  # Longitude
                    random.uniform(6.40, 6.70)   # Latitude
                ]
            }
        }
    }]
)

# Create 2dsphere index for geospatial queries
courses_col.create_index([("location", GEOSPHERE)])

def recommend_nearby_courses(coords, max_km=10):
    """Find published courses within a given radius (in kilometers)."""
    results = courses_col.find({
        "location": {
            "$near": {
                "$geometry": {
                    "type": "Point",
                    "coordinates": coords
                },
                "$maxDistance": max_km * 1000  # Convert km to meters
            }
        },
        "is_published": True
    })
    for course in results:
        print(f"{course['title']} - {course['category']}")


# PERFORMANCE ANALYSIS - Analyze execution time and cost
# Uses .explain() to examine query performance and index usage

def analyze_query_performance(query):
    """Use explain() to analyze MongoDB query performance."""
    explain = courses_col.find(query).explain()
    print("Execution Time (ms):", explain["executionStats"]["executionTimeMillis"])
    print("Documents Examined:", explain["executionStats"]["totalDocsExamined"])
    print("Index Used:", explain["queryPlanner"]["winningPlan"].get("inputStage", {}).get("indexName", "None"))


# ERROR HANDLING EXAMPLE - Catches various MongoDB errors
# Demonstrates duplicate key, validation, and write concern errors

try:
    users_col.insert_one({
        "_id": 123,  
        "user_id": "U001",
        "email": "duplicate@example.com",
        "first_name": "Error",
        "last_name": "Case",
        "role": "admin",  
        "date_joined": datetime.now()
    })
except DuplicateKeyError as e:
    print("Duplicate Key Error:", e)
except WriteError as e:
    print("Validation Error:", e)
except WriteConcernError as e:
    print("Write Concern Error:", e)
except Exception as e:
    print("General Error:", e)
