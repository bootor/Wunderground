@ECHO OFF
g:
cd "\PythonProjects\Wunderground\"
python load_history.py
python calc_sumstates.py
python calc_rolling_precip.py
python calc_hddcdd.py
