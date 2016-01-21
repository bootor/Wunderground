@ECHO OFF
g:
cd "\PythonProjects\Wunderground\"
python load_history.py
python calc_sumstates.py
pythoon calc_rolling_precip.py
python calc_hddcdd.py
