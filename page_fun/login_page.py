import streamlit as st
import extra_streamlit_components as stx
import OrmServer
import time
import datetime

def set_in_cookie(user_name,password):
    if (user_name == 'admin') and (password == 'admin'):
        return True
    else:
        return 'False'

def Login(cookie_manager):
    time_list = time.strftime('%Y-%m-%d', time.localtime(time.time())).split('-')
    year = int(time_list[0])
    month = int(time_list[1])
    day = int(time_list[2]) + 3
    with st.form('form'):
        user_name = st.text_input('用户名')
        password = st.text_input('密码',type='password')
        if st.form_submit_button('登录'):
            response = set_in_cookie(user_name,password)
            if response == True:
                cookie_manager.set('name', 'CJL', expires_at=datetime.datetime(year=year, month=month, day=day))
                st.experimental_set_query_params()
            elif response == 'False':
                st.error('暂未开放')
