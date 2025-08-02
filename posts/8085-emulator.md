---
id: tag:blogger.com,1999:blog-27384460.post-114664248494104984
title: "8085 Emulator"
date: 2006-05-03
author: brainless
---

The College project : An 8085 Microprocessor Kit Emulator  

The project, done in C++ tries to emulate the functions of an 8085 emulator ditto as a hardware trainer kit would work. The purpose is to create a software based 8085 Trainer Kit which looks and works similar. So this one does not have buttons like [ADI] or [MVI]. Instead it is all HEX code stuff buttons and the buttons for Rst (Reset), Set, Ins(Insert)... etc. as one would find in a hardware based 8085 trainer kit.  

The project isnt yet fully complete. The sources are available here :  

[defines.h](http://sumit.pixlie.com/8085_emu/defines_h.html)  

[interpreter.h](http://sumit.pixlie.com/8085_emu/interpret_h.html)  

[interpreter.cpp](http://sumit.pixlie.com/8085_emu/interpret_cpp.html)  

[memory.h](http://sumit.pixlie.com/8085_emu/memory_h.html)  

[memory.cpp](http://sumit.pixlie.com/8085_emu/memory_cpp.html)  

[main.cpp](http://sumit.pixlie.com/8085_emu/main_cpp.html)  

All sources available under [GNU GPL](http://www.gnu.org/licenses/gpl.html)  

This project uses the Irrlicht library for UI : [Irrlicht](http://irrlicht.sourceforge.net/)  

Update (4th May 1:42 AM IST) : At last the code works. It compiles without errors and I have tested with some very simple assembly code. It works ! But some more work needs to be done...  

An archive of all files : [here](http://sumit.pixlie.com/8085_emu/8085_emu.rar)