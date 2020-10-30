import pymysql

dbconnection=pymysql.connect("io3.top","votesystem","192.168.1.1","votesystem" )
cursor=dbconnection.cursor()

def AddUser(username,password):
    