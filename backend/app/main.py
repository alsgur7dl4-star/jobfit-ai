"""
FastAPI 앱 진입점
"""

from fastapi import FastAPI

from app.core.config import settings


app = FastAPI(
    title=settings.app_name,
    description="AI 기반 이력서-채용공고 매칭 플랫폼",
    version="0.1.0",
)


@app.get("/")
def root():
    """루트 — 서비스 기본 정보"""
    return {
        "app": settings.app_name,
        "env": settings.app_env,
        "status": "ok",
    }


@app.get("/health")
def health_check():
    """헬스 체크 엔드포인트"""
    return {"status": "healthy"}
