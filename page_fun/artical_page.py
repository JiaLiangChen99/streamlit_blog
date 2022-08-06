import streamlit as st
import config
import OrmServer
def get_artical_markdown(title):
    artical_markdown = OrmServer.return_artical(title)  
    return {'artical_markdown': artical_markdown}

def artical_page_fun(title,blog_page=0,page=0,type_ = None):
    if (type_ == None) and (blog_page != 0):
        st.markdown('''
                    <a href="{}/?blog={}" target="_parent">点我返回</a>
                    '''.format(config.blog_url,blog_page),unsafe_allow_html=True)
    elif type_ in config.confit_blog_type:
        st.markdown('''
                    <a href="{}/?type={}&page={}" target="_parent">点我返回</a>
                    '''.format(config.blog_url,type_,page),unsafe_allow_html=True)
    markdown = get_artical_markdown(title)
    st.markdown('---')
    st.markdown(markdown['artical_markdown'][0]['markdown'],unsafe_allow_html=True)