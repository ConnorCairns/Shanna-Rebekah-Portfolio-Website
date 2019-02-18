# Shanna Rebekah Portfolio Website

A-level computer science coursework, photography website created with Flask, Bootstrap 4 and React.

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
export shanna_db="sqlite:///name.db"
export shanna_secret_key="secret key"
export shanna_aws_access="S3 public key"
export shanna_aws_secret="S3 private key"

```

#### Windows
```
control panel
system and security
system
advanced system settings
environment variables
```

