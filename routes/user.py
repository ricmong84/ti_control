from flask import Blueprint, render_template
from flask_login import login_required, current_user

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/')
@login_required
def dashboard():
    if current_user.role != 'user':
        return "Acceso denegado"
    return render_template('dashboard_user.html')