from flask import Flask, request, send_from_directory

app = Flask(__name__)
app.secret_key = 'some_secret'
from app import views
