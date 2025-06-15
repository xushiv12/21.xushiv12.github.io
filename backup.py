import requests
import datetime

# ✅ 替换为你的 token 和 repo 信息
GITHUB_TOKEN = "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"
REPO = "xushiv12/1"

# ✅ 自动生成标题和正文
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
title = f"[自动备份] value.txt 数据 - {now}"

with open("value.txt", "r", encoding="utf-8") as f:
    body = f.read()

url = f"https://api.github.com/repos/{REPO}/issues"
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}
data = {
    "title": title,
    "body": body
}

response = requests.post(url, headers=headers, json=data)
print(f"GitHub API 状态码: {response.status_code}")
print(response.json())
