@echo off
setlocal enabledelayedexpansion
cd ../reference/
set parent=%CD%

for /R %%a in (*) do (
	set "current=%%a"
	set current=!current:%parent%=!
	echo !current!
)
pause