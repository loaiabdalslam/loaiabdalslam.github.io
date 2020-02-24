---
Title: Setting up a wifi modem with the CHIP computer
Author: gozar
Date: 2019-10-23 18:57
Slug: setting-up-a-wifi-modem-with-the-chip-computer
Category: Hardware
Tags: modem,tcpser,CHIP
Status: published
...

I was a backer of the original Kickstarter project for the $9 CHIP computer. Over the past several years I accumulated 8 CHIPs and 3 PocketCHIPs. Suffice to say, I'm sitting pretty with CHIPs. 

![My CHIPmodem, with optional battery](https://cdn.gtia.com/pics/2019/CHIPmodem-2019-12-29-800x.jpeg)

My first project with the CHIP computers was setting up [Shairplay](https://github.com/juhovh/shairplay) on one, and hooking it to a 1970s console stereo. The result is a pretty good sounding wireless speaker that I play music from my iPhone or iTunes on the computer.

My next project was to use a CHIP as a wifi modem for my retro computers. I wanted to use the CHIP instead of the Arduino based wifi modem for a couple of reasons. One, I have several CHIPs. Two, I wanted to be able to not only use the modem to connect to BBSes, but I also wanted to be able to ssh to hosts. Finally, I have a couple of old Macs (such as the SE/30) that do not have network cards. Using a CHIP as a PPP server I would be able to give these Macs (and my STs) an IP connections. With the modifications FozzTexx did to [tcpser](https://github.com/FozzTexx/tcpser), I would have a really cool wifi modem that could connect my retro computers to just about anything.

A lot of this article came from came from the hard work of [Raspberry Pi modem](http://podsix.org/articles/pimodem/). 

## Getting the hardware ready

I re-flashed a CHIP, and started to look at how to add a serial port to the little guy. It has a built in UART, but then I would need some level-shifters to make it RS232 compatible. I took the easy way out and bought a FTDI based USB to RS232 cable. My cable arrived, but when I plugged it in... Nothing.

## My kingdom for a driver

Apparently, every Linux distribution under the sun has the FTDI serial driver, except for the CHIP computer with the 4.4.11 kernel. If you have the 4.4.13 kernel, you can skip these steps.

The internet led me to a defunct page on NTC's BBS in which someone had [compiled the driver for the CHIP](https://web.archive.org/web/20180919025028/https://bbs.nextthing.co/t/usb-serial-connection-from-chip-to-cnc-device-large-usb-port/11210/19). Unfortunately, the link to the driver in Drobox was dead. But, all was not lost. I emailed the person who posted the driver, [Daniel Perron](https://github.com/danjperron), and as luck would have it, he still had a copy and sent it to me. It is now [posted on the internet](https://cdn.gtia.com/2019/usbserial.tgz) for others! He was a big help, because the only other solution would be for me to set up and compile the driver, and I don't know if I could have done it.

Once I had the driver, I followed the directions archived at [archive.org](https://web.archive.org/web/20180919025028/https://bbs.nextthing.co/t/usb-serial-connection-from-chip-to-cnc-device-large-usb-port/11210/19) and I then had a serial port.

On the CHIP (and as root), navigate to where the serial drivers will go and create a folder named serial there. Check the name of the kernel, if it is 4.4.13-ntc-mlc you are good to go and do not have to follow these directions.

    cd /lib/modules/4.4.11-ntc/kernel/drivers/usb
    mkdir serial
    cd serial

Now, copy the drivers from the download above into that folder.

Insert the modules:

    sudo insmod usbserial.ko
    sudo insmod ftdi_sio.ko

Now plugging in your FTDI device will give you a /dev/ttyUSB0.

## Fixing updates

You'll need to follow the directions in the [CHIP-Community wiki](http://www.chip-community.org/index.php/Care_and_Feeding#Update_CHIP_Software) to update your apt sources so you can actually update the software on the chip and install software. In a nutshell, replace `ftp.us.debian.org` & `http.debian.net` in `/etc/apt/sources.list` with `archive.debian.org`. Also, replace `opensource.nextthing.co` with either `chip.jfpossibilities.com` or `chip.lotek.fr`. Finally, since the apt sources are no longer being updated, we need to tell apt to ignore any expirations. `sudo nano /etc/apt/apt.conf` and add the line (the fille will probably be blank and you will be creating it):

    Acquire::Check-Valid-Until "false";

Now your apt commands will work!

## Setting up tcpser

I'm using [FozzTexx's fork of tcpser](https://github.com/FozzTexx/tcpser). What tcpser does is provide modem emulation. After adding a USB to RS232 adapter (usually based on the FTDI chip), you can plug it into any computer with an RS232 port and tcpser will act like an Hayes compatible modem.

First, I had to set up the CHIP so I could get the tcpser source and compile it.

    sudo apt update
    sudo apt install git build-essential

Now I clone the git repository:

    git clone https://github.com/FozzTexx/tcpser

And finally, compile that bad boy:

    cd tcpser
    make

A couple minutes later and I had a *tcpser* executable in the directory. I'll move it somewhere sane later, I just wanted to try it out.

    ./tcpser -d /dev/ttyUSB0 -s 19200 '&K0'

(The `&K0` disables flow control, you may need it on, but it worked on my Atari 800 without issue.)

I made a cable that consists mostly of dongles since I didn't have a 9-pin female to female adapter. The cable connected the CHIP to my MegaSTe as my first test. It worked right away!

Tcpser works exactly like a Hayes compatible modem would work. To dial, use `atd` and the IP address of the host. To hang up, use `ath`. Depending on your terminal program, you may be able add ip addresses and port numbers and dial out like the old days. If your terminal program can't handle ip addresses or domain names, you can pass an address book when [starting tcpser at the command line](https://github.com/FozzTexx/tcpser). 

I started writing this article in Vim on my Atari MegaSTe. At 9600 baud it is pretty responsive, except for when it comes time to scroll. My Vim setup is configured for writing, using the [Goyo](https://github.com/junegunn/goyo.vim), [vim-markdown](https://github.com/plasticboy/vim-markdown), and [Pencil](https://github.com/reedes/vim-pencil) plugins.

## What's next?

You can dial out, but it would be nice to connect to the CHIP and then ssh out from there. To do that, install telnetd.

    sudo apt install telnetd

From your favorite retro computer, you can now dial localhost and connect.

    atd localhost

I need to set up tcpser as a service, so it starts when the CHIP starts up. Right now I ssh into my CHIPs and run tcpser under tmux. I'd love to put the [CHIP in a modem case and wire up the LEDs](http://podsix.org/articles/pimodem/), but maybe later.
