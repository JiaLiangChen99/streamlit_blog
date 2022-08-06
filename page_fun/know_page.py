import streamlit as st
def back_home_page():
    st.experimental_set_query_params()

def know_page_fun():
    a = st.button('点击返回',on_click=back_home_page)
    st.write('敬请期待吧')