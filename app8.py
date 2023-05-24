import streamlit as st
from app_img import run_app_img
from app_csv import run_app_csv
from app_about import run_app_about


def main():
    st.title('내 앱 대시보드') # st.tile은 웹브라우저에서 작업을 할려고 할 때 사용함
    
    # 브라우저 왼쪽으로 메뉴 작업
    menu = ['이미지업로드','csv업로드', 'about']
    choice = st.sidebar.selectbox("메뉴", menu)
    # print(choice)

    if choice == menu[0]: 
        run_app_img()        



    elif choice == menu[1]:
        run_app_csv()
           
    else: 
        run_app_about()
        




if __name__ == '__main__':
    main() 