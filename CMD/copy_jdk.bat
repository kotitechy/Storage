@echo off
color 0a
echo copying jdk-8 files 
c:
cd /
cd program Files
cd java
xcopy jdk1.8.0_341 "F:/hack"
F:
move jdk1.8.0_341 "hack"
echo files copied
del hack
pause
