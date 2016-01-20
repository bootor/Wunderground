@ECHO OFF
g:
cd "\PythonProjects\Wunderground\"
python load_history.py
python calc_sumstates.py
