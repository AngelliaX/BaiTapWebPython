from flask import Blueprint, render_template, make_response, redirect, request, url_for
from Models.User import *
mod = Blueprint('routes', __name__)


todos = [{"task":"Sample Todo 1", "done":False},{"task":"Sample Todo 2", "done":False}]



@mod.route('/')
def index():
    print(request.cookies)
    if 'username' in request.cookies:
        return render_template("index.html", todos=todos)
    else:
        return redirect(url_for("routes.login"))




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




@mod.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if not username or not password:
            return render_template("login.html", noti="Vui lòng điền đủ")
        
        result = checkUser(username, password)
        
        if result is True:
            resp = make_response(redirect(url_for('routes.index')))
            resp.set_cookie('username', username, max_age=3*24*60*60)  # Set cookie to last 3 days
            return resp
        else:
            return render_template("login.html", noti=result)
    
    if 'username' in request.cookies:
        return redirect(url_for('routes.index'))
    
    return render_template("login.html")



@mod.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if not (username and password and confirm_password):
            return render_template("register.html", noti="Please fill in all fields")

        if password != confirm_password:
            return render_template("register.html", noti="Password and confirm password do not match")

        result = addUser(username, password)
        if result is True:
            return render_template("register.html", noti="Registration successful")
        else:
            return render_template("register.html", noti=result)

    if 'username' in request.cookies:
        return redirect(url_for('routes.index'))

    return render_template("register.html", noti=None)




@mod.route('/page2')
def page2():
    return render_template("page2.html")







@mod.app_errorhandler(404)
def error404(e):
    return 'Địa chỉ page này không tồn tại', 404




@mod.app_errorhandler(500)
def error500(e):
    return 'Lỗi không xác định', 500