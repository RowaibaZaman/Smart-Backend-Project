from app import create_app, db
from sqlalchemy import text
from flask import jsonify

app = create_app()

with app.app_context():
    try:
        db.create_all()
        db.session.execute(text("SELECT 1")) 
        print("Database connection successful!")
    except Exception as e:
        print(f"Database connection failed: {e}")



if __name__ == '__main__':
    app.run(debug=True)
