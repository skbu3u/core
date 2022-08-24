from fastapi import Depends, Request, Response
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from sqlalchemy.orm import Session

from src.api.schemas.consumables import Consumable, ConsumableCreate
from src.api.schemas.equipments import Equipment, EquipmentCreate
from src.api.schemas.parts import Part, PartCreate
from src.api.schemas.tasks import Task, TaskCreate
from src.api.schemas.users import User, UserCreate
from src.database.models import ConsumableModel, TaskModel
from src.database.models import EquipmentModel
from src.database.models import PartModel
from src.database.models import UserModel
from src.database.service import check_exist_in_db, add_to_db, check_compatibility, check_contains
from src.database.sql import get_db


def add_route(schema, create_schema, db_model, prefix, create_route=False):
    route = SQLAlchemyCRUDRouter(
        schema=schema,
        create_schema=create_schema,
        db_model=db_model,
        db=get_db,
        prefix=prefix,
        create_route=create_route,
        # dependencies=[Depends(AuthHandler().auth_wrapper)]
    )
    return route


users = add_route(User, UserCreate, UserModel, 'users')
equipments = add_route(Equipment, EquipmentCreate, EquipmentModel, 'equipments')
parts = add_route(Part, PartCreate, PartModel, 'parts')
consumables = add_route(Consumable, ConsumableCreate, ConsumableModel, 'consumables')
tasks = add_route(Task, TaskCreate, TaskModel, 'tasks')


@equipments.post("", response_model=Equipment, status_code=201)
def create_one(response: Response, request: Request, equipment: EquipmentCreate, db: Session = Depends(get_db)):
    check_exist_in_db(db=db, schema=equipment, model=EquipmentModel)
    new_equipment = EquipmentModel(name=equipment.name)
    add_to_db(db=db, model=EquipmentModel, new_model=new_equipment)
    check_contains(db=db, schema=equipment, model=PartModel, new_model=new_equipment)
    response.headers["Location"] = request.url._url
    return new_equipment


@parts.post("", response_model=Equipment, status_code=201)
def create_one(response: Response, request: Request, part: PartCreate, db: Session = Depends(get_db)):
    check_exist_in_db(db=db, schema=part, model=PartModel)
    new_part = PartModel(**part.dict())
    add_to_db(db=db, model=PartModel, new_model=new_part)
    check_compatibility(db=db, schema=part, model=EquipmentModel, new_model=new_part)
    check_contains(db=db, schema=part, model=ConsumableModel, new_model=new_part)
    response.headers["Location"] = request.url._url
    return new_part


@consumables.post("", response_model=Part, status_code=201)
def create_one(response: Response, request: Request, consumable: ConsumableCreate, db: Session = Depends(get_db)):
    check_exist_in_db(db=db, schema=consumable, model=ConsumableModel)
    new_consumable = ConsumableModel(**consumable.dict())
    add_to_db(db=db, model=ConsumableModel, new_model=new_consumable)
    check_compatibility(db=db, schema=consumable, model=PartModel, new_model=new_consumable)
    response.headers["Location"] = request.url._url
    return new_consumable


@tasks.post("", response_model=Task, status_code=201)
def create_one(response: Response, request: Request, task: TaskCreate, db: Session = Depends(get_db)):
    check_exist_in_db(db=db, schema=task, model=TaskModel)
    new_task = TaskModel(name=task.name)
    add_to_db(db=db, model=TaskModel, new_model=new_task)
    response.headers["Location"] = request.url._url
    return new_task
