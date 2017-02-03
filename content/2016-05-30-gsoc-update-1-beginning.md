title: GSoC Update 1: The Beginning
date: 2016-05-30 10:37
author: Arnav Dhamija
tags: GSoC, Programming, KDE
category: Article
slug: gsoc-update-1-beginning
sidebarimage: ../images/code.png

I have officially started my [GSoC
project](https://summerofcode.withgoogle.com/projects/#5979393230897152) under
the mentorship of [Boudhayan Gupta ](https://blog.baloneygeek.com/)and [Pinak
Ahuja](http://blog.pinak.me/).  

The project idea's implementation has undergone some changes from what I
proposed. While the essence of the project is the same, it will now no longer
be dependent on Baloo and xattr. Instead, it will use a QList to hold a list
of staged files with a plugin to kiod. My next milestone before the mid-term
evaluation is to implement this in a KIO slave which will be compatible with
the whole suite of KDE applications.  

For the last two weeks, I've been busy with going through hundreds of lines of
source code to understand the concept of a KIO slave. The KIO API is a very
neat feature of KDE - it provides a single, consistent way to access remote
and local filesystems. This is further expanded to KIO slaves which are
programs based on the KIO API which allow for a filesystem to be expressed in
a particular way. For instance, there is a KIO slave for displaying xattr file
[tags](http://vhanda.in/blog/2014/07/tagging-your-files/) as a directory under
which each file marked to a tag would be displayed. KIO slaves even expand to
network protocols allowing for remote access using slaves such as http:/,
ftp:/, smb:/ (for Windows samba shares), fish:/, sftp:/, nfs:/, and webdav:/.
My project requires virtual folder constructed of URLs stored in a QList - an
ideal fit for KIO slaves.  

However, hacking on KIO slaves was not exactly straightforward. Prior to my
GSoC selection, I had no idea on how to edit CMakeLists.txt files and it was a
task to learn to make one by hand. Initially, it felt like installing the
dependencies for building KIO slaves would almost certainly lead to me
destroying my KDE installation, and sure enough, I did manage to ruin my
installation. Most annoying. Fortunately, I managed to recover my data and
with a fresh install of Kubuntu 16.04 with all the required KDE packages, I
got back to working on getting the technical equivalent of a Hello World to
work with a KIO slave.  

This too, was more than a matter of just copying and pasting lines of code
from the [KDE tutorial](https://techbase.kde.org/Development/Tutorials/KIO_Sla
ves/Hello_World). KIO slaves had dropped the use of .protocol files in the KF5
transition, instead opting for JSON files to store the properties of the KIO
slave. Thankfully, I had the assistance of the legendary [David
Faure](https://behindkde.org/david-faure-2). Under his guidance, I managed to
port the KIO slave in the tutorial to a KF5 compatible KIO slave and after a
full week of frustration of dealing with dependency hell, I saw the best Hello
World I could ever hope for:  


![]({filename}/images/kioslave.png)


Baby steps. The next step was to make the KIO slave capable of displaying the
contents of a specified QUrl in a file manager. The documentation for
KProtocolManager made it seem like a pretty straightforward task - apparently
that all I needed to do was to add a "listing" entry in my JSON protocol file
and I would have to re-implement the listDir method inherited from SlaveBase
using a call to SlaveBase::listDir(&QUrl). Unbeknownst to me, the SlaveBase
class actually didn't have any code for displaying a directory! The SlaveBase
class was only for reimplementing its member functions in a derived class as I
found out by going through the source code of the core of kio/core. Learning
from my mistake here I switched to using a ForwardingSlaveBase class for my
KIO slave which instantly solved my problems of displaying a directory.  


![]({filename}/images/helloslave.png)

_Fistpump_


According to my timeline, the next steps in the project are  

  1. Finishing off the KIO slave by the end of this month
  2. Making GUI modifications in Dolphin to accommodate the staging area
  3. Thinking of a better name for this feature?
So far, it's been a great experience to get so much support from the KDE
community. Here's to another two and a half months of KDE development!
