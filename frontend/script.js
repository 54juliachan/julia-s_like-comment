const API_URL = "http://127.0.0.1:8000";

// 取得貼文資料
async function loadData() {
  const res = await fetch(`${API_URL}/post`);
  const data = await res.json();
  document.getElementById("likeCount").textContent = data.likes;
  renderComments(data.comments);
}

// 顯示留言
function renderComments(comments) {
  const list = document.getElementById("commentList");
  list.innerHTML = comments.map(c => `<p>💬 ${c}</p>`).join("");
}

// 按讚
document.getElementById("likeBtn").addEventListener("click", async () => {
  const res = await fetch(`${API_URL}/like`, { method: "POST" });
  const data = await res.json();
  document.getElementById("likeCount").textContent = data.likes;
});

// 留言
document.getElementById("commentBtn").addEventListener("click", async () => {
  const text = document.getElementById("commentInput").value.trim();
  if (!text) return;

  const res = await fetch(`${API_URL}/comment`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text })
  });

  const data = await res.json();
  renderComments(data.comments);
  document.getElementById("commentInput").value = "";
});

loadData();
