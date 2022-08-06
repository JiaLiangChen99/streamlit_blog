import streamlit as st
import config
import OrmServer
def get_api(type_,page):
    get_page = OrmServer.type_max_page(type_)
    if int(page) <= get_page:
        blog_show = OrmServer.return_type(type_,str(page))
        return {'show_data': blog_show,'max_page': get_page}
    else:
        return {'show_data': {},'max_page': get_page}

def side_bar1(type_,page,show_df):
    for num in show_df.keys():
        with st.expander("类型:{}".format(show_df[num]['type']),True):
            st.markdown('### 标题:{}'.format(show_df[num]['title']))
            st.markdown('''
                    <a href="{}/?type={}&page={}&title={}" target="_blank" style='color:black'>{}</a> 
                        '''.format(config.blog_url,type_,page,show_df[num]['title'],show_df[num]['descripe'][:120]),unsafe_allow_html=True)

def side_bar2(blog_type):
    show_list = config.confit_blog_type
    df = [ i for i in show_list if i != blog_type]
    for show_count in range(len(df)):
        st.markdown('''
                    <a href='{}/?type={}&page=1' target="_parent" style='color:black'>{}</a>
                    '''.format(config.blog_url,df[show_count],df[show_count]),unsafe_allow_html=True)

def type_page_fun(blog_type,page):
    blog_url = config.blog_url
    data = get_api(blog_type,page)
    if data['show_data'] == {}:
        st.error('这里没有你要的东西')
    else:
        show_df = data['show_data']
        all_page = data['max_page']
        image_dict = {
            'python':'https://images.pexels.com/photos/1181359/pexels-photo-1181359.jpeg?auto=compress&cs=tinysrgb&w=600',
            'uniapp':'https://images.pexels.com/photos/89955/pexels-photo-89955.jpeg?auto=compress&cs=tinysrgb&w=600',
            '教学设计':'https://images.pexels.com/photos/207691/pexels-photo-207691.jpeg?auto=compress&cs=tinysrgb&w=600',
            '杂谈':'https://images.pexels.com/photos/272802/pexels-photo-272802.jpeg?auto=compress&cs=tinysrgb&w=600'
            }
        st.markdown('''
                    <div align="center"><img src="{}"  / ></div>
                    '''.format(image_dict[blog_type]),unsafe_allow_html=True)
        st.markdown('---')
        col1,col2 = st.columns([4,2])
        with col1:
            side_bar1(blog_type,page,show_df)
        with col2:
            with st.form('find'):
                woud_find = st.text_input('查找文章')
                if st.form_submit_button('提交'):
                    st.success('该功能暂未开放,还在测试中')
            st.markdown('---')
            with st.expander("查看系列文章",True):
                side_bar2(blog_type)
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
                                <li><a href="%s/?type=%s&page=1" target="_parent">首页</a></li>
                                <li><a href="%s/?type=%s&page=%d" target="_parent">下一页</a></li>
                                <li><a href="%s/?type=%s&page=%d" target="_parent">末页</a></li>
                            </ul>
                            </div>
                        </body>
                        ''' % (blog_url,blog_type,blog_url,blog_type,page+1,blog_url,blog_type,all_page) ,unsafe_allow_html=True)
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
                        <li><a href="%s/?type=%s&page=1" target="_parent">首页</a></li>
                        <li><a href="%s/?type=%s&page=%d" target="_parent">上一页</a></li>
                        <li><a href="%s/?type=%s&page=%d" target="_parent">末页</a></li>
                    </ul>
                    </div>
                </body>
                ''' % (blog_url,blog_type,blog_url,blog_type,page-1,blog_url,blog_type,all_page) ,unsafe_allow_html=True)
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
                                <li><a href="%s/?type=%s&page=1" target="_parent">首页</a></li>
                                <li><a href="%s/?type=%s&page=%d" target="_parent">上一页</a></li>
                                <li><a href="%s/?type=%s&page=%d" target="_parent">上一页</a></li>
                                <li><a href="%s/?type=%s&page=%d" target="_parent">末页</a></li>
                            </ul>
                            </div>
                        </body>
                        ''' % (blog_url,blog_type,blog_url,blog_type,page-1,blog_url,blog_type,page+1,blog_url,blog_type,all_page) ,unsafe_allow_html=True)