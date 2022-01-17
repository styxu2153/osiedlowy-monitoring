import configparser
import os

config = configparser.ConfigParser()
config.read('settings.ini')

domena = config['XD']['domena']



#os.system('apt update')
#os.system('apt upgrade')

#os.system('apt install python3-pip python3-dev python3-venv build-essential libssl-dev libffi-dev python3-setuptools')
#os.system('apt install nano')
#os.system('apt remove apache2')
#os.system('apt install nginx')
#os.system('systemctl enable nginx')
#os.system('systemctl start nginx')

#os.system('rm -r /var/www/html')

#os.system('
#os.system('
#os.system('
#os.system('



plik_nginxa = ''
plik_nginxa_template = open('NAZWA_STRONY').readlines()
for l in plik_nginxa_template:
	if l.strip().startswith('server_name'):
		l=l.replace('NAZWA_STRONY', domena)
	plik_nginxa += l

with open("/etc/nginx/sites-available/{}".format(domena), "w") as file1:
    file1.write(plik_nginxa)

os.system('sudo ln -s /etc/nginx/sites-available/{} /etc/nginx/sites-enabled/'.format(domena))

plik_gunicorn = open('flaga.service').read()
with open('/etc/systemd/system/flaga.service2', "w") as f:
	f.write(plik_gunicorn)

print(plik_nginxa)
