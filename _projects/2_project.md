---
layout: page
title: KSG
description: A system call specification generator for kernel fuzzer.
img: assets/img/ksg_arch.png
importance: 1
category: work
---

One thing that I found keep troubling me during writting a kernel fuzzer is the reliance on manually encoded input specification. 
The issue is that the driving force of the current works, the specification, is also the bottleneck of them due to the fact that writing such specification requires an immense amount of domain knowledge while being extremely laborious. 
Yet, automated generation of the specification is still an open problem due to the complexity of the kernel.
To this end, I started another project called KSG, kernel specification generator and this work was accepted by ATC '22.

This work solved two major challenges in specification generation: entry extration and type collection. Overall, KSG utilizes three steps to generate the specifications as shown in following figure:
<div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/ksg_arch.png" title="Workflow of KSG " class="img-fluid rounded z-depth-1" %}
</div>

Specifically, in order to perform analysis for specification generation, one needs to figure the entry points for analysis, that is, the kernel functions that are called by high level system calls.
The issue here is that these entries can be registered into the kernel with different kernel APIs in different locations during different times.
The idea of KSG to address this issue is that how entries are registered into the kernel really doesn't matter, since they're eventually stored into specific fields in high level kernel data structures, which indicates that we can extract entries directly from these fields without caring how entries are registered. 


The second challenge is that the type of a parameter of a system call is not fixed, i.e., it can be cast to different types acoss execution paths, which is a really common design pattern in Linux kernel. 
The goal of KSG is to generate specification for each execution of a entry. 
To achieve this, KSG utilizes Clang Static Analyzer, a source code level symbolic executoin engine, to collect parameters' types under each path with a type propagation algorithm.


KSG is proved to be practical and effective by the evaluation results that 2433 specifications can be automatically generated and 23 vulnerabilities were discovered. 
The tool is implemented with two eBPF program for extry extractioin, multiple CSA checkers for type collection (in C++), and a simple control program for automating the whole process (in rust), with roughly 8000 lines of code.
For some reason, I can not make the source code public avaliable, sorry for that.
For more information, checkout this ATC '22 [paper](assets/pdf/KSG.pdf) please.