---
layout: about
title: about
permalink: /

profile:
  align: right
  image: me.png
  image_cicular: false
  address: >
    <p> sunhao.th@gmail.com</p>
    <p> Tsinghua University </p>
    <p> Beijing, Haidian, China </p>

news: true  
selected_papers: true 
social: true 
---

Since 2020, I have been conducting system security research as a master student advised by Prof. [Yu Jiang](https://sites.google.com/site/jiangyu198964/home) in the system security assurance [group](http://www.wingtecher.com/personen) at [Tsinghua University](https://www.tsinghua.edu.cn/en/).
The lab focuses on improving the security of the infrastructural software stack, and my work there lies in operating system kernels, with an emphasis on Linux kernel security.
The fundamental goal of my research is to improve the correctness of OS kernels, one of the most complicated software, via finding and eliminating the vulnerabilities with the approaches called *fuzz testing* and *symbolic execution*. 

Throughout the past years' research, what I continuously pursue is approaches and algorithms that can solve problems **elegantly**, and, more importantly, can be applied in practice through solid implementation thus making **real impact** to the software industry. For example, I designed and implemented a kernel fuzzer callded [*Healer*](https://github.com/SunHao-0/healer) in `rust`, which is open-sourced and has already found more than 100 vulnerabilities in Linux kernel. 
This work was accepted by [*SOSP '21*](https://dl.acm.org/doi/10.1145/3477132.3483547).
My recent work KSG, a kernel specification generator, utilizes a probe-based tracing and symbolic execution-based type propagation algorithm to generate system call specifications for kernel fuzzer automatically.
This work has led to the discovery of 23 vulnerabilities in Linux kernel and was accepted by **ATC '22**.

The fact is that vulnerabilities continuously appear along with the development of software, e.g., even Linux kernel that is maintained by many gifted engineers contains thousands of bugs.
For this,  system security research does matter and novel mechanisms and theories need to be proposed and applied to reduce, or even eliminate the impact of vulnerabilities to a minimum level in the real world. 
I plan to pursue a **Ph.D. degree** after graduation (in 2023) to continue my research on system security. Please checkout my [CV](assets/pdf/cv.pdf) and kindly send me an email if I'm qualified to work with you. 