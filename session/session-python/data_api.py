import requests

url = 'http://openapi.seoul.go.kr:8088/5478735457726c613131377850776a4b/json/GetParkInfo/1/1000'

response = requests.get(url)

response_json = response.json()
#json_keys = response_json["GetParkInfo"].keys()
data_row = response_json["GetParkInfo"]["row"]

print(len(data_row))

def get_data(gu):
    new_data = []
    for item in data_row:
        place = item["ADDR"]
        if gu in place:
            new_data.append(item)
    return new_data


