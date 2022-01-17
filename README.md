# flaga_test

#### 1. Login do serwera.

```
ssh nazwa_uzytkownika@adres_ip
```


#### 2. Uaktualniamy paczki (packages).

```
apt update
apt upgrade
```

#### 3. Git.


```
apt install git
cd /var/www
git clone https://github.com/lukasz-test/flaga.git
cd flaga
python3 xD.py
```

#### 4. Wewnątrz środowiska (env).

```
python3 -m venv flagaenv
source flagaenv/bin/activate

export FLASK_APP=app.py

nano settings.ini
pip3 install -r requirements.txt

python3 xd.py
```



#### 5. Restartujemy nignxa i serwisy.

```
sudo systemctl start flaga.service
sudo systemctl daemon-reload
systemctl restart nginx
sudo systemctl restart flaga.service
```

