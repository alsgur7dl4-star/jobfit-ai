"""
DB 연결 및 세션 관리
SQLAlchemy 2.0 스타일
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.config import settings


# 엔진 (DB 연결 풀 관리)
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,  # 끊긴 커넥션 자동 감지
    echo=False,  # True로 바꾸면 실행되는 SQL 로그 출력
)

# 세션 팩토리
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


class Base(DeclarativeBase):
    """모든 ORM 모델의 베이스 클래스"""

    pass


def get_db():
    """
    FastAPI 의존성 주입용 DB 세션 생성기
    요청 시작 시 세션 열고, 응답 후 자동 종료
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
