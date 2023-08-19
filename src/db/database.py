import sqlite3
from src.constants.coonstants import DB_NAME , PRESEED_BILLS
from sqlalchemy import text



# this file contains 
class DBManager:
    def __init__(self,db) -> None:
        self.db = db
        self.init_atm_state()

       
    def init_atm_state(self) -> None:
        
        result  =   self.db.session.execute(text("SELECT count(*) FROM ATM")).fetchall()
        
        # if data not exists initiate ATM database based on constant
        if result[0][0] == 0:
            for key , value in PRESEED_BILLS.items():
                sql_str =  f"insert into ATM VALUES ('{key}',{value})"
                self.db.session.execute(text(sql_str))
            self.db.session.commit()
            

    def update_atm_state(self, atm_data: dict)-> None:
        # this functio  need to update state of ATM from memory
        for key, value in atm_data.items():
            sql_str =  f"update ATM set amount = {value} where coin = '{key}' "
            self.db.session.execute(text(sql_str))
        self.db.session.commit()
   

    def load_atm_state(self) -> dict:
        # this function return existing state of coins as dictionary
        sql_str =  "select coin , amount from ATM"
        result = self.db.session.execute(text(sql_str)).fetchall()
        return  {data_el[0]: int(data_el[1]) for data_el in result}
    
    def reset_database(self) -> None:
        self.db.session.execute(text("delete from ATM"))
        self.init_atm_state()

    

    
 