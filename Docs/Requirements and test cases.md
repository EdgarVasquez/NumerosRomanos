# Algebraic numbers To Roman Numbers

## Requirements
##### R1. The system will allow a maximum number of 5000 to be entered.
##### R2. The system will not allow negative number.
##### R3. The system will allow decimal number.
##### R4. The system will not allow letter.
##### R5. The system will ask if you want to convert a number again once the process is finished

## Criteria of acceptance
##### CR 1.1 The system must allow entering Arabic numerals less than or equal to 1000
##### CR 1.2 If the number entered is greater than 1000, it should launch a message that says: the number must be between 1 and 1000
##### CR 2.1 If the number entered is negative, it should launch a message that says: only positive numbers are allowed
##### CR 3.1 The system must allow entering decimal Arabic numerals less than or equal to 1000
##### CR 4.1 the system must not allow the entry of alphabetic data
##### CR 4.2 If the data entered is alphabetic, it should launch a message that says: only positive numbers are allowed
##### CR 5.1 At the end of the conversion process, the system should launch the following message: Do you want to return? Yes/No
##### CR 5.2 If the user enters the word Yes, then the loop continues.
##### CR 5.3 If the user enters the word No, then the loop end.

## Test Case
### END TO END
##### TC 1. The text and the input data must be on the same line
##### TC 2. the roman numeral shown at the end must be between parentheses
### Unit Test
##### TC 3. A letter is entered
#####  **system response** "only positive numbers are allowed"
##### TC 4. A blank space is entered
#####  **system response** "only positive numbers are allowed"
##### TC 5. A blank space is entered
#####  **system response** "only positive numbers are allowed"
##### TC 6. enter a number greater than 1000
#####  **system response** "the number must be between 1 and 1000"
