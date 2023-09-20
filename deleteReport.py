import os

#file_name_and_path = "/home/theopaulo/Documents/PythonFiles/GithubProjects/Gmail-to-Google-Sheets/report.pdf"

def deleteReport(reportFilePath: str):
    try:
        os.remove(reportFilePath)
    except FileNotFoundError:
        print("File does not exist")
