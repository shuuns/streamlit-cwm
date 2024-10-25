import streamlit as st
from views import home, page1

def main():
    """主函式中撰寫您的程式碼"""
    
    # 主標題
    st.title('Streamlit 應用程式')
    # 添加分隔線
    st.markdown('---')

    menu_handler()
    # 添加分隔線
    st.markdown('---')    

    main_others()

    pass

def menu_handler():
    # 側邊欄
    st.sidebar.title('側邊欄')
    st.sidebar.markdown('#### 選單')

    # 側邊欄選單
    options = st.sidebar.selectbox(
        '選擇一個選項：',
        ('home', 'page1', '選項 3')
    )
        # 根據選擇顯示不同內容
    if options == 'home':
        # st.write('您選擇了home')
        home()
    elif options == 'page1':
        page1()
    else:
        st.write('您選擇了選項 3')
    pass

def main_others():
    
    st.subheader("This is a subheader")
    st.text('這是一個文字方塊。')

    st.write('這是一個簡單的 Streamlit 應用程式。')

    st.markdown('# Markdown H1')
    st.markdown('## Markdown H2')
    st.markdown('### Markdown H3')
    st.markdown('#### Markdown H4')

    # 成功
    st.success("Successful")

    # 警告
    st.warning("This is a warning")

    # 資訊警報
    st.info("This is an info alert")

    # 錯誤警報
    st.error("This is an error alert")

    # 異常警報
    st.exception("This is an exception alert")


if __name__ == '__main__':
    main()