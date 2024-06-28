# TermBrowse
TermBrowse (Short for Terminal Browser) is a customizable terminal-based browser made in Python.
## Features
* **Customizability:** You can customize TermBrowse to do more stuff, like only getting and printing a specific div, instead of the entire site.
* **Speed:** It's fast to open and use. The only limit here is your internet speed.
## Contributing/Using:
To help make this browser better, here is what you need to do:
First, you need to fork this repository (look for the fork button on the top right corner of the repo), then clone the repository with this command:
```
git clone https://github.com/your-username/TermBrowse.git
cd ./TermBrowse
```
Make a virtual environment in the directory (this prevents packages in the project from interfering with the host packages)
```
python3 -m venv ./
```
### FOR WINDOWS
```
./Scripts/activate.ps1
```
or, for legacy terminals:
```
./Scripts/activate.bat
```
### FOR LINUX-BASED SYSTEMS
```
source ./bin/activate
```
Now, install the necessary packages with:
```
pip install -r requirements.txt
```
To try the browser out, run `python3 ./src/main.py`. If you want to keep using it, stop right here.
### Contributing only:

First off, fork the repository, then pull it to your device.
Now, make improvements, remembering to commit and push.
Finally, make a pull request. I will review it then accept or deny it.

## Customizing TermBrowse
First, fork the browser on GitHub, then follow the "Contributing" instructions.
### PLEASE DO NOT OPEN A PULL REQUEST FOR CUSTOMIZATIONS. THANKS.
Modify the `siteSpecificInstructions()` function, and keep commiting and pushing to your own repository. You can also modify the look of it.
## LICENSE

MIT License

Copyright (c) 2024 HydeZero

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
