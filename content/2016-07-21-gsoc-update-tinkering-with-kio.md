title: GSoC Update: Tinkering with KIO
date: 2016-07-21 15:18
author: Arnav Dhamija
tags: GSoC, KDE
category: Article
slug: gsoc-update-tinkering-with-kio
sidebarimage: images/code.png

I'm a lot closer to finishing the project now. Thanks to some great support
from my GSoC mentor, my project has turned out better than what I had written
about in my proposal! Working together, we've made a lot of changes to the
project.  

For starters, we've changed the name of the ioslave from "File Tray" to
"staging" to "stash". I wasn't a big fan of the name change, but I see the
utility in shaving off a couple of characters in the name of what I hope will
be a widely used feature.  

Secondly, the ioslave is now completely independent from Dolphin, or any KIO
application for that matter. This means it works _exactly_ the same way across
the entire suite of KIO apps. Given that at one point we were planning to make
the ioslave fully functional only with Dolphin, this is a major plus point for
the project.  

Next, the backend for storing stashed files and folders has undergone a
complete overhaul. The first iteration of the project stored files and folders
by saving the URLs of stashed items in a QList in a custom "stash" daemon
running on top of kded5. Although this was a neat little solution which worked
well for most intents and purposes, it had some disadvantages. For one, you
couldn't delete and move files around on the ioslave without affecting the
source because they were all linked to their original directories. Moreover,
with the way 'mkdir' works in KIO, this solution would never work without each
application being specially configured to use the ioslave which would entail a
lot of groundwork laying out QDBus calls to the stash daemon. With these
problems looming large, somewhere around the midterm evaluation week, I got a
message from my mentor about ramping up the project using a "StashFileSystem",
a virtual file system in Qt that he had written just for this project.  

The virtual file system is a clever way to approach this - as it solved both
of the problems with the previous approach right off the bat - mkdir could be
mapped to virtual directory and now making volatile edits to folders is
possible without touching the source directory. It did have its drawbacks too - as it needed to stage every file in the source directory, it would require a
lot more memory than the previous approach. Plus, it would still be at the
whims of kded5 if a contained process went bad and crashed the daemon.  

Nevertheless, the benefits in this case far outweighed the potential cons and
I got to implementing it in my ioslave and stash daemon. Using this virtual
file system also meant remapping all the SlaveBase functions to corresponding
calls to the stash daemon which was a complete rewrite of my code. For
instance, my GitHub log for the week of implementing the virtual file system
showed a sombre 449++/419--. This isn't to say it wasn't productive though -
to my surprise the virtual file system actually worked better than I hoped it
would! Memory utilisation is low at a nominal ~300 bytes per stashed file and
the performance in my manual testing has been looking pretty good.  

With the ioslave and other modules of the application largely completed, the
current phase of the project involves integrating the feature neatly with
Dolphin and for writing a couple of unit tests along the way. I'm looking
forward to a good finish with this project.  

You can find the source for it here: <https://github.com/KDE/kio-stash> (did I
mention it's now hosted on a [KDE repo](https://quickgit.kde.org/?p=kio-
stash.git)? ;) )
