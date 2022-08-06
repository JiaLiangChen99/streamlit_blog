import streamlit as st
import extra_streamlit_components as stx
from config import confit_blog_type
from page_fun import admin_page,know_page,home_page,error_page,artical_page,blog_page,login_page,source_page,tool_page,type_page
#fastapi qidong: uvicorn main:app --host 0.0.0.0 --port 8080 --reload
def out(cookie_manager,name):
    cookie_manager.delete(name)
    st.session_state.name = None

#@st.cache(suppress_st_warning = True,allow_output_mutation=True)
def get_manager():
    return stx.CookieManager(key='second')

def show_app_title(my_query_params):
    code = 'None'
    title = ''
    if 'title' in my_query_params:
        code = 'title'
        title = my_query_params['title'][0]
    dict = {'None':'Streamlit','title':title}
    text = dict[code]
    st.set_page_config(
     page_title=text,
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded")
    
    
def admin_set():
    st.experimental_set_query_params(admin='admin')

def the_sider_bar(page=None):
    if page == None:
        st.sidebar.markdown('# *streamlit*')
        st.sidebar.markdown('---')
        st.sidebar.markdown('''
                            ## About:
                            
                            此项目是本人在学习[streamlit](https://streamlit.io/)过程中尝试制作,对与此框架还了解不够透彻,且并非前端出生,所以界面设计粗糙.另外如有BUG请见谅
                            
                            若有更好的意见或建议（比如页面排版）,可以联系我v:`cjl15820443028` ——感谢!
                            
                            国内streamlit的相关资料并不多,作者也尽可能分享一些不错的轮子
                            
                            项目前端基于streamlit,后端仅采用[fastapi](https://fastapi.tiangolo.com/zh/)进行静态文件部署,业务逻辑可以直接在streamlit文件中完成。
                            
                            作者资金有限,服务器买海外且配置较低,故有时候访问速度慢,且没时间申请SSL证书(如浏览器可能会说连接不安全请勿上传账号密码信息等,但本站也未涉及到用户浏览器的账号密码等信息，仅做分享文章)
                            
                            本人也即将考研,项目开发也仅是抽空完成的。
                            ''')

#获取网页url中的参数
my_query_params = st.experimental_get_query_params()
#根据参数选择标题初始化类型
show_app_title(my_query_params)
#获取cookie,有延迟
cookie_manager = get_manager()
if cookie_manager.get_all() == {}:
    st.stop()
#获取cookie中的name
name = cookie_manager.get(cookie='name')
#如果name未空
if name == None:
    if 'name' not in st.session_state:
        st.session_state.name = None
#管理员页面才有显示
else:
    if name == 'CJL':
        st.sidebar.button('管理员页面',on_click=admin_set)
    st.session_state.name = name
    st.session_state.check = None
    st.sidebar.button('点我注销',on_click=out,args=(cookie_manager,'name'))
if 'login' in my_query_params:
    login_page.Login(cookie_manager)
elif 'admin' in my_query_params:
    admin_page.admin_page_fun(st.session_state.name,st.session_state.check)
elif 'blog' in my_query_params:
    try:
        page = eval(my_query_params['blog'][0])
        if 'title' in my_query_params:
            the_sider_bar()
            artical_page.artical_page_fun(my_query_params['title'][0],blog_page=page,)
        else:
            page = my_query_params['blog'][0]
            the_sider_bar()
            blog_page.blog_page_fun(page)
    except:
        error_page.st_error()
elif 'dev' in my_query_params:
    the_sider_bar()
    tool_page.tool1_fun()
elif 'knowledge' in my_query_params:
    the_sider_bar()
    know_page.know_page_fun()
elif 'resource' in my_query_params:
    the_sider_bar()
    source_page.source_page_fun()
elif 'type' in my_query_params:
    type_ = my_query_params['type'][0]
    try:
        page_ = eval(my_query_params['page'][0])
        if type_ in confit_blog_type:
            if 'title' in my_query_params:
                the_sider_bar()
                artical_page.artical_page_fun(my_query_params['title'][0],page=page_,type_=type_)
            else:
                the_sider_bar()
                type_page.type_page_fun(type_,page_)
        else:
            the_sider_bar()
            error_page.st_error()
    except:
        the_sider_bar()
        error_page.st_error()       
else:
    the_sider_bar()
    home_page.home_page_fun(st.session_state.name)
    
def ceshi(test1):
    return 'asdf'
st.markdown('''
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-1v3fvcr.egzxvld3 > div{background:rgb(246 244 244)}
            </style>
            ''',unsafe_allow_html=True)
st.markdown('''
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section.css-1k0ckh2.e1fqkh3o9 > div.css-10xlvwk.e1fqkh3o3{background-color:rgb(230 233 240)}
            </style>
            ''',unsafe_allow_html=True)
st.markdown('''
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-1v3fvcr.egzxvld3{background-color:rgb(199 199 199)}
            </style>''',unsafe_allow_html=True)
st.markdown('''
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section.css-1k0ckh2.e1fqkh3o9 > div.css-10xlvwk.e1fqkh3o3 > div.css-hxt7ib.e1fqkh3o2 > div > div:nth-child(1) > div > div:nth-child(2) > div > button{border:0px solid rgba(49, 51, 63, 0.2);color:rgb(34 94 233)}
            </style>
            ''',unsafe_allow_html=True)