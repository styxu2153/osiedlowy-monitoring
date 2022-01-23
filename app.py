from flask import Flask, render_template, redirect, url_for, flash, request
from config import Config
from flask_crontab import Crontab

#logging.basicConfig(filename="test.log", level=logging.DEBUG)

app=Flask(__name__)
app.config.from_object(Config)

from help import bp as help_bp
app.register_blueprint(help_bp)

from flags import bp as flags_bp
app.register_blueprint(flags_bp)

if __name__=="__main__":
    app.run()
