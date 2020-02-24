Title: Taking RetroPie to the next level with a Lenovo IdeaPad Yoga 11s
Author: gozar
Date: 2018-11-25 20:10
Slug: taking-retropie-to-the-next-level-with-a-lenovo-ideapad-yoga-11s
Category: Hardware
Tags: retro,raspberrypi,retropie
Status: published

With the Christmas season coming, and knowing that I would be spending time away from home, I struggled with how to bring some retro along with me. In the past I've taken a modded Xbox and a Raspberry Pi to family gatherings, but both of them require me to commandeer one of the TVs, which usually is another boss battle in and of itself. While trying to think of a solution, I spied my Lenovo IdeaPad Yoga 11s, which was my laptop for several years until I replaced it with a Chromebook last year.

![RetroYoga](https://cdn.gtia.com/pics/2018/RetroYoga-2018-11-25-800x.jpeg)

The Yoga has an 11" screen, i5, 8GB of ram and a 256GB SSD. On specs alone it blows the OG Xbox and Raspberry Pi out of the water. More importantly, it had its own screen in addition to HDMI out, which meant I could use it by itself or with a TV, depending on the family temperament. I just needed to get RetroPie installed. 

# Installing Ubuntu 18.04

There are several distributions to choose from, and this particular machine ran MATE when I used it as a laptop. I decided to install Ubuntu 18.04, for really no reason in particular. If you're curious on how to install Ubuntu, search around, there is no shortage of installation directions and videos.

This step took less than 15 minutes. After the installation, I was pleasantly surprised that the wireless worked. In the past I had to download and compile the wifi driver, but now it worked out of the box!

I set up the default user as *retro*, with a password of *retro*, and automatic log in. This way anyone could start playing without bugging me about passwords.

# Installing RetroPie

I followed the [instructions in the RetroPie wiki on installing RetroPie under Debian/Ubuntu](https://github.com/RetroPie/RetroPie-Setup/wiki/Debian). It was pretty straightforward, but took forever. This step took a few hours to complete.

For the games, I had already downloaded a RetroPie distribution for the Pi and put it on an SD card. I popped the SD card into the built in card reader and dragged the roms to their respective folders.

# Creating a desktop icon

Muggles aren't going to want to start a terminal and type *emulationstation* to start up RetroPie, so I created a desktop icon. From a terminal I typed ```nano ~/Desktop/RetroPie.desktop```. This launched the nano editor, in which I typed the following:

```
#!/usr/bin/env xdg-open

[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Exec=/usr/bin/emulationstation
Name=RetroPie
Comment=

```

# Controllers

What fun is playing RetroPie from the keyboard? Not fun at all. I grabbed several controllers I already had and configured them in RetroPie. This included a couple of USB Xbox 360 controllers, and an Xbox One controller connected over USB, and an OG Xbox controller with a USB adapter. I couldn't get RetroPie to recognize my cheap OG Xbox knock off controllers, so I'll have to work on those at a later date. Since the Yoga only has two USB ports, I also grabbed an USB hub. This is only temporary because I would like to get a smaller USB travel hub.

# Traveling case

To carry the Yoga and controllers to its destination requires a milk crate. I'm going to be looking out for something a little more travel friendly, but this will work for now. The problem is the controllers. They are big and bulky. If I wanted to spend some money I could pick up some travel controllers, but I'm not going to.

I would love a hardshell case which would let me put the Yoga in tablet mode and mount it in the lid while the case holds a wireless keyboard and the controllers, but that's not going to happen.

# In Use

The N64 emulator played Mario Kart 64 flawlessly, with no slowdowns or glitches. Almost all of the games that we played worked well, except for some of the arcade roms, such as Street Fighter II. I'll need to investigate further. One nice feature of using the Yoga is the ability to put the laptop into tablet mode and put it on the side for vertical games such as Frogger and Raiden.

# Future modifications

I don't have Atari 8-bit computer functionality, or any retro computer functionality installed. To complete the set up, it would be nice to be able to play Atari 8-bit, Atari ST, and Amiga games. I also need to troubleshoot Street Fighter II.
