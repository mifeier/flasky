from flask import Flask,render_template,request,url_for,session,redirect
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask_script import Manager

app=Flask(__name__)
app.config['SECRET_KEY']='hard to guess string'
#manager=Manager(app)
bootstrap=Bootstrap(app)
nav=Nav()
nav.init_app(app)

class NameForm(Form):
    name=StringField('What is your name?',validators=[Required()])
    submit=SubmitField('Submit')
@app.route('/',methods=['GET','POST'])
def index():
    form=NameForm()
    if form.validate_on_submit():
        session['name']=form.name.data
        return  redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'))

@app.route('/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

if __name__=='__main__':
    app.run(debug=True)
