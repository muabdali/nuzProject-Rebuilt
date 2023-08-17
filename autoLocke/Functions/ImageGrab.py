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
            result = self.takeScreenshot(filepath, x,y,width,height,section=section)
            print(result)

    def takeScreenshot(self, filepath, x, y, width, height, section):
        screenshot = pyautogui.screenshot(region=(x,y,width,height))
        screenshot.save(filepath)
        result = self.tessRead(path=filepath, section=section)
        return result
    
    def tessRead(self, path, section):
        tesseractRead = imgProcess()
        tesseractResult = tesseractRead.imageEnhance(imagePath=path)
        fuzzyResult = self.fuzzyCompare(text=tesseractResult, section=section)
        return fuzzyResult
        
    # DOES NOT NEED TO BE CALLED SEPERATELY, ALREADY CALLED FROM tessRead.
    def fuzzyCompare(self, text, section):
        fuzzProcess = fuzzChecker()
        if section == "Route":
            tocheckList = "autoLocke/Files/Data/fireredroutes.txt"
            fuzzProduct = fuzzProcess.checkList(pokeList=tocheckList,nameToCheck=text,minScore=85)
        elif section == "Caught":
            tocheckList = "autoLocke/Files/Data/NatDexPokemonG3.txt"
            fuzzProduct = fuzzProcess.checkList(pokeList=tocheckList,nameToCheck=text, minScore=85)
        return fuzzProduct
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


fuzzyRead is a vital function for this program. Since tesseract is innacurate, there will always be spelling errors within
the image_to_text result. FuzzyRead counters this by comparing the given text with a list of expected strings, and choosing the
closest one. 


ORDER OF OPERATION

executeFunction is called.
executeFunction calls takeSection(section, gen)
takeSection() determines the appropriate screenshot dimensions depending on the generation and section. Also determines the filepath.
takeSection() calls takeScreenshot(filepath, dimensions)

takeScreenshot takes a screenshot given the dimensions and saves it to the given filepath
takeScreenshot then takes the filepath, and feeds it into tessRead(section, gen)


tessRead uses the Tesseract-OCR to get a general string given the path.
tessRead then calls fuzzyCompare(text, section)

fuzzyCompare takes the text and compares it to the given section's path.
fuzzyCompare returns the proper text if it finds a match.

The code is then called all the way back and is returned to takeSection with the matching
string.
"""

