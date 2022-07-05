---
layout: post
---

###### **UFUZZ, OSEK/VDX RTOS kernel fuzzer**

UFUZZ is an automated bug discovery tool, designed for embedded RTOS kernels that conform to the OSEK/VDX specification.
It generates test cases with the awareness of the application model, e.g., prioritized tasks, and transfers inputs via directly accessing the memory of guest VM. UFUZZ has been adopted and deployed in a private organization.