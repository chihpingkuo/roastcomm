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

# use python 3.11 since 3.12 will cause pyserial fileno error in pymodbus 3.6.8

# run starlette server
uvicorn roastcomm:app