import os
import urllib.request
import urllib.parse
from datetime import datetime, timezone, timedelta

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

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
day = malaysia_time.day

templates = [
    {
        "core": "能量避坑指南：今天少说多做，别急着解释，行动比争辩更有力量。",
        "do1": "整理手上任务",
        "do2": "主动跟进客户",
        "avoid1": "情绪化回复",
        "avoid2": "临时乱改计划",
        "num": "8",
        "color": "金色",
        "zodiac": "龙、猴"
    },
    {
        "core": "能量避坑指南：今天适合稳住节奏，不求快，只求不乱。",
        "do1": "完成一件拖延事项",
        "do2": "检查财务细节",
        "avoid1": "冲动消费",
        "avoid2": "答应太多事情",
        "num": "3",
        "color": "绿色",
        "zodiac": "虎、兔"
    },
    {
        "core": "能量避坑指南：今天人际磁场较强，贵人来自主动联系。",
        "do1": "联系重要客户",
        "do2": "表达感谢",
        "avoid1": "冷处理关系",
        "avoid2": "说话太直接伤人",
        "num": "6",
        "color": "白色",
        "zodiac": "鸡、牛"
    },
    {
        "core": "能量避坑指南：今天适合清理杂乱，环境顺了，心也会顺。",
        "do1": "整理桌面",
        "do2": "处理旧文件",
        "avoid1": "拖延小事",
        "avoid2": "把问题越堆越多",
        "num": "9",
        "color": "红色",
        "zodiac": "马、蛇"
    },
    {
        "core": "能量避坑指南：今天财气在细节里，别贪大，先守住。",
        "do1": "核对账目",
        "do2": "规划开销",
        "avoid1": "听信小道消息",
        "avoid2": "冒险投资",
        "num": "2",
        "color": "黄色",
        "zodiac": "狗、羊"
    },
    {
        "core": "能量避坑指南：今天适合曝光自己，好机会来自被看见。",
        "do1": "发布内容",
        "do2": "分享观点",
        "avoid1": "自我怀疑",
        "avoid2": "躲在幕后",
        "num": "1",
        "color": "蓝色",
        "zodiac": "鼠、猪"
    },
    {
        "core": "能量避坑指南：今天要养气，不要硬碰硬，退一步反而赢。",
        "do1": "休息调整",
        "do2": "陪伴家人",
        "avoid1": "争输赢",
        "avoid2": "过度消耗",
        "num": "5",
        "color": "咖啡色",
        "zodiac": "牛、龙"
    }
]

item = templates[day % len(templates)]

message = f"""📅 {today} ({weekday_cn}) | 每日能量提醒

✨ 今日核心启示 ：
{item["core"]}

🎯 今日宜做 ：
• {item["do1"]}
• {item["do2"]}

⚠️ 今日避坑 ：
• {item["avoid1"]}
• {item["avoid2"]}

🔢 今日幸运磁场 ：
• 数字：{item["num"]}
• 颜色：{item["color"]}
• 旺生肖：{item["zodiac"]}

---
🔗 想一对一算运势？点击咨询王老师：
👉 https://wa.me/60167272735"""

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
