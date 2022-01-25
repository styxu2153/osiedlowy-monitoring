from flask import Flask, render_template, redirect, url_for, flash, request
from flask_crontab import Crontab
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import csv

#logging.basicConfig(filename="test.log", level=logging.DEBUG)

app=Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
crontab = Crontab(app)

from help import bp as help_bp
app.register_blueprint(help_bp)

from flags import bp as flags_bp
app.register_blueprint(flags_bp)

import models

if __name__=="__main__":
    app.run()
