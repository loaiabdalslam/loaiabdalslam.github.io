Title: Learning cc65
Author: mr.rcollins
Date: 2014-12-09 13:36
Slug: learning-cc65
Category: Software
Tags: cc65

Tonight I've taken my first plunge into finally learning cc65 and writing software for the A8. I'm attempting to convert my ten liner from the ABBUC 2014 contest over to c. Here's the first part, it redefine's the character set to be inverse:


    :::c

    /************************************************ 
     * Crack My Luggage - C version
     *
     * My attempt to rewrite my ten liner for the
     * ABBUC 2014 Ten Line competition for C, while
     * learning C.
     *
     * 12/9/2014
     ************************************************/

    #include <atari.h>
    #include <conio.h>
    #include <peekpoke.h>

    typedef unsigned char byte;

    void setup();

    int main()
    {
        setup();
        gotoxy(2,0);
        cprintf("crack my luggage");

        cgetc();                    // Don't end the program until a key is pressed
        return(0);                  // All done!
    }

    void setup() {
        unsigned int ch,i;
        byte a;

        _graphics(18);
        POKE(559,0);                // Turn off screen
        ch=PEEK(106)-16;
        POKE(756,ch);
        ch=ch*256;

        for (i = 0; i < 1024; i++) { // Redfine character set, make it inverse
            a=127-PEEK(57344L+i);
            //if (a<0) { a=0; }
            POKE(ch+i,a);
        }

        for (i = 0; i < 8; i++) {   // Set space to hash pattern
            POKE(ch+i,85+(85*(i%2)));
            POKE(ch+i+80,127-PEEK(58016L+i));
        }

        POKEW(708,2710);            // Set colors
        POKEW(710,3868);
        POKE(559,34);               // Turn screen back on
    }


