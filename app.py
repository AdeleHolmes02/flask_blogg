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

    if post is None:
        return render_template("post.html", post=None)

    comments = database.get_comments_for_post(post_id)
    tags = database.get_tags_for_post(post_id)

    return render_template(
        "post.html",
        post=post,
        comments=comments,
        tags=tags
    )

@app.route("/posts/<int:post_id>/comments", methods=["POST"])
def add_comment(post_id):
    title = request.form["title"]
    body = request.form["body"]

    if not title or not body:
        post = database.get_post(post_id)
        comments = database.get_comments_for_post(post_id)
        tags = database.get_tags_for_post(post_id)
        error = "Comment title and comment text are required."

        return render_template(
            "post.html",
            post=post,
            comments=comments,
            tags=tags,
            comment_error=error
        )

    database.create_comment(post_id, title, body)

    return redirect(url_for("show_post", post_id=post_id))

@app.route("/posts/new", methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        tags = request.form["tags"]

        if not title or not body:
            error = "Title and body are required."
            return render_template("new_post.html", error=error)

        database.create_post(title, body, tags)

        return redirect(url_for("home"))

    return render_template("new_post.html")

@app.route("/tags/<tag_name>")
def posts_by_tag(tag_name):
    posts = database.get_posts_by_tag(tag_name)
    return render_template("tag.html", posts=posts, tag_name=tag_name)

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

@app.route("/posts/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    database.delete_post(post_id)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)