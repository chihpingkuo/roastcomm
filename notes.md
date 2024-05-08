# create virtual env
py -3 -m venv venv

# activate venv
. venv/Scripts/activate

# install packages
pip install -r requirements.txt

# deactivate
deactivate

# shebang
#!/usr/bin/env python