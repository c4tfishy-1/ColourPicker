@echo off

python -m venv .
call Scripts\activate.bat
pip install -r requirements.txt
deactivate