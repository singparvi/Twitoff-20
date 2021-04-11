"""SQLAlchemy Function and utility functions for TwitOFF"""

from flask_sqlalchemy import SQLAlchemy

# instantiate the Database
DB = SQLAlchemy()


class User(
    DB.Model):  # inheriting the DB.Model class and making a user class. This is how to create table in SQLAlchemy
    """Twitter User table that will correspond to tweets - SQLAlchemy syntax"""
    # create columns now
    id = DB.Column(DB.BigInteger, primary_key=True)  # id column (primary key)
    name = DB.Column(DB.String, nullable=False)  # name column

    def __repr__(self):
        return f'<User: {self.name}>'


class Tweet(DB.Model):
    """Tweet text data - associated with Users Table"""
    id = DB.Column(DB.BigInteger, primary_key=True)  # id column (primary key)
    text = DB.Column(DB.Unicode(300))
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey("user.id"),
                        nullable=False)  # lowercase user table is created therefore lowercase table
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))  # join tables, backref all of the tweets

    # user mapping
    # all the tweets are stored and tied to User object.
    def __repr__(self):
        return f'<Tweet: {self.text}>'
