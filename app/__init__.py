from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# CONFIGURATION
# Not a real key 
app.config['SECRET_KEY'] = '033accb4ee4c8e91842f93c8565d89d3' #HEX(16) GENENERATED 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# ROUTES CONFIGURATION
from app import routes
