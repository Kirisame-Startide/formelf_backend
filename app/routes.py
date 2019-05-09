from app import app
from flask import request
import sys 
sys.path.append('C:\\Users\\Alex Chen\\Documents\\工程\\formelf\\formelf_backend\\app')
import pageGen
import json2replace
import pymysql
import json

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/get')
def get():
    conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='',db='xcx',charset='utf8mb4')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM `templates`")
    ifo=cursor.fetchall()
    dict_=[]
    key_=[]
    i=0
    keys=('templateID','exampleID','evaluateID','templateName','templatePermissions','templateIntro','templateDescription','templateTime','templateCount','templateFormat','templatePrice','templatePic')
    for info in ifo:
        dic=dict(zip(keys,info))
        key_.append('form'+str(i))
        i=i+1
        dict_.append(str(dic))
    jsonData=dict(zip(key_,dict_))
    #print(str(jsonData))
    jsonObj=json.dumps(jsonData)
    return(str(jsonObj))

#    if request.method=='POST':
#        if request.form['type']=='1':
@app.route('/creatTemplate',methods=['POST'])
def crtemp():

    return(0)

@app.route('/getDefaultData',methods=['POST'])
def getdefalut():
    conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='',db='xcx',charset='utf8mb4')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM `templates`")
    ifo=cursor.fetchall()
    return(str(ifo))
#这个是用来获取初始信息的，从这里拿到表的id,名字等信息供用户选择，尚未完工

@app.route('/updateTable',methods=['GET'])
def updateTable():
    try:
        page=pageGen.pageGen(request.args.get('id'))
    except: 
        page='出现问题，请检查:<br/>1.是否提交了get信息<br/>2.提交的id是否存在'
    return(page)
    #get请求一个id，id为json以及docx的编号
#用户请求一个id,返回一个对应json生成的网页。pageGen是生成网页的程序。请求id部分尚不完善。form会提交给doUpdateTable

@app.route('/doUpdateTable',methods=['GET','POST'])
def dut():
    keys=[]
    values=[]
    id_=request.args.get('id')
    for i in request.form:
        keys.append(i)
    for key in keys:
        values.append(request.form.get(key))
    dic=dict(zip(keys,values))
    #dic是用户传回的键值对字典
    result=json2replace.autoproc(dic,id_)
    print(result)
    return(result)
#对表进行更改的主操作，未进行加密，后期应进行加密。autoproc由main函数修改而来，返回值成功1失败0，不过暂时还没写。