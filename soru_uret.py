import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_sql_question(topic):
    prompt = f"""
Sen bir SQL eğitmenisin. Aşağıda verilen konuda 1 adet çoktan seçmeli soru hazırla.
Cevap şıkları A, B, C, D olsun. Cevaplardan sonra hangi şıkkın doğru olduğunu belirt.

Konu: {topic}

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
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.6
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Hata oluştu: {e}"

# Test
if __name__ == "__main__":
    topic = input("Hangi SQL konusundan soru üretmek istersin? ")
    result = generate_sql_question(topic)
    print("\n🧠 Oluşturulan Soru:\n")
    print(result)

