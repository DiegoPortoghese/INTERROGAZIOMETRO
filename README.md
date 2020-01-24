# Todos
End algo
chat group in site 
bind data in site
conferme e chiusura event
index se vuoi , e controlli di registrazione

# Web App: School Interrogation Manager

## Descrizione del cliente
```
vorrei un sito che permetta di organizzare in modo equo, organizzato e sistematico i tanto famigerati "turni" per le interrogazioni scolastiche, 
sono uno studente del quinto anno presso un liceo scientifico, ma purtroppo non ho mai trovato una soluzione a questo problema...
ho provato generatori di numeri casuali, "ruote della fortuna" e analoghi ma né io,
né i miei compagni siamo mai riusciti a trovare qualcosa di veramente valido
va benissimo! 
Nel dettaglio pensavo ad un tool che permettesse di inserire l'elenco degli studenti, 
l'orario scolastico con le varie materie, 
il numero di alunni da interrogare per ogni turno e una serie di altri dettagli utili.
sostanzialmente l'applicazione dovrebbe utilizzare questa serie di informazioni 
per organizzare i turni in modo da distanziare le interrogazioni il più possibile per ogni studente, 
ma rendendo tale intervallo più o meno equo per tutti
vorrei anche avere la possibilità di visualizzare delle tabelle con gli interrogati per ogni ora della settimana, 
di avere la possibilità di salvare in locale e poi caricare dei profili contenenti le informazioni che dicevo nello scorso messaggio... 
tutte features che rendano più semplice l'utilizzo
per ora, io e la mia classe stiamo utilizzando questo sito https://wheelofnames.com/ praticamente con quello
facciamo le estrazioni per ogni turno e in dei file txt teniamo conto di tutti gli estratti
```

# How Install
## clonare la parte git
```
git clone #
```
## installare i pacchetti apt elencati nel file apt-requirements.txt
```
sudo apt-get install nomepacchetto
```
## creare virtualenv e installare pacchetti Python3 
```
virtualenv -p python3 virtualenv; source virtualenv/bin/activate
pip install -r ~/workingcopy/school_interrogation_manager/main/requirements.txt
cd ~/workingcopy/school_interrogation_manager/main
```
## struttura progetto
```
.
├── main //parte django
├── site //frontend nuxt
└── virtualenv
```
## creazione database e utente admin Django
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```
# Server nuxt.js
## install dependencies
```
npm install
```
## serve with hot reload at localhost:3000
```
npm run dev
```