def format_withdraw_result(wirhdraw_dict: dict , coins:list)->dict:
        coins_dict = dict()
        bills_dict = dict()
        coins_str_lst =  [str(x) for x in coins]
        for key , value in wirhdraw_dict.items():
            if key in coins_str_lst:
                coins_dict[key] = value
            else:
                bills_dict[key] = value
        return {"result":
                    {
                        "bills":bills_dict,
                        "coins":coins_dict
                    }
                }