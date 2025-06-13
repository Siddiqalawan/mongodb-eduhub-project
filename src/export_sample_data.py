import json, os
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


# ✅ Custom JSON encoder to handle datetime
class JSONEncoderWithDate(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # Convert datetime to string
        return super().default(obj)

# Get the MongoDB connection string from environment
connection_string = os.getenv("MONGODB_URI")
client = MongoClient(connection_string)

# ✅ Make sure this matches your actual DB name
db = client["eduhub_db"]

# Output folder
output_dir = os.path.join("..", "data", "sample_data_json")
os.makedirs(output_dir, exist_ok=True)

collections = {
    "users": db["users"],
    "courses": db["courses"],
    "enrollments": db["enrollments"],
    "lessons": db["lessons"],
    "assignments": db["assignments"],
    "submissions": db["submissions"]
}

for name, collection in collections.items():
    data = list(collection.find({}, {"_id": 0}))  # exclude _id
    file_path = os.path.join(output_dir, f"{name}.json")
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4, cls=JSONEncoderWithDate)

print("✅ Export completed successfully.")
