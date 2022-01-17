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

Tworzenie i aktywacja środowiska:
```
python3 -m venv flagaenv
source flagaenv/bin/activate
```

Tworzenie zmiennej:
```
export FLASK_APP=app.py
```

Edycja pliku z nazwą domeny. Po wywołaniu nano wpisz po spacji nazwę swojej domeny np (bez "www."): 
domena = nazwa_domeny.pl
```
nano settings.ini
```

Instalacja wymaganych bibliotek.
```
pip3 install -r requirements.txt
```

Uruchom skrypt przygotowujący hosting w serwerze.
```
python3 xd.py
```


sudo systemctl start flaga.service

#### 5. Restartujemy nignxa i serwisy.

```
sudo systemctl daemon-reload
systemctl restart nginx
sudo systemctl restart flaga.service
```


#### 6. Zmiana napisu.

Będąc w folderze flaga edytujemy zawartość pliku xd.txt.
```
cd /var/www/flaga
nano xd.txt
```

Przeładowujemy stronę.
```
sudo systemctl daemon-reload
systemctl restart nginx
sudo systemctl restart flaga.service
```



