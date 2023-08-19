from src.constants.coonstants import COINS,BILLS
from src.db.database import DBManager
from src.process.validator import Validator
from src.helpers.helper import format_withdraw_result


class Atm_State:

    def __init__(self,dbmanager: DBManager) -> None:
        self.dbmanager = dbmanager
        self.atm_state = dbmanager.load_atm_state()

    # count total amoutnof money in ATM
    def _get_total_atm_amount_(self)->float:
        total_amount =  0
        for key,value in self.atm_state.items():
            total_amount += float(key) * value
        return total_amount
    
    # refill operation
    def refill(self , refill_dict: dict) -> dict:
        try:
            validation_result =  Validator.validate_refill_request(refill_dict)
            if validation_result['valitaion_valid'] == False:
                return validation_result
            
            refill_money =  refill_dict.get('money')

            for key,value in refill_money.items():
                self.atm_state[key] = self.atm_state[key] + value
            
            self.dbmanager.update_atm_state(self.atm_state)
            return Validator.get_successfull_refill()
        except:
            return Validator.get_unexpected_error()

    # withdrawn operation  
    def witdraw(self , req: dict) -> any:
        try: 
            validation_result =  Validator.validate_withdraw_request(req)
            if validation_result['valitaion_valid'] == False:
                return validation_result
            
            amount  =  float(req.get('amount'))
            if amount > self._get_total_atm_amount_():
                return Validator.get_not_enough_money()

            wirhdraw_dict = dict()
            check_lst  =  [key for key, value in self.atm_state.items() if float(key) <= amount and value > 0]
            print(check_lst)
            check_lst.sort(reverse = True) 
            for i in check_lst:
                numcheck = int(amount / float(i))
                if numcheck > 0:
                    if numcheck <= self.atm_state[i]:
                        wirhdraw_dict[i] = numcheck
                        self.atm_state[i] =  self.atm_state[i] - numcheck
                        amount = amount - (float(i) * numcheck)
                    else:
                        wirhdraw_dict[i] = self.atm_state[i]
                        self.atm_state[i] = 0
                        amount = amount - (float(wirhdraw_dict[i]) * float(i))

            if amount == 0:
                # it means that exists coins can cover withdrawn
                validation_result =  Validator.check_coins_amount(wirhdraw_dict)
                if validation_result['valitaion_valid'] == False:
                    self.atm_state = self.dbmanager.load_atm_state()
                    return validation_result
                else:
                    self.dbmanager.update_atm_state(self.atm_state)
                    return format_withdraw_result(wirhdraw_dict,COINS)
            else:
                # return status that existing coins can't cover withdrawn
                self.atm_state = self.dbmanager.load_atm_state()
                return Validator.get_not_enough_different_money()
            
        except:
            return Validator.get_unexpected_error()

    
    def reset_atm(self)-> dict:
        try:
            self.dbmanager.reset_database()
            self.atm_state = self.dbmanager.load_atm_state()
        except:
            return Validator.get_unexpected_error()
            


