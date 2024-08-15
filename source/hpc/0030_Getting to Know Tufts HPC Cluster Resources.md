# Cluster Storage and Resources Limits

Author: Delilah Maloney, Sr. High Performance Computing (HPC) Specialist<br>Last Updated Date: 06/08/2024<br>

### Overview and Purpose
High-Performance Computing (HPC) clusters provide powerful resources that allow you to run complex computations and simulations efficiently. Understanding the storage and resource limits of an HPC cluster is crucial for:

- Optimizing Performance: Knowing the limits helps you allocate resources efficiently, ensuring your jobs run smoothly without unnecessary delays.
- Preventing Errors: Exceeding resource limits can cause job failures. Understanding the limits helps you avoid these pitfalls.
- Efficient Resource Use: Helps in planning and distributing your computational workload across available resources.

Tufts HPC Cluster moved to **[MGHPCC](https://www.mghpcc.org/)** in January 2024!



## 1. Cluster Storage

#### Account & Storage Requests

Go to **[Tufts HPC website](https://it.tufts.edu/high-performance-computing)**

For Faculties ONLY: **[HPC for Classes](https://tufts.qualtrics.com/jfe/form/SV_d7o0UZFgK1PFXnv)**

#### Home Directory

Be aware! Your Home Directory (**30GB**, fixed) should be `/cluster/home/your_utln`

If you are not sure how much storage you have used in your home directory, feel free to contact us and we can provide you the number. 

Or, you can use `hpctools` (login or compute node) OR run `$ du -a -h --max-depth=1 ~ | sort -hr` from a **compute node** in your home directory to find out the detailed usage. 

#### Reserach Project Storage

**[Request research project storage](https://it.tufts.edu/research-technology/)**

Your research project storage (from **50GB and up**) path should be `/cluster/tufts/yourlabname/`, and each member of the lab group has a dedicated directory `/cluster/tufts/yourlabname/your_utln`

To see your **research project storage quota** by running the following command from **any node on the new cluster Pax**:

`$ df -h /cluster/tufts/yourlabname ` 

**NOTE:** Accessing your research project storage space for the __first time__ in your current session, please make sure you type out the __FULL PATH__ to the directory `/cluster/tufts/yourlabname/`.



## 2. Cluster Resource Limit

### Partitions

- HPC clusters are divided into different partitions. A partition is a logical collections of nodes that comprise different hardware resources and limits to help meet the wide variety of jobs that get scheduled on the cluster. Compute nodes are grouped into partitions based on functionality and priority levels.

**Partitions Type:**

- **batch***: This is the default partition for standard jobs that do not require any special hardware or configurations.
- **gpu**: This partition is designated for jobs that require GPU resources. 
- **interactive**: This partition is intended for interactive jobs, which are typically shorter in duration and allow users to interact with their jobs in real-time. 
- **largemem**: This partition is for jobs that require large amounts of memory. 
- **mpi**: This partition is for jobs that use the Message Passing Interface (MPI) for parallel computing across multiple nodes. 
- **preempt**: This partition is for jobs that can be preempted (interrupted) to allow higher-priority jobs to run. 

#### Time limit
<u>**Each partition has a specific time limit.**</u>
```
PARTITION       TIMELIMIT      
batch*          7-00:00:00          
gpu             7-00:00:00        
interactive     4:00:00        
largemem        7-00:00:00        
mpi             7-00:00:00         
preempt         7-00:00:00     
```

* **preempt** - Be aware, `preempt` partition consists of most of the nodes on the cluster, including **contrib nodes** from different research labs. When submitting jobs to preempt partition, you acknowledge that your jobs are taking the **risk** of being preempted by higher priority jobs. In that case, you will simply have to resubmit your jobs. 

#### Configuration limit
<u>**Each partition can be configured with different combinations of CPU, memory, and GPU resources.**</u>

Cluster Resource Limit is the following:

* **Public Partitions** (batch+mpi+largemem+gpu) 

  * CPU: 500 cores

    RAM: 2000 GB

    GPU: 5

* **Preempt Partition** (preempt) 

  * CPU: 1000 cores

    RAM: 4000 GB

    GPU: 10
    
[**OnDemand**](https://ondemand.pax.tufts.edu) `Misc`-->`Inventory ` shows more node details (core count & memory)

#### CPUs
- CPUs (Central Processing Units) are the core components of compute nodes responsible for executing computational tasks. Knowing how to request the appropriate number of CPUs is key to optimizing task performance.

#### GPUs
- GPUs (Graphics Processing Units) are essential for tasks requiring high parallelism, such as deep learning and simulations. Tufts HPC cluster offers various types of NVIDIA GPUs in different partitions.

__NVIDIA GPUs__ are available in `gpu` and `preempt` partitions

**Request GPU resources with `--gres`. See details below.**

- If no specific architecture is required, GPU resources can be request with`--gres=gpu:1` 

  - `--gres` : Generic Resource
  - `gpu:1`: requesting one GPU

- You can request more than one type of GPUs with `constraint`, e.g.  

  `--gres=gpu:1 --constraint="t4|p100|v100"`

  - `--constraint`: set constraints on the resources allocated for the task.
  - `t4|p100|v100`: indicates that the task can use a GPU of type t4, p100, or v100, where the | symbol means "or".

- Please **DO NOT** manually set `CUDA_VISIBLE_DEVICES`. 

- Users can ONLY see GPU devices that are assigned to them by using the `$ nvidia-smi`command.

  If you submit batch jobs, it's recommended adding this command in your slurm job submission script.

- `gpu` partition`-p gpu`:

  - NVIDIA A100
    - In "gpu" partition
    - Request with: `--gres=gpu:a100:1`(one A100 GPU, can request up to 8 on one node)
    - `--constraint="a100-80G"`
    - Each GPU comes with 80GB of DRAM
    - Driver supports upto CUDA 12.2
  - NVIDIA P100s
    - In "gpu" partition
    - Request with: `--gres=gpu:p100:1`(one P100 GPU, can request up to 4 on one node)
    - `--constraint="p100"`
    - Each GPU comes with 16GB of DRAM
    - Driver supports upto CUDA 12.2
  - NVIDIA Tesla K20xm
    - In "gpu" partition
    - Request with: `--gres=gpu:k20xm:1`(one Tesla K20xm GPU, can request up to 1 on one node)
    - `--constraint="p100"`
    - Each GPU comes with 6GB of DRAM

- `preempt` partition `-p preempt`:
  - `a100`, `v100`, `p100`, ` rtx_6000`, `t4`
  - NVIDIA T4
    - In "preempt" partition
    - Request with: `--gres=gpu:t4:1`(one T4 GPU, can request up to 4 on one node)
    - `--constraint="t4"`
    - Each GPU comes with 16GB of DRAM
  - NVIDIA P100
    - In "preempt" partition
    - Request with: `--gres=gpu:p100:1`(one P100 GPU, can request up to 6 on one node)
    - `--constraint="p100"`
    - Each GPU comes with 16GB of DRAM
  - NVIDIA rtx_6000
    - In "preempt" partition
    - Request with: `--gres=gpu:rtx_6000:1`(one RTX_6000 GPU, can request up to 8 on one node)
    - `--constraint="rtx_6000"`
    - Each GPU comes with 24GB of DRAM
  - NVIDIA rtx_a6000
    - In "preempt" partition
    - Request with: `--gres=gpu:rtx_a6000:1`(one RTX_A6000 GPU, can request up to 8 on one node)
    - `--constraint="rtx_a6000"`
    - Each GPU comes with 48GB of DRAM
  - NVIDIA rtx_6000ada
    - In "preempt" partition
    - Request with: `--gres=gpu:rtx_6000ada:1`(one RTX_6000Ada GPU, can request up to 4 on one node)
    - `--constraint="rtx_6000ada"`
    - Each GPU comes with 48GB of DRAM
  - NVIDIA V100
    - In "preempt" partition
    - Request with: `--gres=gpu:v100:1`(one V100 GPU, can request up to 4 on one node)
    - `--constraint="v100"`
    - Each GPU comes with 16GB of DRAM
  - NVIDIA A100
    - In "preempt" partition
    - Request with: `--gres=gpu:a100:1`(one A100 GPU, can request up to 8 on one node)
    - `--constraint="a100-80G"`
    - `--constraint="a100-40G"`
    - `--constraint="a100"`
    - Each GPU comes with 40GB of DRAM or 80GB of DRAM


#### Check Cluster Computing Resource Availability

`$ module load hpctools`

`$ hpctools` 

Then follow the on-screen instructions to extract the information you need. 

