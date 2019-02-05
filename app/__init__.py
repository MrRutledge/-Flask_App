
# Where we're importing the packedges form

from flask import Flask
#from flask_debug import Debug
from config import Config
#databases
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#flask-login
from flask_login import LoginManager



app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'


#Debug(app)
#app.run(debug=True)

from app import routes, models
