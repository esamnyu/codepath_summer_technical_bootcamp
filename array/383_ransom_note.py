class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
            magazine = list(magazine)
            # print(magazine)
            #Iterate ransomNote
            for i in ransomNote:
                #Find the same character in magazine
                if i in magazine:
                    #Remove character in magazine until you iterate through all of ransomNote
                    magazine.remove(i)
                else:
                    return False
            return True