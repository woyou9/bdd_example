call C:\Users\and1_\PycharmProjects\PlaywrightFreestyle\venv\Scripts\activate.bat
pytest
start cmd /k "allure serve .\allure_report_results"
timeout /t 10
taskkill /f /IM "java.exe"
deactivate