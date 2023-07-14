@echo off
start brave --app=http://127.0.0.1:5000
start server_handle.pyw
cd src
venv\Scripts\python app.py