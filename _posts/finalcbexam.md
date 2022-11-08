---
toc: true
layout: post
description: Reviewing incorrect answers for Tri 1 Final Exam
categories: [markdown]
title: Tri 1 Final Exam Review
---

Incorrect Questions + explanation

2.
- my answer: It displays true if x is negative and displays false otherwise.
- correct answer: It displays true if x is negative and displays nothing otherwise.
- Explanation: When x is negative, y is assigned the value true and the value of y is displayed. When x is not negative, y is assigned the value false and the display statement is never executed. It WONT display false, just nothing will be displayed.

15.
- my answer: Users can identify and correct errors they encounter when using released versions of the software.
- correct answer: Users can provide feedback that can be used to incorporate a variety of perspectives into the software.
- Explanation: Users can provide feedback that can help inform program design and development. Information gathered from potential users can be used to understand the purpose of a program from diverse perspectives and to develop a program that fully incorporates these perspectives. I accidentally choose the wrong option.

16.
- my answer: The message is broken into packets that are transmitted in a specified order. Each packet must be received in the order it was sent for the message to be correctly reassembled by the recipient’s device.
- correct answer:
- Explanation: Messages are broken into packets, BUT they can be received in any order and still be reassembled.

24.
- my answer: Decimal 5, binary 1011, binary 1101, decimal 12
- correct answer: Decimal 5, binary 1011, decimal 12, binary 1101
- Explanation: Binary 1011 is equivalent to 23+21+20, or decimal 11, and binary 1101 is equivalent to 23+22+20, or decimal 13. The order of the numbers (written in their equivalent decimal format) is 5, 11, 12, 13.

27.
- my answer: A string variable named s and a Boolean variable named a
- correct answer: A string variable named studentName and a Boolean variable named isAbsent
- Explanation: While a string variable and a Boolean variable are appropriate for this situation, the variable names s and a are not meaningful and will make the code segment harder for someone to read.


28.
- my answer: B
- correct answer: C
- Explanation: If the number of units of electricity used is 25 or less, the cost is 5 times the number of units. Otherwise, the cost is 5 times the first 25 units plus 7 times the number of units above 25. For examples, if a customer used 32 units of electricity, they should be charged $5 for the first 25 and $7 for the additional 7 units (32 – 25 = 7 units), for a total charge of $174. THE FIRST 25 U ARE STILL CHARGED AS 5 PER U.

32.
- my answer: [10, 30, 50, 70, 20, 40, 60, 80]
- correct answer: [10, 30, 50, 70]
- Explanation: List is not appended, a copy of myList is assigned to yourList.


35.
- my answer: B & D
- correct answer: A & D 
- Explanation:The last line in the code segment of B sets maxPS to 50 regardless of the value of time, which is incorrect.


37.
- my answer: B
- correct answer: D
- Explanation: B assigns both variable as num1


38.
- my answer:
 A. temp  ←  word1

word3  ←  word1

word1  ←  temp

- correct answer:

B. temp  ←  word1

word1  ←  word3

word3  ←  temp

- Explanation: A makes xylophone both word1 and word3, which is incorrect. 

41.
- my answer: 30
- correct answer: 20
- Explanation: q and s are 30 after the coe is executed, but r is 20. R is assigned the value of p and p is 20.


42.
- my answer: 18
- correct answer: 16
- Explanation: After initially assigning values to the variables, the code segment assigns the value 4 to num3 and assigns the value 8 to num1. The value of sum at the end of the code segment is 8 + 4 + 4, or 16.


43.
- my answer: 10
- correct answer: 15
- Explanation: 10 would be if it was looped 4 times, not 5.


44.
- my answer: 2
- correct answer: 3
- Explanation: The remainder when 23 is divided by 3 is 2, so 23 MOD 3 is 2. Question is asking what what y should be set to.


46.
- my answer: The value of first is false, and the value of second is false.
- correct answer: The value of first is true, and the value of second is true.
- Explanation: The eighth statement assigns the value of c + d / 2 (which is 50) to d.


47.
- my answer:
- correct answer: Assigned d incorrectly.The eighth statement assigns the value of c + d / 2 (which is 50) to d.


48.
- my answer: The value of first is false, and the value of second is false.
- correct answer:The value of first is true, and the value of second is true.
- Explanation: Incorrect. The third statement assigns the value of first (which is true) to second. The fourth statement assigns the value of second (which is true) to first.


49.
- my answer:
word  ←  "no"

word  ←  concat(reverse(word), reverse(word))

- correct answer:
word  ←  "on"

word  ←  concat(reverse(word), word)

- Explanation: The string produced is "on" not "no"