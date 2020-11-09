# Git

### Git 사용목적
1. 프로젝트의 역사를 기록하고 관리 (프로젝트 관리)
2. 여러 브랜치를 만들어 프로젝트 개발의 흐름을 관리
3. 브랜치에서 작업한 내용을 합칠 때 발생하는 문제 해결

> Git은 소프트웨어 개발에 필수적인 버전 관리 시스템입니다. 수많은 기업들이 팀 프로젝트를 진행하기 위해 Git을 사용합니다. 많은 오픈소스 개발자들은 자신의 프로젝트를 GitHub과 같은 원격 저장소에 올려 누구나 보고 쓸 수 있게 공유합니다. 여러분도 Git을 배움으로서 공부와 나눔의 장에 참여할 수 있을 것입니다.

> [버전관리] Git을 사용해 프로젝트를 효율적으로 관리하고 여러 사람과 협업하는 법을 배웁니다. Git으로 자신이 짠 코드의 과거 기록을 보관했다가 문제가 생겼을 때 불러오거나 되돌릴 수 있습니다. 또한 새로운 기능 개발이나 버그 해결과 같은 작업을 브랜치로 나누어 관리할 수 있습니다. 나아가 여러 사람이 한 프로젝트 내에서 효율적으로 협업할 수 있습니다.

### Git 리더 테스트
Git을 사용해 프로젝트를 관리하고 협업하는 방법을 얼마나 알고 있는지 테스트합니다.

프로젝트의 기록을 보관했다가 문제가 생겼을 때 불러오거나 되돌리는 방법
여러가지 작업을 브랜치로 나누어 관리하는 방법
브랜치를 합칠 때 발생하는 문제를 해결하는 방법

---

# Git을 사용한 버전 관리 <입문>

### 01 Git이란?
- 효율적인 협업 가능
여러 개발자들이 동시에 작업했을 때, 버전이 다른
통합하는 별도의 한명이 필요 -> 비교, 병합
- 쉬운 버전관리
백업을 위해 여러 파일을 만들어 관리하지않아도 됨
깃은 버전을 스냅샷 형태로 만듦
로컬에서 손쉽게 버전을 바꿀 수 있음
--> 하나의 파일로 관리할 수 있음

깃은 작업시, 자동으로 옛 버전의 파일을 지워주지않음

##### 깃의 특징

1. 가지치기와 병합  
  - 여러가지 작업을 동시에할때, 섞이면 안되는 상황이 존재
  - 사용자는 main에서독립성을 유지한채, 다른 개발을 진행할 수 있음
  - 기능단위로 작업할 수도 있고, 일 단위로 작업할수도있음
  - 가지를 만들어서 독립적으로 진행. 뻗어나온 가지는 언제든지 병합 가능
  - 개발, 테스트 진행 후, main에서 배포
  - 각 작업에 따라 독립성 유지, 협업 도움
2. 가볍고 빠름  
  - 대부분 서버가 아닌 로컬에서 진행됨 (SVN < git)
  - SVN: 중앙시스템에서 여러 개발자가 접속하여 코드 공유, 네트워크 항상 필요 (중앙에 코드가 존재)
  - 깃: 다른사람과 코드 를 공유할때만 중앙서비스에 접근, 네트워크 속도와 상관없이 빠르게 작업가능(모든 로컬사용자에게 모든 코드 존재)
3. 분산작업  
  - 사용자들은 복사된 프로젝트를 통해 동시에 작업 가능
  - 사용자들은 플젝에 전체코드를 가지고 있음 --> 따라서 단절되어도 개발에 문제가 없음
  - 소스코드 병합에 문제 --> 통합관리자 두어서 역할분담 가능
  - 개발자는 개발에 집중, 통합관리자는 개발된 코드를 병합하는데에 집중가능
4. 프로젝트의 무결점을 보장 (데이터 보장)  
  - 모든 파일은 체크섬이라는 과정을 거침
  - 체크섬: 16진수 문자열(커밋아이디)로 이루어짐
  - 커밋아이디가 같은것은 파일 도는 구성이 모두 같다는 것 -> 누가 어느 파일 작업했는지 기록이 남아서 버전관리가 매우 편리
5. 준비영역을 가짐  
  - working directory -> (git add) -> *staging area* -> (git gommit) -> repository
  - 수정한 것을 반영하기 전에 검토하는 단계
6. 깃은 오픈소스  
  - 오픈소스: 소스코드를 공개한 상태에서 인터넷에 누구나 플젝 발전에 기여할 수 있음
  - 전세계 프로그래머들을 통해 계속해서 발전해나감
  - Git 호스팅 서비스 : github, bigbucket, gitlab

