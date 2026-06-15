from app import app
from models.models import db, SuministroImpresora

DATA = [
    # Modelo, Consumible, Actual, Minimo, Maximo
    ("MX-610", "Toner", 8, 5, 8),
    ("MX-610", "Unidad Imagen", 2, 3, 5),

    ("MX-711", "Toner", 8, 5, 10),
    ("MX-711", "Unidad Imagen", 3, 3, 5),

    ("MX-911", "Toner", 5, 2, 5),
    ("MX-911", "Unidad Imagen", 5, 1, 5),
    ("MX-911", "Botella Desecho", 2, 1, 2),

    ("C748", "Cartucho Amarillo", 2, 2, None),
    ("C748", "Cartucho Negro", 2, 2, None),
    ("C748", "Cartucho Magenta", 2, 2, None),
    ("C748", "Cartucho Cyan", 2, 2, None),
    ("C748", "Botella Desecho", 3, 1, None),
    ("C748", "Kit Fotoconductor", 5, 2, None),

    ("DK-320", "Drum Kit", 0, 0, None),

    ("C725", "Cartucho Amarillo", 3, 2, None),
    ("C725", "Cartucho Negro", 2, 2, None),
    ("C725", "Cartucho Magenta", 3, 2, None),
    ("C725", "Cartucho Cyan", 3, 2, None),
    ("C725", "Botella Desecho", 2, 2, None),
    ("C725", "Kit Fotoconductor", 2, 2, None),
    ("C725", "Unidad Imagen Negro", 2, 1, None),
]

with app.app_context():
    created = 0
    updated = 0
    for modelo, consumible, actual, minimo, maximo in DATA:
        row = SuministroImpresora.query.filter_by(modelo=modelo, consumible=consumible).first()
        if not row:
            row = SuministroImpresora(modelo=modelo, consumible=consumible, actual=actual, minimo=minimo, maximo=maximo)
            db.session.add(row)
            created += 1
        else:
            row.actual = actual
            row.minimo = minimo
            row.maximo = maximo
            updated += 1
    db.session.commit()
    total = SuministroImpresora.query.count()
    print(f"✅ Seed inventario completado. Nuevos: {created} | Actualizados: {updated} | Total: {total}")
