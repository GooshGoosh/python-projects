'''
Todo list web app using Flask
'''


from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__, template_folder="templates")


todos = [{"task": "Sample Todo", "done": False}]


@app.route("/")
def index():
    """Render the index.html template.

    Returns:
        str: Return the specified html template.
    """
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    """Add a task to the todos list.

    Returns:
        redirect obj: Redirect to the specified html template.
    """
    todo = request.form['todo']
    todos.append({"task": todo, "done": False})
    return redirect(url_for("index"))


@app.route("/edit/<int:task_index>", methods=["GET", "POST"])
def edit(task_index):
    """Edits a task in the todos list.

    Args:
        task_index (int): The index of the task that is to be edited.

    Returns:
        redirct obj: Redirect to the specified html template.
        str: Return the specified html template.
    """
    todo = todos[task_index]
    if request.method == "POST":
        todo['task'] = request.form['todo']
        return redirect(url_for("index"))

    return render_template("edit.html", todo=todo, index=task_index)


@app.route("/check/<int:task_index>")
def check(task_index):
    """Mark a task in the todos list as 'complete' or 'incomplete'.

    Args:
        task_index (int): The index of the task to be checked.

    Returns:
        redirect obj: Redirect to the specified html template.
    """
    todos[task_index]['done'] = not todos[task_index]['done']
    return redirect(url_for("index"))


@app.route("/delete/<int:task_index>")
def delete(task_index):
    """Deletes a task from the todos list.

    Args:
        task_index (int): The index of the task to be deleted.

    Returns:
        redirect obj: Redirect to the specified html template.
    """
    del todos[task_index]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
