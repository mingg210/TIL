# 📖  Git & GitHub 정리


> Git과 GitHub의 기본부터 협업 전략까지 총정리!

---

## 💬 Agenda

- Shell, Vim 기본 명령어  
- Git 기본 사용법 (clone, add, commit, push)  
- pre-commit 활용법  
- Git 고급 사용법 (branch, merge, conflict)  
- Git 브랜치 전략 (git flow, GitHub flow 등)  
- GitHub를 활용한 협업 및 이슈 관리  

---

## 💬 목표

- Git의 개념과 작동 방식 이해  
- Commit 메시지 컨벤션 학습  
- Branch 전략을 활용한 코드 관리 능력 강화  
- pre-commit을 이용한 코드 품질 관리  
- GitHub를 통한 협업 프로세스 체험  

---

## 💬 Shell & Vim 명령어 요약

### 📎 Shell 명령어

```bash
ls         # 목록 보기
cd         # 디렉토리 이동
mkdir      # 폴더 생성
touch      # 파일 생성
mv         # 이동/이름 변경
cp         # 복사
rm         # 삭제
cat        # 파일 내용 출력
pwd        # 현재 위치 출력
```


### 📎 Vim 기본 조작

- `i`: 입력 모드  
- `ESC`: 명령 모드  
- `:wq`, `:q!`: 저장 및 종료  
- `dd`, `yy`, `p`, `u`: 편집 명령  

---

## 💬 Git 기초

### 📎 개념

- 분산 버전 관리 시스템 (DVC)  
- Linus Torvalds가 개발  

### 📎 기본 명령어 흐름

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

git clone <repo>
cd <repo>
git status
git add .
git commit -m "커밋 메시지"
git push origin main
```


---

## 💬 Commit 메시지 컨벤션 (Conventional Commits)

```text
<type>: <short summary>

<body>

<footer>
```

---

### 📎 예시

```bash
feat: add login component  
fix: resolve login error  
docs: update README  
refactor: improve fizzbuzz logic  
```

---

## 💬 Pre-commit 설정

```bash
pip install pre-commit
touch .pre-commit-config.yaml
pre-commit install
pre-commit run --all-files
```

👉 pre-commit 공식사이트: https://pre-commit.com

---

## 💬 Branch & Merge

### 📎 브랜치 작업 (기본 예시)

```bash
git branch feature/fizzbuzz
git switch feature/fizzbuzz
# 작업 후
git add .
git commit -m "feat: implement fizzbuzz"
git switch main
git merge feature/fizzbuzz
```

---

### 📎 충돌 해결

```bash
git merge main
# 충돌 발생 시 파일 수정
git add <filename>
git commit
```

---

## 💬 .gitignore 예시

- Git에서 버전 관리하지 않을 파일이나 폴더, 파일 패턴을 지정하는 설정 파일

```gitignore
# macOS
.DS_Store

# Python
__pycache__/
*.py[cod]

# VSCode
.vscode/
```

👉 gitignore.io 활용 추천: https://gitignore.io

---

## 📌 핵심 포인트

1. **기본 흐름**: `git add` → `git commit` → `git push`  
2. **브랜치 전략**: 기능별로 브랜치 생성 후 병합 (`git flow`, `GitHub flow`)  
3. **커밋 메시지**: `Conventional Commits` 규칙 사용 (feat, fix, docs 등)  
4. **코드 품질 관리**: `pre-commit` 훅으로 사전 체크 자동화  
5. **.gitignore**: 추적 제외할 파일 명시로 민감 정보 및 불필요 파일 관리  

---

## 📌 주의사항

- `git reset --hard` 는 복구 불가! 신중하게 사용  
- `git push -f` 는 팀 작업시 위험 (강제 푸시 주의)  
- 민감 정보는 `.gitignore`에 꼭 추가 (`.env`, `secret.json` 등)  
- 충돌 발생 시 메시지를 꼼꼼히 읽고 해결
 
