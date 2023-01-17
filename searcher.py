import webbrowser #importing webbrowser module for openning braweser

#making the url and open it in browser
def TabGenerator(keyword):
    url = "https://www.youtube.com/results?search_query=" + keyword
    webbrowser.open(url,new=1)#new = 1 for open in new window if not opened

#getting every keyword in keywords txt and open it
def LoopingKeyword():
    
    with open('keywords.txt', 'r') as f:
        for keyword in f:  
            TabGenerator(keyword.replace(" ","+"))
        f.close()

LoopingKeyword()
