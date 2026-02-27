py -m venv .venv
call .venv\Scripts\activate.bat
py -m pip install -U pip
pip install -U -r requirements.txt
pyinstaller --clean --noconfirm --noupx battery_status.pyw
pyinstaller --clean --noconfirm --onefile battery_status.pyw
call .venv\Scripts\deactivate.bat
