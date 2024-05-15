from flask import Blueprint, render_template, make_response, redirect, request, url_for

mod = Blueprint('routes', __name__)


todos = [{"task":"Sample Todo 1", "done":False},{"task":"Sample Todo 2", "done":False}]



@mod.route('/')
def index():
    return render_template("index.html", todos=todos)

@mod.route('/add', methods=["POST"])
def add():
    todo = request.form['todo']
    todos.append({"task": todo, "done": False})
    return redirect(url_for("routes.index"))

@mod.route('/edit/<int:index>', methods=["GET", "POST"])
def edit(index):
    todo = todos[index]
    if request.method == "POST":
        todo['task'] = request.form["todo"]
        return redirect(url_for("routes.index"))
    else:
        return render_template("edit.html",todo = todo, index=index)

@mod.route('/check/<int:index>')
def check(index):
    todos[index]['done'] = not todos[index]['done']
    return redirect(url_for("routes.index"))

@mod.route('/delete/<int:index>')
def delete(index):
    del todos[index]
    return redirect(url_for("routes.index"))


@mod.route('/page2')
def page2():
    return render_template("page2.html")


@mod.route('/login')
def login():
	return render_template("index.html")

@mod.app_errorhandler(404)
def error404(e):
    return 'Địa chỉ page này không tồn tại', 404

@mod.app_errorhandler(500)
def error500(e):
    return 'Lỗi không xác định', 500