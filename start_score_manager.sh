project_path=`pwd`
source ${project_path}/venv/bin/activate &&
cd ${project_path}

export FLASK_APP=app.py
export FLASK_DEV=development && flask run --host=0.0.0.0

