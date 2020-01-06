import requests

#Class is a small utility to always append the API key to IEX Calls
class IEXClient:

    def __init__(self, client_id):
        #IEX requires API Key for all API calls
        self.client_id = client_id
        self.auth = {}

    #Get method for calling IEX with the API token appeneded
    def get(self, url, queryParams = "", body = {}):
        formattedUrl = self.formatUrl(url, queryParams)
        resp = requests.get(formattedUrl)

        if resp.ok:
            return resp.json()
        else:
            return "Error Making Call. API returned {}".format(resp.status_code)

    #Method to add query parameters to request URL
    def formatUrl(self, url, queryParams):
        if queryParams is "":
            return url + '?token=' + self.client_id
        else:
            return url + '?token=' + self.client_id + '&' + queryParams