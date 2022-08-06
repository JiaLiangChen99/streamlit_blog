from tinydb import TinyDB,Query,where
import requests
import json
import config
#创建5张表，分别存储type=zhuye ,python ,uniapp ,教育学 ,杂谈
#建立一个索引可以指向哪个文件  {'type':'主页','filename':'main_db'},{'type':'python',filename:python_db}
#read_main_db    获得page好吧 {page:1,}
my_server = config.my_server

'''
博客页面数据的创建格式
db = TinyDB(r'db\blog_main.json')
blog_data1 = {'page':1,'show_data':{'1':{'type':'python','title':'文章1','descripe':'描述1'}}}
blog_data2 = {'page':1,'show_data':{'2':{'type':'python','title':'文章2','descripe':'描述2'}}}
blog_data3 = {'page':2,'show_data':{'1':{'type':'python','title':'文章2','descripe':'描述2'}}}
blog_data4 = {'page':2,'show_data':{'2':{'type':'python','title':'文章2','descripe':'描述2'}}}
db.insert_multiple(
    [blog_data1,blog_data2,blog_data3,blog_data4]
    )
    
python页面数据的创建格式
db = TinyDB(r'db\blog_python.json')
blog_data1 = {'page':1,'show_data':{'1':{'type':'python','title':'文章1','descripe':'描述1'}}}
blog_data2 = {'page':1,'show_data':{'2':{'type':'python','title':'文章2','descripe':'描述2'}}}
blog_data3 = {'page':2,'show_data':{'1':{'type':'python','title':'文章2','descripe':'描述2'}}}
blog_data4 = {'page':2,'show_data':{'2':{'type':'python','title':'文章2','descripe':'描述2'}}}
db.insert_multiple(
    [blog_data1,blog_data2,blog_data3,blog_data4]
    )
    
其他同理



博客文章页面的数据
a1 = """
    ## 1 文章1

    - 支持自定义样式的 Markdown 编辑器
    - 支持微信公众号、知乎和稀土掘金
    - 点击右上方对应图标，一键复制到各平台

    ## 2 Markdown语法教程
    """

db = TinyDB(r'db\artical_data.json')
blog_data1 = {'title':'文章1','markdown':a1}
blog_data2 = {'title':'文章2','markdown':a2}
blog_data3 = {'title':'文章3','markdown':a3}
blog_data4 = {'title':'文章4','markdown':a4}
db.insert_multiple(
    [blog_data1,blog_data2,blog_data3,blog_data4]
    )
'''


#获取博客主页的渲染数据
def return_blog(find_page):  #=>  find_page  页数    return:返回的是第find_page页的博客页面的渲染数据
    #global my_server
    try:
        page = eval(find_page)
    except:
        return 'error'
    if type(page) == int:
        response = requests.get(url='{}/blog/{}'.format(my_server,page))
        return response.json()
    else:
        return 'error'


#博客主页中获取最大页数
def blog_max_page():  
    return int(requests.get(url=my_server+'/blogmax').text)


#获取系列页面的最大页数
def type_max_page(type_):  #=> type_ 传入的是哪个系列文章   return:该系列最大页数
    return int(requests.get(url=my_server+'/typemax/'+type_).text)
    

#获取类型页面数据
def return_type(type_,page):  #=> type_ 传入的是哪个系列文章 page 页数   return:该系列第page页的系列文章数据
    try:
        page = eval(page)
    except:
        return 'error'
    if type(page) == int:
        return requests.get(url=my_server+'/type/'+type_+'/page/'+str(page)).json()
    else:
        return 'error'


##用完整title获取markdown  todo:搜索栏的函数可以在这里加工
def return_artical(title):  #=> title 文章名  return:markdown语句
    print(1)
    return requests.get(url=my_server+'/title/'+ title).json()['artical']

#admin 用户的查看上传功能
def check_page_data(type_,page_,code,real_type=None,number=None,title=None,descripe=None,markdown=None):
    url = my_server+'/upload'
    if code == '查看':
        params = {
            'type_':type_,
            'page_':page_,
            'code':code 
            }
        a = requests.post(url,json.dumps(params)).json()
        return a
    elif code == '上传':
        params = {
            'type_':type_,
            'page_':page_,
            'code':code ,
            'real_type':real_type,
            'number':number,
            'title':title,
            'descripe':descripe,
            'markdown':markdown
            }
        df = requests.post(url,json.dumps(params)).json()
        return df[0],df[1]
    else:
        pass

#admin  删除文章
def remove_artical(title):
    params={"title": title}
    #requests.get(my_server+'/remove/{}'.format(title)).json()
    url = my_server+'/remove'
    html = requests.post(url, json.dumps(params))

#修改
def change_artical(title,newdf):
    params={"title": title,'newdf':newdf}
    url = my_server+'/change'
    html = requests.post(url, json.dumps(params))
    return html.text.replace('"','')


#上传照片
def upload_pic(byte):
    url = my_server + "/file_upload"
    files = {'file': byte}
    r = requests.post(url, files=files)
    return r.json()

