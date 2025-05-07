@echo off
cd /d "C:\DEV\Bot"
python main.py
powershell -Command "Start-Process python -ArgumentList 'main.py' -Verb runAs"
pause
python main.py