##### Git 설치와 초기 설정

- 설치여부 확인  
  - terminal에서 `git`
- `git --version` : 버전확인  
- 사용자 정보 설정  
  - 저장소에 코드를 반영할 때 등록될 사용자 정보를 설정  
  - 프로젝트마다 다른 사용자 정보를 지정하고 싶으면, 저장소 생성 후, `--global` 옵션을 빼고 실행
```sh
git config --global user.name "이름"
git config --global user.email "이메일.email.com"
```
- 설정 정보 확인
`git config --list`

- 깃 저장소가 시작(?생성?)되지 않은 상태에서는 유저 설정 시에 반드시 `--global`을 입력해야함

##### Git 저장소 생성

`git init` : 기존의 디렉토리를 git repository로 설정

- 기존 디렉토리 사용
  - git을 사용할 프로젝트 폴더로 이동 후,  `git init` 명령어를 실행
  - 이후, 프로젝트 디렉토리에 '.git 디렉토리'가 생성되며 저장소 생성이 완료됨
- 새로 디렉토리 생성하여 사용
  - `git init 폴더명`
  - 이 명령어는 아래의 코드를 함축시킴
  ```sh
  mkdir 폴더명
  cd 폴더명
  git init
  cd ..
```
폴더를 생성하고, init을 시키는 것 뿐이지, 현재 pwd는 그대로 유지


> **정리**  
git version : git의 버전 확인  
git init : git저장소 생성  
git config --global user.name "<이름>" : git관련 작업 기록에 남는 이름 수정  
git config --global user.email "<이름>" : git관련 작업 기록에 남는 이름 수정  
git config --list : git 설정 확인  

---
### 02 Git 시작하기
목표:
Git 저장소에 작업내용을 반영
저장소의 세가지 영역
git 저장소의 현재 상태 파악

##### Git 파일 생성
- 새로운 파일 생성 후, 파일을 깃 저장소에 반영하는 방법
*working directory* -> (git add) -> *staging area* -> (git gommit) -> *repository*

[파일 상태 라이프 사이클]
<img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fhomy.tistory.com%2Fm%2F36%3Fcategory%3D743883&psig=AOvVaw13OaBirTpLdya2I3zV4q1J&ust=1605042560160000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCKCG38-v9uwCFQAAAAAdAAAAABAD">

> modified : 뭔가 수정된 상태  
untracked(working directory)/un-modified/modified를 add하게 되면 staged로 이동  
staged에서 commit을 하면 unmodified 상태로 변경  
파일을 지우면 untracked 상태  

만들어진 파일을 준비영역으로 보내야함
`git add 파일명` : staging area로 보냄
`git add .` : 한번에 추가할 파일이 너무 많아, 현재 폴더를 대상으로 지정하여 스테이징 모드로 변경
`git status` : staging area의 어떤 파일이 변경되는지 등의 파일의 상태를 확인할 수 있음

##### Git 저장소 반영
파일을 staging한 이후에, 무엇을 수정하고 추가했는지 메시지를 남겨 저장소에 저장하는 작업
`git commit` : .git 저장소 내에 staging 파일 저장
staged 에 있던 파일들이 repository에 반영이 되므로, 파일들은 unmodified 상태로 돌아가야함
`git commit -m "커밋메시지"` : 준비 영역에 있는 파일들을 저장소에 반영
커밋메시지는 생략할 수 있으나, 반영한 내용을 추후에 쉽게 알 수 있도록 적절한 메시지를 넣어주는 것이 좋다
-m 통해 즉시 메시지 추가 가능
`git commit --amend` : 저장소 반영 내용 변경
앞에서 적은 메세지에 오타가 있거나 누락된 파일이 있을 경우
amend 옵션을 사용하여 수정할 수 있음
-> 텍스트 편집기가 실행되고, 수정하고 싶은 부분을 수정하여 저장하면 됌
`git log` : 저장소 반영 내역
모든 커밋을 확인할 수 있음
commit ~~~로 나오는 ~~~는 16진수 문자열은 커밋id로, 각 커밋이 고유하게 가지고 있는 값이다. + 커밋 메세지도 볼 수 있음
- Git history
commit된 내용은 다음과 같다.
commit id 당,  
> commit size  
tree : 파일트리  
parent  
author : 누가 작성  
commiter : 누가 커밋했는지  
commit message  

'.' 은 경로를 나타낼 때, 현재 working directory를 의미하기도 하며, git 명령어 뒤에 붙었을 때, 경로 내에 잇는 모든 파일을 의미하기도 한다.

