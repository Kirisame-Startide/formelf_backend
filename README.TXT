运行：先安装对应的库flask等
在getinfo目录下打开powershell,输入$env:FLASK_APP = "getinfo.py"
然后flask run以启动服务器
默认地址为http://127.0.0.1:5000/
请求示例：
http://127.0.0.1:5000/updateTable?id=1
id就是表id
请求会发送到http://127.0.0.1:5000/doUpdateTable?id=1
这里是post,get一起进行的，如果成功执行会返回成功执行

app/jsons json文件存放目录
app/docxs docx模板存放目录
app/newdocx 更改后的docx存放目录

使用前要把routes.py中的sys.path.append('C:\\Users\\Alex Chen\\Documents\\工程\\getinfo\\app')改成你当前运行的目录
