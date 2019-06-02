import argparse
import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse

def get_short_url(token, long_url):
  response = requests.get(long_url)
  if response.ok:
    url = "https://api-ssl.bitly.com/v4/bitlinks"
    auth_token = {
      "Authorization": "Bearer {}".format(token)
    }
    data = {
      "long_url": long_url
    }
    response = requests.post(url, headers=auth_token, json=data)
    if response.ok:
      short_url = response.json().get("link") 
      return short_url

def get_click_count(token, url):
  domain = urlparse(url).netloc
  path = urlparse(url).path
  url = "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary".format(domain+path)
  auth_token = {
    "Authorization": "Bearer {}".format(token)
    } 
  response = requests.get(url, headers=auth_token)
  if response.ok:
    click_count = response.json().get("total_clicks")
    return click_count
    
def check_short_url(token, url):
  domain = urlparse(url).netloc
  path = urlparse(url).path
  if domain == 'bit.ly':
    url = "https://api-ssl.bitly.com/v4/bitlinks/{}".format(domain + path)
    auth_token = {
      "Authorization": "Bearer {}".format(token)
    }
    response = requests.get(url, headers=auth_token)
    if response.ok:
      return True    

if __name__ == '__main__':
  load_dotenv()
  token = os.getenv("token")
  parser = argparse.ArgumentParser()
  parser.add_argument(
      'url',
      help='Any url')
  args = parser.parse_args()
  url = args.url
  check_short = check_short_url(token, url)
  if check_short:
    click_count = get_click_count(token, url)
    if click_count:
      print("Your url was clicked {} time(s) ".format(click_count))
    else:
      print("URL is not available")  
  else:
    bitlink = get_short_url(token, url)
    if bitlink:
      print("Short url: {}".format(get_short_url(token, url)))
      click_count = get_click_count(token, bitlink)
      print("Your url was clicked {} time(s) ".format(click_count))    
    else:
      print("URL is not available") 