> TIPS
git commit -m <커밋 메세지>를 이용하면 에디터 없이 바로 커밋 메세지를 작성할 수 있어요.
만약 git commit이라고 적으면 nano에디터가 켜져요.
nano에디터에서는 Ctrl+X -> Y -> Enter 순서로 누르면 저장할 수 있어요.

``` bash
# 실습내용
+ git init
Initialized empty Git repository in /elice/project_file/myproject/.git/
+ git add main.py
+ git commit -m hello
[master (root-commit) e0db31b] hello
 1 file changed, 1 insertion(+)
 create mode 100644 main.py
+ git log
commit e0db31b486017e900435f830a04a7244a0ff9290 (HEAD ->
 master)
Author: Elice <elice@elice.io>
Date:   Thu Oct 8 17:42:20 2020 +0000

    hello
```

##### Git 상태 확인
git 저장소까지 저장 완료. 파일 상태, history를 볼 수 있는 `git status`, `git log`에 대하여 알아보자
`git status` : staging file들의 상태 확인 (준비영역에 있는 파일들 확인)
`git log` : .git repository에 존재하는 history 확인 (커밋 히스토리 확인)
`git diff` : commit 된 파일 중, 변경된 사항을 비교할 때 (뭐가 추가되고 뭐가 삭제되었는지 한눈에 확인 가능)

> commit 을 하게되면 새로운 버전 (새로운 commit id)이 새로 생김. 이전거는 안지움.

`git history`
에서는 이전의 버전과 현재의 버전을 같이 저장하고 있다.
스냅샷의 형태.
이 중, 다른 버전으로 되돌리고 싶을 때는 git hustory를 통해서 되돌릴 수 있다.
`git log`
저장소 반영 내역을 확인하기 위해서 사용
이제까지 커밋했던 모든 내역을 확인할 수 있음

[대표적인 log 옵션들]
`git log -p -2`
`-p, --patch` : 각 commit의 수정결과를 보여주는 diff와 같은 역할을 수행
`-n` : 상위 n개의 commit만 보여줌

`git log --stat`
`--stat` : 어떤 파일이 commit에서 수정되고 변경되었는지, 파일 내 라인이 추가되거나 삭제되었는지 확인

`git log --pretty=oneline`
`--pretty=oneline` : 각 commit을 한 줄로 출력

`git log --graph`
`--graph` : commit간의 연결 관계를 아스키 그래프로 출력
branch가 생기면 아주 유용한 기능

`git log -S function_name`
`-S` : 코드에서 추가되거나 제거된 내용 중, 특정 텍스트(위에서는 function_name)가 포함되어있는지 검사

> TIP
이미 저장소에 commit된 파일을 수정하게 되면 git이 자동으로 변경사항을 인식해서 modified 로 사용자에게 파일이 변경되었음을 알려줍니다.
이때 modified 파일은 untracked 상태이므로 staging을 거쳐서 다시 commit해 줘야겠죠?

``` bash
+ git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        README.txt  # (red)
        crawling.py # (red)

nothing added to commit but untracked files present (use "git add" to track)
+ git add crawling.py
+ git status
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   crawling.py # (green)

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        README.txt # (red)
```

현재 myproject저장소 안에 crawling.py파일이 있는 상태에서 README.txt, rat.py파일이 새로 추가되었습니다.
``` bash
elicer@1ac42aeaa45b:~/myproject$ pwd
/elice/project_file/myproject
elicer@1ac42aeaa45b:~/myproject$ ls
crawling.py  rat.py  README.txt
elicer@1ac42aeaa45b:~/myproject$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   README.txt # red

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   crawling.py # green

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        rat.py # red
```

``` bash
elicer@1ac42aeaa45b:~/myproject$ git reset HEAD README.txt
Unstaged changes after reset:
M       crawling.py
elicer@1ac42aeaa45b:~/myproject$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   crawling.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        README.txt
        rat.py

no changes added to commit (use "git add" and/or "git commit -a")
```

> Tips : 커밋메시지 수정하기
명령어 뒤에 -m "수정할 커밋 메세지" 라고 작성하면 에디터를 켜지 않고 바로 수정이 가능합니다.
git에서 사용가능한 editor는 vim, nano, emacs등등 여러가지가 있습니다. 현재 실습에서는 nano를 이용하여 commit 메세지를 수정하는 editor로 사용하고 있습니다.
nano의 내용 저장 방법은 아래와 같습니다.
저장 : ctrl X + Y + enter

---

### 03 Git 가지치기

##### Git branch
Git Branch: 독립적으로 어떤 작업을 진행하기 위한 개념
각각의 Branch는 다른 Branch에 영향을 받지 않음

