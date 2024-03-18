# Assignment 3 - Query expansion with word embeddings
Thomas Steinthal.

Required packages: Listed in requirements.txt and contained in the venv as3env
Required setup: Run the setup.sh
Required for running: Run the run.sh (OBS. Right now the script does not run through the bash-script but need to be run from terminal with the required arguments)

The assignment contatins the following structure:
- as3env: The venv for the assignment
- data: The downloaded data for the code (remember to download first!): https://www.kaggle.com/datasets/joebeachcapital/57651-spotify-songs/data
- out: The output from the script. For now the script only outputs to terminal
- src: Sourcecode containing:
    - Aiding_ipynb.ipynb: A walkthrough of the code in ipy-format.
    - artist_theme_searcher: The script itself. Takes two arguments as strings: theme (key word) and artist
- README.md: This file
- requirements.txt: Required packages for the script to run
- run.sh: (DOES NOT WORK): The script to be run after setup.sh
- setup.sh: Setup of appropriate environment

Issues with the code:
- The run.sh does not currently take arguments, meaning that the artist_theme_searcher.py need to be run from the terminal itself
- The word-embeddings are solely automatically computed. This gives some bad search words, such as 'me' and 'my'. See also .ipynb. Does not know how to solve this issue right now...
- Data is too large for GitHub. Need to be downloaded by the runner.
- No current use of the out-folder

Notes about the code:
The code works by first reading the model and lyrics in. Then it calculates a vector of the 10 most similar words to the entered 'theme-word' - thus creating a 'theme-vector'. This vector circle a theme with the entered word in the middle. 
Then the code works by creating a list of all the songs that contains one of these words. The list contains of the artists name - meaning that the artist are listed each time they have a song with the required theme words included. This is a little more computationally heavier than taking the artist into account from the beginning, but it is assumed that this way of coding means that the preprocessing only needs to be done once if the user wanted to search for several artists (an extension not currently enabled).
And then finally, the artist_list is isolated by taking a list of the desired artist and counting the times the artist appears in the list of artists. 

Thomas Steinthal, 18/03/2024