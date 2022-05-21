from ..models import OAuth
from .. import db

def merge_users(merge_into, merge_from):
  assert merge_into != merge_from
  OAuth.query.filter_by(user=merge_from).update({'user_id': merge_into.id})
  db.session.delete(merge_from)
  db.session.commit()
  return merge_into