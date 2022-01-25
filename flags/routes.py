from flask import render_template, redirect, url_for, flash, request
from flags import bp
import os, sys, logging
from app import app, db, crontab
from models import Flaga
from flags.forms import AddressForm
import asyncio, aiohttp
from pprint import pprint

#logging.basicConfig(filename="test.log", level=logging.DEBUG)

def encode_link(link: str) -> str:
    link = link.strip()
    link = link.split("//")
    domain_name = link[1]
    link[1] = str(domain_name.encode('idna').decode('utf-8'))
    return "//".join(link)

async def get_http(session: aiohttp.ClientSession, flaga):
    code = ""
    try:
        async with session.get(flaga.domain_name, timeout=3) as response:
            code = response.status
            html = await response.text()
    except:
        code = "110"
    return [flaga.discord_name, flaga.domain_name, code]

async def gather_https():
    flagi  = Flaga.query.all()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for flaga in flagi:
            tasks.append(get_http(session=session, flaga=flaga))

        htmls = await asyncio.gather(*tasks)
        return htmls
    
@crontab.job(minute="*")
def http_GET():
    if not os.path.isfile('run_condition.txt'):
        file_cond = open("run_condition.txt", "x")
        logging.warning('File created!')   
        
        data = asyncio.run(gather_https())
        
        for row in data:
            flaga = Flaga.query.filter_by(domain_name=row[1]).first()
            flaga.status = row[2]
            db.session.commit()
        file_cond.close()
        os.remove('run_condition.txt')
        logging.warning('File removed!')
    else:
        logging.warning('File  exists!')
    
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



