import streamlit as st
from tool.tool1 import tool1_fun
def back_home_page():
    st.experimental_set_query_params()

def tool_page_fun(user=None):
    a = st.button('点击返回',on_click=back_home_page)
    tool = st.sidebar.selectbox('工具包',['abc','efg'])
    st.write('暂未开放')
    tool1_fun()