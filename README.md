# Investment Service
> - 고객 투자 데이터 응답 REST API  개발

## 프로젝트 구조 설명

**core**
- 환경 설정 (settings.py)
- 메인 URL 주소 (urls.py)

**investment**
- 메인 프로젝트 디렉토리
- 모델 설정 (models.py)
- 어드민 설정 (amdin.py)
- api
  - views
    - API를 구현한 비즈니스 로직
  - serializers.py
    - 모델 인스턴스를 JSON 형태로 렌더링
  - urls.py
    - API 주소

