import json
import  os

def pageGen(id_):
    dir=os.getcwd()
    print(dir)
    jsonobj=json.load(open(str(dir)+'\\app\\jsons\\'+str(id_)+'.json', encoding='utf-8'))
    #读取jsons里的json文件，标记为前台传来的id
    page='''<!DOCTYPE html><html><body><form action="doUpdateTable'''+'?id='+str(id_)+'''" method="POST">'''
    for item in jsonobj['result']['data']:
        page=page+item+''':<br><input type="text" name="'''+item+'''"><br>'''
    page=page+'''<input type="submit" value="Submit"></form></body></html>'''
    return(page)
    

