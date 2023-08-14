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