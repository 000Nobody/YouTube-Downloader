import subprocess
import os

if not os.path.isdir('Downloads'):
    os.mkdir('Downloads')
subprocess.run('streamlit run main.py', shell=True)