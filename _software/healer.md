---
layout: post
---

###### **Healer, kernel fuzzer inspired by Syzkaller**

[Healer](https://github.com/SunHao-0/healer) is an automated kernel bug finding tool, written in 17,000+ lines of Rust. 
It utilizes specifications that encode input information to generate system call sequences, and detects kernel bugs via triggering kernel crashes with generated sequences. 
While the idea behind Healer is relatively straightforward, it incorporates many tricks and techniques for efficient runtime behavior... [more](/projects/healer/)
<br>
**KEY RESULTS:** 100+ reported and fixed Linux bugs, 10+ CVEs assigned, 199 stars on github.