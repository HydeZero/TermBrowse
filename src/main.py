from bs4 import BeautifulSoup
import requests
import subprocess
import sys

isClear = False

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == "clear":
            isClear = True

def GetSite(site):
    subprocess.run('clear') if isClear else print("PASS CLEAR AS AN ARGUMENT TO CLEAR THE SCREEN")
    print("Getting URL...")
    try:
        r = requests.get(site)
        print("Parsing...")
        global soup
        soup = BeautifulSoup(r.content, 'html5lib')
    except Exception as e:
        print("An error occured while getting the url. Make sure it is accessable and is valid.")
        print(e)
    siteSpecificInstructions()
def siteSpecificInstructions():
    ## TODO BY YOU: INPUT SITE SPECIFIC INSTRUCTIONS FOR THE BROWSER
    print("NO INSTRUCTIONS MADE YET. CONTENT WILL STILL BE DISPLAYED.")
    print(soup.prettify())
GetSite(input("Input initial URL: "))
