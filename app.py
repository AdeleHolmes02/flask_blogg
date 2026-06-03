from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)


@app.route("/")
def home():
    posts = database.get_all_posts()
    return render_template("index.html", posts=posts)


@app.route("/posts/<int:post_id>")
def show_post(post_id):
    post = database.get_post(post_id)
    return render_template("post.html", post=post)


@app.route("/posts/new", methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]

        if not title or not body:
            error = "Title and body are required."
            return render_template("new_post.html", error=error)

        database.create_post(title, body)

        return redirect(url_for("home"))

    return render_template("new_post.html")

@app.route("/posts/<int:post_id>/edit", methods=["GET", "POST"])
def edit_post(post_id):
    post = database.get_post(post_id)

    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]

        if not title or not body:
            error = "Title and body are required."
            return render_template("edit_post.html", post=post, error=error)

        database.update_post(post_id, title, body)

        return redirect(url_for("show_post", post_id=post_id))

    return render_template("edit_post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)