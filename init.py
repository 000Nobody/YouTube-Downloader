import subprocess
import os

subprocess.run('streamlit run main.py', shell=True)
if not os.path.isdir('Downloads'):
    os.mkdir('Downloads')