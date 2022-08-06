import streamlit as st
import config
import OrmServer

def get_api(page,blog_type=None):
    blog_show = OrmServer.return_blog(str(page))  #
    get_page = OrmServer.blog_max_page()
    return {'show_data': blog_show,'max_page': get_page}

def back_home_page():
    st.experimental_set_query_params()

def side_bar2(set_page):
    st.markdown('''
                <a href='{}/?type=python&page=1' target="_parent" style='color:black'>python</a>
                '''.format(config.blog_url),unsafe_allow_html=True)
    st.markdown('''
                <a href='{}/?type=uniapp&page=1' target="_parent" style='color:black'>uniapp</a>
                '''.format(config.blog_url),unsafe_allow_html=True)
    st.markdown('''
                <a href='{}/?type=教学设计&page=1' target="_parent" style='color:black'>教学设计</a>
                '''.format(config.blog_url),unsafe_allow_html=True)
    st.markdown('''
                <a href='{}/?type=杂谈&page=1' target="_parent" style='color:black'>杂谈</a>
                '''.format(config.blog_url),unsafe_allow_html=True)

def side_bar1(page,show_df):
    for num in show_df.keys():
        with st.expander("类型:{}".format(show_df[num]['type']),True):
            st.markdown('''<span style="display:block;text-align:center;color:red;font-size:30px">{}</span>'''.format(show_df[num]['title']),unsafe_allow_html=True)
            st.markdown('''
                    <a href="{}?blog={}&title={}" target="_blank" style='color:black'>{}</a> 
                        '''.format(config.blog_url,page,show_df[num]['title'],show_df[num]['descripe'][:120]),unsafe_allow_html=True)

def blog_page_fun(page,blog_type=None):
    page = int(page)
    blog_url = config.blog_url
    a = st.button('返回首页',on_click=back_home_page)
    blog_data = get_api(page,blog_type)
    if  blog_data['show_data'] != {}:
        show_df = blog_data['show_data']
        all_page = blog_data['max_page']
        st.markdown('''
                    <div align="center"><img src="{}/blog.jpg" width=703px height=309px / ></div>
                    '''.format(config.fastapi_server),unsafe_allow_html=True)
        st.markdown('---')
        col1,col2 = st.columns([4,2])
        with col1:
            side_bar1(page,show_df)
        with col2:
            with st.form('find'):
                woud_find = st.text_input('查找文章')
                if st.form_submit_button('提交'):
                    st.success('当前功能后台逻辑还未开放请等待(目前也没啥文章哈哈哈,想自己思考一个快速查询的算法):')
            st.markdown('---')
            with st.expander("查看系列文章",True):
                side_bar2(page)
        st.markdown('''
                    <style>
                    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-1v3fvcr.egzxvld3 > div > div:nth-child(1) > div > div:nth-child(3) > div > button{border:0px solid rgba(49, 51, 63, 0.2);background-color:rgb(246 244 244)}
                    </style>
                    ''',unsafe_allow_html=True)
        if page == 1:
            st.markdown('''
                        <style type="text/css">
                            .page-nav{
                            height: 60px;
                            width:100%%;
                            line-height: 60px;
                            text-align: center;
                            overflow: hidden;
                            }
                            .page-nav>ul{
                                overflow: hidden ;
                                margin: 0 30%% ;
                                width:80%% ;
                            }
                            .page-nav>ul>li{
                                float: left;
                                list-style-type: none;
                                margin-right:20px;
                            }
                        </style>
                        <body>
                            <div class="page-nav">
                            <ul align="center">
                                <li><a href="%s/?blog=1" target="_parent">首页</a></li>
                                <li><a href="%s/?blog=%d" target="_parent">下一页</a></li>
                                <li><a href="%s/?blog=%d" target="_parent">末页</a></li>
                            </ul>
                            </div>
                        </body>
                        ''' % (blog_url,blog_url,page+1,blog_url,all_page) ,unsafe_allow_html=True)
        elif page == all_page:
            st.markdown('''
                <style type="text/css">
                    .page-nav{
                    height: 60px;
                    width:100%%;
                    line-height: 60px;
                    text-align: center;
                    overflow: hidden;
                    }
                    .page-nav>ul{
                        overflow: hidden ;
                        margin: 0 30%% ;
                        width:80%% ;
                    }
                    .page-nav>ul>li{
                        float: left;
                        list-style-type: none;
                        margin-right:20px;
                    }
                </style>
                <body>
                    <div class="page-nav">
                    <ul align="center">
                        <li><a href="%s/?blog=1" target="_parent">首页</a></li>
                        <li><a href="%s/?blog=%d" target="_parent">上一页</a></li>
                        <li><a href="%s/?blog=%d" target="_parent">末页</a></li>
                    </ul>
                    </div>
                </body>
                ''' % (blog_url,blog_url,page-1,blog_url,all_page) ,unsafe_allow_html=True)
        else:
                    st.markdown('''
                        <style type="text/css">
                            .page-nav{
                            height: 60px;
                            width:100%%;
                            line-height: 60px;
                            text-align: center;
                            overflow: hidden;
                            }
                            .page-nav>ul{
                                overflow: hidden ;
                                margin: 0 30%% ;
                                width:80%% ;
                            }
                            .page-nav>ul>li{
                                float: left;
                                list-style-type: none;
                                margin-right:20px;
                            }
                        </style>
                        <body>
                            <div class="page-nav">
                            <ul align="center">
                                <li><a href="%s/?blog=1" target="_parent">首页</a></li>
                                <li><a href="%s/?blog=%d" target="_parent">上一页</a></li>
                                <li><a href="%s/?blog=%d" target="_parent">下一页</a></li>
                                <li><a href="%s/?blog=%d" target="_parent">末页</a></li>
                            </ul>
                            </div>
                        </body>
                        ''' % (blog_url,blog_url,page-1,blog_url,page+1,blog_url,all_page) ,unsafe_allow_html=True)
    else:
        st.error('这里没有东西')