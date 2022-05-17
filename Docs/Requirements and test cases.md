# Algebraic numbers To Roman Numbers

## Requirements
<p> R1. The system will allow a maximum number of 5000 to be entered.</p>
<p> R2. The system will not allow negative number.</p>
<p> R3. The system will allow decimal number.</p>
 <p> R4. The system will not allow letter.</p>
<p> R5. The system will ask if you want to convert a number again once the process is finished</p>

## Criteria of acceptance
<p> CR 1.1 The system must allow entering Arabic numerals less than or equal to 1000</p>
<p> CR 1.2 If the number entered is greater than 1000, it should launch a message that says: the number must be between 1 and 1000</p>
<p> CR 2.1 If the number entered is negative, it should launch a message that says: only positive numbers are allowed</p>
<p> CR 3.1 The system must allow entering decimal Arabic numerals less than or equal to 1000</p>
<p> CR 4.1 the system must not allow the entry of alphabetic data</p>
<p> CR 4.2 If the data entered is alphabetic, it should launch a message that says: only positive numbers are allowed</p>
<p> CR 5.1 At the end of the conversion process, the system should launch the following message: Do you want to return? Yes/No</p>
<p> CR 5.2 If the user enters the word Yes, then the loop continues.</p>
<p> CR 5.3 If the user enters the word No, then the loop end.</p>

## Test Case
### END TO END
<p> TC 1. The text and the input data must be on the same line</p>
<p> TC 2. the roman numeral shown at the end must be between parentheses</p>
### Unit Test
<p> TC 3. A letter is entered</p>
<p>  **system response** "only positive numbers are allowed"</p>
<p> TC 4. A blank space is entered</p>
<p> **system response** "only positive numbers are allowed"</p>
<p> TC 5. A blank space is entered</p>
<p>  **system response** "only positive numbers are allowed"</p>
<p> TC 6. enter a number greater than 1000</p>
<p>  **system response** "the number must be between 1 and 1000"</p>
