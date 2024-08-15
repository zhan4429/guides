---
tags: hpc
---

# Tufts HPC Introduction

This secttion provides a high-level introdution to HPC cluster and commonly used terminologies related to HPC cluster.

Author: Delilah Maloney, Sr. High Performance Computing (HPC) Specialist<br>Last Updated Date: 06/08/2024<br>


### What is "HPC"

-   High-performance computing (HPC) refers to the use of powerful computational resources and techniques to solve complex and large-scale problems that are beyond the capabilities of standard desktop computers. HPC systems leverage the power of supercomputers, clusters of computers, and specialized hardware and software to perform massive amounts of calculations at high speeds.

### Key Characteristics of HPC:

-   Parallel Processing: HPC systems break down large problems into smaller tasks that can be processed simultaneously across multiple processors or nodes, significantly reducing computation time.

-   High-Speed Interconnects: These systems use high-speed networking technologies to ensure rapid data transfer between processors and storage units, minimizing latency and maximizing efficiency.

-   Scalability: HPC architectures are designed to scale efficiently, allowing the addition of more computational resources (processors, memory, storage) to handle increasing workloads and more complex problems.

-   Specialized Software: HPC utilizes specialized software, including parallel programming languages, libraries, and frameworks, to optimize performance and manage computational tasks effectively.

### Applications of HPC:

-   Scientific Research: Simulations of physical phenomena, climate modeling, molecular dynamics, astrophysics.
-   Engineering: Computational fluid dynamics, structural analysis, materials science.
-   Healthcare: Genomic analysis, drug discovery, medical imaging.
-   Finance: Risk modeling, financial forecasting, high-frequency trading.
-   Entertainment: Special effects rendering, animation, virtual reality.
-   Artificial Intelligence and Machine Learning: Training complex models, large-scale data analysis.

### What is "Cluster"

-   A computer cluster is a set of loosely or tightly **connected** **computers** **(Nodes)** that work together so that, in many respects, they can be viewed as a single system. Computer clusters have each node set to perform the same/similar tasks, controlled and scheduled by [**software**](#SLURM).

### Nodes

-   Nodes are the fundamental building blocks of High-Performance Computing (HPC) clusters. Each node is an individual computer that contributes to the overall computational power of the cluster.
-   Each node is a single computer in the system, allowing it to perform computations independently. However, the nodes communicate and collaborate to tackle large-scale problems, making the entire cluster significantly more powerful than the sum of its parts.
-   Type of Node:
    -   Compute Nodes: Perform the bulk of computational tasks.
    -   Head Node (Master Node): Manage and coordinate the activities of compute nodes.
    -   Storage Nodes: Provide centralized storage for the cluster.
    -   Login Nodes: Provide access points for users to interact with the cluster.
-   Node Architecture: Each node in an HPC cluster generally consists of one or more **processors (CPUs or GPUs)**, **memory**, and **storage**.

![Cluster Structure: Nodes and User](https://tufts.box.com/shared/static/jciy91ig6j5916uik41eoyxne9xoe6zy.png)

### CPU and GPU

-   CPU -- **Central Processing Unit**

    -   A CPU can never be fully replaced by a GPU

    -   Can be thought of as the **taskmaster** of the entire system, coordinating a wide range of general-purpose computing tasks

-   GPU -- **Graphics Processing Unit**

    -   GPUs were originally designed to create images for computer graphics and video game consoles

    -   GPGPU [more explanation here?]{style="color: red;"}

    -   Performing a narrower range of more specialized tasks

        <img src="https://raw.githubusercontent.com/DelilahYM/ImageHost/master/CPUGPU.png" alt="CPU-GPU" width="60%"/>

-   [any relationship/similarities/difference between CPU and GPU?]{style="color: red;"}

### Memory and Storage

The central processing unit (CPU) of a computer is what manipulates data by performing computations. In practice, almost all computers use a [storage hierarchy](https://en.wikipedia.org/wiki/Memory_hierarchy), which puts fast but expensive and small storage options close to the CPU and slower but less expensive and larger options further away. Generally the fast volatile technologies (which lose data when off power) are referred to as "memory", while slower persistent technologies are referred to as "storage".

-   Memory
    -   Small, fast, expensive
    -   Used to store information for immediate use
-   Storage
    -   Larger, slower, cheaper
    -   Non-volatile (retaining data when its power is shut off)

<img src="https://raw.githubusercontent.com/DelilahYM/ImageHost/master/MemStorage.png" alt="Memory-Storage" width="60%"/>

## Getting help

* **Learning more**: If you would like to learn more about the HPC, we suggest you complete the trainings available in the Section Navigation on the left. 

* **Research**: If you have specific questions about your research use case on the HPC, please reach out to <tts-research@tufts.edu>.  

* **Course Support**: To get help for a course, you should first reach out to your TA or instructor. 

* **General Questions**: For general questions, you can reach out to a Data Lab Assistant. <https://sites.tufts.edu/datalab/services-support/student-lab-assistants/>

* **Consulting**: For consulting on research projects and research support, you can reach out to <tts-research@tufts.edu> to meet with a member of Research Technology. 



<!---
## Applications  

Bioinformatics Only (to start)
This can be 1 - 2 sentences with a hyperlink.
Tufts Go Link <https://go.tufts.edu/hpcmod>
--->



