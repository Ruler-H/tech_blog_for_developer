# <img src="./static/assets/img/favicon-32x32.png" width="2%"> 개발자 최적화 기술 Blog 서비스
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
[10. 개발하며 느낀점](#10-개발하며-느낀점)

## 1. 목표와 기능
### 1-1. 목표
- 개발자들의 기술 Blog에 최적화된 Blog 플랫폼
- 전체 개발자 & 분야별 개발자 커뮤니티 제공 플랫폼  

### 1-2. 기능
- 기술 항목 카테고리를 통해 원하는 기술과 관련된 글과 블로그를 확인할 수 있는 기능
- 분야에 따라 해당하는 분야의 게시글에서 소통할 수 있는 기능
#### [Flow Chart]
<img src="./static/assets/images/flow_chart.png" width="100%"> 

#### [와이어프레임]
- [와이어프레임 테스트 페이지](https://ovenapp.io/view/pKZFo1eFPOl26Xi3pz9lMx9qWFOed01C/eUDJg)  
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
<img src="https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">

### 2-2. 개발 환경
<div>
    <img src="https://img.shields.io/badge/amazonaws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white">
    <img src="https://img.shields.io/badge/nginx-009639?style=for-the-badge&logo=nginx&logoColor=white">
    <img src="https://img.shields.io/badge/visualstudio-007ACC?style=for-the-badge&logo=visualstudio&logoColor=white">
    <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
</div>

### 2-3. 배포 URL
#### [Tech_Blog_For_Developer](http://3.38.12.42/)

## 3. 프로젝트 구조와 개발 일정
### 3-1. 프로젝트 Directory 구조
📦tech_blog_for_developer  
 ┣ 📂accounts  
 ┃ ┣ 📂migrations  
 ┃ ┣ 📂__pycache__  
 ┃ ┣ 📜admin.py  
 ┃ ┣ 📜apps.py  
 ┃ ┣ 📜forms.py  
 ┃ ┣ 📜models.py  
 ┃ ┣ 📜tests.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜views.py  
 ┃ ┗ 📜__init__.py  
 ┣ 📂blog  
 ┃ ┣ 📂migrations  
 ┃ ┣ 📂__pycache__  
 ┃ ┣ 📜admin.py  
 ┃ ┣ 📜apps.py  
 ┃ ┣ 📜forms.py  
 ┃ ┣ 📜models.py  
 ┃ ┣ 📜tests.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜views.py  
 ┃ ┗ 📜__init__.py  
 ┣ 📂board  
 ┃ ┣ 📂migrations  
 ┃ ┣ 📂__pycache__  
 ┃ ┣ 📜admin.py  
 ┃ ┣ 📜apps.py  
 ┃ ┣ 📜forms.py  
 ┃ ┣ 📜models.py  
 ┃ ┣ 📜tests.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜views.py  
 ┃ ┗ 📜__init__.py  
 ┣ 📂main  
 ┃ ┣ 📂migrations  
 ┃ ┣ 📂__pycache__  
 ┃ ┣ 📜admin.py  
 ┃ ┣ 📜apps.py  
 ┃ ┣ 📜models.py  
 ┃ ┣ 📜tests.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜views.py  
 ┃ ┗ 📜__init__.py  
 ┣ 📂media  
 ┃ ┣ 📂accounts  
 ┃ ┣ 📂blog  
 ┃ ┗ 📂board  
 ┣ 📂static  
 ┃ ┣ 📂assets  
 ┃ ┃ ┣ 📂css  
 ┃ ┃ ┃ ┣ 📂apps  
 ┃ ┃ ┃ ┣ 📂authentication  
 ┃ ┃ ┃ ┣ 📂components  
 ┃ ┃ ┃ ┣ 📂dashboard  
 ┃ ┃ ┃ ┣ 📂elements  
 ┃ ┃ ┃ ┣ 📂forms  
 ┃ ┃ ┃ ┣ 📂pages  
 ┃ ┃ ┃ ┣ 📂tables  
 ┃ ┃ ┃ ┣ 📂users  
 ┃ ┃ ┣ 📂images  
 ┃ ┃ ┃ ┣ 📂mockup_image  
 ┃ ┃ ┣ 📂img  
 ┃ ┃ ┗ 📂js  
 ┃ ┣ 📂bootstrap  
 ┃ ┃ ┣ 📂css  
 ┃ ┃ ┗ 📂js  
 ┃ ┗ 📂plugins  
 ┣ 📂tech_blog  
 ┃ ┣ 📂__pycache__  
 ┃ ┣ 📜.env  
 ┃ ┣ 📜asgi.py  
 ┃ ┣ 📜settings.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜wsgi.py  
 ┃ ┗ 📜__init__.py  
 ┣ 📂templates  
 ┃ ┣ 📂accounts  
 ┃ ┃ ┣ 📜login.html  
 ┃ ┃ ┣ 📜password_change.html  
 ┃ ┃ ┣ 📜profile.html  
 ┃ ┃ ┣ 📜profile_edit.html  
 ┃ ┃ ┣ 📜signup.html  
 ┃ ┃ ┗ 📜user_list.html  
 ┃ ┣ 📂blog  
 ┃ ┃ ┣ 📜blog_base.html  
 ┃ ┃ ┣ 📜post_detail.html  
 ┃ ┃ ┣ 📜post_form.html  
 ┃ ┃ ┣ 📜post_list.html  
 ┃ ┃ ┗ 📜post_not_found.html  
 ┃ ┣ 📂board  
 ┃ ┃ ┣ 📜board_base.html  
 ┃ ┃ ┣ 📜board_post_detail.html  
 ┃ ┃ ┣ 📜board_post_form.html  
 ┃ ┃ ┗ 📜board_post_list.html  
 ┃ ┣ 📂main  
 ┃ ┃ ┗ 📜index.html  
 ┃ ┣ 📜404.html  
 ┃ ┗ 📜base.html  
 ┣ 📜CONVENTION.md  
 ┣ 📜db.sqlite3  
 ┣ 📜manage.py  
 ┣ 📜README.md  
 ┗ 📜requirements.txt  

### 3-2. 프로젝트 URL 구조
|app: main |views 함수 이름|html 파일이름|
|:--------|:------------|:---------|
|'/' |index         |index.html |

|app: accounts |views 함수 이름|html 파일이름   |
|:------------|:------------|:------------|
|'login/'      |login         |login.html    |
|'signup/'     |signup        |singup.html   |
|'logout/'     |logout        |
|'profile/'    |profile       |profile.html  |
|'profile/edit/\<int:pk\>/'|profile_edit|profile_edit.html|
|'profile/password_change/'|password_change|password_change.html|
|'subscribe/'|subscribe       |user_list.html|
|'subscribe/manage/\<int:pk\>/'|subscribe_manage|

|app: blog  |views 함수 이름  |html 파일이름   |
|:-------------|:--------------|:------------|
|'list/\<int:pk\>/'|postlist|post_list.html|
|'\<int:pk\>/'|post_detail|post_detail.html|
|'edit/\<int:pk\>/'|postedit|post_form.html|
|'write/'|postwrite|post_form.html|
|'delete/\<int:pk\>/'|postdelete|
|'search/\<int:pk\>/'|postlist|post_list.html|
|'comment_add/'|comment_add|
|'comment_delete/\<int:pk\>/'|comment_delete|
|'comment_edit/\<int:pk\>/'|comment_edit|
|'recomment_add/'|recomment_add|
|'recomment_delete/\<int:pk\>/'|recomment_delete|
|'recomment_edit/\<int:pk\>/'|recomment_edit|
|'other/\<int:other_pk\>/'|otehr_postlist|post_list.html|

|app: board  |views 함수 이름  |html 파일이름   |
|:-------------|:--------------|:------------|
|''|board_list|board_post_list.html|
|'\<int:pk\>/'|board_detail|board_post_detail.html|
|'write/'|board_write|board_post_form.html|
|'edit/\<int:pk\>/'|board_edit|board_post_form.html|
|'delete/\<int:pk\>/'|board_delete|
|'comment/write/'|comment_write|
|'comment_delete/\<int:pk\>/'|comment_delete|
|'comment_edit/\<int:pk\>/'|comment_edit|
|'recomment_write/'|recomment_write|
|'recomment_delete/\<int:pk\>/'|recomment_delete|
|'recomment_edit/\<int:pk\>/'|recomment_edit|


### 3-3. 개발 일정
<img src="./static/assets/images/tech_blog_wbs.png" width="100%">

## 4. 기능 요구사항 목록
<img src="./static/assets/images/function_demand_list.png" width="100%">

## 5. 데이터베이스 모델링(ER Diagram)
<img src="./static/assets/images/Tech_Blog_ERDiagram.png" width="100%">  

## 6. User Interface
|||
|-|-|
|<img src="./static/assets/images/ui_image/main_top.png" width="100%">메인페이지 상단|<img src="./static/assets/images/ui_image/main_mid.png" width="100%">메인페이지 중간|
|<img src="./static/assets/images/ui_image/main_bottom.png" width="100%">메인페이지 하단|<img src="./static/assets/images/ui_image/main_profile.png" width="100%">메인페이지 프로필 클릭 화면|
|<img src="./static/assets/images/ui_image/login.png" width="100%">로그인 화면|<img src="./static/assets/images/ui_image/signup.png" width="100%">회원가입 화면|
|<img src="./static/assets/images/ui_image/profile.png" width="100%">프로필 화면|<img src="./static/assets/images/ui_image/profile_setting.png" width="100%">프로필 수정 화면|
|<img src="./static/assets/images/ui_image/blog_post_write.png" width="100%">블로그 포스트 생성 화면|<img src="./static/assets/images/ui_image/blog_post_list.png" width="100%">블로그 글 목록 화면|
|<img src="./static/assets/images/ui_image/blog_post_detail.png" width="100%">블로그 글 보기 화면|<img src="./static/assets/images/ui_image/blog_post_edit.png" width="100%">블로그 글 수정 화면|
|<img src="./static/assets/images/ui_image/subscribe.png" width="100%">구독 블로그 리스트 화면|<img src="./static/assets/images/ui_image/board_post_list.png" width="100%">개발자 게시판 리스트 화면|
|<img src="./static/assets/images/ui_image/board_post_detail.png" width="100%">개발자 게시판 글 보기 화면|<img src="./static/assets/images/ui_image/board_post_write.png" width="100%">개발자 게시판 글 생성 화면|
|<img src="./static/assets/images/ui_image/board_post_edit.png" width="100%">개발자 게시판 글 수정 화면|

## 7. 메인 기능
### 7-1. 계정 기능  
<img src="./static/assets/images/function_gif/accounts_function.gif" width="100%"><br/>
- 기본적으로 계정과 관련된 회원 가입, 로그인, 로그아웃 기능을 제공합니다.
- 가입된 이후 프로필을 관리할 수 있는 기능을 통해 본인의 개발 분야와 프로필 이미지를 관리할 수 있습니다.

### 7-2. 블로그 기능  
<img src="./static/assets/images/function_gif/blog_function.gif" width="100%"><br/>
- 로그인된 유저를 대상으로 글 작성, 목록, 상세보기, 삭제 기능을 제공합니다.
- 로그인되지 않은 유저는 글 목록 및 글 상세보기 기능만 제공받습니다.

### 7-3. 댓글&대댓글 기능
<img src="./static/assets/images/function_gif/comment_function.gif" width="100%"><br/>
- 로그인된 유저를 대상으로 블로그 글 혹은 게시판 글에 댓글을 작성, 수정, 삭제할 수 있는 기능을 제공합니다.

## 8. 추가 기능
### 8-1. 구독 기능
<img src="./static/assets/images/function_gif/subscribe_function.gif" width="100%"><br/>
- 마음에 드는 글을 작성한 유저를 구독하는 기능으로 다른 유저의 블로그에 들어가 구독을 할 수 있습니다. 해당 기능은 ajax를 이용한 비동기 처리를 통해 구현하여 화면의 이동없이 기능을 사용할 수 있습니다.
- 구독한 계정들은 subscribe 페이지를 통해서 관리할 수도 있습니다.

### 8-2. 게시판 기능
<img src="./static/assets/images/function_gif/board_function.gif" width="100%"><br/>
- 기본적으로 제공되는 기능은 블로그 기능들과 동일하게 글 작성, 수정, 삭제 기능을 제공하지만, 다른 유저가 작성한 글들과 함께 자신의 글이 목록에서 같이 보인다는 차이가 있습니다.

## 9. 개발 이슈
### 9-1. 회원가입 암호화가 안되는 문제
#### 9-1-1. 문제 상황
- 회원가입을 커스텀하면서 admin 페이지에서는 회원가입 시 비밀번호 암호화가 진행되는 것에 반해 커스텀한 회원가입은 비밀번호를 암호화하지 않고 DB에 저장하는 현상이 발생했고, 이에 따른 사이드 이펙트로 커스텀 회원가입을 통해 가입된 계정은 로그인되지 않는 현상이 발생했습니다.
#### 9-1-2. 해결 방법
- Django가 제공하는 비밀번호 암호화를 적용하기 위해서는 아래와 같이 set_password 함수를 이용해야 한다는 것을 확인하였습니다. 해당 방법을 적용한 이후 DB 확인 결과 암호화가 적용되어 있는 것을 확인하였고, 로그인 기능도 정상 동작하는 것을 확인하였습니다.
    ```python
    user = User()
    user.set_password(password)
    ```
### 9-2. 다대다 관계에서 삭제 시 상대 테이블 데이터가 삭제되는 문제
#### 9-2-1. 문제 상황
- 구현하고 있는 기능 중 구독 기능은 유저와 유저 모델 간의 다대다 관계로 구현 중에 있습니다. 구독을 취소하게 되면 구독 중인 유저들 중 자신의 구독 목록에서 대상 유저를 삭제해야 하는데 단순히 다대다 관계가 삭제되는 것이 아닌 삭제 대상 유저가 유저 테이블에서도 삭제되는 상황이였습니다.
#### 9-2-2. 해결 방법
- 기존에 사용하였던 delete 함수를 사용하는 것이 아닌 remove 함수를 사용하여 대상 유저 데이터를 다대다 관계에서 삭제하는 방법으로 해결할 수 있었습니다.

### 9-3. 첨부된 파일이 POST 요청으로 넘어오지 않는 문제
#### 9-3-1. 문제 상황
- type이 file로 지정된 input 태그에 첨부된 파일이 POST 요청으로 넘어올 때 대상 값이 넘어오지 않는 상황이였습니다.
#### 9-3-2. 해결 방법
- 대상 값을 받기 위해서 아래처럼 코드를 작성했습니다.
```
request.POST.get['upload_file']
```
- 문제의 원인은 파일을 받기 위해서는 POST를 쓰는게 아닌 FILE을 써서 받아야 한다는 점이였습니다. 원인을 확인한 후 아래와 같이 수정하여 문제를 해결할 수 있었습니다.
```
request.FILE.get['upload_file']
```
## 10. 개발하며 느낀점
- 처음 프로젝트의 목표를 정하고 Tech Blog라면 그 자체로 개발할 컨텐츠가 많다라는 생각이 들었습니다. 때문에 기획 단계에서 개발하고 싶고 좋은 컨테츠라고 생각하는 기능들을 전부 기획하게 되었습니다. 이렇게 프로젝트를 진행하던 중에 마감 기한이 다가오면서 개발해야 할 기능들이 너무 많아 개발에 아쉬운 부분들이 계속해서 생기게 되었습니다. 이러한 경험을 하게 되면서 개발자로서 마감 기한이 정해진 프로젝트를 대상으로 '개발하고 싶은 것', '좋은 컨텐츠라고 생각하는 것'보다 마감 기한 안에 개발할 수 있는 정도를 확실하게 파악하여 그것을 기반으로 기획을 하는 것이 프로젝트에 좋은 기획이 될 수 있음을 알게 되었습니다.
- 이전에는 더 좋은 기술을 가지고 있는 것, 자신만의 획기적인 코드를 알고있는 것들이 개발에 있어서 중요하다고 생각했습니다. 하지만 이번 프로젝트를 진행하면서 생각을 바꾸게 되었습니다. 그것들보다 더 중요한 것은 기초적인 것들을 얼마나 잘 숙지하고 있는가라는 것입니다. 아무래도 한번 개발한 이후에 스스로 개발한 코드들에 코드로서 갖추어야 할 기본적인 기능들이 제대로 구현되어 있지 않다면 계속해서 지난 코드들을 복기해야 하고, 이는 곳 개발 비용이 늘어남을 의미하기 때문입니다. 물론 좋은 기술과 자신만의 코드도 개발에 있어 중요한 일부가 되겠지만, 기본적인 것이 기반되어 있지 않다면 좋은 기술, 자신만의 코드는 장점이 될 수 없기 때문입니다. 이러한 경험들을 통해 저는 기본이 탄탄한 개발자가 되어야 한다라는 생각을 갖게 되었습니다.