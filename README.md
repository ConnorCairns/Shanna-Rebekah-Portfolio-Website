# Shanna Rebekah Portfolio Website

Top quality A* A-level coursework

## How to run
Requires python 3.6 or above

### Linux
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python db.py
python run.py
```

### Windows
```
py -3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python db.py
python run.py
```

## Environment variables
For all features to work environment variables need to be set for email username and password, database URI and secret key
<br>
Web server will have to be restarted after adding

#### Linux
```
nano .bash_profile (or equivalent ex. .zshrc)
export email_username="email"
export email_pass="password"
```

#### Windows
```
control panel
system and security
system
advanced system settings
environment variables
```

