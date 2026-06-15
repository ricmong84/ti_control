from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from models.models import db, Ceco
from routes.utils import admin_required

ceco_bp = Blueprint('ceco', __name__, url_prefix='/ceco')

@ceco_bp.route('/')
@login_required
@admin_required
def list_ceco():
    q = request.args.get("q", "").strip()
    query = Ceco.query
    if q:
        like = f"%{q}%"
        query = query.filter(
            (Ceco.ceco.ilike(like)) |
            (Ceco.nombre_jefatura.ilike(like)) |
            (Ceco.area.ilike(like))
        )
    cecos = query.order_by(Ceco.ceco.asc()).all()
    return render_template('ceco/list.html', cecos=cecos, q=q)


@ceco_bp.route('/create', methods=['GET', 'POST'])
@login_required
@admin_required
def create_ceco():
    if request.method == 'POST':
        ceco = request.form.get('ceco', '').strip()
        nombre = request.form.get('nombre', '').strip()
        area = request.form.get('area', '').strip()

        if not ceco or not nombre or not area:
            flash("Todos los campos son obligatorios.", "danger")
            return render_template('ceco/form.html', mode="create")

        c = Ceco(ceco=ceco, nombre_jefatura=nombre, area=area)
        db.session.add(c)
        db.session.commit()
        flash("CECO creado correctamente.", "success")
        return redirect(url_for('ceco.list_ceco'))

    return render_template('ceco/form.html', mode="create")


@ceco_bp.route('/<int:ceco_id>/edit', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_ceco(ceco_id):
    c = Ceco.query.get_or_404(ceco_id)

    if request.method == 'POST':
        c.ceco = request.form.get('ceco', '').strip()
        c.nombre_jefatura = request.form.get('nombre', '').strip()
        c.area = request.form.get('area', '').strip()

        if not c.ceco or not c.nombre_jefatura or not c.area:
            flash("Todos los campos son obligatorios.", "danger")
            return render_template('ceco/form.html', mode="edit", c=c)

        db.session.commit()
        flash("CECO actualizado.", "success")
        return redirect(url_for('ceco.list_ceco'))

    return render_template('ceco/form.html', mode="edit", c=c)


@ceco_bp.route('/<int:ceco_id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_ceco(ceco_id):
    c = Ceco.query.get_or_404(ceco_id)
    db.session.delete(c)
    db.session.commit()
    flash("CECO eliminado.", "info")
    return redirect(url_for('ceco.list_ceco'))