master: 프로젝트의 main 파일을 가지고 있음
develop: 개발목적의 branch, 배포를 위해서 merge 가능
topic: 기능단위, 작업단위로 빼서 독립된 작업 후 병합 가능

- Git Branch 종류
  - main branch: 배포할 수 있는 수준의 안정적인 branch
  - topic branch: 기능 추가나 버그 수정과 같은, 단위 작업을 위한 branch (수시로 생겼다가 없어질 수 있음)

`git branch 이름` : 브랜치 생성
master branch: 처음에 가지고 있는 기본값. 처음 레포 만들때 자동으로 만들어지는 브랜치
`git branch` : 현재 브랜치 확인, 존재하는 브랜치 확인 가능
`git checkout 이름` : 브랜치 전환, 작업할 브랜치 선택

HEAD -> master : HEAD 포인터가 master을 가리키고 있음. HEAD가 가리키는 것이 현재 브랜치

- Git Navigation
checkout은 branch를 전환하는데 사용할 수도 있고, 아래와 같이 `git log`로 확인한 snapshot을 넘나들때도 사용 가능
`git checkout <snapshot hash(16진수)>`

``` bash
$ git log --pretty=oneline
  ohdnwh1... (HEAD->master) this is master
  d9ejf03... another snapshot
$ git checkout d9ejf03
  ... is now at d9ejf03 another snapshot
$ git log --pretty=oneline
  d9ejf03... (master) this is master
  ohdnwh1... (HEAD) another snapshot // HEAD 이동
```
> snapshot의 hash값을 이용하여 과거의 파일 내용을 확인할 수 있음  

> 현재 git 저장소의 master브랜치가 선택되어 있습니다.  
여기서 master브랜치는 항상 안정된 상태여야 합니다.  
이 말은 항상 원활히 동작하는 상태여야 한다는 뜻입니다.    
따라서 새로운 기능을 추가하기 위해서는 토픽 브랜치를 만들어 작업을 해야 합니다.  

##### fast forward
fast-forward 병합방법
- `like_feature` branch의 working directory에서 새로운 정보를 넣어 commit 해보기 (현재, master가 c2 체크포인드에 위치)
  1. `like_feature`의 위치로 이동하기
  `git checkout like_feature`
  2. 작업하면 새로운 체크포인트가 생김
  새로운 체크포인트는 작업중인 브랜치만 반영
  c3 체크포인트에 like_feature가 있음
  3. `like_feature` branch에서의 작업을 마치고, `master` branch로 통합 // Merge
  4. `master` branch로 이동하여 `like_feature` branch를 병합
  ``` bash
  $ git checkout master
  $ git merge like_feature
  ```
  master가 c3 체크포인트로 이동
  like_feature의 내용이 master에 병합됨
  따라서 master가 가진 내용이 like_feature의 내용과 동일

  `like_feature` branch의 내용이 `master` branch에서 업데이트 된 내용이기 때문에 곧바로 merge됨
  이렇게 merge가 이루어지는 것을 fast-forward 라고 부름

정리: master branch에서 다른 변경 없이, 새로운 부분만 추가되는 경우 (체크포인트: c1-c2-c3 일자형)

##### Merge
- 갈라지는 branch의 경우, 각각의 branch의 working directory에서 같은 파일의 내용을 다르게 수정.
--> 파일을 동시에 수정한 경우
> 중요: 각각의 branch는 다른 branch의 영향을 받지 않기 때문에, 여러 작업을 동시에 진행할 수 있음

- 파일을 동시에 수정한 경우(갈라지는 branch)
`git log --graph --all` : commit graph를 확인할 수 있음
`git log --pretty=oneline --graph --all` // 이렇게 사용 가능

`git checkout master`을 이용하여 master로 checkout한 후, `git merge like_feature`로 merge 시도
``` bash
$ git checkout master
switched to branch 'master'
$ git merge like_feature
[main ~~~~~] update#~~~
Merge made by the 'recursive' strategy # @@@@ 여기
  ~~~~ | 2 +-
  1 file changed, ~~~~
```
- 수행이후, `master`와 `like_feature`는 같은 체크포인트를 가리키지 않음
> c2에서 갈라진 c3(like_feature 수정), c4(master 수정)가 합쳐져, c5(HEAD->master)가 됨
따라서 merge 이후에 master는 c5를, like_feature는 c3을 가리키고 있음

- git branch 삭제
`git branch --merged` : merge된 branch를 볼 수 있음 (merge 옵션)
`git branch -d 브랜치이름` : 사용을 마친 branch는 해당 명령어를 사용하여 삭제 가능 (d 옵션)

