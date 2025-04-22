import openai
import os
from dotenv import load_dotenv
from prompts import build_sql_prompt

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_sql_bot(question):
    prompt = build_sql_prompt(question)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Sen bir SQL uzmanısın."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content.strip()

# Test
if __name__ == "__main__":
    user_question = input("SQL ile ilgili bir soru sor: ")
    answer = ask_sql_bot(user_question)
    print("\nBot'un Cevabı:\n", answer)



