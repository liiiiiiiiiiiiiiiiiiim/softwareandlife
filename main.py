import streamlit as st

st.set_page_config(page_title="BR 키오스크 🍨", page_icon="🍦")

st.title("🍦 베스킨라빈스 키오스크")
st.write("환영합니다! 주문을 도와드릴게요 😄")

# -----------------------------------
# 1. 매장/포장 선택
# -----------------------------------
st.header("1️⃣ 이용 방식 선택")
eat_option = st.radio(
    "매장에서 드시나요? 포장해서 가져가시나요?",
    ("매장에서 먹기 🍽️", "포장해가기 🛍️")
)

# -----------------------------------
# 2. 용기 선택 (맛 개수 설정)
# -----------------------------------
st.header("2️⃣ 용기 선택")
container = st.selectbox(
    "원하시는 용기를 골라주세요!",
    ("싱글 레귤러(1가지 맛)", "더블 주니어(2가지 맛)", "파인트(3가지 맛)")
)

# 용기별 맛 개수와 가격 설정
container_info = {
    "싱글 레귤러(1가지 맛)": {"count": 1, "price": 3500},
    "더블 주니어(2가지 맛)": {"count": 2, "price": 5900},
    "파인트(3가지 맛)": {"count": 3, "price": 8200}
}

max_flavors = container_info[container]["count"]

# -----------------------------------
# 3. 맛 고르기
# -----------------------------------
st.header("3️⃣ 아이스크림 맛 선택 🍨")

flavors = [
    "아몬드 봉봉", "엄마는 외계인", "민트초코", "뉴욕치즈케이크",
    "초코나무숲", "베리베리 스트로베리", "슈팅스타", "레인보우 샤베트"
]

selected_flavors = st.multiselect(
    f"최대 {max_flavors}가지 맛을 선택할 수 있어요!",
    flavors
)

# 선택 개수 제한 안내
if len(selected_flavors) > max_flavors:
    st.error(f"❗ {max_flavors}가지까지만 선택 가능합니다.")
    selected_flavors = selected_flavors[:max_flavors]

# -----------------------------------
# 4. 최종 가격
# -----------------------------------
st.header("4️⃣ 결제 금액 확인 💰")

price = container_info[container]["price"]
st.subheader(f"총 결제 금액: **{price:,}원** 입니다!")

# -----------------------------------
# 5. 결제 선택
# -----------------------------------
st.header("5️⃣ 결제 방법 선택")

pay = st.radio(
    "결제 수단을 선택해주세요 😊",
    ("💳 카드 결제", "💵 현금 결제", "📱 기프티콘 결제")
)

if st.button("결제 진행하기"):
    if pay == "💳 카드 결제":
        st.success("💳 카드 결제 화면으로 이동합니다! 카드를 넣어주세요 😊")
    elif pay == "💵 현금 결제":
        st.success("💵 현금 투입구에 돈을 넣어주세요! 감사합니다 😄")
    else:
        st.success("📱 기프티콘 번호를 입력해주세요! 확인 후 바로 결제됩니다 😊")

