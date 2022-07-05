---
layout: post
---

###### **KSG, kernel syscall specification generator**

Writting system call specifications for kernel fuzzers requires significant amount of domain knowledge while being laborious. 
To address this, I designed and implemented a kernel specification generator (KSG) with 7000+ lines of C++ code based on Clang Static Analyzer. 
KSG utilizes a probe-based tracing and a symbolic execution-based type propagation algorithm...[more](/projects/KSG) 
<br>
**KEY RESULTS:** 2433 automatically generated specifications and 23 bugs.