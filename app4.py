import streamlit as st
import pandas as pd

def main():
    st.title('내 앱 대시보드') # st.tile(내용)은 웹브라우저에서 표시를 할려고 할 때 사용함

    df = pd.read_csv('data/iris.csv')

    # 버튼
    if st.button('데이터보기'):
        st.dataframe(df)

    name = 'Mike'
    # 대문자 버튼을 누르면 대문자로 표시
    # 소문자 버튼을 누르면 소문자로 표시
    if st.button('대문자'):
        st.text(name.lower())

    if st.button('소문자'):
        st.button(name.upper())

    st.dataframe(df)
    # petal_length 컬럼을 정렬하고 싶다
    # 오름차순정렬, 내림차순정렬 두가지 옵션 중 하나를 선택하도록 만들자

    status = st.radio('정렬을 선택하세요', ['오름차순','내림차순'])
    print(status)

    if status == '오름차순' :
        st.dataframe(df.sort_values('petal_length'))
    elif status == '내림차순':
        st.dataframe(df.sort_values('petal_length', ascending=False))

    # 체크박스
    if st.checkbox('데이터프레임 보이기'):
        st.dataframe(df.head(3))
    else :
        st.write('데이터가 없습니다')

    # 셀렉트박스(여러개 중에 1개를 선택)radio랑 다름
    language = ['Python','Java','C','Go','PHP']
    
    selected_lang = st.selectbox('선호하는 언어를 선택하세요', language)

    if selected_lang == 'Python':
        st.text('파이썬이 최고이지')
    elif selected_lang == 'Java':
        st.text('역시 어려움')
    elif selected_lang == 'C':
        st.text('이제는 퇴물이 되어버림 ㅡ,.ㅡ')
    elif selected_lang == 'Go':
        st.text('이건 뭐지?')
    elif selected_lang == 'PHP':
        st.text('웹브라우저에서 많이 썼던 것으로 기억')

if __name__ == '__main__':
    main() 