# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:17:15 2020

@author: CEC
"""

import urllib.parse
import requests



main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Quito"
dest = "Loja"
key = "cLAVwTv8jDuIIMxEGGNLkJJMHdKv5NDA"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)