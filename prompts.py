def build_sql_prompt(user_input):
    return f"""
Sen bir SQL dili uzmanısın. Kullanıcı SQL ile ilgili bir soru sorduğunda,
detaylı ama sade bir şekilde açıklama yap. Gerekirse örnek SQL kodu ver.

Soru: {user_input}
Cevap:
"""
