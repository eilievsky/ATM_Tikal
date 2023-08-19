# this file conatisn class that will be used for requets validations

from src.constants.coonstants import MAX_AMOUNT , BILLS, COINS , MAX_COINS_NUM

class Validator:
    def __init__(self) -> None:
        pass
   
    @staticmethod
    def validate_withdraw_request(req: dict) -> dict:
        
        validation_response = dict()

        # check if body is empty
        if len(req) == 0:
            validation_response['valitaion_valid'] =  False
            validation_response['validation_message'] = 'Empty body'
            validation_response['validation_status'] = 422
            return validation_response

        # check if body i have not correct value as a key   
        if req.get('amount') is None:
            validation_response['valitaion_valid'] =  False
            validation_response['validation_message'] = 'Not correct format in request body'
            validation_response['validation_status'] = 422
            return validation_response

        # check if amount is actually float
        check_num = str(req.get('amount'))
        try:
            float(check_num)            
        except ValueError:
            validation_response['valitaion_valid'] =  False
            validation_response['validation_message'] = 'Bad amount value'
            validation_response['validation_status'] = 422
            return validation_response

        # check is requets is exceeded max amount
        if float(str(req.get('amount'))) > MAX_AMOUNT:
            validation_response['valitaion_valid'] =  False
            validation_response['validation_message'] = 'Unprocessable Entity'
            validation_response['validation_status'] = 422
            return validation_response
        
        validation_response['valitaion_valid'] =  True
        validation_response['validation_message'] = 'OK'
        validation_response['validation_status'] = 200
        return validation_response


    @staticmethod    
    def validate_refill_request(req: dict) -> dict:

        validation_response = dict()
        # check if body is empty

        if len(req) == 0:
            validation_response['valitaion_valid'] =  False
            validation_response['validation_message'] = 'Empty body'
            validation_response['validation_status'] = 422
            return validation_response
        
         # check if body i have not correct value as a key   
        if req.get('money') is None:
            validation_response['valitaion_valid'] =  False
            validation_response['validation_message'] = 'Not correct format in request body'
            validation_response['validation_status'] = 422
            return validation_response
        
        money_check_lst =  BILLS + COINS
        check_dict =  req.get('money')
        for el in check_dict.keys():
            if float(el) not in money_check_lst:
                validation_response['valitaion_valid'] =  False
                validation_response['validation_message'] = 'Unsupported bill'
                validation_response['validation_status'] = 422
                return validation_response
            
        validation_response['valitaion_valid'] =  True
        validation_response['validation_message'] = 'OK'
        validation_response['validation_status'] = 200
        return validation_response
            
    @staticmethod
    def check_coins_amount(wihdraw_dict) -> dict:
        validation_response = dict()
        num_of_coins = 0
        for value in wihdraw_dict.values():
            num_of_coins += value
        
        if num_of_coins > MAX_COINS_NUM:
            validation_response['valitaion_valid'] =  False
            validation_response['validation_message'] = 'Too many coins'
            validation_response['validation_status'] = 422
            return validation_response
        
        validation_response['valitaion_valid'] =  True
        validation_response['validation_message'] = 'OK'
        validation_response['validation_status'] = 200
        return validation_response
    

    @staticmethod
    def get_not_enough_money(money_amount: float)->dict:
        validation_response = dict()
        validation_response['valitaion_valid'] =  True
        validation_response['validation_message'] = f'Conflict. Max amount money for withdraw is {money_amount}'
        validation_response['validation_status'] = 409
        return validation_response
    
    @staticmethod
    def get_not_enough_different_money()->dict:
        validation_response = dict()
        validation_response['valitaion_valid'] =  False
        validation_response['validation_message'] = "Conflict. ATM don't have enough varition of coins and bills to provide request amount"
        validation_response['validation_status'] = 409
        return validation_response
        
    @staticmethod
    def get_successfull_withdraw()->dict:
        validation_response = dict()
        validation_response['valitaion_valid'] =  True
        validation_response['validation_message'] = 'OK. Withdraw successfull'
        validation_response['validation_status'] = 200
        return validation_response
    
    @staticmethod
    def get_successfull_refill()->dict:
        validation_response = dict()
        validation_response['valitaion_valid'] =  True
        validation_response['validation_message'] = 'OK. Refill successfull'
        validation_response['validation_status'] = 200
        return validation_response
    
    @staticmethod
    def get_unexpected_error()->dict:
        validation_response = dict()
        validation_response['valitaion_valid'] =  False
        validation_response['validation_message'] = 'Unexpected server error'
        validation_response['validation_status'] = 500
        return validation_response




        
        



        

        
        
            
        


        
