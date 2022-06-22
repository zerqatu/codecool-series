from flask import Flask, render_template, request, jsonify
from data import queries
from dotenv import load_dotenv
import math


load_dotenv()
app = Flask('codecool_series')


@app.route('/base.html')
def base():
    return render_template('base.html')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/shows')
@app.route('/shows/most-rated')
def most_rated():
    order_by = request.args.get("order-by")
    order_type = request.args.get("order-type")
    if not (order_by or order_type):
        order_by = "Rating"
        order_type = "desc"
    page = request.args.get("page")
    if page:
        current_page = int(page)
    else:
        current_page = 0
    headers = ["Title", "Year", "Runtime", "Rating", "Genres", "Trailer", "Homepage"]
    shows = queries.most_rated_shows(current_page, order_by, order_type)
    last_page = math.ceil(len(queries.count_entries()) / 15)
    return render_template('most-rated.html', shows=shows, headers=headers, current_page=current_page,
                           last_page=last_page, order_by=order_by, order_type=order_type)


@app.route('/tv-show/<id>')
@app.route('/show/<id>')
def show_details(id):
    show = queries.show_details(id)
    seasons = queries.get_seasons(id)
    return render_template('show-details.html', show=show, seasons=seasons)


@app.route('/ratings')
def avg_ratings():
    ratings = queries.get_avg_ratings()
    return render_template('avg-ratings.html', ratings=ratings)


@app.route('/ordered-shows')
def ordered_shows():
    return render_template('ordered-shows.html')


@app.route('/api/ordered-shows')
def api_asc():
    asc, desc = queries.get_all_ordered_shows()
    return jsonify(asc=asc, desc=desc)


@app.route('/actors')
def get_actors():
    return render_template('actors.html')


@app.route('/api/actors')
def actors_api():
    actors = queries.get_actors()
    return jsonify(actors=actors)


@app.route('/api/shows-by-actor/<actor_id>')
def shows_by_actor(actor_id):
    shows = queries.get_shows_by_actor(actor_id)
    return jsonify(shows=shows)


@app.route('/birthday-actors')
def birthday_actors():
    actors = queries.get_birthday_actors()
    return render_template('birthday-actors.html', actors=actors)


def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
