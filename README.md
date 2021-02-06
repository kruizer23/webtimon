# WebTimon
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  

Python program that checks the availability of a web page and sends an SMS in case or problems. It extracts the web page title and compares it to the expected value. Combined with a CRON-job, WebTimon serves as a website monitor that automatically sends you an SMS when the website is unavailable.

## Installation

Before installing WebTimon, make sure that your Linux system has Python and Git development related packages installed. 

* Debian: `sudo apt install git make gcc python3 python3-dev virtualenv pandoc`
* Ubuntu: `sudo apt install git make gcc python3 python3-dev virtualenv pandoc`
* Fedora: `sudo dnf install git make gcc python3 python3-devel python3-virtualenv pandoc`
* openSUSE: `sudo zypper install git make gcc python3 python3-devel python3-virtualenv pandoc`

To get the code, clone the Git repository to a subdirectory inside your own home directory: 

`git clone git@github.com:kruizer23/webtimon.git ~/webtimon`

Alternatively, you can directly download the source code from the [WebTimon repository](https://github.com/kruizer23/webtimon) on GitHub and extract its contents to directory `~/webtimon`.

Installing WebTimon is now as simple as running these commands from the `~/webtimon` directory:

`make clean all`

`sudo make install`

All users on your system can now run WebTimon, simply by typing `webtimon` in the terminal.

After completing the WebTimon installation, you can remove the cloned / downloaded Git repository:

`rm -rf ~/webtimon`

## Removal

Run the following command to remove WebTimon from your system:

`sudo make uninstall`

