from flask import Flask,render_template,request,url_for
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from flask_script import Manager

app=Flask(__name__)
#manager=Manager(app)
bootstrap=Bootstrap(app)
nav=Nav()
nav.init_app(app)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<name>')
def user(name):
    return render_template('user.html',name=name)
if __name__=='__main__':
    app.run(debug=True)
