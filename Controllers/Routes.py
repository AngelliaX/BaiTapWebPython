from flask import Blueprint, render_template, make_response, redirect

mod = Blueprint('routes', __name__)


@mod.route('/')
def home():
    return render_template("index.html")

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