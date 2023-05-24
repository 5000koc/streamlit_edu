import streamlit as st
import plotly.express as px
import altair as alt
import pandas as pd


def main():
    st.title('내 앱 대시보드') # st.tile은 웹브라우저에서 작업을 할려고 할 때 사용함

    df1 = pd.read_csv('data/lang_data.csv') 
    st.dataframe(df1)   

    st.write(df1.shape)

    print(df1.columns[1:])

    lang_list = df1.columns[1: ]

    choice_list = st.multiselect('언어를 선택하세요', lang_list)

    # 유저가 아무것도 선택하지 않았을 때 처리
    print(choice_list)
    if len(choice_list) > 0:

        df1[choice_list]

        choice_df = df1[choice_list]
        st.dataframe(choice_list)

        #스트림릿이 제공하는 라인차트
        st.line_chart(choice_df)

        # 스트림릿이 제공하는 영역차트
        st.area_chart(choice_df)

    df2 = pd.read_csv('data/iris.csv')

    # 스트림릿이 제공하는 바차트
    df3 = df2[['sepal_length', 'sepal_width']]
    st.bar_chart(df3)

    # Altair를 이용한 차트 작성하기
    chart = alt.Chart(df2).mark_circle().encode(
        x='petal_length',
        y='petal_width',
        color = 'species'
    )
    st.altair_chart(chart)

    #스트림릿의 map차트
    df4 = pd.read_csv('data/location.csv', index_col=0)

    print(df4)
    st.map(df4, 5)

    df5 = pd.read_csv('data/prog_languages_data.csv', index_col=0)
    st.dataframe(df5)

    # plotly의 pie차트(파이차트는 비율을 보고 싶을 때)
    fig1 = px.pie(df5, 'lang', 'Sum', title='각 프로그래밍언어의 비율') #차트의 제목을 붙이고 싶을 때 title을 넣어주면 된다)
    st.plotly_chart(fig1)

    # plotly의 bar차트

    df6 = df5.sort_values('Sum', ascending=False)

    fig2 = px.bar(df6, x='lang', y='Sum', title='각 프로그래밍언어의 비율')
    st.plotly_chart(fig2)




if __name__ == '__main__':
    main() 