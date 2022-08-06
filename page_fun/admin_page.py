import streamlit as st
from tinydb import TinyDB,Query
import OrmServer


@st.cache()
def check_page_data(type_,page_,code,real_type=None,number=None,title=None,descripe=None,markdown=None):
    if code == '查看':
        a = OrmServer.check_page_data(type_,page_,code)
        return a
    elif code == '上传':
        a,b = OrmServer.check_page_data(type_,page_,code,real_type,number,title,descripe,markdown)
        return a,b
    elif code == '修改':
        return 0




def check_database(session):
    data = ''
    upload = ''
    select1 = st.sidebar.selectbox('导航栏',['文章上传校验','修改文章','文章查看','文章上传','删除文章','上传图片'])
    if select1 == '文章上传校验':
        markdown_test = st.sidebar.text_area('请输入Markdown内容测试')
        st.markdown(markdown_test)
    elif select1 == '文章查看':
        st.error('如果上传了文章记得清理下cache!!!!!!!!!!!!!!!!!!!!!!!')
        st.warning('请严格按下面顺序进行，先查看了有没有问题，再选择上传')
        with st.sidebar.form(key='new'):            
            type_ = st.selectbox('查看哪个页面',['主页','python','uniapp','教学设计','杂谈'])
            page_ = st.number_input('查看的页数',min_value=1,value=1)
            if st.form_submit_button('查看'):
                data = check_page_data(type_,str(page_),'查看')
        if data == '':
            st.write('')
        else:
            st.write(data)
    elif select1 == '文章上传':
        upload1 = ''
        upload2 = ''
        with st.sidebar.form('up'):
                type_ = st.selectbox('哪个页面',['主页','python','uniapp','教学设计','杂谈'])
                page_ = st.number_input('页数',min_value=1,value=1)
                real_type = st.selectbox('上传类型',['python','uniapp','教学设计','杂谈'])
                number = st.number_input('当页第几篇',min_value=1,value=1)
                title = st.text_input('标题')
                descripe = st.text_area('概述')
                markdown = st.text_area('正文Markdown')
                if st.form_submit_button('ok'):
                    upload1,upload2 = check_page_data(type_,str(page_),'上传',real_type,str(number),title,descripe,markdown)
        if (upload1 != '') and (upload2 != ''):
            st.write(upload1)
            st.write(upload2)
    elif select1 == '删除文章':
        with st.sidebar.form('del'):
            title = st.text_input('输入标题')
            if st.form_submit_button('确定'):
                OrmServer.remove_artical(title)
                st.success('删除成功')
    elif select1 == '修改文章':
        a = []
        with st.sidebar.form('change_ar'):
            title = st.text_input('请输入文章')
            if st.form_submit_button('查找'):
                artical_markdown = OrmServer.return_artical(title)
                a = {'artical_markdown': artical_markdown}
        with st.form('new'):
            st.write(a)
            newdf = st.text_area('输入新的Markdown')
            if st.form_submit_button('确定'):
                html_text = OrmServer.change_artical(title,newdf)
                if html_text == 'ok':
                    st.success('成功')
    elif select1 == '上传图片':
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            bytes_data = uploaded_file.getvalue()
            st.write(uploaded_file.name)
             
def admin_page_fun(admin,session):
    if admin == 'CJL':
        st.write('进入管理员页面')
        check_database(session)
        
    
   