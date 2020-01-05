import requests

#Class is based on the following guide: https://www.reddit.com/r/algotrading/comments/c81vzq/td_ameritrade_api_access_2019_guide/
class IEXClient:

    def __init__(self, client_id):
        #IEX requires API Key for all API calls
        self.client_id = client_id
        self.auth = {}

    #Get method for calling unsecured TD Ameritrade endpoints
    def get(self, url, queryParams = "", body = {}):
        formattedUrl = self.formatUrl(url, queryParams)
        resp = requests.get(formattedUrl)
        return resp.json()

    #Get method for calling secured TD Ameritrade endpoints
    def secureGet(self, url, queryParams = "", body = {}):
        self.checkAuth()
        formattedUrl = self.formatUrl(url, queryParams)
        resp = requests.get(url = formattedUrl, data = body)
        return resp.json()

    #Method to add query parameters to request URL
    def formatUrl(self, url, queryParams):
        if queryParams is "":
            return url + '?token=' + self.client_id
        else:
            return url + '?token=' + self.client_id + '&' + queryParams