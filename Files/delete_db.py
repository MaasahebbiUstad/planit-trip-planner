import os

db_path = os.path.join("instance", "planit.db")

if os.path.exists(db_path):
    os.remove(db_path)
    print("Deleted planit.db from instance/")
else:
    print("planit.db not found in instance/")
