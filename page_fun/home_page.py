import streamlit as st
import config
import OrmServer

@st.cache  #需要重新运行
def read_url():
    blog_url,my_fastapi = config.blog_url,config.fastapi_server
    return blog_url,my_fastapi

def home_page_fun(df):
    st.markdown('## 哪有什么岁月静好，不过有人在替你负荆前行罢了')
    blog_url,my_fastapi = read_url()
    a = st.markdown('''
                <div align="center"><img src='{}/backgroud.jpg' width=100% height=100%  /> </div>   
                '''.format(my_fastapi),unsafe_allow_html=True)
    if df == None:
        st.markdown('''
            <a>如果你想尝试更多功能(以后的事情，目前还未有)，请进行<a href="{}/?login=1"  >登录(开玩笑的本人太懒了暂时还没写登录接口你可以进去体验下而已)</a></a>
        '''.format(blog_url),unsafe_allow_html=True)
    st.markdown('---')
    st.markdown('''
                <div align="center"><b style="color:black;font-size:40px">分区<b></div>
                ''',unsafe_allow_html=True)
    '''
    记录大坑：HTML标签中，不要用h标签，比如我下面分类页面用了H标签，那渲染的时候会自动跳到底下去就很不爽，本来显示在上面就不动了
    '''
    col1,col2,col3 = st.columns(3)
    with col1:
        st.markdown('''
               <div align="center"><a href="https://www.baidu.com/" target="_parent"><img src="https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"  width=160px height=160px/></a></div>
                ''',unsafe_allow_html=True)
        st.markdown('''
        <div align="center"><p>博客</p></div>
                ''',unsafe_allow_html=True)
        st.markdown('''
               <div align="center"><a href="https://jialiangchen99-streamlit-blog-main-2csjzy.streamlitapp.com/?resource=1" target="_parent"><img src="{}/conputer.jpg"  width=160px height=160px/></a></div>
                '''.format(my_fastapi),unsafe_allow_html=True)
        st.markdown('''
        <div align="center"><p>资源</p></div>
                '''.format(blog_url,my_fastapi),unsafe_allow_html=True)
    with col2:
        st.markdown('''
               <div align="center"><a href="{}/?dev=1" target="_parent"><img src="{}/beg.jpg"  width=160px height=160px/></a></div>
                '''.format(blog_url,my_fastapi),unsafe_allow_html=True)
        st.markdown('''
        <div align="center"><p>工具库</p></div>
                '''.format(blog_url,my_fastapi),unsafe_allow_html=True)
    with col3:
        st.markdown('''
               <div align="center"><a href="{}/?knowledge=1" target="_parent"><img src="{}/readding.jpg"  width=160px height=160px/></a></div>
                '''.format(blog_url,my_fastapi),unsafe_allow_html=True)
        st.markdown('''
        <div align="center"><p>知识库</p></div4>
                '''.format(blog_url,my_fastapi),unsafe_allow_html=True)
