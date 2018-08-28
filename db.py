from app import db, start
print("Importing db...")
db.create_all(app=start())
print("Created database!")