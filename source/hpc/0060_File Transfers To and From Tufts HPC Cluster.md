# File Transfers To/From Tufts HPC Cluster

- **Author**: <br>Delilah Maloney<br>  Sr. High Performance Computing (HPC) Specialist<br>  Research Technology, Tufts Technology Services
- **Last Updated Date**:
<br>6/15/2024

#### Overview:
This guide provides clear instructions on how to transfer files to and from the Tufts HPC cluster using various tools and protocols.

> **File Transfer Hostname**
>
> - xfer.cluster.tufts.edu = xfer.pax.tufts.edu
>
> **File Transfer Protocol**
>
> - SCP(Secure Copy Protocol)
> - SFTP(SSH File Transfer Protocol)
> - rsync over SSH
>
> **Recommended Tools**
>
> - Windows Only: **[WinSCP](https://winscp.net/eng/index.php)**
> - Cross-Platform: **[FileZilla](https://filezilla-project.org/)**    
> - Cross-Platform: **[Cyberduck](https://cyberduck.io/)**
> - Web Interface:**[OnDemand](https://ondemand.pax.tufts.edu)** (Only for transfering files size **less than 976MB per file.**)



### 1. Using OnDemand for File Transfers

- Go to OnDemand:

  **[https://ondemand.pax.tufts.edu/]( https://ondemand.pax.tufts.edu/)** 

- Nagigate to **`Files`**
- Use the **`Upload`** or **`Download`** buttons to transfer. 
- Make sure you navigate to the destination/source directory on cluster using the **`Go To`** button before transfering files.

  
### 2. Using Terminal for File Transfers
**Terminal**   <img src="https://agaric.coop/sites/default/files/2019-04/Terminalicon2.png" alt="Terminal" width=10%>

- **Hostname** for file transfer: xfer.cluster.tufts.edu

- NOTE:
    
     * __Local_Path__ : Path to your files or directory on your local computer
     * __Cluster_Path__ :Path to your files or directory on the cluster
       * Home Directory: */cluster/home/your_utln/your_folder*
       * Research Project Storage Space Directory: */cluster/tufts/yourlabname/your_utln/your_folder*

    ***Execute from your local machine terminal.* **

    General Format:

    `$ scp From_Path To_Path`

    `$ rsync From_Path To_Pat`

    ***NOTE: If you are transfering very large files that could take hours to finish, we would suggest using `rsync` as it has ability to restart from where it left if interrupted.***
    
    Exmaple:

    **File** Transfer with `scp`or `rsync`:

    * Download from cluster

    `$ scp your_utln@xfer.cluster.tufts.edu:Cluster_Path Local_Path  `

    `$ rsync your_utln@xfer.cluster.tufts.edu:Cluster_Path Local_Path`

    * Upload to cluster

    `$ scp Local_Path your_utln@xfer.cluster.tufts.edu:Cluster_Path`

    `$ rsync Local_Path your_utln@xfer.cluster.tufts.edu:Cluster_Path`

    **Directory** Transfer with `scp` or `rsync`:

    * Download from cluster

    `$ scp -r your_utln@xfer.cluster.tufts.edu:Cluster_Path Local_Path  `

    `$ rsync -azP your_utln@xfer.cluster.tufts.edu:Cluster_Path Local_Path`

    * Upload to cluster

    `$ scp -r Local_Path your_utln@xfer.cluster.tufts.edu:Cluster_Path`

    `$ rsync -azP Local_Path your_utln@xfer.cluster.tufts.edu:Cluster_Path`

    
