Title: GozMind - My 10 liner for the NOMAM 2014 competition
Author: gozar
Date: 2014-02-18 20:10
Slug: gozmind-my-10-liner-for-the-nomam-2014-competition
Category: Software
Tags: contest,tbxl

Over Christmas break I really started to get back into using my Atari
800xl. I got my MyIDE+Flash set up to work with Action! because I've
always wanted to learn it. Then I read about the [BASIC Ten-Liners -
Contest
2014](http://atariage.com/forums/topic/221948-basic-ten-liners-contest-2014/).
I had a snow day today, so I am proud to announce GozMind. It's
basically a clone of Mastermind. Unfortunately, trying to fit it into 10
lines was tough. So tough that the code to guess consists of the built in
characters, *!@#$%&. After you enter your guess with the controller,
pressing the fire button will have the computer tell you how you did.
An * means you have the right character in the right place. An O means
that you have the right character, it's just in the wrong place.

![Gozmind Screenshot](https://cdn.gtia.com/gozmind/gozmind.png)

Bootable atr available here:
[gozmind-v140218.atr](https://cdn.gtia.com/gozmind/gozmind-v140218.atr)

# Program breakdown

I'm not really happy with how the code looks. It's quite a mess. Maybe
I'll go back and refactor, but for right now it works. :-)

## Line 10

![10.png (640×56)](https://cdn.gtia.com/gozmind/10.png)

* DIM C$(14): Holds the characters for the code. It also holds a
 duplicate set in inverse. The inverse is used as a indicator for the
 active place for the player
* S$(4): The solution
* G$(4): Player guess
* O$(4): Temp for scoring player guess
* A$(4): Holds how the player did with their guess
* H$(1),D$(1),M$(1),B$(1): To save a character in the lines
* C$="!#$%&@INVERSE": The characters used for the code
* H$="*":D$=".":M$="O":B$=" ": Used to save characters in the solve
 procedure
* Y=1: What row are we working on

## Line 20

![20.png (640×73)](https://cdn.gtia.com/gozmind/20.png)

This is my favorite line of the program. To create a random code to
guess, the program randomly picks a number from 0 to 1295. Why 1295?
That is 5555 is base 6. We have 6 codes from which to select, so we
want to use base 6. Once a random number is selected, it is converted to
base 6. Since strings in Atari Basic start with one, we have to add one
to each character. Each digit is converted to a string and then place in
S$. The graphics mode is selected and GOZMIND is printed at the top.

## Line 30

![30.png (640×54)](https://cdn.gtia.com/gozmind/30.png)

* G$="7777":C=1:G=VAL(G$(C,C)):LC=C:A$="....": Sets up the start for the
* player. C is the current character the player is working on.
* REPEAT :PAUSE 5:
* EXEC S2S: Convert G$ to the characters of the code and store in O$
* POSITION 5,Y:? #6;O$;"  ";A$: Print the current guess (O$). A$ will be
the what characters are right, once the player makes a complete guess. 

## Line 40 & 50

![40.png (640×55)](https://cdn.gtia.com/gozmind/40.png)

![50.png (640×67)](https://cdn.gtia.com/gozmind/50.png)

Reads the joystick, and adjusts the variables related to the current
code and position. If statements are used to keep the values in range.
It adjusts the character in G$ depending on what the player has
selected. The repeat loop is waiting for a guess in all 4 slots and for
the player to push the button. Once satisfied, execute the SOLVE
procedure.

## Line 60

![60.png (640×53)](https://cdn.gtia.com/gozmind/60.png)

![70.png (640×54)](https://cdn.gtia.com/gozmind/70.png)

Prints how well the player did on the right side of the screen. It them
increments Y to go to the next row and checks to see if the player has
solved the puzzle yet or if the player has exhausted all 10 tries. If
the game has ended, wait until the player to press the button to start a
new game. Else, continue playing.

## Line 80 PROC S2S

![80.png (640×53)](https://cdn.gtia.com/gozmind/80.png)

Converts the numbers in G$ to the characters to print on the screen. The
computer only deals with numbers, but we need to covert to characters
for the player.

## Line 90 & 100 PROC SOLVE

![90.png (640×54)](https://cdn.gtia.com/gozmind/90.png)

![100.png (640×54)](https://cdn.gtia.com/gozmind/100.png)

The toughest code to write. O$ is a copy of the solution, because we are
going to destroy the variable as we go. First it finds out which character selected
by the player is correct and in the correct place. The for loop goes
through each character of the solution, and checks for a match in the
players guess. If there is a correct guess, the current position of A$
is set to * and the position has one added. We then set that position in
O$ to a . and in the guess to space so it doesn't match any further.

The code then goes through the solution one character at a time and
checks for the right character just in the wrong position. This time, if
there is a match, it is added as an O to A$.

