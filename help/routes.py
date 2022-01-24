from flask import render_template, redirect, request, url_for, flash
from help import bp
from help.forms import HelpForm
import csv

@bp.route('/help-add', methods=['GET', 'POST'])
def help_add():
    form = HelpForm()

    if form.validate_on_submit():
        user_name = form.name.data
        domain_name = form.domain_name.data

        with open('help.csv', 'a', encoding='UTF-8', newline="") as f:
            writer = csv.writer(f)

            data_to_insert = [user_name, domain_name]
            writer.writerow(data_to_insert)

        domain_link = "http://" + domain_name
        with open('./flagi.txt', 'a', encoding='UTF-8') as f:

            f.write("\n")
            f.write(domain_link)
            
        return redirect(url_for('help.help_list'))

    return render_template('help_add.html', form=form)


@bp.route('/help')
def help_list():
    help_data = {}

    with open('help.csv', 'r', encoding='UTF-8', newline="") as f: 
        reader = csv.reader(f)

        for row in reader:
            help_data[row[0]] = row[1]

    return render_template('help_list.html', help_data=help_data)