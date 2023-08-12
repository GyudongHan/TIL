import plotly.graph_objects as go 
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title("확인")
    with st.sidebar:
        st.header("Sidebar")
        day = st.selectbox("요일 선택", ["Thur", "Fri", "Sat", "Sun"])

    tips = sns.load_dataset("tips")
    filtered_tips = tips.loc[tips['day'] == day]
    # st.dataframe(filtered_tips)
    top_bill = filtered_tips['total_bill'].max()
    top_tip = filtered_tips['tip'].max()

    # tab1, tab2, tab3 = st.sidebar.tabs(['Totab Bill', 'Tip', 'Size'])
    tab1, tab2, tab3 = st.tabs(['Total Bill', 'Tip', 'Size'])
    with tab1:
        fig, ax = plt.subplots()
        st.header("Total Bill")
        sns.histplot(filtered_tips['total_bill'], kde=False, ax=ax)
        st.pyplot(fig)
    with tab2:
        st.metric("최고 지불", top_bill)
    with tab3:
        st.metric("최고 팁", top_tip)


if __name__ == "__main__":
    main()