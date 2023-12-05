echo "BUILD START"
pyhton3.9 -m pip install requirements.txt
pyhton3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"
