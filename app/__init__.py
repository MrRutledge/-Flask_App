
# Where we're importing the packedge form

from flask import Flask
from flask_debug import Debug
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

Debug(app)
app.run(debug=True)

from app import routes
