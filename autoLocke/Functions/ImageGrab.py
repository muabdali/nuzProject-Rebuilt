import pyautogui
from autoLocke.Files.Data.CordsDict import routeCordDictionary, caughtRouteDictionary


class screenshotClass:
    def __init__(self):
        self.routeDict = routeCordDictionary
        self.caughtDict = caughtRouteDictionary


    # Requires the section (Route or Caught), and Generation because different games have different ss cords.
    # Takes the section and assigns it the appropriate list from routeCordDictionary or caughtRouteDictionary
    def takeSection(self, section, gen):
        routeDictGen = self.routeDict[gen]
        x, y, width, height = routeDictGen[0], routeDictGen[1], routeDictGen[2], routeDictGen[3]
        if section == "Route":
            filepath = "autoLocke/Files/Images/RouteImage.png"
            self.takeScreenshot(filepath, x, y, width, height)
        else:
            filepath = "autoLocke/Files/Images/CaughtImage.png"

    def takeScreenshot(self, filepath, x, y, width, height):
        screenshot = pyautogui.screenshot(region=(x,y,width,height))
        screenshot.save(filepath)

ia = screenshotClass()
ia.takeSection(section="Route", gen="fireRed")