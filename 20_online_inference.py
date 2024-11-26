import json
import requests
#Local server que podemos realizar o deploy dos modelos
data = {
    "dataframe_split": {"columns": ["input"], "data": [15]},
    "params": {"model_name": "model_1"},
}

headers = {"Content-Type": "application/json"}
endpoint = "http://127.0.0.1:5000/invocations"

r = requests.post(endpoint, data=json.dumps(data), headers=headers)
print(r.status_code)
print(r.text)