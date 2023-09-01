from flask import render_template, request

from .import bp

@bp.route('/')
def index():
    return render_template('/index.html', page=request.blueprint)
