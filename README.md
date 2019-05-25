# Buying Credit Frontend
Our Frontend is based on a Python Flask Server and made with the CSS Framework [materialize.css](https://github.com/Dogfalo/materialize)

## Dev Setup
```bash
python3 -m venv venv/
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

## Production Setup
```bash
gunicorn --bind 0.0.0.0:8000 wsgi
```

