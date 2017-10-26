# import schedule
# import time

# def job():
#     print("I'm working...")
#     time.sleep(15)
#     print('done working')

# schedule.every(10).seconds.do(job)
# # schedule.every().hour.do(job)
# # schedule.every().day.at("10:30").do(job)

# while 1:
#     schedule.run_pending()
#     #time.sleep(1)

# from celery import Celery

# app = Celery('post_listing', broker='amqp://localhost')

# @app.task
# def add(x, y):
#     return x + y

from cloudant.client import Cloudant
from PHP_DB_API import PHP_DB_API
from Stubhub_Python_API import Stubhub_Python_API
import requests
import sys

stubhub_env = sys.argv[1]

db_object = PHP_DB_API()
stubhub_object = Stubhub_Python_API(stubhub_env)

sample_ticket={"eventId":103137716,
"quantity":1,
"section":206,
"row":10,
"price":200,
"seats":[1,2],
"deliveryOption":'PDF'}

x = stubhub_object.postListing(sample_ticket)

print (x)
print(x.text)
print(x.status_code)




# headers ={
# 	     "Content-type" : "application/json",
#          "token":global.get("token")
# }