import requests
import json


def req(base_url, req_type,route,params,token=None,headers=None):

	full_url= "%s/%s" %(base_url,route)


	response = None

	if req_type == 'GET':
		response = requests.get(full_url,headers=headers,params=params)
	elif req_type == 'POST':
		print(params)
		response = requests.post(full_url, headers=headers,data=json.dumps(params))
	elif req_type == 'PUT':
		response = requests.put(full_url, headers=headers,data=json.dumps(params))
	elif req_type == 'DELETE':
		response = requests.delete(full_url, headers=headers,params=params)
	else:
		return None

	return response


class Stubhub_Python_API():

	def __init__(self, stubhub_env):

		if stubhub_env == "local":
			self.base_url="http://localhost:5000"
		else:
			self.base_url="https://stubhub-services-python.mybluemix.net"


	def postListing(self,listingDict):

		req_type="POST"
		route="postlisting"
		params=listingDict

		
		return req(self.base_url,req_type,route,params)


