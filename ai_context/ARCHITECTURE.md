<!-- 
프로젝트 구조와 역할 정의 파일 

폴더 구조
레이어 구조
각 파일 역할
프론트/백 통신 방식
-->

# ARCHITECTURE

## Root
- frontend
- backend
- ai_context

## Backend
- app/api: router
- app/services: business logic
- app/repositories: DB access
- app/models: ORM model
- app/schemas: request/response DTO
- app/core: config, database, security

## Frontend
- src/pages
- src/components
- src/services
- src/hooks

## Communication
- Frontend uses backend REST API
- Backend returns JSON
- Auth will be JWT-based