from flask import Flask, render_template, redirect, url_for, flash
from flask_crontab import Crontab
from config import Config
import time
import requests
import os, sys, logging
import csv

logging.basicConfig(filename="test.log", level=logging.DEBUG)

app=Flask(__name__)
app.config.from_object(Config)
crontab = Crontab(app)

from help import bp as help_bp
app.register_blueprint(help_bp)

def encode_link(link: str) -> str:
    link = link.strip()
    link = link.split("//")
    domain_name = link[1]
    link[1] = str(domain_name.encode('idna').decode('utf-8'))
    return "//".join(link)

def get_html(link: str):
    try:
        page = requests.get(encode_link(link), verify=False)
        return page.status_code
    except requests.exceptions.ConnectionError as err:
        return "CONNECTION ERROR"

@crontab.job(minute="*/5")
def http_GET():
    data = []   
    with open("flagi.txt") as flagi:
        for link in flagi:
            data.append([link.strip(), get_html(link)])
    
    with open('flagi.csv', 'w', encoding='UTF-8', newline="") as f:
        writer = csv.writer(f)
        
        for row in data:
            writer.writerow(row)

@app.route('/')
def index():
    address_data = {}
    with open("flagi.csv", 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        for row in reader:
            address_data[row[0]] = row[1]
    return render_template('index.html', statuses=address_data)

@app.route('/test')
def test():
    return f'<h1>Chwilowo nic tu nie ma, platforma testowa</h1> <a href={ url_for("index") }>COFNIJ</a>'
    

if __name__=="__main__":
    app.run()
