# Things to Know about Different Datasets

Many Sign language datasets have compatible vocabularies for example many are in some way aligned with the ASL LEX 2.0 vocabulary, but their gloss formatting are not consistent:
* "asllex:#9_oclock" in the ASLKG versus "9_oclock" in Sem-Lex versus "9OCLOCK" in ASL Citizen
* OHISEE in ASL Citizen versus "oh_i_see" in Sem-Lex and "asllex:oh_i_see" in the ASLKG
* both "asllex:think_chin.m4v" and "asllex:think_chin" in the ASLKG, meanwhile it's "THINKCHIN " in ASL Citizen and "think_chin" in Sem-Lex

Many have non-alphanumeric characters, e.g. "$" or "#" 

## ASL LEX 2.0
* There are some items with commas in the name, e.g. "release, rescue"

## Sem-Lex specifically:
From https://github.com/leekezar/SemLex

Things to know about this dataset
* It has at least 922 files which have duplicates. Found with rdfind. Also it's duplicated in the metadata.csv, sometimes across splits.
* It has glosses with spaces (e.g. "last year")
* It has glosses with commas in them ()
* Some of the videos are poor quality and you cannot get the framerate reliably, example at https://github.com/sign-language-processing/pose/issues/127.


## ASL Citizen: 

* Participant 46 often repeats signs
* Do NOT try to parse the gloss name from the filename, use the splits. Some of them have "seedGLOSS" pattern, some of them have don't match the metadata 
* there is one file with a very strange name: 4.7299129501965353e-7-seedSOUR in the ASL Citizen train split


## ASL Knowledge Graph
* ASL Knowledge Graph has duplicates and weird characters
* "release, rescue" and "release,_rescue" both existing in the ASLKG, duplicated in all other ways
* both "asllex:think_chin.m4v" and "asllex:think_chin" are in here.

# Popsign ASL
Actually it does not use not glosses at all, but English prompts. So "bank" might get signs for river bank, financial bank, etc.


