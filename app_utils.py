import os
import streamlit as st

# 디렉토리이름과 파일을 주면 해당 디렉토리에 파일을 저장해주는 함수 강사님의 
def save_uploaded_file(directory, file):
    # 1. 저장할 디렉토리가 있는지 확인하고 없으면 디렉토리를 먼저 만든다
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 2. 디렉토리가 있으니 파일을 저장
    with open(os.path.join(directory, file.name),'wb') as f :
        f.write(file.getbuffer())
    return st.success('파일 저장 완료')    