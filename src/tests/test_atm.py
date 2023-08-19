from src.process.atm import Atm_State
from src.db.database import DBManager

db_manager =  DBManager()
atm =  Atm_State(dbmanager=db_manager)

withdraw_dict = {'amount':30}

print(atm.witdraw(req=withdraw_dict))

refill_dict = { "money":{
"0.1": 5, "5": 20, "20": 15, "100": 30
} }

# print (atm.refill(refill_dict))
# print (atm._get_total_atm_amount_())


withdraw_dict = {'amount':3000}

print(atm.witdraw(req=withdraw_dict))

