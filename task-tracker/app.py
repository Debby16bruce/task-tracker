from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tasks", methods=["GET", "POST"])
def task_list():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
    return render_template("tasks.html", tasks=tasks)

@app.route("/delete/<int:index>")
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect(url_for("task_list"))

if __name__ == "__main__":
    app.run(debug=True)
 
