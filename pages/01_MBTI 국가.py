import streamlit as st
import plotly.express as px

# 데이터 불러오기 (위에서 생성한 df 사용)
# df = pd.read_csv('mbti_data.csv')  # 실제 파일로 저장할 경우

st.title("🌏 국가별 MBTI 비율 시각화")

# 국가 선택
country = st.selectbox("국가를 선택하세요:", df['Country'].tolist())

# 선택한 국가 데이터 추출
country_data = df[df['Country'] == country].iloc[0, 1:]
country_data = country_data.sort_values(ascending=False)

# 색상 설정: 1위 빨간색, 나머지는 그라데이션
colors = ['red'] + px.colors.sequential.Blues[len(country_data)-1]

fig = px.bar(
    x=country_data.index,
    y=country_data.values,
    color=country_data.index,
    color_discrete_sequence=colors,
    labels={'x':'MBTI 유형', 'y':'비율 (%)'},
    title=f"{country}의 MBTI 비율"
)

st.plotly_chart(fig, use_container_width=True)
