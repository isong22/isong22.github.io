'''
 *
 *	decomp (decompose sorta) 
 *
 *	using BeautifulSoup4 to parse html-xml FILE
 * 	   file contains multiple previous format songs in one file
 *	put results into separate files 
 *	
 *
 *	userName = input("Enter the Birthday person's name: ")
'''

import sys, getopt
from bs4 import BeautifulSoup


filename = None

## html text templates for top and head
html_top = '''<html>
<head>
<META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=utf-8">
'''
html_head2 = '''
<link rel="stylesheet" type="text/css" href="iSong.css">
</head>
<body LANG="en-US" DIR="LTR">
'''

#####  data structs
anchors = []
titles  = []

###  function to print a song
def print_song(title, fname, html_s):
    ## print a formatted soup song div
    print("FNAME = " + fname)
    print(html_top);
    ## probably could use replace_with here as well as the H2s below, maybe later as an exercise
    print("<title>" + title.string + "</title>");
    print(html_head2);
    ## since there are h2s and h3s, we want all as h2 ? for better souping down the road
    #### print(title);
    print("<h2>" + title.string + "</h2>");
    print(html_s.encode("utf8"));
    print("</body>\n</html>");

### filter function to get lyrics-body in either a class or id tag
###	yes, virginia, they come from all over
def filter_class_or_id(tag):
    return ((tag.has_attr('class') and 'lyrics-body' in tag['class']) or (tag.has_attr('id') and tag['id'] == 'lyrics-body'))

if filename == None:
	filename = input ("Filename to split:")

## put input here to get filename if missing
input_file = open(filename, "r")
## put the file into the soup-bowl
soup = BeautifulSoup(input_file, 'html.parser')
input_file.close()

######  walk the soup -build anchors and titles  ########
##      load the anchors(filenames) into a list since they arent children or siblings
##      need the name= cause its gonna be a filename, not html
for anchor in soup.find_all('a'):
    anchors += [ anchor.get('name') ]
##      yes virginia we want the html here cause were just gonna print back out, simple as cheese
titles = soup.find_all(["h2", "h3"])

