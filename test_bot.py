import openai
import os

from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_sql_bot(question):
    prompt = f"""
Sen bir SQL dili uzmanısın. Kullanıcı SQL ile ilgili bir soru sorduğunda,
detaylı ama sade bir şekilde açıklama yap. Gerekirse örnek SQL kodu ver.

Soru: {question}
Cevap:
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen bir SQL uzmanısın."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Hata oluştu: {e}"

# Test
print("Başlıyor...")

user_question = "INNER JOIN nedir?"
answer = ask_sql_bot(user_question)

# Cevabı bir dosyaya yazalım:
with open("cevap.txt", "w", encoding="utf-8") as file:
    file.write(answer)

print("Bitti. 'cevap.txt' dosyasını kontrol et.")
