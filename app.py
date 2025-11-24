from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# Simple in-memory list
todos = []

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple To-Do</title>
</head>
<body>
    <h1>📝 Simple To-Do List</h1>

    <form method="POST" action="/add">
        <input type="text" name="task" placeholder="Enter task..." required>
        <button type="submit">Add</button>
    </form>

    <h3>Tasks:</h3>
    <ul>
        {% for t in todos %}
            <li>
                {{ t }}
                <a href="/delete/{{ loop.index0 }}">
                    <button>Delete</button>
                </a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE, todos=todos)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        todos.append(task)
    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(todos):
        todos.pop(index)
    return redirect("/")

if __name__ == "__main__":
    app.run()
