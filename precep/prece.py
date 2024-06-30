from flask import Blueprint, render_template

bp = Blueprint('prece', __name__, url_prefix='/prece')

@bp.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@bp.route('/documentos')
def documentos():
    return render_template('documentos.html')

@bp.route('/labor')
def labor():
    return render_template('labor.html')

@bp.route('/historia')
def historia():
    return render_template('historia.html')

@bp.route('/novedades')
def novedades():
    return render_template('novedades.html')
