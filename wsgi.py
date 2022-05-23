from app import create_app, db
from app.models import User, Role, Bookmark, OAuth

app = create_app()


@app.shell_context_processor
def make_shell_context():
  return {'db': db, 'User': User, 'Role': Role, 'Bookmark': Bookmark, 'OAuth': OAuth}
