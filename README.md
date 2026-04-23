# JobFit AI

> AI 기반 이력서-채용공고 매칭 플랫폼. 이력서와 공고를 벡터 임베딩으로 분석하고, LLM이 매칭도·강점·약점을 해석해 커리어 의사결정을 돕습니다. MCP(Model Context Protocol) 서버를 통해 Claude Desktop에서 자연어로 직접 조회·상담할 수 있습니다.

**Status**: 🚧 개발 중 (2026.04 ~ )

---

## 프로젝트 배경

취업 준비 과정에서 겪은 문제 의식에서 출발한 개인 포트폴리오 프로젝트입니다.

- 채용공고는 쏟아지지만 "내 이력서와 얼마나 맞는지" 객관적으로 확인하기 어렵다
- LLM(ChatGPT, Claude)에 물어보면 답은 잘 해주지만, 매번 이력서와 공고를 수동으로 붙여넣어야 한다
- MCP(Model Context Protocol)를 활용하면 AI 비서에게 영구적인 커리어 컨텍스트를 제공할 수 있지 않을까?

## 주요 기능 (계획)

### 핵심 기능
- 📄 이력서 업로드 (PDF/DOCX 파싱 → 구조화)
- 🔍 채용공고 자동 수집 (사람인 API / 공공데이터 API / 수동 입력)
- 🎯 이력서-공고 매칭도 계산 (벡터 임베딩 기반 코사인 유사도)
- 🤖 LLM 분석 (강점·약점·개선 제안)
- ⭐ 즐겨찾기 및 지원 이력 관리

### 차별화 기능
- **MCP 서버**: Claude Desktop에 연결하여 자연어로 "내게 맞는 공고 알려줘", "이 공고 약점은?" 같은 질의 가능
- **RAG 기반 상세 분석**: 공고 전문을 벡터DB에 저장하여 정확한 세부 질의 응답
- **권한 매트릭스 관리**: 일반/프리미엄/관리자 역할별 메뉴·기능 권한 세밀 제어

## 기술 스택

### Backend
- **FastAPI** (Python 3.11+)
- **SQLAlchemy 2.0** + Alembic
- **PostgreSQL 16**
- **Pydantic v2**
- **PyJWT** + passlib[bcrypt]
- **httpx** (외부 API 비동기 호출)

### AI / ML
- **Anthropic / OpenAI API** (LLM 호출)
- **sentence-transformers** (한국어 임베딩)
- **ChromaDB** 또는 Qdrant (벡터 저장소)
- **MCP Python SDK**

### Frontend
- **React 19** + TypeScript
- **Vite**
- **Material-UI (MUI) v7**
- **axios** + TanStack Query
- **React Router**

### Infrastructure
- **Docker** + Docker Compose
- **GitHub Actions** (CI)

## 데이터 소스

| 소스 | 용도 | 상태 |
|------|------|------|
| 사람인 Job Search API | 사기업 채용공고 | 신청 중 |
| 공공데이터포털 채용정보 | 공공기관 채용공고 | 신청 예정 |
| 사용자 수동 입력 | API 미제공 공고 (LLM 파싱) | 계획 |

> 수집된 공고 데이터는 상업적 재배포 없이 개인 포트폴리오 시연 및 기능 학습 목적으로만 사용합니다.

## 시스템 아키텍처

```
┌────────────────────┐
│  React + MUI       │
└─────────┬──────────┘
          │
┌─────────▼──────────┐      ┌────────────────┐
│  FastAPI Backend   │◄────►│  MCP Server    │
│                    │      │ (Claude 연동)    │
└──┬─────────────┬───┘      └────────────────┘
   │             │
   ▼             ▼
┌──────┐   ┌──────────┐
│  PG  │   │ ChromaDB │
└──────┘   └──────────┘
```

## 로드맵

- [x] 프로젝트 기획 및 기술 스택 결정
- [ ] 개발환경 세팅 (Docker, FastAPI 뼈대)
- [ ] 회원/인증 시스템 (JWT + Refresh Rotation)
- [ ] 권한/메뉴 관리 (RBAC + 매트릭스)
- [ ] 이력서 파싱 (PDF → 구조화 데이터)
- [ ] 공고 수집 파이프라인
- [ ] 벡터 임베딩 + 매칭 알고리즘
- [ ] LLM 분석 레이어
- [ ] React + MUI 프론트엔드
- [ ] MCP 서버 구현
- [ ] Docker Compose 통합 배포
- [ ] 데모 영상 및 문서화

## 면책 조항

- 본 프로젝트는 개인 포트폴리오 및 기술 학습 목적으로 제작됩니다
- 채용 결정 또는 고용 조언의 공식 도구가 아닙니다
- 외부 API에서 수집된 데이터의 재배포 없이 개인 사용에 한정합니다

## License

MIT

## Contact

- GitHub: [@본인아이디](https://github.com/본인아이디)
- Email: 본인메일@example.com
