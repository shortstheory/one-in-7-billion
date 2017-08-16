title: What I've been upto
date: 2016-12-19 11:09
author: Arnav Dhamija
tags: College, Life, KDE
category: Article
slug: this-semester-has-gone-little-too-fast

This semester has gone a _little_ too fast for my liking. Though there were
plenty of good memories and takeaways from this semester, it has been by far
my most stressful time in this college yet. Between taking on a number of
technical projects and trying to rescue a sharply falling SG due to a poor T1,
there has been very little free time this sem. Above all, this sem has shown
me just how limited of a resource brain power is. Thinking about solving
problems wears me out much more easily than it used to.  

That's not to say what I've been doing is all drudgery. Some interesting
projects that I've been working on:  


### GSoC 2016 Project - kio-stash

Yup, this [project](https://github.com/KDE/kio-stash) has been in the pipeline
for months. While it (mostly) works on a clean install of KDE, it has some
bugs with copying with mtp:/ device slaves and isn't very well integrated with
Dolphin yet. It is in my best interest to have this shipped with KDE
Frameworks as soon as possible, so I'm looking into patching Dolphin with
better, more specific action support for my project.  

### IEEE Signal Processing Cup 2017 - Real-Time Beat Tracking Challenge

The premise of this project doesn't seem very complicated - a team just needs
to submit an algorithm which can successfully detect the beats in a song in
real-time on an embedded device. Heck, I had already implemented the same on
an Arduino with a microphone for rather [fancy lighting in my hostel
room](https://www.youtube.com/watch?v=lMb1XScNgOs). Unfortunately, as I've
learned the hard way, anything that looks simple is deceptive and this project
is a perfect example. For one thing, a song by itself in the amplitude-time
domain is nearly impossible to extract any data from, so it requires a (Fast)
Fourier Transform to extract frequency bin amplitudes to get anything useful
from it. Next, obtaining beat onset and detection requires generating a
tempogram to find the BPM of a song to find the approximate beat positions.
There are many interesting approaches and different algorithms to solve this
problem. Fortunately, I'm not doing this alone and the seniors I'm working
with have a better understanding of the more difficult mathematical components
of this project, leaving me free to code in C++ and deploy it on actual
hardware.  

### foss@bphc

This project is a society on campus I started with
[three](https://github.com/aero31aero/)
[programmers](https://github.com/TestSubjector) [far](https://github.com/Nischay-
Pro/) more competent than myself. It all started in September this year
when we had the two-day long [Wikimedia
Hackathon](https://www.mediawiki.org/wiki/Wikimedia_Hackathon_BPHC) on campus.
Though my contribution to Wikimedia was small, I got a lot out of the
hackathon by meeting the people from Amrita University who came for organising
the event. Listening to what
[Tony](https://www.mediawiki.org/wiki/User:01tonythomas) and
[Srijan](http://srijanagarwal.me/) had to say about how much working for
foss@amrita had benefited them made me realise how much room for improvement
there was in BPHC. As far as this society goes, things are still in their
infancy, yet I feel there is just enough critical mass of talent and
enthusiasm in open source development to push this society forward. We even
have our own
[Constitution](https://fossbphc.github.io/docs/constitution.html)!  

### Making a personal website?

While Blogspot has been a faithful home for this blog for over half a decade,
it is time to move to a modern solution for hosting. Plus setting up a website
will teach me a bit about web development too, and I've needed an excuse to
learn it for a while. Surely it can't be all that hard, right?  

### Burnout

While the slew of all these technical projects seemed like a good idea at the
time, it has pushed me closer to burning out. It is the same feeling as what I
felt the same time last year, albeit for different reasons.  

Some of it has carried over from studying harder at the end of this sem than I
had done so before. To my surprise, studying under pressure was actually more
effective than it was without. In some ways, it was a throwback to studying
for the number of exams nearly a couple of years ago. It has made me question
whether any of my education was as much for the knowledge as it was for the
desperation of avoiding failure. I still haven't figured it out, but at least
I feel like I'm not as adverse to putting in the hours for getting a decent
CGPA as I had been last semester.  

There have been compromises in other spheres of college life as well,
investing so much time in studying or doing projects has made me cut down my
participation in other clubs and I've quit nearly all the non-technical clubs
I joined last year. There's more than that too - I feel it's much harder to be
fully immersed in anything anymore.  

Maybe it's just something else which requires more soul searching.
