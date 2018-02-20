"""
This script is used for generating a lexical diversity score for a .txt document. 
"Lexical diversity" here refers to the variety of different words used in a text. 
It is dependent on the Natural Language Toolkit (NLTK), which provides the tools I have used 
to tokenize the text, i.e. create a list of each individual word or symbol used in the text. 
The script then compares this list to the actual wordcount of the text, generating a score.
In the study for which this script was written, lexical diversity scores ("D-Scores") for corpora of student 
texts were collected and compared against the grades received in order to determine any correlations 
between vocabulary usage and grading. 

A sample usage/output would look like this: 
>>> import * from lda.py
>>> lda(essay1.txt)
0.3335

"""

#This line imports the nltk library
import nltk

#This line imports the word_tokenize method from the NLTK, which is used to generate a list of tokens.
from nltk import word_tokenize

#Here we define the primary method of this script, lda (lexical diversity analyzer). It takes a file name as an argument.
def lda(fname):

#Here we create a variable to house the list of tokens and instantiate by passing the file through the word_tokenize() method.
   tokens = word_tokenize(open(fname).read())
   
   #Now we must normalize the tokens by making them all lower case.
   words = [w.lower() for w in tokens]
   
   #Finally, we return the lexical diversity score by applying the formula for deriving lexical diversity (Tokens/Wordcount).
   return len(set(words))/ len(words)
