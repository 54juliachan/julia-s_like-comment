from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 🔧 允許前端跨來源存取
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🧠 用 dictionary 儲存資料
data = {
    "likes": 0,
    "comments": []
}

# ✅ 取得目前資料
@app.get("/post")
def get_post():
    return data

# ❤️ 按讚功能
@app.post("/like")
def add_like():
    data["likes"] += 1
    return data

# 💬 新增留言
@app.post("/comment/{text}")
def add_comment(text: str):
    data["comments"].append(text)
    return data
