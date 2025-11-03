from database import SessionLocal, ChatHistory, init_db
from ai_service import get_ai_response

def save_to_db(question, answer):
    session = SessionLocal()
    chat = ChatHistory(user_message=question, bot_response=answer)
    session.add(chat)
    session.commit()
    session.close()

def run_chatbot():
    init_db()
    print("🤖 Chatbot is ready! (type 'exit' to quit)")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chatbot terminated.")
            break

        # 1) AI 응답 받기
        ai_response = get_ai_response(user_input)

        # 2) DB 저장
        save_to_db(user_input, ai_response)

        # 3) 출력
        print("Bot:", ai_response)

if __name__ == "__main__":
    run_chatbot()
