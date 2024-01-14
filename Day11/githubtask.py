import requests

response = requests.get(
    "https://api.github.com/repos/hashicorp/terraform/pulls")

complete_detail = response.json()

for i in range(len(complete_detail)):
    print(complete_detail[i]["user"]["login"])
