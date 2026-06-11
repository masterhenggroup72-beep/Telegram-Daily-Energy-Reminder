import os
import json
import urllib.request
import urllib.parse
from datetime import datetime, timezone, timedelta

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

malaysia_time = datetime.now(timezone.utc) + timedelta(hours=8)

weekdays = {
    0: "星期一",
    1: "星期二",
    2: "星期三",
    3: "星期四",
    4: "星期五",
    5: "星期六",
    6: "星期日"
}

today = f"{malaysia_time.year}年{malaysia_time.month}月{malaysia_time.day}日"
weekday_cn = weekdays[malaysia_time.weekday()]

prompt = f"""
你是一位说话直白、干练的玄学运势顾问。
不要讲复杂术语，只给用户最直接的能量建议。

今天是 {today}（{weekday_cn}）。

请根据今天日期，生成一段不超过150字的每日能量提醒。

规则：
1. 如果是星期一、星期三、星期五：请给一句核心启示，并加入“王老师点评”。
2. 如果是其他日期：请直接输出“能量避坑指南”。
3. 不要解释，不要多余开场白。
4. 严格按照以下格式输出：

📅 {today} ({weekday_cn}) | 每日能量提醒

✨ 今日核心启示 ：
[内容]

🎯 今日宜做 ：
• [动作1]
• [动作2]

⚠️ 今日避坑 ：
• [动作1]
• [动作2]

🔢 今日幸运磁场 ：
• 数字：[数字]
• 颜色：[颜色]
• 旺生肖：[生肖]

---
🔗 想一对一算运势？点击咨询王老师：
👉 https://wa.me/60167272735
"""

data = {
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ],
    "temperature": 0.8
}

request = urllib.request.Request(
    "https://api.openai.com/v1/chat/completions",
    data=json.dumps(data).encode("utf-8"),
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    },
    method="POST"
)

with urllib.request.urlopen(request) as response:
    result = json.loads(response.read().decode("utf-8"))

message = result["choices"][0]["message"]["content"]

telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

telegram_data = urllib.parse.urlencode({
    "chat_id": CHAT_ID,
    "text": message
}).encode("utf-8")

telegram_request = urllib.request.Request(
    telegram_url,
    data=telegram_data,
    method="POST"
)

with urllib.request.urlopen(telegram_request) as response:
    print(response.read().decode("utf-8"))
