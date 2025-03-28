import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import openai
from datetime import datetime

# 환경 변수 로드
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# 디스코드 봇 인텐트 설정
intents = discord.Intents.default()
intents.message_content = True

# 명령어 접두사를 "!"로 설정한 봇 객체 생성
bot = commands.Bot(command_prefix="!", intents=intents)

# 사용자별 하루 사용 횟수 제한 (예: 하루 최대 100회)
usage_count = {}

@bot.event
async def on_ready():
    print(f"{bot.user} 로그인 성공!")

@bot.command(name="구인구직")
async def guingujik(ctx, *, query: str):
    user_id = str(ctx.author.id)
    today = datetime.now().strftime("%Y-%m-%d")
    
    # 사용 횟수 초기화 및 갱신
    if user_id not in usage_count or usage_count[user_id]["date"] != today:
        usage_count[user_id] = {"date": today, "count": 0}
    
    if usage_count[user_id]["count"] >= 100:
        await ctx.send("❌ 오늘 상담 횟수를 모두 사용했어요! 내일 다시 시도해 주세요.")
        return
    elif usage_count[user_id]["count"] >= 90:
        await ctx.send("⚠️ 오늘 사용 횟수가 90회를 넘었어요. 남은 기회를 신중하게 사용해 주세요.")
    
    # IT 구인구직 상담을 위한 시스템 프롬프트
    system_prompt = (
        "당신은 IT 구인구직 전문가입니다. 기업과 구직자에게 맞춤형 조언과 정보를 제공하며, "
        "최신 IT 채용 트렌드와 기업의 요구사항, 구직자의 역량 분석을 고려해 답변합니다. "
        "답변은 항상 친절하고 명확한 존댓말로 작성해 주세요."
    )
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": query}
    ]
    
    try:
        # OpenAI ChatCompletion API 호출
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.5,
            max_tokens=256,
            top_p=0.8
        )
        answer = response.choices[0].message.content
        await ctx.send(answer)
        usage_count[user_id]["count"] += 1
    except Exception as e:
        print("OpenAI 오류:", e)
        await ctx.send("❗챗봇 응답 중 오류가 발생했어요. 잠시 후 다시 시도해 주세요.")

bot.run(DISCORD_TOKEN)