from flask import Flask, render_template, request
import pandas as pd
import random

app = Flask(__name__)

# Load CSV files
flights_df = pd.read_csv('data/flights.csv')
price_bands_df = pd.read_csv('data/price_bands.csv')
accommodations_df = pd.read_csv('data/accommodations.csv')

def get_upcoming_trips():
    # Filter flights for upcoming trips (for simplicity, not filtering by date here)
    return flights_df.to_dict('records')

def get_random_accommodation():
    # Return a random accommodation recommendation
    record = accommodations_df.sample(n=1).to_dict('records')[0]
    return record

def ai_based_recommendations():
    # Simulate AI-based space travel suggestions (e.g., filter flights based on some logic)
    recommended = flights_df[flights_df['class'] == 'Luxury Cabin'].to_dict('records')
    # In a real scenario, you might run a recommendation algorithm here
    return recommended

@app.route('/')
def home():
    # Home page displays random accommodation recommendations
    accommodation = get_random_accommodation()
    return render_template('home.html', accommodation=accommodation)

@app.route('/dashboard')
def dashboard():
    upcoming_trips = get_upcoming_trips()
    ai_recommendations = ai_based_recommendations()
    return render_template('dashboard.html', 
                           upcoming_trips=upcoming_trips, 
                           ai_recommendations=ai_recommendations)

if __name__ == '__main__':
    app.run(debug=True)
