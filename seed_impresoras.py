from app import app
from models.models import db, Impresora

DATA = [
    ("10.70.100.20", "70166PHH08PZF", "Lexmark MX611dhe", "HDT - Piso1 Recepcion", "UTLCCA022P"),
    ("10.70.100.21", "74637C66001T3", "Lexmark MX711", "HDT - Centro de contactos (Piso 1)", "UTLCCA022P"),
    ("10.70.100.22", "70166PHH09XGH", "Lexmark MX611dhe", "HDT - Imagenes Medicas (Piso 1)", "UTLCCA022P"),
    ("10.70.100.23", "74637C66007PT", "Lexmark MX711", "HDT - Admision Hospitalaria (Piso 1)", "UTLCCA022P"),
    ("10.70.100.24", "74637C66007LT", "Lexmark MX711", "HDT - Farmacia (Piso 1)", "UTLCCA022P"),
    ("10.70.101.20", "74636C6601DY6", "Lexmark MX711", "HDT - Logistica y Operaciones (PB)", "UTLCCA022P"),
    ("10.70.101.21", "70166PHH095PH", "Lexmark MX611dhe", "HDT - Control Equipos de Esterilizacion (PB)", "UTLCCA022P"),
    ("10.70.101.22", "70167GHH0C9LH", "Lexmark MX611dhe", "HDT - PB Seguridad", "UTLCCA022P"),
    ("10.70.101.23", "70167PHH0DXHV", "Lexmark MX611dhe", "HDT - Planta Baja Nutricion", "UTLCCA022P"),
    ("10.70.101.25", "74637C66007PZ", "Lexmark MX711", "HDT - Piso 0 - Consulta Externa Recepcion", "UTLCCA022P"),
    ("10.70.102.20", "74637C66007R3", "Lexmark MX711", "HDT - Quirofano (Piso 2)", "UTLCCA022P"),
    ("10.70.102.21", "74637C66007GX", "Lexmark MX711", "HDT - Pre Anestesia (Piso 2)", "UTLCCA022P"),
    ("10.70.102.22", "74637C66007P5", "Lexmark MX711", "HDT - Area Quirurgica (Piso 2)", "UTLCCA022P"),
    ("10.70.102.23", "74637C66007RV", "Lexmark MX711", "HDT - USUMAQ (Piso 2)", "UTLCCA022P"),
    ("10.70.102.24", "74637C66007N3", "Lexmark MX711", "HDT - UTI (Piso 2)", "UTLCCA022P"),
    ("10.70.102.25", "74637C66001T2", "Lexmark MX711", "HDT - UCI (Piso 2)", "UTLCCA022P"),
    ("10.70.103.20", "74637C66007K3", "Lexmark MX711", "HDT - Ala Sur (Piso 3)", "UTLCCA022P"),
    ("10.70.103.21", "74637C66007R0", "Lexmark MX711", "HDT - Ala Norte (Piso 3)", "UTLCCA022P"),
    ("10.70.103.22", "74637C66007GF", "Lexmark MX711", "HDT - Area Administrativa (Piso 3)", "UTLCCA022P"),
    ("10.70.104.22", "74636C6600VGW", "Lexmark MX711", "HDT - Ala Norte (Piso 4)", "UTLCCA022P"),
    ("10.70.104.23", "74635C6603FB0", "Lexmark MX711", "HDT - Ala Sur (Piso 4)", "UTLCCA022P"),
    ("10.70.105.20", "70166PHH09XH9", "Lexmark MX611dhe", "HDT - Torre Administrativa - Auditoria", "UTLCCA023P"),
    ("10.70.105.21", "74636C6601D3Z", "Lexmark MX711", "HDT - Torre Administrativa - Gerencia General", "UTLCCA023P"),
    ("10.70.105.22", "7421013003516", "Lexmark MX911", "HDT - Torre Administrativa - Recursos Humanos (P2)", "UTLCCA023P"),
    ("10.70.105.23", "7528740011P8L", "Lexmark CX725", "HDT - Modulo A Recursos Humanos", "UTLCCA023P"),
    ("10.70.105.24", "7421013004551", "Lexmark MX911", "HDT - Torre Administrativa - Financiero 1", "UTLCCA023P"),
    ("10.70.105.25", "502633942282H", "Lexmark C748", "HDT - Torre Administrativa - Experencia al Cliente", "UTLCCA023P"),
    ("10.70.105.26", "70167PHH0DXHL", "Lexmark MX611dhe", "HDT - Torre Administrativa - Financiero 2", "UTLCCA023P"),
    ("10.70.51.111", "70166PHH09474", "Lexmark MX611dhe", "HDT - Nutricion", "UTLCCA023P"),
    ("10.70.51.65", "701644HH03D35", "Lexmark MX611dhe", "HDT - Programacion Quirurgica", "UTLCCA023P"),
    ("10.90.101.20", "70167PHH0DXGX", "Lexmark MX611dhe", "HDT - Edificio Negro", "UTLCCA023P"),
    ("10.90.102.20", "74637C66007H8", "Lexmark MX711", "HDT - CE Servicios Clasificacion (Piso 0)", "UTLCCA023P"),
    ("10.90.103.20", "74637C660025L", "Lexmark MX711", "HDT - CE Citas (Piso 1)", "UTLCCA023P"),
    ("10.90.103.21", "74637C66007MY", "Lexmark MX711", "HDT - CE Jefatura Medica (Piso 1)", "UTLCCA023P"),
    ("10.90.103.22", "70166PHH09VX1", "Lexmark MX611dhe", "HDT - CE Farmacia (Piso 1)", "UTLCCA023P"),
    ("10.90.104.22", "74637C66007HW", "Lexmark MX711", "HDT - CE Expedientes (Piso 2)", "UTLCCA023P"),
    ("10.90.104.23", "74637C66007HN", "Lexmark MX711", "HDT - CE Voz Paciente (Piso 2)", "UTLCCA023P"),
    ("10.90.105.22", "74637C66007H0", "Lexmark MX711", "HDT - CE Planificacion Quirurgica (Piso 3)", "UTLCCA023P"),
    ("10.90.106.20", "70166PHH09XHN", "Lexmark MX611dhe", "HDT - UVI Observacion", "UTLCCA023P"),
    ("10.90.106.21", "74635C6603K3N", "Lexmark MX711", "HDT - UVI Recepcion", "UTLCCA023P"),
    ("10.90.108.20", "70166PHH09X7H", "Lexmark MX611dhe", "HDT - Edif Amarillo Rehabilitacion", "UTLCCA023P"),
    ("10.90.108.21", "701644HH03D16", "Lexmark MX611dhe", "HDT - Piso 0 - Salud Preventiva", "UTLCCA023P"),
    ("10.90.108.23", "70167GHH0D9K6", "Lexmark MX611dhe", "HDT - PS Edificio Amarillo", "UTLCCA023P"),
    ("10.90.109.20", "70166PHH095CW", "Lexmark MX611dhe", "HDT - Edificio G Pago Pacientes #1", "UTLCCA023P"),
    ("10.90.109.21", "74636C6600VM0", "Lexmark MX711", "HDT - Edificio G Pago Proveedores #1", "UTLCCA023P"),
    ("10.90.109.22", "74635C6603HX4", "Lexmark MX711", "HDT - Edificio G Pago Proveedores #2", "UTLCCA023P"),
    ("10.90.109.23", "70167GHH0DBGW", "Lexmark MX611dhe", "HDT - Edificio G Pago Pacientes #2", "UTLCCA023P"),
    ("10.90.11.49", "70167GHH0D9GB", "Lexmark MX611dhe", "HDT - Albergue", "UTLCCA023P"),
    ("10.90.110.20", "74636C6601DLC", "Lexmark MX711", "HDT - Modulo 1 Ala Sur", "UTLCCA023P"),
    ("10.90.110.21", "74636C6601DWC", "Lexmark MX711", "HDT - Modulo 1 Ala Norte", "UTLCCA023P"),
    ("10.90.111.20", "74636C6601D36", "Lexmark MX711", "HDT - Modulo A Unidad de Trasportes", "UTLCCA023P"),
    ("10.90.112.20", "74637C66001RM", "Lexmark MX611dhe", "HDT - Clinica del Dolor", "UTLCCA023P"),
    ("10.90.114.20", "70166PHH09XG4", "Lexmark MX611dhe", "HDT - Modulo 2 Rehabilitacion", "UTLCCA023P"),
    ("10.90.116.10", "50263794G58WK", "Lexmark C748", "HDT - Centro Informativo Torre", "UTLCCA023P"),
    ("10.90.12.101", "70166PHH09WZK", "Lexmark MX711", "HDT - Modulo 2 Trabajo Social", "UTLCCA023P"),
]

with app.app_context():
    created = 0
    updated = 0

    for ip, serie, modelo, ubicacion, servidor in DATA:
        row = Impresora.query.filter_by(ip=ip).first()

        if not row:
            row = Impresora(
                ip=ip,
                serie=serie,
                modelo=modelo,
                ubicacion=ubicacion,
                servidor=servidor
            )
            db.session.add(row)
            created += 1
        else:
            # Actualiza si cambió algún dato
            changed = False
            if row.serie != serie:
                row.serie = serie
                changed = True
            if row.modelo != modelo:
                row.modelo = modelo
                changed = True
            if row.ubicacion != ubicacion:
                row.ubicacion = ubicacion
                changed = True
            if row.servidor != servidor:
                row.servidor = servidor
                changed = True

            if changed:
                updated += 1

    db.session.commit()

    total = Impresora.query.count()
    print(f"✅ Seed impresoras completado. Nuevas: {created} | Actualizadas: {updated} | Total: {total}")