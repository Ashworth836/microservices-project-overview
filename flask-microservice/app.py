from flask import Flask, jsonify, request
from models import db, Rating

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/book_ratings_db'
db.init_app(app)

# POST endpoint for submitting a rating
@app.route('/title/user-ratings', methods=['POST'])
def submit_rating():
    data = request.get_json()
    title = data.get('title')
    rating = data.get('rating')

    # Logic to create and save a new rating in the database
    new_rating = Rating(title=title, rating=rating)
    db.session.add(new_rating)
    db.session.commit()

    return jsonify({'message': 'Rating submitted successfully'}), 201

# GET endpoint for retrieving all rating information for a book
@app.route('/title/user-ratings', methods=['GET'])
def get_ratings():
    title = request.args.get('title')

    # Logic to query the database and calculate average rating
    ratings = Rating.query.filter_by(title=title).all()
    average_rating = calculate_average_rating(ratings)

    return jsonify({
        'title': title,
        'average_rating': average_rating,
        'ratings': [rating.rating for rating in ratings]
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

