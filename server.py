"""
hello_mcp 서버
- 나의 첫 번째 MCP 서버
- 3개의 간단한 Tool: greet, add_numbers, current_time
"""

import os
from datetime import datetime
from zoneinfo import ZoneInfo
from mcp.server.fastmcp import FastMCP

# ── FastMCP 인스턴스 생성 ──────────────────────────────
# mcp = FastMCP(
#     "hello-mcp",
#     #version="0.1.0",
# )

# ── FastMCP 인스턴스 생성 (Render용 HTTP 방식) ──────────────────────────────
mcp = FastMCP(
    "hello-mcp",
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 10000)),
)


# ── Tool 1: 인사하기 ──────────────────────────────────
@mcp.tool()
def greet(name: str, language: str = "ko") -> str:
    """사용자에게 인사합니다.

    Args:
        name: 인사할 대상의 이름
        language: 인사 언어 (ko: 한국어, en: 영어, ja: 일본어)
    """
    greetings = {
        "ko": f"안녕하세요, {name}님! 반갑습니다.",
        "en": f"Hello, {name}! Nice to meet you.",
        "ja": f"こんにちは、{name}さん！はじめまして。",
    }
    return greetings.get(language, greetings["ko"])


# ── Tool 2: 숫자 더하기 ───────────────────────────────
@mcp.tool()
def add_numbers(a: float, b: float) -> str:
    """두 숫자를 더한 결과를 반환합니다.

    Args:
        a: 첫 번째 숫자
        b: 두 번째 숫자
    """
    result = a + b
    # 정수인 경우 소수점 제거
    if result == int(result):
        result = int(result)
    return f"{a} + {b} = {result}"


# ── Tool 3: 현재 시간 ────────────────────────────────
@mcp.tool()
def current_time(timezone: str = "Asia/Seoul") -> str:
    """현재 날짜와 시간을 반환합니다.

    Args:
        timezone: 시간대 (예: Asia/Seoul, America/New_York, Europe/London)
    """
    try:
        tz = ZoneInfo(timezone)
        now = datetime.now(tz)
        return (
            f"현재 시간 ({timezone}):\n"
            f"  날짜: {now.strftime('%Y년 %m월 %d일')}\n"
            f"  시간: {now.strftime('%H시 %M분 %S초')}\n"
            f"  요일: {now.strftime('%A')}"
        )
    except KeyError:
        return f"오류: '{timezone}'은(는) 유효하지 않은 시간대입니다."


# ── 서버 실행 ────────────────────────────────────────
# if __name__ == "__main__":
#     mcp.run()

def main():
    mcp.run(transport="streamable-http")

if __name__ == "__main__":
       main()
