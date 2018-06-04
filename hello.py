# from flask import Flask,render_template,request,url_for,session,redirect,flash
# import os
# from flask_nav import Nav
# from flask_nav.elements import *
# from flask_wtf import Form
# from wtforms import StringField,SubmitField
# from wtforms.validators import Required
# from flask_sqlalchemy import SQLAlchemy
# from flask_script import Shell
# from flask_migrate import Migrate,MigrateCommand
# from flask_script import Manager
# from flask_bootstrap import Bootstrap
# from flask_mail import Mail
#
# basedir=os.path.abspath(os.path.dirname(__file__))
# app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']=\
#     'sqlite:///'+os.path.join(basedir,'data.sqlite')
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
# app.config['MAIL_SERVER']='smtp.googlemail.com'
# app.config['MAIL_PORT']=587
# app.config['MAIL_USE_TLS']=True
# app.config['MAIL_USERNAME']=os.environ.get('MAIL_USERNAME')
# app.config['MAIL_PASSWORD']=os.environ.get('MAIL_PASSWORD')
# db=SQLAlchemy(app)
# app.config['SECRET_KEY']='hard to guess string'
# #manager=Manager(app)
# bootstrap=Bootstrap(app)
# nav=Nav()
# nav.init_app(app)
# migrate=Migrate(app,db)
# manager=Manager(app)
# manager.add_command('db',MigrateCommand)
# mail=Mail(app)
#
#
# class NameForm(Form):
#     name=StringField('What is your name?',validators=[Required()])
#     submit=SubmitField('Submit')
#
# class Role(db.Model):
#     __tablename__='roles'
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(64),unique=True)
#     users=db.relationship("User",backref='role',lazy='dynamic')
#     def __repr__(self):
#         return  self.name
#
# class User(db.Model):
#     __tablename__ = 'users'
#     id=db.Column(db.Integer,primary_key=True)
#     username=db.Column(db.String(64),unique=True,index=True)
#     role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
#     def __repr__(self):
#         return  self.username
#
# def make_shell_context():
#     return dict(app=app,db=db,User=User,Role=Role)
# manager.add_command("shell",Shell(make_context=make_shell_context()))
# @app.route('/',methods=['GET','POST'])
# def index():
#     form=NameForm()
#     if form.validate_on_submit():
#         user=User.query.filter_by(username=form.name.data).first()
#         if user is None:
#             user=User(username=form.name.data)
#             db.session.add(user)
#             session['know']=False
#         else:
#             session['konw']=True
#         session['name']=form.name.data
#         form.name.data=''
#         return  redirect(url_for('index'))
#     return render_template('index.html',form=form,name=session.get('name'),know=session.get('know',False))
#
# @app.route('/<name>')
# def user(name):
#     return render_template('user.html',name=name)
#
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'),404
#
# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'),500
#
# if __name__=='__main__':
#     manager.run()
