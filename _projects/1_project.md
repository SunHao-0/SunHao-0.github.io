---
layout: page
title: Healer
description: A kernel fuzzer inspired by Syzkaller
img: assets/img/healer_arch.png
importance: 1
category: work
---

The essential idea of kernel fuzz testing is to generate high quality inputs to trigger kernel crash; thus, the effectiveness of these works depends on the capability of input generation.
Yet, the approach utilized by the state-of-the-art work is designed to guarantee its efficiency but the effectiveness is sacrificed, and methods that guarantee the quality of input are not adopted mainly because they're expensive. 
After digging into the kernel, I found that the fundamental principle of input generation is influence relations between system interfaces, so I proposed to guide the generation with relations. I designed an algorithm called relation learning that combines static and dynamic learning to infer such relations accurately with minimum overhead to make this proposal practical. To verify this idea, I implemented a tool called [Healer](https://github.com/SunHao-0/healer) from scratch with more 17,000 lines of `rust` code, which is open-sourced and has gained 198 stars.

<div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/healer_arch.png" title="Architecture of Healer" class="img-fluid rounded z-depth-1" %}
</div>

In general, Healer is a kernel fuzzer inspired by [Syzkaller](https://github.com/google/syzkaller).
Similar to Syzkaller, Healer uses the syscall information provided by the [Syzlang](https://github.com/google/syzkaller/blob/master/docs/syscall_descriptions.md) [description](https://github.com/google/syzkaller/tree/master/sys/linux) to generate sequences of system calls that confirm to the parameter structure constraints and partial semantic constraints, and finds kernel bugs by continuously executing the generated call sequences to cause kernel crashes.
Unlike Syzkaller, Healer does not use an empirical [choice-table](https://github.com/google/syzkaller/blob/master/prog/prio.go), but detects the influence relationships between syscalls by dynamically removing calls in the minimized call sequences and observing coverage changes, and uses the influence relationships to guide the generation and mutation of call sequences. In addition, Healer also uses a different architectural design than Syzkaller as shown in the above figure.

For more information, checkout this github [repo](https://github.com/SunHao-0/healer).