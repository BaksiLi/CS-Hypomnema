CS-Hypomnema: Computer Science Notes Collection
---
[![Licence: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

Note-taker: [Baksi](https://github.com/BaksiLi)   

This repository curates divers computer science notes, whereas its scope is bounded by my own interests, and it will keep updating as limited knowledge will never suffice. 

If you are looking for a structured CS course, you should probably go for a programme offered by accredited organisations. 
However, I will advice some courses/books for the subjects that are not covered but important.

Anyone is more than welcomed to give suggestions, or even raise a PR.   

Lastly, please feel free to **star this repository** if you found it interesting or boring (yeah, p ∨ ¬p).    

# Catalogue
According to [Curriculum Guidelines for Undergraduate Programs in Computer Science](https://dl.acm.org/citation.cfm?id=2534860) (p. 14) by ACM and IEEE Computer Society, there are eighteen knowledge areas (KA) that consist the body of knowledge, which are used to **label notes in this collection** for reference. 

<details>
<summary>Keyword Table</summary>

| Code |           Knowledge Area           |     |               (continued)               |
|:----:|:----------------------------------:|:---:|:---------------------------------------:|
|  AL  | Algorithms and Complexity          |  OS | Operating Systems                       |
|  AR  | Architecture and Organization      | PBD | Platform-base Development               |
|  CN  | Computational Science              |  PD | Parallel and Distributed Computing      |
|  DS  | Discrete Structures                |  PL | Programming Languages                   |
|  GV  | Graphics and Visualization         | SDF | Software Development Fundamentals       |
|  HCI | Human Computer Interaction         |  SE | Software Engineering                    |
|  IAS | Information Assurance and Security |  SF | Systems Fundamentals                    |
|  IM  | Information Management             |  SP | Social Issues and Professional Practice |
|  NC  | Networking and Communication       |     |                                         |

</details>

[About learning](https://github.com/BaksiLi/CS-Hypomnema/tree/master/Statement.md) gives more details on the structure of knowledge.

## I. Introductions

1. [***Introduction to Computer Science***](https://github.com/BaksiLi/CS-Hypomnema/tree/master/Resources/General/IntroToCS.md) ![Editing](https://img.shields.io/badge/status-revising-lightgreen.svg)   
	Note based on CS50x 2017 course, the content and structure is somewhat different from the [official syllables](http://docs.cs50.net/2017/x/syllabus.html).	It covers the basics of C, Python, Web Programming content like Javascript, HTML and CSS, as well as some important concepts in computer science like Computational Complexity.
<!-- Keywords: `C`, `Python`, `JavaScript`, `HTML/CSS`,`SQL`, `basic data structures` and `algorithms` et.c. -->

1. ***Introduction to Web Development*** ![Pending](https://img.shields.io/badge/status-Pending-orange.svg)    
	Note based on CS50w course structure. It covers Git, HTML/CSS, JavaScript, Web Frameworks like Flask, Django et.c.

1. ***Zsh (Z shell) Development with Comparison to Bash*** ![Pending](https://img.shields.io/badge/status-Pending-orange.svg)   
	This is a *Learn X in Y minutes*-styled tutorial of  Zsh development. It act as a fast introduction for programmers, esp. those who have knowledge about Bash.
	
<!-- 1. Philosophy of Information -->
<!-- 1. Network -->

## II. Algorithmics
[//]: # (I am also planning to sort out a more detailed general Algorithm note from my previous notes.)   
For reading materials, [*Algorithms*](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) by S. Dasgupta et al is a good and concise book recommended by UC San Diego courses; 
[*Introduction to Algorithms*](https://www.amazon.co.uk/Introduction-Algorithms-Thomas-H-Cormen/dp/0262033844/) by T. H. Cormen recommended by MIT courses is quite detailed in proofs ([solutions](https://github.com/gzc/CLRS) of the exercises also available). \*   
There are also many open-source collections of algorithm implementations, which are useful during study, e.g. in [Python](https://github.com/TheAlgorithms/Python) and [Java](https://github.com/TheAlgorithms/Java).   
In addition, for visualizations there is [Data Structure Visualizations](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html).   

1. [***Graph Theory and Algorithms (with Python)***](https://github.com/BaksiLi/CS-Hypomnema/tree/master/Resources/Algorithm/Graph/GraphAlgorithm.md) ![Editing](https://img.shields.io/badge/status-revising-lightgreen.svg)   
<sub>This note is uploaded but still upon editing for mathematical details.</sub>   
	A summary note from [NET04x](https://www.imt-atlantique.fr/fr/formation/moocs-et-cours-ouverts/moocs/advanced-algorithmics-and-graph-theory-python) (IMTx) and [ALGS202x](https://www.edx.org/course/graph-algorithms-uc-san-diegox-algs202x) (UCSanDiegoX) with a nicely balanced theoretical and practical content. In the end, an example on applying combinatorial game theory to win a game described by graph is provided.    
	For anyone who wishes to go deeper in the computational theory (esp. after studied Chapter IV), reading of *Complexity and NP-Complete Problems* is highly recommended.

1. ***Complexity and NP-Complete Problems*** ![Pending](https://img.shields.io/badge/status-Pending-orange.svg)   
	A note from [ALGS203x](https://www.edx.org/course/np-complete-problems-uc-san-diegox-algs203x) (UCSanDiegoX). It covers NP-completeness, approximate algorithms and algorithm analysis.

\* <sub>Although I have never finished reading any one of them :(</sub>  

## III. Maths & Stats
Mathematics prerequisites covered by [Mathematics for Computer Science](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-spring-2015/index.htm) (MIT).

1. ***Coding theory (with Python)*** ![Pending](https://img.shields.io/badge/status-Pending-orange.svg)   
	This is a coding theory text (thanks to Prof. PPM) with Python implementations. Not ready to upload so far.

## IV. Scientific Computing
### i. Mathematica (Wolfram Language)
1. [***Learn Mathematica by Example***](https://github.com/BaksiLi/Wolflang-Workshops/blob/master/resources/myNote.nb) ![Editing](https://img.shields.io/badge/status-revising-lightgreen.svg)   
	I wrote this notebook alongside with learning. The official tutorial, [*Fast Introduction for math students*](http://www.wolfram.com/language/fast-introduction-for-math-students/en/) is a good source of reference as well.
1. [***WolfLang Workshops***](https://github.com/BaksiLi/Wolflang-Workshops) ![Editing](https://img.shields.io/badge/status-updating-lightgreen.svg)      
	This is a collection of notebooks, each has its own topic. 
	For more inspiring notebooks, cf. [Notebook Archive](https://www.notebookarchive.org) by Wolfram Foundation.
	
	<details>
	<summary>Workshop Lists</summary>
	
	1. [Country flags colour analysis](https://github.com/BaksiLi/Wolflang-Workshops/blob/master/resources/AnalyzeFlagColours.nb): An analysis on the dominant colours of the country flags around the world.
	1. [Impaint: Remove texts from Images](): This workshop starts from a simple usage – removing texts or any unwanted elements from an image – and therefore introduces *Impaint* function in Wolflang.
	1. [Amateur sleuthing of NK nuclear tests](https://github.com/BaksiLi/Wolflang-Workshops/blob/master/resources/NorthKoreaSleuthing.nb): Note from Stephen Wolfram's live stream chat. I have added some parts into it as well.
	
	</details>
	
[//]: # (### ii. Machine Learning Specification)
## V. Quantum Computing
For reading materials, [Quantum Computation and Quantum Information (Cambridge, 2010)](https://books.google.co.uk/books?id=-s4DEy7o-a0C) is the choice, though a bit dated, it is a classical reference for stepping into the field.

1. ***D-Wave machine Introduction*** ![Pending](https://img.shields.io/badge/status-Pending-orange.svg)   
	This was part of my undergraduate thesis topic. The code is available now, see [here](https://github.com/BaksiLi/CS-Hypomnema/blob/master/Resources/Quantum/D-Wave/mapcl.py).   
	
<!-- As I've been studied about Quantum technologies for so long, and early notes are hand-written, the note in this part may lack of detail for fundamental stuffs. Another book (I know from my uni course) [Introduction to Quantum Information Science (Oxford, 2006)]() -->

# Acknowledgement
Unless otherwise specified, the repository CS-Hypomnema and its contents are Copyright [BaksiLi](https://github.com/BaksiLi), and are licenced under the Creative Commons [BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/) (*Attribution-NonCommercial-ShareAlike 4.0 International*) Licence. 

<sub>I used *Byword* (with Standard Markdown Syntax) for taking notes. However, it might encounter problems of compilation on GitHub, *esp.* with LaTeX. I will try to tackle this in the future. </sub>

Copyright (c) 2019 BaksiLi
