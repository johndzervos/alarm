# alarm

install dependencies:
```
sudo apt install build-essential gcc git graphviz-dev graphviz libblas-dev libboost-dev liblapack-dev libpq-dev libpython3-dev make memcached pandoc python3-dev python3-pip python3-setuptools python3 curl postgresql-contrib redis
```

install poetry:
```
wget https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py && python3 get-poetry.py --version 0.12.10 && rm get-poetry.py
```

Create virtual environment:
```
sudo -H pip3 install virtualenv virtualenvwrapper
source $HOME/.poetry/env
export WORKON_HOME=~/.virtualenvs
mkdir -p $WORKON_HOME
poetry config settings.virtualenvs.path $WORKON_HOME
```
Add loading the correct path for storage of all virtual environments to your .bashrc so that they are always available on starting bash:
```
echo 'export WORKON_HOME=$HOME/.virtualenvs' >> ~/.bashrc
```
Add the Python path all virtual environments should use:
```
echo 'export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3' >> ~/.bashrc
```
Include some virtualenvwrapper scripts 
```
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc
```
To check if the above worked, close the terminal and open a new console. Check if `mkvirtualenv` is known.

Now create a virtual environment with a name you like:
```
mkvirtualenv {{name of the new virtualenv}} --python "$(which python3.6)"
```
how to use:
```
workon crunchr
(alarm) cd /path/to/directory/
(alarm) setvirtualenvproject
(alarm) deactivate
```
