from flask import Blueprint, render_template, make_response, redirect, request, url_for
from Models.User import *
from Models.TodoList import *
mod = Blueprint('routes', __name__)
import time


# todos = [{"task":"Sample Todo 1", "done":False},{"task":"Sample Todo 2", "done":False}]



@mod.route('/')
def index():
    print(request.cookies)
    if 'username' in request.cookies:
        todos = get_todo_list(request.cookies["userId"])
        return render_template("index.html", todos=todos,
                                              username = request.cookies["username"],
                                              userId = request.cookies["userId"],
                                              time=time.time())
    else:
        return redirect(url_for("routes.login"))

@mod.route('/user/<int:id>', methods=["GET"])
def user(id):
    user = getUser(id)    
    return render_template("profile.html", user = user)



@mod.route('/addTodo', methods=["POST"])
def addTodo():
    try:
        print('called 1')
        id = request.form.get('todoId')
        title = request.form.get('todoTitle')
        data = request.form.get('description')
        status = request.form.get('status')
        userId = request.form.get('userId')
        print('called 2')
        insertTodo(id, title, data, status, userId)
        print('called 3')
        print(id, title, data, status, userId)
        return redirect(url_for("routes.index"))
    except Exception as e:
        return str(e)

@mod.route('/add', methods=["POST"])
def add():
    todo = request.form['todo']
    todos.append({"task": todo, "done": False})
    return redirect(url_for("routes.index"))

@mod.route('/editTodo', methods=["POST"])
def editTodo():
    id = request.form.get('todoId')
    title = request.form.get('todoTitle')
    data = request.form.get('description')
    status = request.form.get('status').replace('\n', '')
    updateTodo(title, data, status, id)
    return redirect(url_for("routes.index"))
    

# @mod.route('/edit/<int:index>', methods=["GET", "POST"])
# def edit(index):
#     todo = todos[index]
#     if request.method == "POST":
#         todo['task'] = request.form["todo"]
#         return redirect(url_for("routes.index"))
#     else:
#         return render_template("edit.html",todo = todo, index=index)


# @mod.route('/check/<int:index>')
# def check(index):
#     todos[index]['done'] = not todos[index]['done']
#     return redirect(url_for("routes.index"))

@mod.route('/deleteTodo', methods=["POST"])
def deleteTodo():
    id = request.form.get('id')
    removeTodo(id)
    return redirect(url_for("routes.index"))


# @mod.route('/delete/<int:index>')
# def delete(index):
#     del todos[index]
#     return redirect(url_for("routes.index"))




@mod.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if not username or not password:
            return render_template("login.html", noti="Vui lòng điền đủ thông tin!")
        
        result = checkUser(username, password)
        
        if result is True:
            user = getUserByNameAndPass(username, password)
            resp = make_response(redirect(url_for('routes.index')))
            resp.set_cookie('username', username, max_age=3*24*60*60)  # Set cookie to last 3 days
            resp.set_cookie('userId', str(user[0]), max_age=3*24*60*60)
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
            return render_template("register.html", noti="Vui lòng điền đủ thông tin!")

        if password != confirm_password:
            return render_template("register.html", noti="Mật khẩu và xác nhận mật khẩu phải trùng khớp nhau!")

        result = addUser(username, password)
        if result is True:
            return render_template("register.html", noti="Registration successful")
        else:
            return render_template("register.html", noti=result)

    if 'username' in request.cookies:
        return redirect(url_for('routes.index'))

    return render_template("register.html", noti=None)

@mod.route('/logout')
def logout():
    resp = make_response(redirect(url_for('routes.login')))
    resp.set_cookie('username', '', expires=0)
    return resp


@mod.route('/page2')
def page2():
    return render_template("page2.html")







@mod.app_errorhandler(404)
def error404(e):
    return 'Địa chỉ page này không tồn tại', 404




@mod.app_errorhandler(500)
def error500(e):
    return 'Lỗi không xác định', 500