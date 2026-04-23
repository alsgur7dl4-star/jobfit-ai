<!-- 
프론트와 백엔드가 연결될 때 매우 중요

 -->

 # API_SPEC

## Auth
### POST /auth/signup
- request:
  - email
  - password
  - name
- response:
  - id
  - email
  - name

### POST /auth/login
- request:
  - email
  - password
- response:
  - access_token
  - token_type

## Posts
### GET /posts
- query:
  - page
  - size
  - keyword
- response:
  - items
  - total_count
  - page
  - size

### POST /posts
- request:
  - title
  - content
- response:
  - id
  - title
  - content
  - created_at