from . import admin
from ..decorators import admin_required
from flask_login import login_required
from flask import render_template

@admin.route('/')
@admin_required
@login_required
def admin():
  return render_template('admin/index.html')
