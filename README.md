# FastApi Project Template

## Stack
* FastApi
* SQLAlchemy2[async]
* Alembic
* Pydantic
* Pydantic-settings


## How to run

__Linux__
```shell
# Init venv
python3 -m venv .venv

# Activate venv
source .venv/bin/activate

# Install deps
pip3 install -r requirements.txt

# Set which .env file must be used and run
APP_ENV=dev uvicorn app.main:app --reload 
```

__Windows PowerShell__
```powershell
# Init venv
python3 -m venv .venv

# Activate venv
.\.venv\Scripts\activate.ps1

# Install deps
pip3 install -r requirements.txt

# Set which .env file must be used
$Env:APP_ENV = 'dev'

# Run
uvicorn app.main:app --reload
```

## How to develop

_All SQLAlchemy models must be writen in app/core/models.py_

All Dependencies in app/api/deps.py

Services in app/api/routes folder in separate file for each service

Service connects to main router in app/api/main.py 