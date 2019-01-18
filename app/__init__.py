
# Where we're importing the packedges form

from flask import Flask
#from flask_debug import Debug
from config import Config
#databases
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#Debug(app)
#app.run(debug=True)

from app import routes, models