``` bash
#앞에서 master 브랜치에 새로운 기능을 추가하려면 새로운 브랜치를 만들어 그곳에 작업을 해야한다고 했죠?
#현재 add_app 브랜치에 작업을 한 뒤 커밋을 한 상태입니다.
#이 내용을 master 브랜치에 적용하기 위해 두 브랜치를 병합해 봅시다.

#현재 브랜치를 확인해보고 master브랜치로 이동해 봅시다.
#git log를 이용해 커밋 기록을 확인해 봅시다! 총 몇개의 커밋이 있나요?
#git merge add_app을 이용해 add_app브랜치와 병합해 봅시다. 아래와 같이 결과에서 Fast-forward가 있으면 성공입니다.
#git log를 이용해 다시 커밋 기록을 확인해 봅시다! add_app의 커밋 기록까지 잘 병합되었나요?

$ git log
$ git checkout master
$ git merge add_app
$ git log
```
``` git
----------------------------------------------------------------
+ git log
commit cd35f94672e20192e464837dca2ff11bbfa5b5eb (HEAD ->
 add_app)
Author: jhchang <secbullet@daum.net>
Date:   Fri Aug 16 13:58:49 2019 +0900

    add app

commit a2076d9ef8c0f2f5245ecfbff814655849240d90 (master)

Author: jhchang <secbullet@daum.net>
Date:   Fri Aug 16 13:57:59 2019 +0900

    add module
+ git checkout master
Switched to branch 'master'
+ git merge add_app
Updating a2076d9..cd35f94
Fast-forward
 app.py | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 app.py
+ git log
commit cd35f94672e20192e464837dca2ff11bbfa5b5eb (HEAD -> master, add_app
)
Author: jhchang <secbullet@daum.net>
Date:   Fri Aug 16 13:58:49 2019 +0900

    add app

commit a2076d9ef8c0f2f5245ecfbff814655849240d90
Author: jhchang <secbullet@daum.net>
Date:   Fri Aug 16 13:57:59 2019 +0900

    add module
```

##### conflict (충돌)
git 에서 병합시 충돌의 위험이 있음
Merge Conflict 이유: merge한 두 branch에서 같은 파일을 변경했을 때 충돌 발생

// 작업내용은 다르지만, 같은 파일을 변경하지 않으면 충돌 X
`git merge 브랜치이름` 명령 수행시 충돌이 일어나면 콘솔에 `... CONFLICT...in ~~, merge failed` 라고 알려줌

`git status` 명령어로 어느 파일에서 충돌이 발생했는지 확인 가능
> 양쪽에서 접근하려 한 경우, "unmerged path ... both modified : ... " 발생

파일을 열어보면,
`<<<<<<< HEAD`, `======`,`>>>>>>> 브랜치이름`
이렇게 바뀌어있다.
위 버전을 쓸것인지, 아래 버전을 쓸것인지, 적절히 혼합하여 쓸것인지는 사용자가 직접 수정을 해주어야한다.
수정 완료 후, `<<<<<<< HEAD`, `======`,`>>>>>>> 브랜치이름`와 같이, 깃에서 추가해준 기호들을 삭제해준다.
이후, `git add`, `git commit`과정을 거쳐, 다시 merge해준다.

> merge할 때, (merge 후에)남겨지는 큰 브랜치로 이동해서 명령어를 쳐야함 (git merge 이름) // 이 명령어에 들어갈 브랜치는 "merge되어 없어지는 브랜치"의 이름을 써야한다.

git merge시, 발생하는 문제를 해결하는 것도 중요하나,
충돌방지: master branch의 변화를 지속적으로 가져와서 충돌이 발생하는 부분을 제거하는 것
제일 좋은 방법은 master branch가 자주 변경되지 않는 것
master branch는 배포가 가능한 수준의 안정적 version만 가지고 있어야 함

>Hint
터미널에서 다음과 같은 명령어를 입력하면 nano에디터를 이용해 module1.py파일을 만들고 수정할 수 있습니다.
$ nano module1.py
nano 에디터를 닫을때는 Ctrl X -> Y -> Enter로 닫을 수 있다는거 기억하시죠?
실행 버튼을 눌렀을 때 뿐만아니라 answer.sh내에 git log명령어를 사용하면 제출 후에 여러분의 저장소 커밋 히스토리를 확인 할 수 있습니다.
사용가능한 git log옵션은 아래와 같습니다.
$ git log --oneline
$ git log --pretty=oneline
$ git log --all
$ git log --graph
---

> master브랜치로 이동한뒤 add_app브랜치와 병합해 주세요.
병합이 완료된 뒤에는 add_app브랜치를 삭제해 주세요.
git checkout master
git merge add_app
git branch -d add_app

