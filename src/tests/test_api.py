#execute test only when service is running
from src.constants.coonstants import MAX_AMOUNT , BILLS, COINS , MAX_COINS_NUM

import requests
import unittest


class TestATM(unittest.TestCase):
    URL = 'http://127.0.0.1:3000'

    def test_health_check(self):

        resp_message = {"message": "ATM is running"}

        data = requests.post(url=self.URL)
        self.assertEqual(data.status_code,200)
        print("Health check done")

    def test_refill_success(self):
        data = {"money":{ "0.1": 5, "5": 20, "20": 15, "100": 30 }}
        resp_message = {"message": "OK. Refill successfull"}

        test_url =  self.URL + '/atm/refill'

        resp = requests.post(url=test_url,json=data)
        self.assertEqual(resp.status_code,200)
        self.assertDictEqual(resp.json(),resp_message)
        print("Refill check done")
    
    def test_refill_empty_body(self):
        data = {}
        resp_message = {"message": "Empty body"}

        test_url =  self.URL + '/atm/refill'

        resp = requests.post(url=test_url,json=data)
        self.assertEqual(resp.status_code,422)
        self.assertDictEqual(resp.json(),resp_message)
        print("Refill empty body done")

    def test_refill_not_correct_format(self):
        data = {"mmmm":"dddd"}
        resp_message = {"message": "Not correct format in request body"}

        test_url =  self.URL + '/atm/refill'

        resp = requests.post(url=test_url,json=data)
        self.assertEqual(resp.status_code,422)
        self.assertDictEqual(resp.json(),resp_message)
        print("Refill not correct format done")

    def test_refill_not_supported_coint(self):
        data = {"money":{ "0.1": 5, "4445": 20, "20": 15, "100": 30 }}
        resp_message = {"message": "Unsupported bill"}

        test_url =  self.URL + '/atm/refill'

        resp = requests.post(url=test_url,json=data)
        self.assertEqual(resp.status_code,422)
        self.assertDictEqual(resp.json(),resp_message)
        print("Refill not supported coin done")
    
    def test_withdrawal_amount_check(self):
        data = {"amount":"3000"}
        resp_message = {"message": "Unprocessable Entity"}

        test_url =  self.URL + '/atm/withdrawal'

        resp = requests.post(url=test_url,json=data)
        self.assertEqual(resp.status_code,422)
        self.assertDictEqual(resp.json(),resp_message)
        print("Withdrawal amount check done")

    def test_withdrawal_empty_body(self):
        data = {}
        resp_message = {"message": "Empty body"}

        test_url =  self.URL + '/atm/withdrawal'

        resp = requests.post(url=test_url,json=data)
        self.assertEqual(resp.status_code,422)
        self.assertDictEqual(resp.json(),resp_message)
        print("Withdrawal empty body done")

    def test_withdrawal_not_correct_format(self):
        data = {"aaaa":"333"}
        resp_message = {"message": "Not correct format in request body"}

        test_url =  self.URL + '/atm/withdrawal'

        resp = requests.post(url=test_url,json=data)
        self.assertEqual(resp.status_code,422)
        self.assertDictEqual(resp.json(),resp_message)
        print("Withdrawal not correct format done")

    def test_withdrawal_bad_amount_value(self):
        data = {"amount":"ddd"}
        resp_message = {"message": "Bad amount value"}

        test_url =  self.URL + '/atm/withdrawal'

        resp = requests.post(url=test_url,json=data)
        self.assertEqual(resp.status_code,422)
        self.assertDictEqual(resp.json(),resp_message)
        print("Withdrawal bad amount value done")
    

if __name__ ==  "__main__":
    tester =  TestATM()

    tester.test_health_check()
    tester.test_refill_success()
    tester.test_refill_empty_body()
    tester.test_refill_not_correct_format()
    tester.test_refill_not_supported_coint()
    tester.test_withdrawal_amount_check()
    tester.test_withdrawal_empty_body()
    tester.test_withdrawal_bad_amount_value()
    tester.test_withdrawal_not_correct_format()





