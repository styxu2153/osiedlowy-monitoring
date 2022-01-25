from flask import render_template, redirect, url_for, flash, request
from flags import bp
import requests
import csv
import time
import os, sys, logging
from app import app, db
from models import Flaga
from flags.forms import AddressForm

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

def http_GET():
    data = []   
    flagi  = Flaga.query.all()
    
    for flaga in flagi:
        data.append([flaga.discord_name, flaga.domain_name, get_html(flaga.domain_name)])

    for row in data:
        flaga = Flaga.query.filter_by(domain_name=row[1]).first()
        flaga.status = row[2]
        db.session.commit()

@bp.route('/')
def index():
    flagi = Flaga.query.all()
    
    return render_template('index.html', flagi=flagi)

@bp.route('/address-add', methods=['GET', 'POST'])
def address_add():
    form = AddressForm()
    
    if form.validate_on_submit():
        discord_name = form.name.data
        domain_link = "http://" + form.domain_name.data
        
        new_address = Flaga(discord_name=discord_name, domain_name=domain_link)
        db.session.add(new_address)
        db.session.commit()
        flash('Registered website successfully!')
        return redirect(url_for('flags.index'))

    return render_template('address_add.html', form=form)

@bp.route('/refresh')
def refresh():
    http_GET()
    return redirect(url_for('flags.index'))

'''
@bp.route('/address-migrate')
def address_migrate():
    with open('adresy.csv', encoding='UTF-8') as f:
        reader = csv.reader(f)
    
        for row in reader:
            flaga = Flaga(discord_name=row[0], domain_name=row[1])
            db.session.add(flaga)
            db.session.commit()
'''
