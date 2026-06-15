from flask import Flask
from flask_login import LoginManager
from config import Config
from models.models import db, User
from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.user import user_bp
from routes.ceco import ceco_bp
from routes.entregas import entregas_bp
from routes.impresoras import impresoras_bp
from routes.inventario import inventario_bp
from routes.activos import activos_bp

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(entregas_bp)
app.register_blueprint(impresoras_bp)
app.register_blueprint(inventario_bp)
app.register_blueprint(activos_bp)


db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(user_bp)
app.register_blueprint(ceco_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)