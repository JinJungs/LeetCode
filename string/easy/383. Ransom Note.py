class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteArr = list(ransomNote)
        magazineArr = list(magazine)

        for ransomNoteLetter in ransomNoteArr:
            if ransomNoteLetter in magazineArr:
                magazineArr.remove(ransomNoteLetter)
            else:
                return False

        return True