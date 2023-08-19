from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from src.db.database import DBManager

db_manager =  DBManager()

print(db_manager.load_atm_state())


update_atm_dict =  {'200': 5, '100': 4, '20': 3, '10': 2, '1': 1, '5': 0, '0.1': 0, '0.01': 0}

db_manager.update_atm_state(update_atm_dict)

print(db_manager.load_atm_state())

