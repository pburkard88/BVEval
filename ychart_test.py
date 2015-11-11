# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
import requests
from getpass import getpass

BASE_URL = 'https://ycharts.com/financials/'
LOGIN_URL = 'https://ycharts.com/login'
company = 'AAPL'
frequency = 'quarterly'
entries_to_keep = 5

username = raw_input('Enter YCharts email: ')
password = getpass('Enter YCharts password: ')

payload = {'username': username, 'password': password, 'next': '/financials/APPL/cash_flow_statement/quarterly', 'auth_submit': 'Sign In'}

client = requests.session()

# Retrieve the CSRF token first
client.get(LOGIN_URL)  # sets cookie
client.headers['referer'] = 'https://ycharts.com/login?next=/financials/APPL/cash_flow_statement/quarterly'
csrftoken = client.cookies['csrftoken']

payload['csrfmiddlewaretoken'] = csrftoken

p = client.post(LOGIN_URL, data=payload)
  
r = client.get(BASE_URL + company + '/cash_flow_statement/' + frequency)    

soup = BeautifulSoup(r.text)

print (soup.find(id='report')).prettify()