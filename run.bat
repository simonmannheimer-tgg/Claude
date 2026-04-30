@echo off
cd /d "%~dp0"
"C:\Program Files\Python312\python.exe" -m pip install playwright beautifulsoup4 lxml --quiet
"C:\Program Files\Python312\python.exe" -m playwright install chromium --quiet
"C:\Program Files\Python312\python.exe" tgg_plp_auditor.py 2>&1
pause