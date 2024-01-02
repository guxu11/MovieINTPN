# MovieINTPN
> MovieINTPN (Movie Interpreter) is a command line tool to add caption in user-specified languages to movies

## Installation
1. clone this repo
```shell
git clone git@github.com:guxu11/MovieINTPN.git
```
2. [OPTIONAL] Create a virtual environment to install the required packages. By default, AutoSub will be installed globally. 
```shell
python3 -m pip install --user virtualenv
virtualenv -p python3 venv
source sub/bin/activate
```
3. install autosub (autosub should be installed in the same virtual environment with Step 2 if you took that)
```shell
pip install autosub
```

4. install [ffmpeg](https://www.ffmpeg.org/download.html)
5. build `movieINTPN` with source code
```shell
python setup.py
```
After installing
```shell
$ movieintpn -h

usage: MovieINTPN [-h] -i INPUT [-o OUTPUT] -il INPUT_LANGUAGE [-ol OUTPUT_LANGUAGE] [-ro]

Movie Caption

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
  -o OUTPUT, --output OUTPUT
  -il INPUT_LANGUAGE, --input_language INPUT_LANGUAGE
  -ol OUTPUT_LANGUAGE, --output_language OUTPUT_LANGUAGE
  -ro, --retain_origin
```
## License
MIT
## Contact
xgu@sfsu.edu