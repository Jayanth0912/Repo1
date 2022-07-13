#Requirements
#Debugging
#Logging
import logging

import speedtest
import flask
# Import the pygame module
# import pygame
#
# # Import pygame.locals for easier access to key coordinates
# # Updated to conform to flake8 and black standards
# x = pygame
# # Initialize pygame
# pygame.init()

# INFO,DEBUG,WARNING,ERROR,CRITICAL

import traceback
from logging import getLogger
# Python Fundamentals LiveLessons (Video Training)
logging.basicConfig(filename="day8.log",format="%(asctime)s %(message)s",filemode="w")

logger = getLogger()
logger.setLevel(logging.CRITICAL)
def fun1(a,b):
    try:
        logger.info("Inside Fun1")
        p = "vinay"
        x = a+b
        logger.info("After Addition")
        y = a-b
        logger.info("After Sub")
        z = a + p
        logger.info("123456789")
        logger.info(a/b)
        logger.info("Returning Fun1")
        return a/b
    except Exception as e:
        # logger.error(str(e))
        # logger.error(traceback.print_exc())
        # raise(e)
        logger.error(traceback.format_exc())
        # print(e)

def fun2(a,b):
    try:
        logger.info("Inside Fun2")
        c = fun1(a,b)
        logger.info("Returning Fun2")
        return c
    except Exception as e:
        logger.error(traceback.print_exc())
        # print(e)


fun2(10,0)




# import speedtest
# import datetime
# st = speedtest.Speedtest()
#
# print("Checking Download Speed")
# download_speed = st.download()
# t = datetime.datetime.now()
# print(round(download_speed/1024/1024))
# time = "{hh}:{mm}:{ss}".format(hh=t.hour,mm=t.minute,ss=t.second)
# # str(t.hour) + str(t.minute) + str(t.second)
# with open("speed.log","w") as file_var:
#     file_var.write(str(round(download_speed/1024/1024)) + " , "+ time)

logger.info("INFO Log") #- Info, warning, error and critical
logger.debug("DEBUG Log") #- All Log types
logger.warning("Warning Log") # Warning Critical and Error
logger.error("Error Log") #Critical and Error
logger.critical("Critical Log") #Critical