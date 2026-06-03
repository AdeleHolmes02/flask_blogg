from flask import Flask, render_template
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


if __name__ == "__main__":
    app.run(debug=True)