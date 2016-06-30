import urllib

def read_text():
    quotes = open("C:\Python27\movie_quotes.txt.txt")
    content = quotes.read()
    quotes.close()
    check_profanity(content)

def check_profanity(content):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+content)
    output = connection.read()
    #print(output)
    if "true" in output:
        print("Curesed words found !")
    elif "false" in output:
        print("No cursed words found :)")
    else:
        print("Could not scan the doc..")
    connection.close()
    
read_text()
