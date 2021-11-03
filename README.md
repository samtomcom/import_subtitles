# Import Subtitles



In order to get \*arr to run a python script, I had to use a batch file to call it.  
It's possible that on any \*nix based systems you may have to use a shell file in a similar way,
but I only have \*arr running on Windows so I cannot test that.

## Usage



## Requirements

* Sonarr/Radarr installed
* Python 3.6+ installed and added to your system PATH

## Installation

1. Clone the repository

    git clone https://github.com/samtomcom/import_subtitles.git

2. Edit `execute.bat` to the correct location.
3. Naviage to Sonarr/Radarr [Settings > Connect > + > Custom Script](https://i.imgur.com/UOhYbNf.png), fill in the Path variable to `your\install\path\execute.bat`
4. Test and save
