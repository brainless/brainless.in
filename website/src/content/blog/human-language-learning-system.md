---
id: tag:blogger.com,1999:blog-27384460.post-114753832212899050
title: "Human Language Learning System"
pubDate: 2006-05-13
author: Sumit Datta
---

Its Exam time going on now... so cant think much :P But for few days two different ideas have been making rounds in my brain(ahh brainless has a brain o.O). The first one involves a different approach to UI of information kiosk type sites. I will discuss this one later with some examples.  

But the second one seems more interesting to me. It comes from my direct need or wish to learn many global (human) languages other than English. I have never come across a community based language learning system, even though the community has been able to create and maintain such beautiful efforts like Wikipedia. I believe the reason is partly the absense of such a system. Here I will try to express my thoughts, which are just the surface of the system. I want more people to think so we have a real practical solution which can be easily implemented.  

Learning human languages I hope is something liked by most people and it is important too. To learn a language easily we need some reference of the target (the language which we are going to learn) and some other language we already know. For example if I want to learn Spanish the easiest way would be for someone to start some simple verbal explanation or introduction to the language. This aided with visual examples like the written words of pictures of the object being described is very helpful. This case is very easy to do in real life or maybe over special direct audio/visual communication system. What could be a good solution is a right mixture of existing open protocols which enable text, audio, image and video transmission on internet and an application to present it all in the required manner. If all this seems a bit confusing then read the following example:  

I want to learn Spanish. Assume that I find a person, say Jack who knows both English and Spanish and is willing to teach me. The general way is to introduce me to the alpahbet and to smaller words (with their respective English meanings). Starting with "A for Apple" thing is better when the picture of Apple is there (Apple maybe known to most people in the world, but there maybe other unknown things). The addition of voice in the background is needed.  

Then we to some grammer stuff where it is about more explanation using voice and text. Next Jack could start showing be smaller paragraphs of text and read them out so that I can practice reading in my mind. This would help with the ability to underline the word (or words block) he is reading currently in a 10 line text. It will help me to keep track of the word he is currently speaking (as in some karaoke stuff I have seen).  

This is the basing process. Now the following just brings out the important points in this system:
* Text in target language and also support text in the known language is written by the author (a teacher for example). Text can be rendered to image, if there are issues with fonts. Jack simply types text in the application as a slide-by-slide basis (as in a presentation).
* Thus a "Slide" becomes a basic block of the system. A slide can contain text, image, audio, video. The slide can be well described in terms of the items (text, image, etc.) it contains. Image, audio and video can be encoded using formats like png, vorbis, theora respectively or other better open formats that I dont know of. The slide itself is basically xml tags which describe what items it contains.
* A number of slides make up a "Presentation". The presentation is an xml file. Simple :)
* The items needed within the slides are simply "linked" by URL to the actual (image, audio, etc.) files.
* The xml does contain the text though which is supposed to be displayed.

I am not going into the details of tags for xml file etc. But I will give an example of what Jack and I should find once such a system exists.  

First lets see how Jack does his work:
* An application exists which allows Jack to create new slide and add text to each slide.
* On the first slide he types the Spanish equivalent of "A" and records his voice for the alpahbet. Also he may record a reference audio "Pronounced as in ..." or something else which helps in the learning process. In this slide the text is too simple and doesnt need an underline.
* Images can be linked in each slide as they are linked in html. Ofcourse he may create his own image or link image from a public server.
* Jack continues to process until he completes the full alphabet and that is thinks is enough for the presentation "Introduction to Spanish". Nice work Jack.

The presentation file along with the image or audio can be either be in separate files available through HTTP or similar, or in a single compressed file. The presentation xml file must have a certain name. The item files (image, audio, etc) if present in the compressed file are fetched from that file itself with the option to checkout the online URL for updated content. It is not compulsory that all the item files remain in the compressed file, in which case the URL is used to simply fetch them.  

Now one fine morning I want to learn Spanish (atleast try ...). I simply search the well known spanish-pedia or something and get hold of Jacks "Introduction to Spanish". I download the full compressed file or simply click on the presentation xml. A browser plugin downloads the required items and I start learning... hurray... I know the Spanish alphabet.  

Jack starts working on his second part of the series. He types few short paraghaphs which make good use of the alphabet. Here he adds underlines to text. He could do that in the following way:
* Type out the full paragraph of a slide.
* After typing is done select a word or few words (maybe a sentence) and do a "ctrl+U" or something similar. Also with the selected text: speak and record the words/sentence as they should be pronounced.
* The application keeps track of the time sequence for each underlined segment and its audio. This can simply be expressed in the xml itself as timestamps.

In a similar fashion Jack completes the presentation and as earlier I use it to learn more Spanish.  

Thats all for now... keep thinking. Discuss and comment your thoughts. Cheers!