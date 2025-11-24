from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1 style='color: #4CAF50;'>Hello Render! 🚀</h1><p>Your Flask App is Running Successfully.</p>"

@app.route("/about")
def about():
    return "<h2 style='color: #2196F3;'>About Page</h2><p>This is a colorful Flask app example!</p>"

if __name__ == "__main__":
    app.run(debug=True)
