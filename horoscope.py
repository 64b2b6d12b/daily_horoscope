#!/usr/bin/env python3

import config
import sys
from requests import request
from bs4 import BeautifulSoup as bs

def horoscope(star_sign):
	url = "https://www.astrospeak.com/horoscope/" + star_sign
	response = request("GET", url)
	soup = bs(response.text, 'html.parser')
	locater = soup.select("#sunsignPredictionDiv > div.fullDIV > div.lineHght18 > div")
	quote = str(locater[0].previousSibling).strip()
	return quote

def pushover(quote):
	url = 'https://api.pushover.net/1/messages.json'
	api_key = config.api_key
	user_key = config.user_key
	qs = {
	"token":api_key,
	"user":user_key,
	"message":quote
	}
	response = request("POST", url, params=qs)
	return response.text

star_sign = sys.argv[1]

quote = horoscope(star_sign)

print(pushover(quote))
