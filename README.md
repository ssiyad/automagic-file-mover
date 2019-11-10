# Moover
#### Automagic File Mover
<br/><h3 align="center">Please help this repo with a :star: if you find it useful! :blush:</h3><br/>


## What is this?
Moover is a program designed to automatically move files between directories. The main aim of the project is to organize files in a structured manner. File are categorized based on their extension which will be improved in future to categorize based on type.


## Prerequisites
- git
- python3


## Setup
```shell
git clone https://github.com/ssiyad/automagic-file-mover
cd automagic-file-mover
python3 -m venv venv
source venv/bin/activate
pip install requirements.txt
```

## Usage
```python
python -m moover
```


## Optional arguments
```shell
-s, --source         Directory to watch
-d, --destination    Directory to move files
-e, --existing       Arrange existing files in source directory
-h, --help           Shows help message
```

Default `source` is `Downloads` and default `destination` is `Moover`

---
## Contribution
- Report issues
- Open pull request with improvements
- Spread the word
- Contact me directly at [Telegram](http://t.me/ssiyad)
---