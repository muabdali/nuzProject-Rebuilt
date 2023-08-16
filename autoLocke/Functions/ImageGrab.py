import pyautogui
from autoLocke.Files.Data.CordsDict import routeCordDictionary, caughtRouteDictionary
from fuzzyRead import fuzzChecker
from tesseract import imgProcess

class screenshotClass:
    def __init__(self):
        self.routeDict = {
            'fireRed':[242, 47, 745, 121],
        }

        self.caughtDict = caughtRouteDictionary




    # Requires the section (Route or Caught), and Generation because different games have different ss cords.
    # Takes the section and assigns it the appropriate list from routeCordDictionary or caughtRouteDictionary


    def takeSection(self, section, gen):
        routeDictGen = self.routeDict[gen]
        x, y, width, height = routeDictGen[0], routeDictGen[1], routeDictGen[2], routeDictGen[3]
        if section == "Route":
            filepath = "autoLocke/Files/Images/RouteImage.png"
            result = self.takeScreenshot(filepath, x, y, width, height)
            print(result)
        else:
            filepath = "autoLocke/Files/Images/CaughtImage.png"
            result = self.takeScreenshot(filepath, x,y,width,height)
            print(result)

    def takeScreenshot(self, filepath, x, y, width, height):
        screenshot = pyautogui.screenshot(region=(x,y,width,height))
        screenshot.save(filepath)
        result = self.tessRead(path=filepath, section="")
        return result
    
    def tessRead(self, path, section):
        tesseractRead = imgProcess()
        tesseractResult = tesseractRead.imageEnhance(imagePath=path)
        fuzzyResult = self.fuzzyCompare(text=tesseractResult, section=section)
        
    def fuzzyCompare(self, text, section):
        fuzzProcess = fuzzChecker()
        if section == "Route":
            tocheckList = "autoLocke/Files/Data/fireredroutes.txt"
            fuzzProcess.checkList(pokeList=tocheckList,nameToCheck=text,minScore=85)
        elif section == "Caught":
            tocheckList = "autoLocke/Files/Data/NatDexPokemonG3.txt"
            fuzzProcess.checkList(pokeList=tocheckList,nameToCheck=text, minScore=85)

    def executeFunction(self, section, gen):
        self.takeSection(section, gen)

        



"""
Summary:

takeSection requires section, and gen variables.
The Section should be one of "Route" or "Caught", which would capture the Route or Caught pokemon respectively. 
Gen is which generation of game. For example, to catch the Route of Fire Red, you would need different image dimensions than
Emerald. 


takeScreenshot gets called from takeSection. It requires the filepath, x,y,width and height, which are the dimensions of the
screenshot requested. All of these variables are given automatically from takeSection and they vary(able) based on which
section was requested.

"""