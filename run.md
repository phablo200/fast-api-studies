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

# Install sqlalchemy
pip3 install sqlalchemy

# Install passlib
pip3 install passlib

# Install bcrypt
pip3 install bcrypt


# Install Python-mulpart
pip3 install python-multipart


# Install Python-jose
pip3 install python-jose

# Install aiofiles
pip3 install aiofiles

# Install all requirements.txt
pip3 install -r requirements.txt