from bs4 import BeautifulSoup
import requests
import subprocess

def GetSite(site):
    subprocess.run(['clear'])
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
