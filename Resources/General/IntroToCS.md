<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
Introduction to Computer Science  
---  
# Content

- [Introduction](#intro)  
- [Main](#main)    
	1. [I: Programming](#w0)
	1. [II: C Language Fundamentals](#w1)
	1. [III: Arrays](w2)
	1. [IV: Algorithms](w3)
	1. [V: Memory](w4)
	1. [VI: Data Structures](w5)
	1. [VII: Web and Internet](w6)
	1. [IIX: Python](w8)
	1. [IX: SQL](w9)
	1. [X: JavaScript](w10)
	1. [Final Project](final)
- [Future Study](#future)

---
# Introduction
Note-taker: [Baksi](https://github.com/BaksiLi)  
This article is written based on the note of CS50x 2017 of Harvard University, lectured by <a mailto="malan@havard.edu">David J. Malan</a>. The content and structure may be slightly different from the [official syllables](http://docs.cs50.net/2017/x/syllabus.html) since I have restructured and filled it with new materials. Nevertheless, all the knowledge are covered and extended beyond their scope. The original course video and other supporting materials could be found in the [seminar page](http://cs50.tv/2017/fall/#about,lectures), or in their channel [cs50 live](https://www.youtube.com/user/cs50tv/).
 
# Main
## I. Programming [w0]
### Scratch
 [Scratch](www.scratch.mit.edu) is a visual toolkit for amatures to learn and grab an idea of *programming*. <img src="http://www.quarrylane.org/uploaded/Summer/images/ScratchBlogLogo.jpg" alt = "Scratch logo" width = "330" />
### How programme works?  
- **Computers** are information processing automata; they are dumb machines in the sense that they do *only* what user instructed, but at the same time very clever if the people behind are intellegent.
- A computer **programme** is a collection of instructions to achieve specific tasks. It is a liminal artefact, since instructions are abstract but the operations are done in the physical world. **Binaries** corresponed directly to specific instructions. Tasks are approached by **Algorithms**.  
- **Assembly Language** enabled the programmers to use symbolics instead of binaries, but it is symbol-to-operation therefore low-level and not portable. 
- **Higher-level Language** are designed, *FORTRAN* (FORmula TRANslation) language is the first. They requires **compilers** for translating programme statements into machine instructions. **Operating System** channeled all input and output (i.e. I/O) operations.
### Relavent readings at the stage
- How Computers Work, Tenth Edition
Ron White
Que Publishing, 2014
ISBN 0-7897-4984-X
- *Code: The Hidden Language of Computer Hardware and Software*, First Edition
Charles Petzold
Microsoft Press, 2000
ISBN 0-735-61131-9
- *Programming in C*, Fourth Edition
Stephen G. Kochan
Pearson Education, 2015
ISBN 0-321-77641-0
- *Hacker’s Delight*, Second Edition
Henry S. Warren Jr.
Pearson Education, 2013
ISBN 0-321-84268-5

## II. C Language Basics [w1]
### Environment
#### CS50 IDE
- Environment: Cloud [IDE](https://ide.cs50.io/) platform, [CS50.h Reference](https://reference.cs50.net/math/modf). The library is available at GitHub, *cf.* [libcs50](https://github.com/cs50/libcs50).
- Debugging in IDE: `eprintf`, ` help50` and `debug50`.
#### In situ
- Editors: [Vim](https://en.wikipedia.org/wiki/Vim_(text_editor)) or [Elipse](https://en.wikipedia.org/wiki/Eclipse_(software)) for Hardcore players. The presenter uses [Atom](https://atom.io/).
- IDEs are good and easy to install. 
	- C: MacOS users can (sometimes must) install [Xcode](https://developer.apple.com/xcode/); for cross-flatform [Visual Studio Code](https://code.visualstudio.com/).
	- Python: [Anaconda](https://www.anaconda.com/distribution/) (with its Spyder) is the default choice for data scientists, while [PyCharm](https://www.jetbrains.com/pycharm/) is more compatible with other uses. However, in early 2019 Anaconda and JetBrains announced that they will [join forces to launch 'PyCharm for Anaconda'](https://www.businesswire.com/news/home/20190404005205/en/Anaconda-JetBrains-Join-Forces-Launch-%E2%80%98PyCharm-Anaconda%E2%80%99), so no more troubles in the future.
### C language
- Introduction to *C* language and basic *Bash* instructions
- Good coding style is important. [CS50 style guide of C](https://manual.cs50.net/style)
### [Problem set #1](https://docs.cs50.net/2017/x/psets/1/pset1.html)
- Hello World  
- Functions  
- IO & Loop  

## III. Arrays [w2]
### Array structure
- String: it turns out that underneath the hood, strings are a little more mundane - **grid of information**, sometimes known as bucket. Lee takes those contiguous block of memory "- L - e - e - \0 -" in RAM.  
	`int main(int argc, string argv[])`  
### Python
- Recursion in Python: functions can call themselves. For example:
	<details>

	``` python
	def factorial(n):
		if  n == 1:  # base case
			return 1
		return n * factorial(n - 1)
	```
	
	</details>
cf. [Recursion Factorial](https://www.cs.usfca.edu/~galles/visualization/RecFact.html) visualization.
- Object-Oriented Programming features in Python: paradigm based on object. For example:
	<details>

	```python
	class Coordinates:
		def __init__(self, x, y):
			self.x = x
			self.y = y
		
		def shift(self, x, y):
			self.x += x
			self.y += y
			
	p = Coordinates(1, 2)
	p.shift(1, 1)
	print('x = {}, y = {}'.format(p.x, p.y))
	```

	</details>
### [Problem set #2](https://docs.cs50.net/2017/x/psets/2/pset2.html)
- Caesar Cipher
- Vigenere Cipher
- [Crack Cytology question](https://docs.cs50.net/problems/crack/crack.html)

## IV. Algorithms [w3]
**Algorithm** is the method for problem solving, involves a finite series of steps. "In computing practice the algorithm denotes the expression on paper of the proposed computing process (often by means of a flowchart) prior to the preparation of the programme. If no algorithms is possible a heuristic solution has to be sought {in which it involves trial and error, as in iteration.}."

### Addressing a Computational Problem   
- Formulation:  express the problem formally
- Specification: find the algorithm
- Implementation: coding

### Computational complexity
- In terms of the growth rate (# of operations against input size $n$), functions are ordered:
> Logarithmic $log(n)$, Linear $an + b$, Quadratic $an^2 + bn + c$, Polynomial $an^z + \dots + an^1 + an^0\text{ with constant }z$, Exponential $a^n\text{ with constant }a$, Factorial $n!$
- **Asymptotic complexity** measures the effieciency. Its notations is to indicate the running time of a give algorithm, which takes the behaviour with increasing input size into account. 
	- $O$, a.k.a. asymptotic upper bound -> worst-case scenario.
	- $\Omega$, a.k.a. asymptotic lower bound -> best-case scenario.
	- $\Theta$ notes when $\Omega = O$, known as the asymptotically tight bound.
- Constants and low-order terms are droped, which means two algorithms may have the same $O$ even though one is always faster than the other. Ordered:
> $log(n)\leq n\leq n^2\leq n^z\leq a^n\approx n!$

![Complexity illustration, $z=3$. © Author.](resources/complexity.png)

- Further in algorithm and computational complexity theory, cf. *Graph Theory and Algorithms (with Python)* note.

[#]: (MARKER)
### Search and Sort
1. Search (in a sorted list)
	- Linear: Search linearly, i.e. if asking to guess a number in the range of 100, then $O(n)$.  
	- Binary (Divide & Conquer Algorithm): $O(log_2 n)$.  
		<details>
	
		```python
		def binary_search(list, n):	
			low = 0
			high = len(list) - 1
			while low <= high:
				mid = (low + high) / 2
				guess = list[mid]
				if guess == n:
					return mid
				if guess > n:
					high = mid - 1
				else:
					high  = mod + 1
			return None
		```
		
		</details>
1. Sorting  
	1. **Counting sort**: Time Complexity: O(n+k) where n is the number of elements in input array and k is the range of input.
	1. **Selection sort** gets slower&slower through time because the whole list is scanned everytime.  $\Omega(n^2)$ ok 
 `for i from 0 from n-1: find smallest between i'th and n-1'th: swap smallest with i'th ` 
		<details>
	
 		```python
 		def findsmallest(arr):
 			smallest = arr[0]
 			smallest_index = 0
 			for i in range(1, range(arr)):
 				if arr[i] < smallest:
 					smallest = arr[i]
 					smallest_index = i
 			return smallest_index
 			
 		def selection_sort(arr):
 			arr_new = []
 			for i in range(len(arr)):
 				smallest = findsmaillest(arr)
 				arr_new.append(arr.pop(smallest))
 			return arr_new
 		```
		
		</details>
	1. **Bubble sort** that swap only consecutive pairwises every time.
 `repeat until no swaps: for i from 0 to n-2: if i'th and i+1'th elements out of order: swap them`  
Upper boundary $(n-1) + (n-2) + ... + 1 \\ = \frac{n(n-1)}{2} = O(n^2)$  ; Lower boundary $\Omega$ = n
	1.  **Insertion sort**(Counting sort)
`for i from 1 to n-1: call 0'th throgh i-1'th elements the sorted side: remove i'th element: insert into sorted side in order `  
	1. **Merge sort**
`On input of n elements: if n<2: return; else: sort left half of elements; sort right half of elements; merge sorted halves `  → $T(n) = T(\frac{n}{2}) + T(\frac{n}{2}) + O(n) \\ \stackrel{\text{if n \geq 2}}{=} O(nlogn)$  

	<details>
	
	```C
	int sigma(int m){
		int sum = 0;
		for(int i = 1; i <= n; i++){
			sum += i;
		}
	 }
	 ```
	 *aut pro*:  
	 ```C
	 int sigma(int m){
	 	if(m <= 0){
	 		return 0;
	 	}else{
	 		return (m + sigma(m - 1));
	 	}
	 }
	 ```
	 in a **Reflexive** or **inductive** or **recursive** calls (use the defination again & again) fashion.
	 
	 </details>
	 
1. [Problem set #3](https://docs.cs50.net/2017/x/psets/3/pset3.html)  
 <input type="checkbox" name="pset3" checked='True'> Status <br/>
	- Find, either less or more comfortable: (latter one is chosen)
		- how to **configurate a compiler**
		- how to **write programme in multiple files**
	- Implement Game of Fifteen  

## V. Memory [w4]
1. Underneath the hood: **RAM**
	Same "incantation of strings" are different, in the sense of memory. Why?
	Notice that if you run a programme in terminal, your computer would give that programme the illusion of a really big chunk of memory all on its own. When main is called, main is given a stack space.	... [sloppily drawn]  
	A string is technically just the address of a character in memory (the first byte of your 'string' array, ends with '\0').   Therefore when two individually defined strings are compared, they are different since their address are different. It is just an address, AKA a **pointer**.  
	A string is a synonym for a data type called `char *`, `strcmp()` can compare two strings from their pointers. 
	
	 [//]: # (He who wonderfully sat down with me at  office hours one day in the dining hall, trying to help me understand pointers because it was just so much more technical than the other stuffs. This is among those topics that might take a little bit of time to sink in, but it does. and when it does, it really is that proverbial light bulb that goes off. and for me that light bulb went off right then and there.) 
	`malloc()` tells computer to give a block of memory of sizeof(xx), and return it to main().  
1. Pointer arithmetic  
syntatic sugar `s[i]` is just `*(s+i)`   
[output is atrocious, pretty verbose] `valgrind` to check **memory leak**. `free()` .  stack overflow/ heap overflow/ buffer overflow.  

	|:-:|:-:|:-:|
	 | Arrary | Linked list
	Read | O(1) | O(n)
	Insert |  O(n) | O(1)
	Remove | O(n) | O(1)
1. file structures
	- Picture:
		- BMP(Bit map): see [Bitmaps & Palette Manipulation](http://www.brackeen.com/vga/bitmaps.html).
		![Grid of pixels](resources/bpm.jpg)
		hex editor: ` xxd -c 24 -g 3 -s 54 smiley.bmp `. `-s 54` stead for starting from adress 00000036 which is 54 in hexadecimal since 14 + 40 = 54 lines (bytes) the metadate of a 24-bit BMP has. Further descriptions -> [this](https://docs.cs50.net/problems/whodunit/whodunit.html#background)  
		In c there is *struct* can be defined.  RGB colour.
		- JPEG image:  
![beginning of JPEG](resources/jpg.png)
Incidentally, HTML and CSS (languages in which webpages can be written) model colors in this same way. If curious, see http://en.wikipedia.org/wiki/Web_colors for more details.
	- CSV (Comma separated)
### [Problem set #4](https://docs.cs50.net/2017/x/psets/4/pset4.html): Forensics  
<input type="checkbox" name="pset3" checked="True"> Status <br/>
	- [Whodunit](https://docs.cs50.net/problems/whodunit/whodunit.html#background): restore a forensic image by switching certain pixels into other colours. To be familiar with the structure of 24-bit uncompressed BMPs.  
	- Resize  NTBC;  
	- [Recover](https://docs.cs50.net/problems/recover/recover.html)  

## VI. Data Structures [w5]
1. Data structure allows more flexible running, memory are allocated dynamically, rather than using remalloc(), free() and so frequently.  
	- **Node** type is essential.  

	|:-:|
	n|
	*next|  

	*ut idem pro*:
	
	 ```C
	typedef struct node{
		int n; 
		struct node *next;
	} 
	node; 
	```
	
1. Consider a **collection of nodes** that are linked together by pointers. The starting pointer and the ending null. In order to achive the function of *insert*, *remove* and *search*.   
The running time of search  would always be O(n) since the only way of searching is just linear. code as below:

	```C
	bool search(int n, node *list){
		node *ptr = list;
		while (ptr != NULL){
		// access n inside node addressed by ptr
			if (ptr->n == n){
				return true;
			}
			ptr = ptr->next;
		}
		return false;
	}
	``` 
	
	- **Stack** type: Push and Pop (?LIFO data structure)  

	```C
	typedef struct stack{
		int *numbers;  // numbers[CAPACITY]
		int size;
	}
	stack;
	``` 
	
	- **Queue** type: enqueue and dequeue   

	```C
	typedef struct queue{
		int front;
		int *numbers;  // numbers[CAPACITY]
		int size;
	}
	queue;
	``` 
	
	- **Tree** type: <!--58:00-->
![tree](resources/tree.png)
	*Binary search tree*, left smaller right greater. *aut idem pro*:  
		 
	```C
	typedef struc node{
	int n;
	struct node *left;
		struct node *right;
	}
	node;
	``` 
	therefore searching fuction:
	```C
	bool search(int n, node *tree){
		if (tree == NULL)
		{
			return false;
		}
		else if (n < tree->n)
		{
			return seach(n, tree->left);
		}
		else if (n > tree->n)
		{
			return seach(n, tree->right);
		}
		else
		{
			return true;
		}
	}
	 ``` 
	but for the case of text, this is not that practical -> **Huffman coding**.
	![huffman tree](resources/huffman.png)
	Compression certainly has a lower limit, relavent to *information entropy*.  
	
	```C
	typedef struc node
	{
		char symbol;
		float frequency;
		struct node *left;
		struct node *right;
	}
	node;
	``` 	
	
	- **Hash tables**: Linear probing, or dynamically extended linked lists.  
	- **Trie** type, widely used as spelling checker model (dictionary!).  
	- **Min Heap** used in Graph Algorithms.
1. [Problem set #5](https://docs.cs50.net/2017/x/psets/5/pset5.html): Mispellings  
<input type="checkbox" name="pset3" checked="True"> Status <br/>
	- [Speller](https://docs.cs50.net/problems/speller/speller.html): `submit50 cs50/2017/x/speller`  
	- Understand [C compiler](https://docs.cs50.net/problems/speller/speller.html#code-makefile-code)
	- the [form](https://forms.cs50.net/2017/x/psets/5)   

## VII. Web and Internet [w6]
 [//]: # (Waited to be reviewed after refered to a book.)  
1. Internet models. 
	- A central **protocal** is used to assign certain settings to all the devices, so called **router**. It is a typical example, and a special type of software called **DHCP** (Dynamic Host Configuration Protocal). 
	- At the first time a device is connected, a unique identifier, is given to it. **IP adress**, **Ether & Inet**.  
	- **DNS** helps the conversion between numerical address into more human-friendly host names, or fully qualified domain names (& thankfully no more mnemonics). Look up server address by cmd `nslookup xxxx`.  
	- **Routers** globally system. Trace the route one query at a time to somewhere. `traceroute -q 1 xxxx`. 
	- **Packet** leverage a feature of IP and its sister protocol(s) **TCP**(and others like **UDP** that often used for live streaming). The former fragment the info, and the TCP associates and guarantee fragments.  
	- **Port** number.  
	- **Firewall** and **VPN**.  
		- curl ifconfig.me, open a specific port: sudo pfctl -vnf /etc/pf.conf
		- show who is using lsof -i:8000 [open port](http://blog.csdn.net/human8848/article/details/52268337)
	- To conclude: xx  

1. **HTTP**(Hyper Text Transmitting Protocol): "Handshake agreement", contents are written in **HTML**(Hyper Text Markup Language). <!-- Succint -->  
	- **Status code**(Table).
	- `telnet sss.harvard.edu 80`. N.B. telnet and ftp are no longer available due to some "insecure" reason (or due to 32bit) on macOS 10.13, so nc, ssh and stfp is used instead. `curl -I ` just for header.  
1. **CSS**  

[//]: # (Week 7: Machine Learning. This section is removed to another note, acting as an introduction.)

## VII. Week 8: Python [w8] 
1. The meaning of object type, value, and identity. Depending on the type of the object, it could be either immutable (*e.g.*, strings and tuples) or mutable (*e.g.*, dictionaries and lists). Methods are functions associated with objects, whereas data attributes are data associated with objects.   
	Polymorphism to operators   
	Typing or assigning data types feres to the set of rules that the language uses to ensure that the part of the program receiveing the data knows how to correctly interpret that data. Some langaguages are **statically typed**, like C/C++; whilst other languages are **dynamically typed**, like Python. Static typing means that type checking is perfoormed during compile time, whereas dynamic typing means that type checking is performed at run time. 
	Therefore for an immutable object, like an int, Python creates a new object when operation is done; otherwise for a mutable object, it changes only the value at the address.   
	
	``` 
	>>> N1 = 3
	>>> N2 = N1
	>>> N2 += 1
	>>> N1
	3
	>>> N2
	4
	``` 
	but for a mutable list:   

	``` 
	>>> L1 = [19, 2, 3]
	>>> L2 = L1  # A.K.A **Shallow copy**
	>>> L2[0] = 3
	>>> L1
	[3, 2, 3]
	>>> L2
	[3, 2, 3]
	>>> L1 == L2
	True
	>>> L1 is L2
	True
	>>> L3 = list(L1)  # or L3 = L1[:], A.K.A **Deep copy**
	>>> L3
	[3, 2, 3]
	>>> L3 == L1
	True
	>>> L3 is L1
	False
	```
	More features of Python, see
	
2. Web App with Python. 
	![model](resources/model.png)
	using http.server module b;
1. [Problem set #6](https://docs.cs50.net/2017/x/psets/6/pset6.html): Sentimental
	NTBC
	Flask, Twitter application, Analyzer
<input type="checkbox" checked="True" name="pset3"> Status <br/>  

## IIX. Week 9: SQL [w9]
1. Model part of Web  
 
1. [Problem set #7](https://docs.cs50.net/2017/x/psets/7/pset7.html): C$50 Finance  
<input type="checkbox" name="pset3"> Status <br/>  

## IX. Week 10: JavaScrip [w10]
1. [Problem set #8](https://docs.cs50.net/2017/x/psets/8/pset8.html): Mashup
	- [Google map JS API](https://developers.google.com/maps/web/) powered by [Google Developers](console.developers.google.com)
	- [Google JS tutorial](https://developers.google.com/maps/documentation/javascript/tutorial)  
	- [SQLite csv_import](https://www.sqlite.org/cli.html#csv_import)
<input type="checkbox" name="pset3"> Status <br/>  

## X. Week 11: Final Project [final]
- [Project Page](https://docs.cs50.net/2017/fall/project/project.html)  

---
# Further Study [future]
- 【Updated 2019】[CS50 Beyond](https://cs50.harvard.edu/beyond/2019/winter/lectures/) is a 6-days lecture series that provides a continuation of CS50 in Web Development.
- Further in Languages
	- Learn [C language@cppreference.com](http://en.cppreference.com/w/c/language)
	- Maybe learn the 'better C' *C++*?
- Specified path
	- Data Science: [6.00.2x: Introduction to Computational Thinking and Data Science](https://www.edx.org/course/introduction-computational-thinking-data-mitx-6-00-2x-6) (which is considered as the continuous course of 6.00.1x, equivalent to cs50x)
	- Web: [CS50's Web Programming with Python and JavaScript](https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript)
	- Game Development: [CS50's Introduction to Game Development](https://www.edx.org/course/cs50s-introduction-to-game-development)
	- Mobile Apps: [CS50's Mobile App Development with React Native](https://www.edx.org/course/cs50s-mobile-app-development-with-react-native)

- More Courses
	- [Life after CS50!](https://cs50.stackexchange.com/questions/2890/life-after-cs50)
	- [Self study for Stanford's MSCS Foundation courses](https://backdoorgraduteschooladmissions.quora.com/Self-study-for-Stanfords-MSCS-Foundation-courses?share=1&srid=n9RZ), esp. CS107 - [Programming Paradigms](https://see.stanford.edu/Course/CS107) by Stanford
- ET CETERA
