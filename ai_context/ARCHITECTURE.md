<!-- 
프로젝트 구조와 역할 정의 파일 

폴더 구조
레이어 구조
각 파일 역할
프론트/백 통신 방식
-->

# ARCHITECTURE

## 프로젝트 구조
- frontend: React 애플리케이션
- backend: FastAPI 애플리케이션
- ai_context: 프로젝트 상태 및 문서 관리 파일

## 백엔드 구조
- app/api: HTTP 요청을 받는 라우터 계층
- app/services: 비즈니스 로직 계층
- app/repositories: DB 접근 계층
- app/models: SQLAlchemy ORM 모델
- app/schemas: 요청/응답 DTO
- app/core: 설정, DB 연결, 보안 관련 공통 모듈

## 프론트엔드 구조
- src/pages: 페이지 단위 컴포넌트
- src/components: 공통 UI 컴포넌트
- src/services: 백엔드 API 통신 모듈
- src/hooks: 커스텀 훅

## 통신 규칙
- 프론트엔드는 백엔드 REST API와 통신한다
- 백엔드는 JSON 형식으로 응답한다
- 인증 방식은 JWT 기반으로 확장할 예정이다

## 설계 원칙
- model과 schema를 분리한다
- router와 service를 분리한다
- repository는 DB 접근만 담당한다