
# import datetime
#
# print(datetime.datetime.now())

# Python program to test
# internet speed

# import speedtest
#
# st = speedtest.Speedtest()
#
# option = int(input('''What speed do you want to test:
#
# 1) Download Speed
#
# 2) Upload Speed
#
# 3) Ping
#
# Your Choice: '''))
#
#
# if option == 1:
#
# 	print(st.download())
#
# elif option == 2:
#
# 	print(st.upload())
#
# elif option == 3:
#
# 	servernames =[]
#
# 	st.get_servers(servernames)
#
# 	print(st.results.ping)
#
# else:
#
# 	print("Please enter the correct choice !")


from turtle import st

# import pyspeedtest
#
# test = pyspeedtest.SpeedTest("www.youtube.com")
#
# test.ping()
# test.download()
# test.upload()




import speedtest

st = speedtest

download_speed = st.download()
print("Your Download speed is", download_speed)

upload_speed = st.upload()
print("Your Upload speed is", upload_speed)





# import pyspeedtest
#
# from symbol import test
# print(pyspeedtest.SpeedTest())
#
# test.ping()
# test.download()
# test.upload()