> 충돌 해결하기
엘리스 토끼와 모자장수에게 발생한 충돌을 직접 해결해 봅시다. 현재 충돌이 난 file은 crawling.py파일입니다.
현재 Git 프로젝트에는 master, elice, madhatter의 3가지 branch가 있습니다.
각 branch에서의 마지막 작업이 다음과 같다고 가정하고 elice와 madhatter의 내용을 모두 반영한 file을 커밋해 봅시다.
----------------------------------------
엘리스 토끼의 crawling.py
----------------------------------------
def elice_javascript() :
'''
    this file is elice's javascript func
'''
if __name__ == '__main__' :
    elice_javascript()
---------------------------------------
모자장수의 crawling.py
----------------------------------------
def perfect_time_check() :
'''
    He is murdering time!
'''
if __name__ == '__main__' :
    perfect_time_check()
----------------------------------------
병합 이후
----------------------------------------
def elice_javascript() :
'''
    this file is elice's javascript func
'''
def perfect_time_check() :
'''
    He is murdering time!
'''
if __name__ == '__main__' :
    elice_javascript()
    perfect_time_check()
----------------------------------------
지시사항
git status를 통해 현재 상태를 확인한 뒤 충돌을 해결하고 진행중인 병합을 완료해주세요.
충돌을 해결하고 병합을 완료하기 위해 crawling.py 파일을 열어 설명의 병합 이후 코드를 정확하게 작성해 주세요.
madhatter브랜치도 elice브랜치와의 병합을 진행해 주세요.
주의사항
충돌을 해결하고 commit을 완료해야 merge가 완벽하게 진행된 것입니다. 정확한 채점을 위해 각 branch는 지우지 말아주세요.
----------------------------------------
내 코드
----------------------------------------
// 실행해서 일단 crawling.py를 모두 같은 파일로 만들어주어야함
git add crawling.py
git commit -m "d"
git checkout madhatter
git merge elice
git checkout master
git merge madhatter
// 이상하다...

### 04 Git 원격 저장소

##### 원격저장소 받아오기
원격저장소: 인터넷이나 네트뤄크 어딘가에 있는 저장소
ex) github, gitlab... 호스팅 서비스
`git clone` : 기존의 git repository(원격으로 존재/로컬에 존재)를 복사
1. 원하는 프로젝트에 clone버튼을 누른다.
2. 2개의 옵션(SSH, HTTPS) 중, `clone with HTTPS` 옵션으로 clone
3. `git clone` 뒤에 clone 버튼으로 확인한 원격 저장소의 주소를 넣어줌
-> 내 로컬에 원격저장소의 사본이 저장

원격 저장소는 아래의 명령어로 연결할 수 있다.
`$ git remote add origin https://git~~~/~~~`

저장소 주소의 구성
"https://" + "gitlab.com/"(웹 호스트 서비스) + "group/"(그룹명) + "project"(프로젝트 명)

- 원격저장소 추가
`git remote` : 연결된 원격 저장소 확인
`git remote show origin` : origin에 어떤 원격 저장소가 붙어있는지 볼 수 있음 -> git clone해서 저장소 복사한 뒤, 저장소를 원격 저장소와 연결하고 있는 것
`git remote rename 원래이름 바꿀이름` : 원격저장소 단축 이름을 변경
`git remote rm 이름` : 주소가 변경되었거나, 필요 없어진 저장소는 아래의 명령어로 삭제할 수 있음

>TIP
git clone명령어를 실행하면 현재 폴더 내에 새로운 폴더를 하나 더 생성합니다.
예를 들면 현재 위치해 있는 폴더가 myproject 라고 한다면 git clone으로 생성된 폴더는 myproject/"위대하고 멋있는 모자팔기 앱의 저장소"로 생성됩니다.
따라서 myproject폴더는 저장소가 아닌 상태이죠.
만약 myproject 폴더를 저장소로 쓰고 싶다면 git clone명령의 마지막에 . 을 찍어주면 됩니다.

##### 원격저장소 동기화
- 저장소 갱신
  `pull` : 원격저장소에서 데이터 가져오기 + 병합 (merge)
  `fetch` : 원격저장소에서 데이터 가져오기

- 저장소 갱신 - pull
원격저장소에서 데이터를 가져와 로컬데이터와 병합
`git pull`
`git log all` -> 찍어보면 커밋 내역을 확인할 수 있다. (HEAD->master, origin/master)의 의미는, master 원격 저장소와 origin 의 로컬 master 브랜치가 서로 병합이되었으므로 둘은 동시에 같은 체크포인트를 가리키고 있다는 의미이다.

