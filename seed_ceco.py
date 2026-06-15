print("SEED CECO INICIANDO...")
from app import app
from models.models import db, Ceco

DATA = [
    ("7007-03","Arturo Brenes Serrano","Auditoría Interna"),
    ("7007-13","Fabián Víquez Monge","Riesgos y Cumplimiento Normativo"),
    ("7007-02","Luis Antonio Monge Cordero","Gerencia General"),
    ("7007-31","Jairo Rodríguez Villalobos","Jurídico"),
    ("7007-51","Melissa Calderón Cerdas","Experiencia al Cliente"),
    ("7007-81","María Fernanda Poveda De Lemos","Gestión de Calidad"),
    ("7007-70","Jaime Barquero Fonseca","Capital Humano"),
    ("7007-70","Juan José Díaz Gómez","Capital Humano-Unidad de Compensación y Benficios"),
    ("7007-80","Kenneth Rojas Calderón","Dirección General de Servicios de Salud"),
    ("7007-22","Vanessa Morales Campos","Emergencias"),
    ("7007-24","Víctor Carballo Garrón","Imágenes Médicas"),
    ("7007-54","Gustavo Ruiz Jiménez","Seguros Comerciales"),
    ("7007-54","Marialaura Granados Gómez","Centro de Gestión de Seguros Personales"),
    ("7007-63","Susana Barquero Álvarez","Farmacia Ambulatoria"),
    ("7007-28","Evelyn Rojas Cordero","Farmacia Hospitalaria"),
    ("7007-62","Rosalyn Gayle Sandoval","Enfermería Ambulatorio"),
    ("7007-30","Marco Morales Alfaro","Enfermería Hospitalización"),
    ("7007-23","José Antonio Quirós Torres","Consulta Externa"),
    ("7007-29","Hellen Vásquez Aguilar","Clínica del Dolor"),
    ("7007-41","Gioconda Soto Arias","Rehabilitación"),
    ("7007-26","Karol Delgado Ramírez","Subdirección de Servicios Hospitalarios"),
    ("7007-20","Desiree Rojas Sterner","Hospitalización"),
    ("7007-25","Jessica Fernández Rodríguez","Hospitalización"),
    ("7007-21","Fernando Peralta","Servicios Quirúrgicos"),
    ("7007-80","Grettel Fallas Monge","Adquisiciones"),
    ("7007-13","Andrey Padilla Murcia","Finanzas"),
    ("7007-50","Diego Vargas Pérez","Planificación Estratégica"),
    ("7007-11","Gabriel Bolaños Rodríguez","Operaciones"),
]

with app.app_context():
    inserted = 0

    for ceco, nombre, area in DATA:
        exists = Ceco.query.filter_by(ceco=ceco, nombre_jefatura=nombre).first()
        if not exists:
            db.session.add(Ceco(ceco=ceco, nombre_jefatura=nombre, area=area))
            inserted += 1

    db.session.commit()
