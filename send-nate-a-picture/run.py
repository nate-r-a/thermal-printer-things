#!flask/bin/python
from app import app
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.run(debug=False, host="0.0.0.0")
