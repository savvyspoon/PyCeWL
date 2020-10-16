# PyCeWL

Custom word list generator written in Python.  This project is the result of trying 
to use CeWL by diginija and having issues getting Ruby to cooperate. 

## Installation
```
git clone https://github.com/savvyspoon/PyCeWL.git

cd PyCeWL

python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt

```

## Usage
```
Usage: pycewl.py [OPTIONS]

Options:
  --url TEXT                  URL to run scan against
  --speed [Slow|Medium|Fast]  Time between page parsings,
                              Fast=0,Medium=2,Slow=10

  --useragent TEXT            Set custom user-agent. Default = PyCeWL 1.0
  --verbose TEXT              Set verbosity
  --email                     Show emails gathered from spider
  --help                      Show this message and exit.
```


## License