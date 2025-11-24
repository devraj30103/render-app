from flask import Flask, request

app = Flask(__name__)

todos = []

@app.route("/")
def home():
    return "<h2>Simple To-Do List</h2><br>" + "<br>".join(todos)

@app.route("/add")
def add():
    task = request.args.get("task")
    if task:
        todos.append(task)
        return f"Added: {task}"
    return "Please add task like /add?task=BuyMilk"

@app.route("/list")
def list_tasks():
    return "<br>".join(todos)

if __name__ == "__main__":
    app.run(debug=True)
