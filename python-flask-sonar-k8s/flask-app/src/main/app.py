from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    title = "I have successfully built a Flask application using Python"
    msg = "This application is deployed on to Kubernetes using Argo CD"
    return render_template("index.html", title=title, msg=msg)


if __name__ == "__main__":
    app.run(debug=True)
