## *Russian Wordle Solver (Tinkoff 5букв)*
### Overview

This is a simple script to solve Russian variant of Wordle game now used in "Tinkoff 5букв"

### History of development

1. Find a list of all Russian words. Special thanks to [HARRIX](https://github.com/Harrix/Russian-Nouns) and his repo
2. Filter the main text file `russian_nouns.txt` and make a new file with only 5 letter words `n5.txt`.
Now nearly 3500 words left.
3. Replace `ё` letter with `е` using notepad. Also, remove strange words with hyphens. Like `хи-хи`
4. Lets count in how many words each letter occurs and make a rating:

| Char | Count | Char | Count | Char | Count |
|------|-------|------|-------|------|-------|
| а    | 1806  | п    | 564   | ы    | 197   |
| о    | 1280  | м    | 522   | х    | 194   |
| к    | 1159  | в    | 452   | ж    | 177   |
| р    | 1077  | б    | 446   | ф    | 170   |
| е    | 969   | д    | 431   | й    | 152   |
| и    | 865   | з    | 347   | ц    | 152   |
| т    | 862   | г    | 331   | ю    | 89    |
| л    | 821   | я    | 272   | щ    | 45    |
| н    | 776   | ь    | 271   | э    | 35    |
| с    | 738   | ш    | 256   | ъ    | 5     |
| у    | 621   | ч    | 210   |      |       |

5. Write a function to iterate through filtered words and check for chars that have
to be present in the word, for chars that must not be present in the word, and for regex pattern
match for chars that are in the correct position.
6. Find the words to filter the biggest part of our dictionary. Words that consist of most popular letters: 
[КРОАТ](https://ru.wiktionary.org/wiki/%D0%BA%D1%80%D0%BE%D0%B0%D1%82),
[СЕЛИН](https://ru.wiktionary.org/wiki/%D1%81%D0%B5%D0%BB%D0%B8%D0%BD) 
and than [ОБДУВ](https://ru.wiktionary.org/wiki/%D0%BE%D0%B1%D0%B4%D1%83%D0%B2) 
or [ОПИУМ](https://ru.wiktionary.org/wiki/%D0%BE%D0%BF%D0%B8%D1%83%D0%BC).
Most of the time first two will do the job.

### HOWTO
1. Start your game with any word or use my tactic (КРОАТ -> СЕЛИН). Use words one by one or both right away.
2. Input received hints to `solver` function. First chars that ARE NOT in target word (as a string), 
then chars that ARE in target word (as a string). If correct position for char is found, add it as
a third argument.
3. Choose the best candidate from the received output and use it in your game. Repeat from step 2 
until endgame. Good luck!  

### Example:
Hints: `а, в, т, к, с, б, з` are not in the target word, `о, м, е` are 
in target word and `м` is found to be the 1st letter. Function will look like this:  
>`solver(exclude="автксбз", include="оме", pattern="м....")`   

And the results will be:

> 3  
> меццо мопед мохер
