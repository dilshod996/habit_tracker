import requests
from datetime import datetime

creating_endpoint = "https://pixe.la/v1/users"


USERNAME = "dilshod"
TOKEN = "hiicomebackagain"
graph_id = "dima1"
parameters = {"token": TOKEN,
              "username": USERNAME,
              "agreeTermsOfService": "yes",
              "notMinor": "yes"}
#########Creating data
# response = requests.post(url=creating_endpoint, json=parameters)
# print(response.text)
today = datetime.now()


graph_endpoint = f"{creating_endpoint}/{USERNAME}/graphs"

graph_parameters= {"id":graph_id,
                   "name": "Coding Task",
                   "unit": "mins",
                   "type": "int",
                   "color": "shibafu"}

headers = {"X-USER-TOKEN": TOKEN}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)
graph_value_endpoint =f"{creating_endpoint}/{USERNAME}/graphs/{graph_id}"

graph_value_params = {"date":today.strftime("%Y%m%d"),
                      "quantity":input("How many mins did you learn programmong today? ")}


response = requests.post(url=graph_value_endpoint, json=graph_value_params, headers=headers)
print(response.text)

############ Updating data
# https://pixe.la/v1/users/dilshod/graphs/dima1/20220502
# update_endpoint = f"{creating_endpoint}/{USERNAME}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"
# new_pixel_data = {
#     "quantity": "100"
# }
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# response = requests.delete(url=update_endpoint, json=graph_value_params, headers=headers)
# print(response.text)