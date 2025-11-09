from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth, users, chat, widgets, home

app = FastAPI(title="MiniHome AI Platform")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 배포 시 도메인 지정
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(chat.router, prefix="/api/chat", tags=["Chat"])
app.include_router(widgets.router, prefix="/api/widgets", tags=["Widgets"])
app.include_router(home.router, prefix="/api/home", tags=["Home"])

@app.get("/")
def root():
    return {"message": "Welcome to MiniHome AI API 🚀"}
