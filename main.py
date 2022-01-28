from flask import render_template, redirect, url_for, request
from forms import RateMovieForm, AddMovie
from flask_bootstrap import Bootstrap
from database import Movie, app, db
from search_movies import search_movies


Bootstrap(app)


@app.route("/")
def home():
    if request.args.get("id"):
        movie_to_delete_id = request.args.get("id")
        movie_to_delete = Movie.query.get(movie_to_delete_id)
        db.session.delete(movie_to_delete)
        db.session.commit()
        return redirect(url_for("home"))
    all_movies = db.session.query(Movie).all()
    all_movies.sort(key=lambda movie: movie.rating, reverse=True)
    for movie in all_movies:
        movie.ranking = all_movies.index(movie) + 1
    # for index in range(len(all_movies)):              # Apenas outro modo, mas com o mesmo resultado
        # all_movies[index].ranking = index + 1
    db.session.commit()
    return render_template("index.html", all_movies=all_movies)


@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    form = RateMovieForm()
    movie_to_update = Movie.query.get(id)
    if form.validate_on_submit():
        movie_to_update.rating = form.new_rating.data
        movie_to_update.review = form.new_review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form, movie_to_edit=movie_to_update.title)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        movie_title = form.movie_title.data
        movies_result = search_movies(movie_title)
        return render_template("select.html", movies=movies_result)
    return render_template("add.html", form=form)


@app.route("/select")
def select():
    add_new_movie = Movie(
        title=request.args.get("title"),
        year=request.args.get("year"),
        description=request.args.get("descr"),
        rating=request.args.get("rating"),
        img_url=request.args.get("img"),
    )
    db.session.add(add_new_movie)
    db.session.commit()
    movie_id = Movie.query.filter_by(title=request.args.get("title")).first()
    movie_id = movie_id.id
    return redirect(url_for("edit", id=movie_id))


if __name__ == '__main__':
    app.run(debug=True)
