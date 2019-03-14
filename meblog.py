

from app import app, db
from app.models import User, Post

#shell context used for API
@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Post':Post}
