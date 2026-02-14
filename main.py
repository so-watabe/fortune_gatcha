import streamlit as st
import random
import time

st.title("🎰 運勢ガチャアプリ")

fortunes = ["大吉", "中吉", "小吉", "吉", "末吉", "凶", "大凶"]
colors = ["赤", "青", "緑", "黄色", "紫", "ピンク", "オレンジ"]
missions = [
    "笑顔で挨拶する",
    "部屋を5分掃除する",
    "水を多めに飲む",
    "SNSにポジティブ投稿",
    "10分勉強する"
]

if "history" not in st.session_state:
    st.session_state.history = []

placeholder = st.empty()

def draw_fortune():
    while True:
        fortune = random.choice(fortunes)
        if len(st.session_state.history) == 0 or fortune != st.session_state.history[-1]["fortune"]:
            break
    return fortune

if st.button("🎲 ガチャを引く"):
    with st.spinner("運勢を占っています..."):
        for i in range(3, 0, -1):
            placeholder.markdown(f"# {i}...")
            time.sleep(1)

    fortune = draw_fortune()

    number = random.randint(1, 100)
    mission = random.choice(missions)

    result = {
        "fortune": fortune,
        "color": color,
        "number": number,
        "mission": mission
    }

    st.session_state.history.append(result)

    placeholder.markdown(f"# 🎉 {fortune} 🎉")
    st.balloons()

    st.markdown(f"### 🎨 ラッキーカラー: **{color}**")
    st.markdown(f"### 🔢 ラッキーナンバー: **{number}**")
    st.markdown(f"### 🚀 今日のミッション: **{mission}**")

if st.session_state.history:
    st.subheader("📜 履歴")
    for i, item in enumerate(reversed(st.session_state.history), 1):
        st.write(f"{i}回目 → {item['fortune']} / {item['color']} / {item['number']}")

if st.session_state.history:
    latest = st.session_state.history[-1]
    share_text = f"""
今日の運勢は【{latest['fortune']}】！
ラッキーカラー: {latest['color']}
ラッキーナンバー: {latest['number']}
ミッション: {latest['mission']}

#100DaysOfCode #Streamlit
"""
    st.text_area("📢 シェア用テキスト", share_text)


