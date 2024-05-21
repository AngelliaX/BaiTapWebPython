from flask import Flask
from Controllers import Routes


app = Flask(__name__,template_folder='Views/templates', static_folder='Views/static')

# app = Flask(__name__,template_folder='TEMP-Frontend/CHAPGPT')


app.register_blueprint(Routes.mod)

if __name__ == '__main__':
    app.run(host="localhost", port=5000)