call C:\Users\and1_\PycharmProjects\PlaywrightFreestyle\venv\Scripts\activate.bat
pytest
start cmd /k "allure serve .\allure_report_results"
tasklist /FI "IMAGENAME eq java.exe"
deactivate