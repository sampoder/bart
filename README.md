# 🚇 BART sculpture 

TLDR: The sculpture lights up whenever a train is about to arrive at Downtown Berkeley (feel free to change the station in `main.py`[^1])! I built this for [DESINV 23](https://classes.berkeley.edu/content/2025-spring-desinv-23-1-lec-1), a class on creative programming & electronics at UC Berkeley.

<img src="https://github.com/user-attachments/assets/77100e8e-62af-4791-991e-9d8a15e23017" width= "600px" />

## Showcase / Description of Finished Piece

As a young person living in the Bay Area, BART is an important part of my life. And I love BART! I use it to [visit friends, run errands, head to parks etc.](https://sampoder.com/bart_ed.pdf) There's one problem, however. BART doesn't come very often. Where I grew up trains arrived every 3 to 5 minutes on average. Meanwhile, BART operates with headways of about 20 minutes. 

I built a piece that I could leave on my desk to keep track of the trains arriving at Downtown Berkeley. It has two modes: standard and leave the house. When in standard mode, it lights up when a train arrives and makes a sound when a train leaves. Meanwhile, in "leave the house" mode it lights up the train about thirteen minutes before a train leaves and makes a noise when there's twelve minutes before it leaves. That's because it takes me twelve minutes to walk to the station.

Here's what it looked like:

<img width="600px" alt="Screenshot 2025-02-14 at 12 00 05 AM" src="https://github.com/user-attachments/assets/76a8ae04-1055-41f5-9798-839b90f75e83" />

The finished piece is a replica BART train that was made out of laser cut / engraved acrylic. It has two RGB LEDs inside of it (these make the colour). When connected to a computer running the Python script, it lights up when a train is at the configured station. This data is pulled from [BART's legacy API](https://api.bart.gov/docs/overview/index.aspx). The Python script then commands the Arduino to light the train up a certain colour via serial communication. The colour of the train is based on the BART line, for example trains to Berryessa from Downtown Berkeley are orange while trains to Millbrae / San Francisco are red.

<img width="600px" alt="Screenshot 2025-02-14 at 12 00 15 AM" src="https://github.com/user-attachments/assets/22ee0e2e-b6b2-4929-9a2c-0b7c25c6c823" />

The original inspiration was a light-up plane that I drew in class (not a super serious idea), alongside some other ideas:

<img width="600px" src="https://github.com/user-attachments/assets/9f39fe87-e353-4962-9282-d947e2cee3c9" />

People already complain about the noise planes make - I doubt too many people would enjoy them creating this amount of light (I think it'd be cool though!). That did get me thinking transportation as a theme though. 

And that thinking progressed into this idea of reconstructing the entire BART station (each train represented a different direction):

<img width="600" alt="Screenshot 2025-02-21 at 6 19 33 PM" src="https://github.com/user-attachments/assets/63eda38b-8af6-4f86-8f56-26bfdb0658dc" />

However, I ended up going with one train because I thought this design would be bulky and take up too much space on my desk. I decided that if I wanted to illustrate direction I could animate a strip of Neopixels in the future.

To create the shell for the project, I designed a couple of pieces I could laser cut using Figma. Figma probably isn't the best software for this - but it's something I'm very comfortable with and that I knew could do the job. With more time, I would have CAD-ed it.

Here's my Figma setup:

<img width="600" alt="Screenshot 2025-02-21 at 6 28 43 PM" src="https://github.com/user-attachments/assets/6a1e16cc-caa9-44cc-bf45-9338ee658e4b" />

I then exported this as an SVG and set it up in Adobe Illustrator to be laser cut. I did this all at the [Jacobs Hall Makerspace](https://jacobsinstitute.berkeley.edu/making-at-jacobs/).

The first laser cut had a slight problem, the engraving was too faint so it was hard to distinguish the train design (I was engraving most of the acrylic and leaving the outline of train un-engraved):

<img width="600" src="https://github.com/user-attachments/assets/841f2f24-9a86-47bc-8b55-f44e0a48e0d8" />

(you can see how it's a bit patchy)

This was because the laser cutter / engraver is stronger in the centre. Going forward, I did my future engraving from the centre of the bed.

So now I had the shell of it! I hot-glued all the pieces together to make the full train. Next step was wiring, here's what the circuit looked like:

<img width="600" alt="Screenshot 2025-02-21 at 6 46 00 PM" src="https://github.com/user-attachments/assets/236564f9-3857-4f54-9d41-047e129eee6a" />

Last thing to do was to program it! As I mentioned earlier I'm running a Python script on my laptop and communicating with Arduino using serial. I originally used the [Transit App's API](https://transitapp.com/apis) but it was probably overkill for this purpose. Though using this knowledge, I built this little menu bar app to help me keep track of transit nearby:

<img width="401" alt="Screenshot 2025-02-21 at 6 52 58 PM" src="https://github.com/user-attachments/assets/6fa3454e-8984-4b03-8489-a8fe6f893d57" />

But anyways! With it coded up, I now had a working thing. Just imagine if there was a purple BART line:

<img width="600px" alt="Screenshot 2025-02-14 at 12 00 52 AM" src="https://github.com/user-attachments/assets/337af8bd-26f2-4a38-8a45-2d2378e87b7d" />

And here's the noise it makes if the train is leaving:

https://github.com/user-attachments/assets/8d63fbfe-5397-4607-a32a-b0ea8b4b94a8

## Reflection

I had a lot of fun making this! I don't think I'd used a laser cutter since high school before this (sadly) and it was great to try out some new APIs I hadn't used either. Plus BART makes me happy so seeing this thing on my mantlepiece everyday makes me happy (I had to use the Arduino for more projects)!

<img width="600px" alt="Screenshot 2025-02-21 at 7 01 02 PM" src="https://github.com/user-attachments/assets/0cdc0c37-27f0-40e3-a97f-7d44894fde3c" />

This project started with me building something practical but over time it morphed into having a different message. Not missing the train became less important to the story because as I showed it people, it became clear to me that people enjoyed it because it reminded them of fond memories using BART. BART is critical infrastructure for me and my peers - only a few of us have cars and the logistics of driving in the Bay Area is a nightmare. So we use BART for everything and anything; I think that's why this made people smile when I showed it to them. Plus anything that lights up is cool! Waiting for the train is also a universal experience, so in a way, this piece highlights the importance of funding BART so it can have more frequent schedules / they can reduce the wait times. [That's a relevant topic at the moment.](https://www.bart.gov/about/financials/crisis)

If I was to make the project again, there'd be a couple of things I'd change:

* Designing joints for my laser cut pieces so I wouldn't have had to hot glue the piece together.
* Modelling the train in CAD - this would have allowed me to properly create the diagonal shape of a BART train. Plus I want to improve my CAD skills so I can do more.
* Using an ESP32. That would have allowed me to make API calls from my Arduino code directly and not have to run a separate Python script.

This project isn't going to waste. I'm using my electronics for future projects and keeping the structure as an ornament on my mantlepiece.

But at the end of the day, the most fun part of this project was showing it to friends and seeing them smile as it lit up. So thanks to everyone who said nice things about it and gave me helpful feedback!

## Sources

Thanks to these sources for helping me:

Dr. Sudhu's Arduino Tutorial: https://github.com/loopstick/ArduinoTutorial

BART's API documentation: https://api.bart.gov/docs/overview/index.aspx

Taylor S. Marks' playsound module: https://github.com/TaylorSMarks/playsound

[^1]: https://api.bart.gov/docs/stn/stns.aspx
