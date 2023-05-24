import streamlit as st
from datetime import datetime
from app_utils import save_uploaded_file

def run_app_image():
    st.subheader('이미지 파일 업로드')
    img_file = st.file_uploader('이미지를 업로드하세요', type=['png','jpg','jpeg'])
    if img_file is not None:

        print(type(img_file))
        
        print(img_file.name)
        print(img_file.size)
        print(img_file.type)

        # 유저가 올린 파일을 서버에서 중복되지 않게 처리하기 위해 파일명을 현재시간 조합으로 만든다
        current_time = datetime.now()
        print(current_time) #현재시간
        print(current_time.isoformat().replace(':', '_') + '.jpg')

        filename = current_time.isoformat().replace(':', '_') + '.jpg'

        img_file.name = filename

        save_uploaded_file('image', img_file)

        st.image('image/'+filename) # 업로드한 이미지 파일을 미리보기 해주는 기능