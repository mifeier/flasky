import os
from app import create_app,db
from app.models import User,Role
from flask_script import Manager,Shell,Server
from flask_migrate import Migrate,MigrateCommand
from flask_login import login_required

app=create_app(os.getenv('FLASK_CONFIG') or 'default')
manager=Manager(app)
migrate=Migrate(app,db)

def make_shell_context():
    return dict(app=app,db=db,User=User,Role=Role)
server=Server(host='0.0.0.0',port=5000)
manager.add_command('shell',Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    """Run the unit tests"""
    import unittest
    tests=unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

# @app.route('/')
# def index():
#     return '<h1>Hello World!</h1>'


# @app.route('/secret')
# @login_required
# def secret():
#     return 'Only authenticated users are allowed!'

if __name__=='__main__':
    manager.run()
