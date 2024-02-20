Assignment 1 - Thomas Steinthal

TL;DR
- Due to issues with copying the path, the filepath to the data is a bit long and clumsy
- Comments below are also included in the .ipynb-notebook
- The fun_rmv_punct(s) could be expanded to take which features to look for as an argument
- Alternatives in the code include:
    - Merging the two functions for linguistic features is possible, but keeping them as two makes it easier to manipulate immediate adjustments (for now)
    - The main-chunk of code in itself could be a function in itself





In this assignment, I am going to loop over several essays, written by high school students, and create a dataframe in which particular aspects of the essays are assigned. I will be creating several dataset, in which each entry represents an essay in a given folder with following attributes:

Relative frequency of ```nouns```, ```verbs```, ```adjectives``` and ```adverbs``` per 10000 words.
Total number of unique names of ```names```, ```locations``` and ```organisations```.


I like ```functions```. That's why I have a collection of all relevant functions underneath:

Fun_list_files(path): Takes a filepath and returns a list of the content, sorted

Fun_rmv_punct(s): Takes a string, s, and removes all meta-data. Could be expanded to remove more complex phenomena but has been hardcoded for now

Fun_cou_rel_ling(doc, feature, per): Takes a doc (the nlp-object), a feature list (with the codes for the features as string) and a value for the denominator. A simple for-loop with count, does the job

Fun_cou_tot_propn: As above (no denominer though...). Could potentially be merged with the fun_cou_rel_ling to avoid redundancy, but leaving them like this allows for fine-tuning of the two elements (linguistic features and PROPN)


The entire code is explained below:

First we create a ```for-loop``` for each folder in the USE-corpus. We need to output one df for each of these so we start defining it (as a list). Then we list the files in the folder.

Another ```for-loop``` is created for each file in the folder. Again we need an output, that we can append as a row to the dataframe, so that is created (or nullified). The file is also ```loaded```. 

First we need some ```preprocessing```. We do this with the fun_rmv_punct(text), before we ```convert``` the text to a spaCy-readable-format. 

Now we can start ```appending``` features to our row-list. First we pluck the four linguistic feature with the fun_cou_rel_freq and then we find the names entities with fun_cou_tot_freq. 

With the final list constructed, we have a list, that represent the file-specific-row in the final dataframe. We append this to the df_fea_list (that eventually will become output) before looping over again.

Having looped through the entire set of files in the folder, we ```convert``` the file to a df with pd and ```save``` it with its name. Becuase the load of the process is heavy, a small print() let's us know how far the computer has got. All in all, the code took 3 minutes to run. 

