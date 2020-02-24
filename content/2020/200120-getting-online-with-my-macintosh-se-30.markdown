---
Title: Getting online with my Macintosh SE/30
Author: gozar
Date: 2020-01-20 16:52
Slug: getting-online-with-my-macintosh-se-30
Category: Hardware
Tags: mac,network
Status: published
...

![My SE/30 on IRC](https://cdn.gtia.com/pics/2020/SE30-2020-01-20-800x.jpeg)

One of my goals for creating the [CHIP wifi modem](https://gtia.com/2019/10/23/setting-up-a-wifi-modem-with-the-chip-computer/) was to use it as a networking device with my SE/30. Today I tried it out as a modem. My first issue was the fact I didn't have any communication software on the SE/30. Well, I take that back. I did have something in Microsoft Works on the machine, but it's not, shall we say, full featured.

After some quick research, I came across [Zterm](https://macintoshgarden.org/apps/zterm). Getting it to my SE/30 required the usage of another Mac. I downloaded the .sit file with my Windows machine and copied it to a floppy disk. The disk then went in my 20th Anniversary Mac. From there I uncompressed the sit file and put the resultant folder on a Mac formatted floppy. Finally, I took the floppy to my SE/30 and copied over Zterm 1.0.1. Originally I tried the 1.1beta version, but it wouldn't launch on my SE/30. I'm assuming it's something to do with System 7.1.

Using Zterm has been amazing. I switched the terminal emulation to VT100, and the only screen corruption issues I've had is when smart quotes or unicode is shown. That is to be expected. I can use tmux and Vim without issue. In fact, this article is being written with the SE/30 under Vim.

If you want to use a classic Mac online, then making a wifi modem and using Zterm is a pretty powerful combination. This set up does require some comfort at the command line so you can do stuff online.
