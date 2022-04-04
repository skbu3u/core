from fastapi import HTTPException


def check_exist_in_db(db, schema, model):
    db_model = db.query(model).filter(model.name == schema.name).first()
    if db_model:
        raise HTTPException(status_code=400, detail=f"{schema.name} already exist")


def add_to_db(db, model, new_model):
    if isinstance(new_model, model):
        db.add(new_model)
        db.commit()
        db.refresh(new_model)


def check_compatibility(db, schema, model, new_model):
    compatibility_list = [i.strip().lower() for i in schema.compatibility.split(",")]
    for compatibility in compatibility_list:
        db_equipment = db.query(model).filter(model.name == compatibility).first()
        if db_equipment:
            db_equipment.parts.append(new_model)