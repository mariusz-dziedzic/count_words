Just run the exe file

or:

Before starting:
- The program is available in a version to run in Jupyter Notebook and in a standard Python file.
Before starting, make sure you have the PySimpleGUI library installed, without it the program will not work. To install, execute the command in the CMD terminal:
pip install PySimpleGUI 

And in Jupiter
!pip install wordcloud
!pip install PySimpleGUI 

Description: 
- After starting the user should select the text file (* .txt) to analyze it. After pressing the appropriate button, the program shows the number of all words, the number of unique words and the list of words together with the number of their occurrences. 
- In the case of running the script by Jupyter, the program has been enhanced to display a word cloud. (This option is not available when running a script from a Python file, because as the "wordcloud" library is not supported since Python 3.7). The word cloud is also saved to a file with a .png extension.
