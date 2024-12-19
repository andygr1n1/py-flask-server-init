from flask import Flask, render_template, jsonify
from flask_cors import CORS
from routes.routes_heroes import HeroRoutes
from helpers.test_connection import test_db_connection
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, template_folder='.')

CORS(app)

DATABASE_URI = os.getenv('DATABASE_URI')
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()


# Call the function to test the connection
test_db_connection(engine, session)

@app.route('/')
def index():
    return render_template('./index.html')

# get heroes
hero_routes = HeroRoutes(app, session)

if __name__ == '__main__':
    app.run(debug=True, port=5000)