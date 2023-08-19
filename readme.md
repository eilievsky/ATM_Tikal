# ATM Service

## General Technical Details
- Development is don using Flask restAPI framework
- Python version 3.11
- Database SQLite3 (already predefined with with nessesary table)

## Modules / Directories
- process - contains main functionality of ATM
- db - all database operaations
- helpers - functions for general usage
- constants - constant values for service activation

## Activation
Open app.py file and execute it in VSCode (or using any other python activation option)
Service will be initialize with access through following address 'http://127.0.0.1:5000'

## Usage
### Withdrawal request
~~~
curl -L -g -X POST 'http://127.0.0.1:5000/atm/withdrawal' -H 'Content-Type: application/json' --data-raw '{ "amount":"25.00"}'
~~~
### Refill request
~~~
curl -L -g -X POST '{{host}}:{{port}}/atm/refill' -H 'Content-Type: application/json' --data-raw '{
"money":{ "0.1": 5, "5": 20, "20": 15, "100": 30 }}'
~~~
### Reset request
This was done to allow and reset database to initial state as part of this assignment
~~~
curl -L -g -X POST 'http://127.0.0.1:5000/atm/reset' 
~~~