- 저장소 갱신 - fetch
`git log origin/master` 이렇게 변경된 파일을 확인하고 merge해준다.
update ~~~ 라고 되어있으면, `git merge origin/master` 이렇게... --> fast-forward 방식으로 master와 origin/master가 병합됨

> fetch, pull: 원격 저장소의 내용을 로컬 저장소로 가져올 수 있음

- 저장소 발행
로컬저장소에서 작업한 내용을 원격저장소에 반영 (원격저장소로 데이터 전송)
`$ git push origin master`

다른사람이 먼저 push한 상태에서는 push할 수 없다.
다른사람이 작업한 것을 merge부터 해줘야함

> 요약
1. `git remote add origin` (또는 다른 원격저장소 이름)으로 로컬저장소와 연결합니다.
2. `git fetch` 또는 `git pull`을 이용하여 원격저장소의 내용을 동기화합니다.
3. fetch를 실행한 경우, `git merge origin/master`로 병합을 완료해줍니다.
4. `git push origin master`를 이용하여 변경된 사항을 원격저장소에 전달해줍니다.

>Tip
pull은 로컬 저장소에 있는 master를 자동으로 원격저장소에 있는 내용과 합쳐주는 역할을 수행합니다.
git pull이 이루어지지 않는 경우는 보통 다른사람이 올린 commit의 내용과 내 컴퓨터에 존재하는 내용이 서로 충돌할 때입니다.
이러한 현상은 하나의 브랜치에서 여러 사람이 동시에 작업하면 발생할 확률이 높아지게 됩니다.
따라서 여러 개의 브랜치를 나누고 각자 브랜치에서 작업한 후에 웹호스팅 서비스에 존재하는 merge request로 하나씩 합쳐가는 방식을 사용하면 충돌이 일어나는 것을 막을 수 있고 매번 새롭게 merge해야하는 수고를 덜 수가 있습니다.

##### origin이란?
- origin/master
내 컴퓨터에 저장되어있는 저장소와 원격저장소를 연결하기 위해서 아래와 같은 명령을 사용함
`git remote add origin https://~~~`
이는 원격저장소의 단축이름을 origin으로 지정한다는 것
주소(https:)와 이름(origin)을 사용하여 git remote를 add
-> git remote의 이름을 origin으로 설정한것!
origin이 아닌 다른 이름으로 원격저장소의 이름을 지정할 수 있다.
그러나 기본적으로 만들어진 원격저장소의 이름은 origin이 default 값이다.
때문에, *clone으로 복사해온 저장소의 이름은 origin으로 통일하게 된다.*
`git remote -v` : `-v` 옵션을 사용하면 지정한 저장소의 이름과 주소를 함께 볼 수 있다.

여러 원격 저장소가 있는 상태에서 `git remote -v`를 사용하면, 두개의 저장소가 있는것을 확인할 수 있다.
``` bash
$ git remote -v
origin 주소 (fetch)
oritin 주소 (push)
```

##### 예제1
```
>원격 저장소 변경 내용 받아오기
jessy의 컴퓨터에는 원격저장소에 연결된 로컬 저장소가 준비되어 있습니다. 오늘 아침 jessy는 동료에게서 부터 새로운 버젼의 file이 원격저장소에 업로드 되었다는 얘기를 들었습니다.
jessy는 원격저장소에 있는 내용을 로컬저장소로 받아와 어떤 부분이 바뀌고 추가되었는지 확인해 보려 합니다.
_
지시사항
원격 저장소 origin에 있는 데이터를 가져와서 로컬 저장소의 master에 반영해 주세요.
_
Hint
원격저장소에서 정보를 받아오기 위해서는 두가지 방법이 있습니다.
한가지 방법은 데이터를 가져오고 후에 master를 merge해서 최종으로 동기화하는 방식이었고
다른 하나는 데이터를 가져오면서 merge까지 같이 진행되는 방식이었죠.
_
0. git log --graph를 통해서 어떤 내용이 변경되었는지 확인
1. `git fetch origin master` 원격저장소에 있는 데이터를 가져와서 local의 master 브랜치에 적용하기 // git fetch origin master // origin의 내용을 master로 가져오기
2. `git merge origin/master` // 현재 브랜치가 master브랜치이므로, origin의 master브랜치와 merge가 되어야함 -> fast-forward 방식으로 머지 완료!, 변경파일 볼 수 있음
// 1, 2: git pull origin master

> git pull  
git push origin master  
// 실제로는 pull을 먼저 하지 않으면 오류가 난다. // 변경사항이 있기 때문
ㅇㅇ

> git pull없이 git push ~~먼저 한 경우, 아래와 같은 오류가 난다.
---
elicer@c355751c0f33:~/myproject$ git push origin master
[45] Connection from 127.0.0.1:54022
[45] Extended attributes (16 bytes) exist <host=127.0.0.1>
[45] Request receive-pack for '/git_remote_repository'
To git://127.0.0.1/git_remote_repository
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'git://127.0.0.1/git_remote_repository'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
[30] [45] Disconnected
elicer@c355751c0f33:~/myproject$
---
```

