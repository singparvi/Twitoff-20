"""Main app/routing for Twitter"""

from flask import Flask, render_template
from models import DB, User, Tweet
from twitter import *


# function to intialize the flask instance


# create the application
def create_app():
    """Create and configuring an instance of the Flask application"""

    # location of the Flask application and look in the current directory
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # with app.app_context():
    DB.init_app(app)

    # DB.init_app(app)  # initialize the DB with this application, DB is an instance of SQLAlchemy class

    # add a decorator
    @app.route('/')
    def root():
        # DB.drop_all()
        # DB.create_all()
        # app_user = User(id=1, name='app_user')
        # DB.session.add(app_user)
        # DB.session.commit()

        # return render_template('base.html',
        #                        title='Home',
        #                        users=User.query.all())
        return "text"
        # PS muse: when you are using Title = Home you are using Jinja2

    return app



#
# if __name__ == '__main__':
#     create_app().run()
