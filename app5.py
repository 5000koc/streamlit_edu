import streamlit as st
from PIL import Image

def main():
    st.title('내 앱 대시보드') # st.title은 웹브라우저에서 작업한 결과를 보려고 할 때 사용함

    # 사진과 영상을 보여주는 방법
    img = Image.open('data/image_03.jpg')

    print(img)

    st.image(img)

    st.image(img, use_column_width= True)

    # 다른 곳에 있는 이미지를 저장하지 않고 이미지URL만 불러와서 보여주기
    st.image('https://cdn.epnc.co.kr/news/photo/201907/91021_81259_3048.jpg')

    # 동영상 불러오기
    video_file = open('data/video1.mp4', 'rb')
    st.video(video_file)


if __name__ == '__main__':
    main() 