import os
import os.path
import sys
import requests
import time
from selenium import webdriver
from shutil import which
import urllib.parse as up


def authentication(client_id, redirect_uri):
    client_id = client_id + '@AMER.OAUTHAP'
    url = 'https://auth.tdameritrade.com/auth?response_type=code&redirect_uri=' + up.quote(redirect_uri) + '&client_id=' + up.quote(client_id)

    options = webdriver.ChromeOptions()

    if sys.platform == 'darwin':
        # MacOS
        if os.path.exists("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"):
            options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        elif os.path.exists("/Applications/Chrome.app/Contents/MacOS/Google Chrome"):
            options.binary_location = "/Applications/Chrome.app/Contents/MacOS/Google Chrome"
    elif 'linux' in sys.platform:
        # Linux
        options.binary_location = which('google-chrome') or which('chrome') or which('chromium')

    else:
        # Windows
        if os.path.exists('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'):
            options.binary_location = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
        elif os.path.exists('C:/Program Files/Google/Chrome/Application/chrome.exe'):
            options.binary_location = 'C:/Program Files/Google/Chrome/Application/chrome.exe'

    chrome_driver_binary = which('chromedriver') or "C:\Python\PythonFinance"
    driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

    driver.get(url)

    # Fully automated oauth2 authentication (if tdauser and tdapass were intputed into the function, or found as environment variables)
    authUrl = input('after giving access paste URL here, hit enter to continue')
    code = up.unquote(authUrl.split('code=')[1])

    driver.close()

    resp = requests.post('https://api.tdameritrade.com/v1/oauth2/token',
                         headers={'Content-Type': 'application/x-www-form-urlencoded'},
                         data={'grant_type': 'authorization_code',
                               'refresh_token': '',
                               'access_type': 'offline',
                               'code': code,
                               'client_id': client_id,
                               'redirect_uri': redirect_uri})
    if resp.status_code != 200:
        raise Exception('Could not authenticate!')
    return resp.json()


def refresh_token(refresh_token, client_id):
    resp = requests.post('https://api.tdameritrade.com/v1/oauth2/token',
                         headers={'Content-Type': 'application/x-www-form-urlencoded'},
                         data={'grant_type': 'refresh_token',
                               'refresh_token': refresh_token,
                               'client_id': client_id})
    if resp.status_code != 200:
        raise Exception('Could not authenticate!')
    return resp.json()