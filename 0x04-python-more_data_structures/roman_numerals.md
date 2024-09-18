# Roman to integer

## Task
Create a function `def roman_to_int(roman_string):` that converts a Roman numeral to an integer.

    - You can assume the number will be between 1 to 3999.
    - `def roman_to_int(roman_string)` must return an integer
    - If the roman_string is not a string or None, return 0
### Thought Process
1. Roman numerals
`num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}`

2. How Roman numerals work
If a smaller numeral precedes a larger one, subtract the smaller numeral
If a maller numeral follows a larger one, add them together
eg. IV = 5 - 1 = 5, VI = 5 + 1 = 6, CMLXVI = 1000 - 100 + 50 + 10 + 5 + 1 = 966 etc.

## Logic
1. Create a map of Roman numerals to their integer values
    `num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}`
2. Initialize a total variable to accumulate the integer value
    `total = 0`
3. Iterate through the `roman_string`:
    - for each character, check if it's smaller than the next character.
        - if it is smaller, subtract from the total
        - else add to total
    - return the result (`total`)