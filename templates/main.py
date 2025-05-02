from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle submitted form data here
        return "Form submitted successfully!"
    return render_template("ass1wadq.html")
