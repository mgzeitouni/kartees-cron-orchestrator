import requests
import json

base_url="https://kartees-api.mybluemix.net/api"
version = "v3"
username="mark"
password="mark"


def req(req_type,route,params,token=None,headers=None):

	full_url= "%s/%s/%s" %(base_url, version,route)

	if route !="/login":
		headers={"token":token}

	response = None

	if req_type == 'GET':
		response = requests.get(full_url,headers=headers,params=params)
	elif req_type == 'POST':
		response = requests.post(full_url, headers=headers,data=params)
	elif req_type == 'PUT':
		response = requests.put(full_url, headers=headers,data=json.dumps(params))
	elif req_type == 'DELETE':
		response = requests.delete(full_url, headers=headers,params=params)
	else:
		return None

	return response

def login():

	route = "/login"
	params={"user": username,"pass":password}
	req_type="POST"

	return req(req_type,route,params).json()['token'] or None




class PHP_DB_API():

    def __init__(self):

    	self.token = login()

    def next_to_post(self):

   		route="/queue/create"
   		params=None
   		req_type="GET"

   		return req(req_type,route,params,self.token)

   

