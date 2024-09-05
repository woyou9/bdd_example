import os
import subprocess


# def delete_allure_files(directory):
#     for file_name in os.listdir(directory):
#         if file_name.endswith(".json"):
#             file_path = os.path.join(directory, file_name)
#             os.remove(file_path)
#
#
# def run_allure_report():
#         process = subprocess.Popen(
#             ['allure.bat', 'serve', r'.\allure_report_results'])
#
#         subprocess.run(
#             ['allure.bat', 'generate', '--clean', r'.\allure_report_results', '-o', r'.\allure_report_html'])
#
#         while len(os.listdir(r'.\allure_report_html')):
#             delete_allure_files(r'.\allure_report_results')
#         webbrowser.open(r'.\allure_report_html\index.html')
# Jakieś kombinacje żeby odpalić allure serve, zamienić milion tych plików .json na raport html, usunąć syf i odpalić raport
