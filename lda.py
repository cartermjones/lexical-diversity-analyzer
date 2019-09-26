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
