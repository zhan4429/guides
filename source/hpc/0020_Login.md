# Cluster Login Methods

Author: Delilah Maloney, Sr. High Performance Computing (HPC) Specialist<br>Last Updated Date: 06/08/2024<br>

### Overview and Purpose

The first step in using a HPC cluster is to establish a connection from our laptop to the cluster.

This tutorial introduce you two methods to connect with clusters, explain the difference between the two methods and give suggestions who might choose one over the the other methods.

### Prerequisites:

All Login methods in the following below require you to have:

- Active Tufts HPC Cluster Account
- 2FA will be required with Tufts network login via command line.
- Off-campus Non-Tufts Network please first connect to [Tufts VPN](https://access.tufts.edu/vpn) before proceed to login.

***

### Method 1. Shell Access 

#### For Mac OSX & Linux - Command Line:  

- Command for Shell environment (default: bash):

  - `$ ssh your_utln@login.cluster.tufts.edu` 

- Command with GUI:<br>
*X Window system needs to be installed on your local computer.

  - `$ ssh -XC your_utln@login.cluster.tufts.edu`
or
  - `$ ssh -YC your_utln@login.cluster.tufts.edu`

- Explanation of the Command:
  - `ssh`: The command to initiate an SSH connection.The SSH protocol aka **Secure Shell** is a method for secure remote login from one computer to another.
  - `-X` or `-Y`: These options enable X11 forwarding. -X is more secure, while -Y is more permissive and might be needed for some applications that don't work well with -X.
  - `-C`: This option enables compression, which can speed up the transfer of data over the network.
  - `your_utln@login.cluster.tufts.edu`: Replace your_utln with your actual Tufts username. This is the address of the remote HPC cluster.

- What Happens After Running the Command for Login:
  - You will be prompted to enter your password.
  - You will complete the 2FA process if required.


Now you are on a **Login Node** of the cluster (login-prod-0x) and in your **Home Directory** (~ or */cluster/home/your_utln*). 

`$ [your_utln@login-prod-02 ~]`

There are 3 login nodes: `login-prod-01`, `login-prod-02`, `login-prod-03` 

***Please DO NOT run any software on the login nodes.***

#### For Windows

- **[PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/learn/remoting/ssh-remoting-in-powershell-core?view=powershell-7.2)**
- **[WSL - Windows Subsystem for linux](https://learn.microsoft.com/en-us/windows/wsl/install)**
- **[PuTTY](https://www.putty.org/)**  
- **[Cygwin](https://www.cygwin.com/)** 

**Hostname**: `login.cluster.tufts.edu` or `login.pax.tufts.edu`

***

### Method 2. OnDemand 
**Open OnDemand** is a browser-based High Performance Computing (HPC) portal.
 <img src="https://tufts.box.com/shared/static/njo2ih0ne2mmretxqxwp9jlztdsm8yxj.png" alt="CPU-GPU" width="60%"/>

Preferred browser: **Chrome or FireFox**

- Go to [**OnDemand**](https://ondemand.pax.tufts.edu) (0ff-campus Non-Tufts Network please first connect to Tufts VPN)

- Use your **Tufts UTLN** and **password** to login. 

TAH-DAH! You are on Tufts HPC cluster!

Click the tab at the top __`Clusters`__, then select  __`Tufts HPC Shell Access`__, to start a shell access to the HPC cluster. 

**`Tufts HPC Shell Access`** = `$ ssh your_utln@login.pax.tufts.edu`

Or use the `>_Open in Terminal` button in `Files` to open a terminal in whichever directory you navigated to.
<span style="color: red;"> I did not find the "open in terminal" under Files </span>

If you need X11 access through OnDemand to display any GUI applications, please temporarily use our [OnDemand](https://ondemand.pax.tufts.edu) **`Clusters`** for this option:

**`Tufts HPC FastX11 Shell Access`** = `$ ssh -XC your_utln@login.pax.tufts.edu` (with X11 for GUI applications)

OR 

you also have the option to use the `Xfce Terminal` under new  [OnDemand](https://ondemand.pax.tufts.edu) `Interactive Apps`.


