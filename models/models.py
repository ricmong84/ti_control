from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import UniqueConstraint
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # admin | user
    entregas = db.relationship('EntregaEquipo', backref='usuario', lazy=True)
    reportes_impresora = db.relationship('ReporteImpresora', backref='usuario', lazy=True)


    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Ceco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ceco = db.Column(db.String(20), nullable=False)
    nombre_jefatura = db.Column(db.String(150), nullable=False)
    area = db.Column(db.String(150), nullable=False)

    __table_args__ = (
        UniqueConstraint('ceco', 'nombre_jefatura', name='uq_ceco_jefatura'),
    )
    
    from datetime import datetime

class EntregaEquipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Seguridad / propiedad del registro
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Selección “Área” realmente apunta a un registro de Ceco (para autollenado)
    ceco_id = db.Column(db.Integer, db.ForeignKey('ceco.id'), nullable=False)

    edificio = db.Column(db.String(100), nullable=False)
    piso = db.Column(db.String(50), nullable=False)

    # Estos se autollenan desde Ceco, pero los guardamos para “foto” del momento
    area = db.Column(db.String(150), nullable=False)
    ceco = db.Column(db.String(20), nullable=False)
    jefatura = db.Column(db.String(150), nullable=False)

    nombre = db.Column(db.String(150), nullable=False)
    justificacion = db.Column(db.Text, nullable=False)
    equipo_actual = db.Column(db.String(200), nullable=False)

    fecha_entrega = db.Column(db.Date, nullable=False)

    observaciones = db.Column(db.Text, nullable=True)

    nueva_placa_sifa = db.Column(db.String(100), nullable=False)

    extension = db.Column(db.String(30), nullable=True)
    ubicacion_exacta = db.Column(db.String(250), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    
from datetime import datetime

from datetime import datetime

class Impresora(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(50), unique=True, nullable=False)
    serie = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(100), nullable=False)
    ubicacion = db.Column(db.String(200), nullable=False)
    servidor = db.Column(db.String(100), nullable=False)


class ReporteImpresora(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    impresora_id = db.Column(db.Integer, db.ForeignKey('impresora.id'), nullable=False)

    ip = db.Column(db.String(50), nullable=False)
    serie = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(100), nullable=False)
    ubicacion = db.Column(db.String(200), nullable=False)

    contacto = db.Column(db.String(150), nullable=False)
    extension = db.Column(db.String(50), nullable=True)
    descripcion = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    impresora = db.relationship("Impresora")
    


class SuministroImpresora(db.Model):
    __tablename__ = "suministro_impresora"

    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(50), nullable=False)          # MX-610, C748, etc.
    consumible = db.Column(db.String(120), nullable=False)     # Toner, Unidad Imagen...
    actual = db.Column(db.Integer, nullable=False, default=0)
    minimo = db.Column(db.Integer, nullable=False, default=0)
    maximo = db.Column(db.Integer, nullable=True)              # puede ser null
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint('modelo', 'consumible', name='uq_modelo_consumible'),
    )


class SuministroMovimiento(db.Model):
    __tablename__ = "suministro_movimiento"

    id = db.Column(db.Integer, primary_key=True)
    suministro_id = db.Column(db.Integer, db.ForeignKey("suministro_impresora.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    delta = db.Column(db.Integer, nullable=False)  # +1, -1, +5, etc.
    nota = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    suministro = db.relationship("SuministroImpresora")


class ActivoTI(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placa_sifa = db.Column(db.String(50), unique=True, nullable=False)
    serie_service_tag = db.Column(db.String(100), nullable=True)
    marca = db.Column(db.String(100), nullable=True)
    modelo = db.Column(db.String(150), nullable=True)
    tipo_equipo = db.Column(db.String(100), nullable=True)
    ip = db.Column(db.String(50), nullable=True)
    activo = db.Column(db.Boolean, default=True)


from datetime import datetime

class ReporteEquipo(db.Model):
    __tablename__ = "reporte_equipo"

    id = db.Column(db.Integer, primary_key=True)

    activo_id = db.Column(db.Integer, db.ForeignKey("activo_ti.id"), nullable=True)

    placa_sifa = db.Column(db.String(50), nullable=True)
    serie_service_tag = db.Column(db.String(100), nullable=True)
    marca = db.Column(db.String(100), nullable=True)
    modelo = db.Column(db.String(150), nullable=True)
    tipo_equipo = db.Column(db.String(100), nullable=True)
    direccion_ip = db.Column(db.String(50), nullable=True)

    ubicacion = db.Column(db.String(200), nullable=True)

    
    edificio = db.Column(db.String(150), nullable=True)
    sas = db.Column(db.String(100), nullable=True)

    usuario_reporta = db.Column(db.String(150), nullable=False)
    tecnico = db.Column(db.String(150), nullable=True)

    observaciones = db.Column(db.Text, nullable=False)
    extension = db.Column(db.String(50), nullable=True)
    fecha_reporte = db.Column(db.DateTime, default=datetime.utcnow)

    estado = db.Column(db.String(30), default="pendiente")
    fecha_atencion = db.Column(db.DateTime, nullable=True)

    activo_equipo = db.relationship("ActivoTI")
