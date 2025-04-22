import streamlit as st
import openai
import os
from dotenv import load_dotenv

# API anahtarını yükle
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=openai.api_key)

# Sayfa başlığı ve düzeni
st.set_page_config(page_title="SQL Chatbot + Soru Üretici", layout="centered")

st.title("🧠 SQL Uzmanı Chatbot ve Soru Üretici")
st.markdown("Bu uygulama SQL ile ilgili chatbot yanıtları ve otomatik test soruları üretir.")

# Sekmeli yapı
tab1, tab2 = st.tabs(["🗨️ Chatbot", "📋 Soru Üretici"])

# ----------- Chatbot Sekmesi -----------
with tab1:
    st.subheader("🔍 SQL Sorusu Sor")
    user_question = st.text_area("SQL ile ilgili sorunuzu yazın:", height=100)
    
    if st.button("Cevapla"):
        with st.spinner("Yanıt hazırlanıyor..."):
            prompt = f"""
Sen bir SQL uzmanısın. 
Kullanıcıdan sadece SQL ile ilgili teknik sorular alırsın.
Konu örnekleri: SELECT, INSERT INTO, GROUP BY, PRIMARY KEY, INNER JOIN, LEFT JOIN, WHERE, ORDER BY, vb.
Bunlar büyük veya küçük harfle yazılabilir, fark etmez.

Eğer gelen soru SQL dışıysa şu şekilde yanıt ver:

"Bu sistem yalnızca SQL ile ilgili teknik soruları yanıtlayabilir."


Soru: {user_question}
"""
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                st.success(response.choices[0].message.content.strip())
            except Exception as e:
                st.error(f"Hata oluştu: {e}")

# ----------- Soru Üretici Sekmesi -----------
with tab2:
    st.subheader("🧪 SQL Konusuna Göre Test Sorusu Üret")
    
    konu = st.selectbox("Konu Seçin", [
        "INNER JOIN", "LEFT JOIN", "GROUP BY", "ORDER BY", "WHERE", "PRIMARY KEY", "FOREIGN KEY"
    ])
    
    if st.button("Soru Üret"):
        with st.spinner("Soru oluşturuluyor..."):
            prompt = f"""
Sen bir SQL eğitmenisin. Konu: {konu}
Bu konuda çoktan seçmeli 1 soru oluştur. Şıkları A, B, C, D olarak ver ve doğru cevabı da belirt.

Cevap formatı şöyle olsun:
Soru: ...
A) ...
B) ...
C) ...
D) ...
Doğru cevap: ...
"""
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                st.success(response.choices[0].message.content.strip())
            except Exception as e:
                st.error(f"Hata oluştu: {e}")
