from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# 🔧 允許前端跨來源
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

# ❤️ 按讚
@app.post("/like")
def add_like():
    data["likes"] += 1
    return data

# 💬 留言資料模型
class Comment(BaseModel):
    text: str

# 💬 新增留言（用 JSON body）
@app.post("/comment")
def add_comment(comment: Comment):
    data["comments"].append(comment.text)
    return data
