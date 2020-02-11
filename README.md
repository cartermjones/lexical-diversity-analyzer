# lexical-diversity-analyzer
This script is used for generating a lexical diversity score for a .txt document. "Lexical diversity" here refers to the variety of different words used in a text. 

It is dependent on the Natural Language Toolkit (NLTK), which provides the tools I have used 
to tokenize the text, i.e. create a list of each individual word or symbol used in the text. The script then compares this list to the actual wordcount of the text, generating a score.

In the study for which this script was written, lexical diversity scores ("D-Scores") for corpora of student texts were collected and compared against the grades received in order to determine any correlations between vocabulary usage and grading. 

A sample usage/output would look like this: 

<code>import * from lda.py

lda(essay1.txt)

0.3335</code>

This script was originally used for research done as part of a graduate seminar at Texas A&M University - Texarkana, and this research was subsequently presented at the Fall 2016 conference of the Arkansas Philological Association. 
