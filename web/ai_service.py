import os
import openai

# 환경변수 또는 직접 입력해도 됨
openai.api_key = os.getenv("OPENAI_API_KEY", "YOUR_API_KEY_HERE")

def get_ai_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",   # 또는 gpt-4, gpt-4o 등
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return response["choices"][0]["message"]["content"]
