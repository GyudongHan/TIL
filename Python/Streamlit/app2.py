# -*- coding: UTF-8 -*-
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.graph_objects as go

def calculat_sales_revenue(price, total_sales):
    revenue = price * total_sales
    return revenue

iris = sns.load_dataset('iris')
# 그래프 그리기 전 변수 확인용 st.dataframe(iris.head())

def plot_matplotlib():
    st.title('산점도 matplotlib')
    fig, ax = plt.subplots()
    ax.scatter(iris['sepal_length'], iris['sepal_width'])
    st.pyplot(fig)

def plot_seaborn():
    st.title('산점도 seaborn')
    fig, ax = plt.subplots()
    sns.scatterplot(iris, x = 'sepal_length', y = 'sepal_width')
    st.pyplot(fig)

def plot_plotly():
    st.title('Scatter Plot with Plotly')
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x = iris['sepal_length'],
                   y = iris['sepal_width'],
                   mode='markers')
    )
    st.plotly_chart(fig)

def main():
    st.title("오후 수업")

    price = st.slider("단가: ", 1000, 10000, value=5000)
    total_sales = st.slider("전체 판매 수", 1, 1000, value=500)
    st.write(price, total_sales)

    if st.button("매출액 계산"):
        result = calculat_sales_revenue(price, total_sales)
        st.write("전체 매출액은", "{:,}".format(result), "원(KRW)")

    # 체크박스
    x = np.linspace(0,10,100)
    y = np.sin(x)

    show_plot = st.checkbox("시각화 표시")
    st.write(show_plot)
    fig, ax = plt.subplots()
    ax.plot(x,y)

    
    if show_plot:
        st.pyplot(fig)

    st.write('---')
    plot_type = st.radio(
        "어떤 타입의 산점도를 보고 싶으세요?",
        ("matplotlib", "seaborn", "plotly","시각화 끄기")
    )
    if plot_type == "시각화 끄기":
        st.write(" ")
    else:
        st.write(plot_type)

    if plot_type == "matplotlib":
        plot_matplotlib()
    elif plot_type == "seaborn":
        plot_matplotlib()
    elif plot_type == "plotly":
        plot_matplotlib()
    elif plot_type == "시각화 끄기":
        st.write(" ")
    else:
        st.error("에러")

    st.write('---')

    # selectbox
    st.markdown('## Raw Data')
    st.dataframe(iris)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("### Selectbox")
    st.write(iris['species'].unique())
    col_name = st.selectbox('1개의 종을 선택하세요!', iris['species'].unique())
    st.write(col_name)

    result = iris.loc[iris['species'] == col_name].reset_index(drop=True)
    # st.dataframe(result)

    st.title('Scatter Plot with plotly')
    fig = go.Figure()
    
    fig, ax = plt.subplots()
    ax.scatter(result['sepal_length'], result['sepal_width'])
    st.pyplot(fig)

    # seaborn을 이용한 scatter
    # fig, ax = plt.subplots()
    # sns.scatterplot(result, x = 'sepal_length', y = 'sepal_width')
    # st.pyplot(fig)


    st.write('---')
    # MultiSelect
    cols = st.multiselect("복수의 컬럼 선택", iris.columns)
    st.write(cols)
    filtered_iris = iris.loc[:, cols]
    st.dataframe(filtered_iris)

    







































if __name__ == "__main__":
    main()