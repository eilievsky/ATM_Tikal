# Not active file to test validator class

from src.process.validator import Validator 

test_dict1 = { 'amount':'abc'}

test_dict2 = { 'ssssss':'abc'}

test_dict3 = {}

test_dict4 = { 'amount':'121'}

test_dict5 = { 'amount':2222}


# result_dic1 = Validator.validate_withdraw_request(test_dict1) 
# print(test_dict1)
# print(result_dic1)

# result_dic1 = Validator.validate_withdraw_request(test_dict2) 
# print(test_dict2)
# print(result_dic1)


# result_dic1 = Validator.validate_withdraw_request(test_dict3) 
# print(test_dict3)
# print(result_dic1)


# result_dic1 = Validator.validate_withdraw_request(test_dict4) 
# print(test_dict4)
# print(result_dic1)

# result_dic1 = Validator.validate_withdraw_request(test_dict5)
# print(test_dict5)
# print(result_dic1)


# withdraw_dict1= {'100':5,'50':10,'1':40}
# withdraw_dict2= {'100':5,'50':10,'1':35}
# withdraw_dict3= {'100':5,'50':10,'1':20}


# print(Validator.check_coins_amount(withdraw_dict1))
# print(Validator.check_coins_amount(withdraw_dict2))
# print(Validator.check_coins_amount(withdraw_dict3))


refill_dict1 = {}
refill_dict2 = {'money':{'100':4,'30':5,'5':3}}
refill_dict3 = {'fff':{'100':4,'30':5,'5':3}}
refill_dict4 = {'money':{'200':4,'1':5,'0.01':3}}





print(Validator.validate_refill_request(refill_dict1))
print(Validator.validate_refill_request(refill_dict2))
print(Validator.validate_refill_request(refill_dict3))
print(Validator.validate_refill_request(refill_dict4))