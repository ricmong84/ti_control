python -c "from app import app; from models.models import db,User;
with app.app_context():
 u=User.query.filter_by(username='admin').first()
 if not u:
  u=User(username='admin',role='admin'); u.set_password('admin1234'); db.session.add(u)
 else:
  u.role='admin'; u.set_password('admin1234')
 db.session.commit()
 print('✅ admin listo'); print([(x.id,x.username,x.role) for x in User.query.all()])"
