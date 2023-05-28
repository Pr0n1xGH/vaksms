# vaksms

VakSms is a Python library that provides an API for interacting with the vak-sms.com service. It allows you to perform various operations such as getting the user's balance, retrieving available phone numbers, renting temporary phone numbers, activating SMS codes, and more.

## Installation

You can install the library using pip:
```shell
pip install vaksms
```

## Usage
Get apikey: https://vak-sms.com/api/vak/ <br>
Services: https://vak-sms.com/api/vak/#serviceCodeList1 <br>
Countres and operators: https://vak-sms.com/api/vak/#countryOperatorList1

```python

from vaksms import vaksms

# Create an instance of the vaksms class with your API key
vakapi = vaksms('your_apikey')

# Get the user's balance
balance = vakapi.getBalance()
print(f"Current balance: {balance}")

# Get the number of available numbers for a specific service
count = vakapi.getCountNumber('service_code')
print(f"Available numbers: {count}")

# Get a temporary phone number
number = vakapi.getNumber('service_code')
print(f"Temporary number: {number}")

# Extend the duration of a previously received number
extended_number = vakapi.prolongNumber('service_code', 'phone_number')
print(f"Extended number: {extended_number}")

# Change the status of an operation ID
status = vakapi.setStatus('operation_id', 'end')
print(f"Status: {status}")

# Activate SMS code for a specific operation ID
sms_code = vakapi.getSmsCode('operation_id')
print(f"SMS code: {sms_code}")
```
