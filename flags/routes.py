from flask import render_template, redirect, url_for, flash, request
from flags import bp
from flask_crontab import Crontab
import requests
import csv
import time
import os, sys, logging
from app import app

crontab = Crontab(app)

#logging.basicConfig(filename="test.log", level=logging.DEBUG)

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

@crontab.job(minute="*/8")
def http_GET():
    data_to_work = []
    data = []   
    with open("adresy.csv", 'r', encoding="UTF-8") as f:
        reader = csv.reader(f)

        for row in reader:
            data_to_work.append([row[0].strip(), row[1].strip()])
    
    for row in data_to_work:
        data.append([row[0], row[1], get_html(row[1])])

    with open('flaga.csv', 'w', encoding='UTF-8', newline="") as f:
        writer = csv.writer(f)
        
        for row in data:
            writer.writerow(row)

@bp.route('/')
def index():
    address_data = []
    with open("flaga.csv", 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        for row in reader:
            address_data.append([*row])
    return render_template('index.html', statuses=address_data)

@bp.route('/address-add', methods=['GET', 'POST'])
def address_add():
    if request.method == "POST":
        discord_name = request.form['discord_name']
        domain_name = request.form['domain_name']
        domain_link = "http://" + domain_name
        
        with open('adresy.csv', 'a', encoding='UTF-8') as f:
            writer = csv.writer(f)
            writer.writerow([discord_name, domain_link])
        
        return redirect(url_for('flags.index'))

    return render_template('address_add.html')