##### 예제2
```
> 원격저장소에 변경 내용 push하기  
원격저장소에 로컬에서 변경한 내용을 push해 봅시다.  
현재 진행되던 프로젝트를 친구와 같이 진행하기 위해 원격저장소를 만드려고 합니다.  
원격 저장소의 주소는 /elice/project_file/git_remote_repository이며, 현재 비어있는 상태입니다.  
위 주소의 원격저장소에 로컬저장소의 내용을 push해 봅시다.  
지시사항  
rat라는 이름의 원격 저장소를 만들어 주세요.  
rat원격 저장소에 로컬저장소의 내용을 push해서 동기화 해 주세요.  
_
Hint
로컬저장소에서 remote가 추가되었는지 확인해보려면 git remote 또는 git remote -v를 사용하면 되는 걸 잊지 않았죠?

>
---
git remote add rat /elice/project_file/git_remote_repository
git push rat master
--------------------------------
remote 추가가 완료되었습니다. +50
트래킹 브랜치 rat/master가 생성되었습니다. +50
push가 완료되었습니다.
--------------------------------
```

##### 예제3
```
> 원격저장소 내용이 변경되어 있을 때 push하기
우리가 해야할 업무를 마쳐서 저장소에 내가 만든 데이터를 업데이트 하려고 합니다.
그런데 push가 이루어지지 않고 다음과 같은 결과를 얻었습니다.
-
! [rejected]        master -> master (fetch first)
error: failed to push some refs to '../git_remote_repository'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
-
저장소를 살펴본 결과 팀원 중 한 사람이 수정한 파일을 원격 저장소에 나보다 먼저 올려놨기 때문이라는 것을 알게 되었습니다.
위의 문제를 해결하고 push를 진행해 봅시다.
_
지시사항
현재 app.py의 내용이 나의 저장소에 있는 내용과 원격저장소에 있는 내용이 서로 다릅니다. 이 때문에 pull을 실행하여 원격저장소의 내용을 받아올 수 가 없습니다.
따라서 아래의 순서로 작업을 진행해 주세요.
1. modified.py에 수정되어야 할 내용을 적어주세요.
2. 5번째줄 주석 아래에 origin 원격 저장소에서 받아오는 명령어를 작성해 주세요.
3. 11번째줄 주석 아래에 충돌이 난 app.py를 해결하는 명령어를 작성해 주세요.
_
원격저장소에서 받아온 내용
print("this file was change'')
Copy
나의 저장소에 있는 내용
print("hello, world!")
Copy
최종 app.py의 내용
print("hello, world!")
print("this file was change")
Copy
※ 채점을 위해 터미널 실행중간에 app.py의 내용을 modified.py 의 내용으로 교체합니다. app.py파일이 아닌 modified.py에 최종 app.py 의 내용을 적어주세요.

다음과 같이 graph가 생성되면 push를 완료할 수 있습니다.
-
내코드
// 다른 사람이 이미 원격저장소에 push한 경우, merge를 먼저 진행하고, push해야함.. 그렇지 않으면 reject 발생함
어디가 충돌나는지 `git diff`명령어로 확인 가

git pull origin master
\cp -f modified.py app.py #modified.py내용을 app.py로 복사하기
# 변경된 내용은 add와 commit 해줘야한다.

[최종]
git pull origin master

\cp -f modified.py app.py

git add app.py
git commit -m "dd"

git push origin master

```
```
근데 결과가 이래? 근데 100점
+ git pull origin master
[36] Connection from 127.0.0.1:54634
[36] Extended attributes (16 bytes) exist <host=127.0.0.1>
[36] Request upload-pack for '/git_remote_repository'
remote: Counting objects: 3, done.
remote: Total 3 (delta 0), reused 0 (delta 0)
[31] [36] Disconnected
Unpacking objects: 100% (3/3), done.
From git://127.0.0.1/git_remote_repository
 * branch            master     -> FETCH_HEAD
 * [new branch]      master     -> origin/master
Auto-merging app.py
CONFLICT (content): Merge conflict in app.py
Automatic merge failed; fix conflicts and then commit the result.
```
