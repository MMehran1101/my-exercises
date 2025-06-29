import json
import requests

response = requests.get("https://BrsApi.ir/Api/Market/Gold_Currency.php?key=Freey1dU3B3OA0pWzXhopEWZYD4BoDAw")
data = response.json()
gold = data['gold']
# print(json.dumps(data, indent=4, ensure_ascii=False))



print(gold['name'] == 'طلای 18 عیار')
