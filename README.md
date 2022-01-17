# flaga_test

# 1. Login do serwera.

```
ssh nazwa_uzytkownika@adres_ip
```


# 2. Uaktualniamy paczki.

```
apt update
apt upgrade
```

# 3. Instalujemy git'a.


```
apt install git
cd /var/www
git clone https://github.com/lukasz-test/flaga.git
cd flaga
python3 xD.py
```



python3 -m venv flagaenv
source flagaenv/bin/activate

export FLASK_APP=app.py

apt install nano
nano settings.ini
pip3 install -r requirements.txt
pip3 install wheel
pip3 install gunicorn

python3 xd.py


sudo systemctl start flaga.service
sudo systemctl daemon-reload
systemctl restart nginx
sudo systemctl restart flaga.service


