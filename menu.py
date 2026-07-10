import requests


class Menu:

    def api_call(self):

        results = {}

        url = 'https://open.er-api.com/v6/latest/USD'

        result = requests.get(url)

        data = result.json()

        datas = data["rates"]

        for index, (currency_name, value) in enumerate(list(datas.items())[:10], start = 1):

            if index <= 10:
                
                results[currency_name] = value 
        print(results)
        return results