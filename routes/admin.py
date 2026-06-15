from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from models.models import db, User
from .utils import admin_required


admin_bp = Blueprint('admin', __name__, url_prefix='/admin')
equipo_bp = Blueprint("equipo", __name__, url_prefix="/equipo")

@admin_bp.route('/')
@login_required
@admin_required
def dashboard():
    return render_template('dashboard_admin.html')


# ---------------------------
# CRUD USUARIOS
# ---------------------------
@admin_bp.route('/users')
@login_required
@admin_required
def users_list():
    users = User.query.order_by(User.id.asc()).all()
    return render_template('users/list.html', users=users)


@admin_bp.route('/users/create', methods=['GET', 'POST'])
@login_required
@admin_required
def users_create():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        role = request.form.get('role', 'user')
        password = request.form.get('password', '').strip()

        if not username or not password:
            flash("Usuario y contraseña son obligatorios.", "danger")
            return render_template('users/form.html', mode="create")

        if User.query.filter_by(username=username).first():
            flash("Ese usuario ya existe.", "warning")
            return render_template('users/form.html', mode="create")

        u = User(username=username, role=role)
        u.set_password(password)
        db.session.add(u)
        db.session.commit()
        flash("Usuario creado correctamente.", "success")
        return redirect(url_for('admin.users_list'))

    return render_template('users/form.html', mode="create")


@admin_bp.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
@login_required
@admin_required
def users_edit(user_id):
    u = User.query.get_or_404(user_id)

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        role = request.form.get('role', 'user')
        password = request.form.get('password', '').strip()

        if not username:
            flash("El usuario no puede estar vacío.", "danger")
            return render_template('users/form.html', mode="edit", u=u)

        # validar duplicado (excepto el mismo)
        existing = User.query.filter_by(username=username).first()
        if existing and existing.id != u.id:
            flash("Ese nombre de usuario ya está en uso.", "warning")
            return render_template('users/form.html', mode="edit", u=u)

        u.username = username
        u.role = role
        if password:
            u.set_password(password)  # solo si se escribe algo

        db.session.commit()
        flash("Usuario actualizado.", "success")
        return redirect(url_for('admin.users_list'))

    return render_template('users/form.html', mode="edit", u=u)


@admin_bp.route('/users/<int:user_id>/delete', methods=['POST'])
@login_required
@admin_required
def users_delete(user_id):
    u = User.query.get_or_404(user_id)

    # Opcional: evitar que se borre el último admin
    if u.role == "admin":
        admins = User.query.filter_by(role="admin").count()
        if admins <= 1:
            flash("No puedes eliminar el último administrador.", "danger")
            return redirect(url_for('admin.users_list'))

    db.session.delete(u)
    db.session.commit()
    flash("Usuario eliminado.", "info")
    return redirect(url_for('admin.users_list'))


@equipo_bp.route("/")
@login_required
def dashboard_equipo():
    return render_template("equipo/dashboard.html")
