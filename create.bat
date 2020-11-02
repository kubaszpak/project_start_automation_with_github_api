@echo off

IF "%1"=="" GOTO :EOF

: cd /d %~dp0

cd /d %PYTHONPATH%

: cd create_git

SET "dirname=%1"

python -m create_git %dirname%

cd %dirname%

git init

git remote add origin https://github.com/%GU%/%dirname%.git

git pull origin master

echo # %dirname% > Readme.md

git add .

git commit -m "Initial commit"

git push -u origin master

code .



