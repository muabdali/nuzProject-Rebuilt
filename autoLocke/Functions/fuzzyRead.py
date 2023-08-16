from fuzzywuzzy import process

class fuzzChecker:
    @staticmethod
    def checkList(pokeList, nameToCheck, minScore):
        with open(pokeList, 'r') as f:
            string_list = [line.strip() for line in f]
        best_match, score = process.extractOne(nameToCheck, string_list)
        if score < minScore:
            return None
        else:
            return best_match
    

        """
        This file contains a single class with a single function.
        The function utilizes fuzzywuzzy to compare the scanned text to the desired results.
        
        Due to the inherent inaccuracy in pytesseract, sometimes it may give an incorrect
        string, for example, instead of Route 1, it will give Roote 1. FuzzyChecker will take
        "Roote 1", compare it to all the route names, and return the proper name, in this case
        "Route 1". this is vital as the for loop that checks for route names ONLY recognises correctly
        spelt names.
        
        In the future, this should be updated to the new fuzzywuzzy library named "thefuzz", but for now it 
        should do the job.
        """