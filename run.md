# Installing venv
python3 -m venv fast-api-env

# Activating venv
source fast-api-env/bin/activate

# Intsalling fastapi
pip3 install fastapi

# Installing uvicorn
pip3 install uvicorn

# Check version uvicorn
uvicorn --version

# Start server
uvicorn main:app --reload

# Fast Api has default docs
/docs
/redoc
