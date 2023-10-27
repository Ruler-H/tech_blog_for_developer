# 개발자 기술 블로그 최적화 Blog 서비스
## 목차
[1. 목표와 기능](#1-목표와-기능)  
[2. 개발 기술 및 환경, 배포 URL](#2-개발-기술-및-환경-배포-url)  
[3. 프로젝트 구조와 개발 일정](#3-프로젝트-구조와-개발-일정)  
[4. 기능 요구사항 목록](#4-기능-요구사항-목록)  
[5. 데이터베이스 모델링(ER Diagram)](#5-데이터베이스-모델링er-diagram)  
[6. User Interface](#6-user-interface)  
[7. 메인 기능](#7-메인-기능)  
[8. 추가 기능](#8-추가-기능)  
[9. 개발 이슈](#9-개발-이슈)  
[10. 후기](#10-후기)

## 1. 목표와 기능
### 1-1. 목표
- 개발자들의 기술 Blog에 최적화된 Blog 플랫폼
- 전체 개발자 & 분야별 개발자 커뮤니티 제공 플랫폼  

### 1-2. 기능
- 기술 항목 태그를 통해 원하는 기술과 관련된 블로그 글을 확인할 수 있는 기능
- 분야에 따라 해당하는 게시판에서 소통할 수 있는 기능
#### [Flow Chart]
<img src="./static/assets/images/flow_chart.png" width="100%"> 

#### [와이어프레임]
- [Mockup 테스트 페이지](https://ovenapp.io/view/pKZFo1eFPOl26Xi3pz9lMx9qWFOed01C/eUDJg)  
<img src="./static/assets/images/mockup_qr.png" width="10%">  

|||
|-|-|
|<img src="./static/assets/images/mockup_image/01_main_top.png" width="100%">메인페이지 상단|<img src="./static/assets/images/mockup_image/03_main_bottom.png" width="100%">메인페이지 하단|
|<img src="./static/assets/images/mockup_image/02_main_top_profile_click.png" width="100%">메인페이지 프로필 클릭 화면|<img src="./static/assets/images/mockup_image/04_accounts_Login.png" width="100%">로그인 화면|
|<img src="./static/assets/images/mockup_image/05_accounts_Register.png" width="100%">회원가입 화면|<img src="./static/assets/images/mockup_image/06_accounts_Profile.png" width="100%">프로필 화면|
|<img src="./static/assets/images/mockup_image/07_accounts_Profile_Edit.png" width="100%">프로필 수정 화면|<img src="./static/assets/images/mockup_image/08_My Blog_Create.png" width="100%">블로그 포스트 생성 화면|
|<img src="./static/assets/images/mockup_image/09_My Blog_List.png" width="100%">블로그 글 목록 화면|<img src="./static/assets/images/mockup_image/10_My Blog_Detail.png" width="100%">블로그 글 보기 화면|
|<img src="./static/assets/images/mockup_image/11_My Blog_Edit.png" width="100%">블로그 글 수정 화면|<img src="./static/assets/images/mockup_image/12_My Blog_Subscribe.png" width="100%">구독 블로그 리스트 화면|
|<img src="./static/assets/images/mockup_image/13_DevSquare_List.png" width="100%">개발자 게시판 리스트 화면|<img src="./static/assets/images/mockup_image/14_DevSquare_Detail.png" width="100%">개발자 게시판 글 보기 화면|
|<img src="./static/assets/images/mockup_image/15_DevSquare_Create.png" width="100%">개발자 게시판 글 생성 화면|<img src="./static/assets/images/mockup_image/16_DevSquare_Edit.png" width="100%">개발자 게시판 글 수정 화면|

## 2. 개발 기술 및 환경, 배포 URL
### 2-1. 개발 기술
#### [기술 - FE]  
<div>
    <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white">
    <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
    <img src="https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
    <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
</div>

#### [기술 - BE]
<div>
    <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
    <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
</div>

#### [기술 - DB]
<img src="https://img.shields.io/badge/postgresql-4169E1?style=for-the-badge&logo=postgresql&logoColor=white">

### 2-2. 개발 환경
<div>
    <img src="https://img.shields.io/badge/visualstudio-007ACC?style=for-the-badge&logo=visualstudio&logoColor=white">
    <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
</div>

### 2-3. 배포 URL
#### [배포 URL 추가 필요]

## 3. 프로젝트 구조와 개발 일정
### 3-1. 프로젝트 Directory 구조
#### [추후 추가 필요]  

### 3-2. 프로젝트 URL 구조
|URL 경로  |views 함수 이름  |html 파일이름   |비고 |
|:-------:|:--------------:|:------------:|:---:|
|'blog/'  |postlist        |post_list.html|     |
#### [추후 수정 필요]  

### 3-3. 개발 일정
<img src="./static/assets/images/WBS_예시.png" width="100%">

#### [추후 변경 필요]

## 4. 기능 요구사항 목록
<img src="./static/assets/images/function_demand_list.png" width="100%">

### [추후 변경 필요]

## 5. 데이터베이스 모델링(ER Diagram)
<img src="./static/assets/images/Tech_Blog_ERDiagram.png" width="100%">  

### [차후 DB 모델 변경시 변경 필요]

## 6. User Interface
### [개발 후 작성 필요]

## 7. 메인 기능
### [개발 후 작성 필요]
## 8. 추가 기능
### [개발 후 작성 필요]
## 9. 개발 이슈
### [개발 중 작성 필요]
## 10. 후기
### [개발 후 작성 필요]