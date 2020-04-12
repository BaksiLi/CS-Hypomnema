<style TYPE="text/css">
code.has-jax {font: inherit; font-size: 100%; background: inherit; border: inherit;}
</style>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    tex2jax: {
        inlineMath: [['$','$'], ['\\(','\\)']],
        skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'] // removed 'code' entry
    }
});
MathJax.Hub.Queue(function() {
    var all = MathJax.Hub.getAllJax(), i;
    for(i = 0; i < all.length; i += 1) {
        all[i].SourceElement().parentNode.className += ' has-jax';
    }
});
</script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-AMS_HTML-full"></script>
# NP Problems

<!-- vim-markdown-toc GFM -->

  * [NP-Completeness](#np-completeness)
  * [Search Problems](#search-problems)
    * [**Boolean satisfiability problem** (SAT)](#**boolean-satisfiability-problem**-(sat))
    * [Travelling Salesperson Problem (TSP)](#travelling-salesperson-problem-(tsp))
    * [Hamiltonian Cycle Problem (HCP)](#hamiltonian-cycle-problem-(hcp))
    * [Longest Path Problem](#longest-path-problem)
    * [Integer Linear Programming (ILP)](#integer-linear-programming-(ilp))
    * [Independent Set Problem](#independent-set-problem)
    * [P and NP](#p-and-np)
* [Reductions](#reductions)

<!-- vim-markdown-toc -->

## NP-Completeness
This is covered in the last note (Graph Algorithm).

Efficient algorithm doesn't go through all the possible solutions.

## Search Problems
- **Search problem** means that given an instance, to find a solution or report that none exists.
	> DEF: A search problem is defined by an algorithm $C$ that takes an instance $I$ and a  candidate solution $S$, and runs in time polynomial in the length of $I$. We say that $S$ is a  solution to $I$ iff. $C(S,I)=true$.
	
### **Boolean satisfiability problem** (SAT)
- CNF (Conjunctive Normal Form):
	$$(x\lor y\lor z)(x\lor \overline{y})(y\lor \overline{z})(z\lor \overline{x})(\overline{x}\lor \overline{y}\lor \overline{z})$$
	where x, y, z are Boolean variables, the bar over them indicates negation, clauses are disjunctions (logical or) of literals.   

- SAT is defined
  > Input: Formula $F$ in CNF.
  >
  > Output: All possible assignments of Boolean values to the variables of $F$ satisfying the clauses, if exists; else return unsatisfiable.

- Example
  - $(x \vee \bar{y})(\bar{x} \vee \bar{y})(x \vee y)$ satisfied by $x=1$ and $y=0$.
  - $(x \vee y \vee z)(x \vee \bar{y})(y \vee \bar{z})(z \vee \bar{x})(\bar{x} \vee \bar{y} \vee \bar{z})$ unsatisfiable.

- It is a canonical hard problem, and useful since many combinatorial problems can be naturally stated in terms of SAT and solved by *SAT solver*.

- For SAT, the given instance $I$ is a Boolean formula (in CNF), and $S$ is a satisfying assignment of Boolean constants to its variables. The corresponding algorithm $C$ checks whether $S$ satisfies all clauses of $I$. So it is a search problem.

### Travelling Salesperson Problem (TSP)
- Given a weighted complete graph ($|V|=n\implies|E|={n\choose 2}=\frac{n(n-1)}{2}$), TSP is defined
  > Input: Pairwise distances between $n$ cities and a budget $b$. 
  > 
  > Output: A **cycle** that visits each vertex exactly once and has total length at most $b$.

- TSP is a search problem: Given a sequence of vertices, it is easy to check whether it is a cycle visiting all the vertices of total length at most $b$. 
- TSP is usually states as an **optimization** problem; we stated its **decision version** to guarantee that a candidate solution can be efficiently checked for correctness.

- Algorithms:
	- Brute-force (Check all permutations): $O(n!)$.
	- Dynamic programming $O(n^{2}2^{n})$ (will see later).
	- No significantly better upper bound than above is known. There are *heuristic algorithms* and *approximation algorithms*.
  
- We can compare MST (Minimum Spanning Tree problem) to MST.

	|o|MST|TSP|
	|:-:|:-:|:-:|
	|Decision version| given $n$ cities, connect them by $(n-1)$ road of minimal total length | given $n$ cities, connect them *in a path* by $(n-1)$ roads of minimal total length|
	|O|Linear|No polynomial algorithm known|
	
- Detailed descriptions and implementation of algorithms, see *Graph Theory and Algorithms (with Python)*

### Hamiltonian Cycle Problem (HCP)
- For a given graph, HCP is defined.
  > Input: A graph.
  >
  > Output: A cycle that visits each vertex of the graph exactly once.

- It is similar to *Eulerian Cycle Problem* (ECP) which find the cycle that visit every edge exactly once.
	- Theorem: An undirected graph has an Eulerian cycle iff it is connected and the degree of each vertex is even.
  
- Comparison

	|o|ECP|HCP|
	|:-:|:-:|:-:|
	|Decision version| find a cycle visiting each edge exactly once | find a cycle visiting each vertex exactly once |
	|O|Linear|No polynomial algorithm known|

### Longest Path Problem
- LPP is defined.
  > Input: A weighted graph, two vertices $s$, $t$, and a budget $b$.
  >
  > Output: A simple path (no repeated vertices) of total length *at least* $b$.

- It is similar to *Shortest Path Problem* which finds a simple path from $s$ to $t$ of total length at most $b$. Which uses BFS in linear time.

### Integer Linear Programming (ILP)
- It is defined.
  > Input: A set of linear inequalities $Ax\leq b$.
  >
  > Output: Integer solution.

- Example
  - $$\begin{aligned} x_{1} & \geq 0.5 \\-x_{1}+8 x_{2} & \geq 0 \\-x_{1}-8 x_{2} & \geq-8 \end{aligned}$$
    - No Integer Solution!

- Comparison

  |LP|ILP|
  |:-:|:-:|
  |Find a *real* solution of a system of linear inequalities | Find an *integer* solution of a system of linear inequalities |
  |Efficient solved for some pathological cases using ellipsoid method or interior point method |No polynomial algorithm known|

- The SAT can be easily reduced to the integer linear programming problem. For this, for each variable $x_i$ of the input formula, add two inequalities $0\leq x_i$ and $x_i\leq 1$.
  - Then, for each clause like $\left(x_{i} \vee \bar{x}_{j} \vee \bar{x}_{k}\right)$ add an inequality $x_{i}+\left(1-x_{j}\right)+\left(1-x_{k}\right) \geq 1$.
  - More formally, for each clause of the form $\left(\ell_{1} \vee \ell_{2} \vee \cdots \vee \ell_{k}\right)$ add an inequality $m_1 + m_2 + \cdots + m_k \leq 1$. Here, $m_i$ is equal to $\ell_i$, if $\ell_i$ is a variable $x_j$, and $m_i = (1-x_j)$, if $\ell_i$ is the nagation of a variable $x_j$.
  - Example: The ILP of 
    $$\left(x_{1} \vee x_{2}\right)\left(x_{1} \vee \bar{x}_{2}\right)$$ 
    is $0 \leq x_{1} \leq 1,0 \leq x_{2} \leq 1, x_{1}+x_{2} \geq 1, x_{1}-x_{2} \geq 0$.

### Independent Set Problem
- It is defined.
  > Input: A graph and a budget $b$.
  >
  > Output: A subset of vertices of size at least $b$ such that no two of them are adjacent (no edge between them).

- Comparison
  
  |Independent set in a tree|Independent set in a graph|
  |:-:|:-:|
  |Find an independent set of size at least $b$ in a given tree | 〻graph |
  |Efficient Solution | No polynomial algorithm known|

### P and NP
- Recall the definition of a search problem. 
- The **Class NP** is defined.
  > NP (Non-deterministic Polynomial time) is the class of all search problems. In other words, it contains all problems whose solutions can be efficiently *verified*.
- Examples of class NP: TSP, Longest path, ILP, IS on graphs.
  
- The **Class P** is defined.
  > P is the class of all search problems that can be *solved* in polynomial time.
- Examples of class P: MST, Shortest Path, LP, IS on trees.

- The main open problem (Millennium Prize) in Computer Science is
  > Is **P** equal to **NP**?

  - If $\mathrm{P}=\mathrm{NP}$, then all search problems can ve solved in polynomial time.
  - If $\mathrm{P} \neq \mathrm{N P}$, then there exist search problems that cannot be solved in polynomial time.

# Reductions
