# -*- coding: utf-8 -*-

# homework 18
# shlom41k

"""
# Module for creating application, database and manager
"""


from flask import Flask
from flask_migrate import Migrate, MigrateCommand, Manager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

from settings import DATABASE_URI


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI    # URL address for database
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = False      # Auto commit
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False      # Significant overhead

db = SQLAlchemy(app)

if not database_exists(db.engine.url):
    create_database(db.engine.url)
    print("Created")

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    pass