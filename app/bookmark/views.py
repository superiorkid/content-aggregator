from flask import request, url_for, redirect, flash, render_template, abort
from . import bookmark
from ..models import Bookmark, User
from flask_login import login_required, current_user
from .. import db


@bookmark.route('/')
@login_required
def bookmark_item():
  # ordered item by descending order
  bookmark = current_user.bookmarks.order_by(Bookmark.timestamp.desc()).all()

  return render_template('bookmarks.html', bookmark=bookmark)


@bookmark.route('/add')
@login_required
def add():
  blog_name = request.args.get('name')
  blog_img_url = request.args.get('img')
  title = request.args.get('title')
  link = request.args.get('link')
  posted = request.args.get('posted')

  bookmarks = Bookmark(blog_name= blog_name, blog_img_url=blog_img_url, title=title, link=link, posted=posted, user=current_user)
  db.session.add(bookmarks)
  db.session.commit()

  flash('Item Saved Successfully', 'success')
  return redirect(url_for('bookmark.bookmark_item'))


@bookmark.route('/<id>/delete')
@login_required
def delete(id):
  item = Bookmark.query.filter_by(id=id).first()

  if item:
    db.session.delete(item)
    db.session.commit()
    flash('Item Deleted Successfully', 'danger')
    return redirect(url_for('bookmark.bookmark_item'))

  abort(404, description='Resources not found')



