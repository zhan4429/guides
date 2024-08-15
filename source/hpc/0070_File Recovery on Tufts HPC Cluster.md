# File Recovery on Tufts HPC Cluster

- **Author**: <br>Delilah Maloney<br>  Sr. High Performance Computing (HPC) Specialist<br>  Research Technology, Tufts Technology Services
- **Last Updated Date**:
<br>6/15/2024

## Background:
- Researchers often work with large datasets and complex simulations, making regular backups essential. The Tufts HPC cluster uses a snapshot system to automatically create backups of user data, allowing for quick recovery of lost or modified files.
- What is a **Snapshot**:A read-only copy of the filesystem or directory at a specific point in time. Snapshots on the Tufts HPC cluster are taken daily, capturing the state of your files and directories at that moment. They allow you to recover data in case of accidental deletion or modification.



## Important Note

- This instruction **ONLY** applies to **Tufts HPC cluster**. 
- The snapshots are taken daily. The snapshot frequency may vary based on current policies and setups.
- Not all changes and modifications to all files are reflected in the snapshots. If a file is created, modified, and/or deleted within a couple of hours, it may or may not be captured in the snapshots depending on the timing.
- **DO NOT** modify or delete any snapshots. There is no snapshot of snapshots.
- The following steps need to be executed in Command Line Interface (shell, terminal, .etc). Users can access also access and recover files from OnDemand interface using the mentioned directory path.



Snapshots can be accessed directly from any directories on the cluster now!

## Example Scenario:

In the following example, the **target directory path** from which directory the files/directories were missing is `/cluster/home/tutln01/work`. 

In your case, it can be any paths such as `/cluster/home/$USER/folder1/folder2` or `/cluster/tufts/yourlab/$USER/folder3`

### Find Snapshots

- Navigate to the target directory path: go to **any directory** (project or home, in this example, it's `/cluster/home/tutln01/work` ) where you need files to be recovered 
- Access to the `.snapshot` of that directory.

```
[tutln01@login-prod-01 ~]$ cd /cluster/home/tutln01/work
[tutln01@login-prod-01 work]$ pwd
/cluster/home/tutln01/work
[tutln01@login-prod-01 work]$ cd .snapshot
[tutln01@login-prod-01 .snapshot]$ date
Mon Apr 24 10:15:59 EDT 2023
[tutln01@login-prod-01 .snapshot]$ ll
total 0
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-03-21_14_38_07_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-03-22_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-03-23_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-03-24_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-03-25_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-03-26_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-03-27_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-03-28_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-03-29_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-03-30_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-03-31_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-01_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-02_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-03_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-04_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-05_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-06_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-07_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-08_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-09_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-10_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-11_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-12_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-13_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-14_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-15_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-16_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-17_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-18_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-19_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-20_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-21_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-22_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-23_07_00_00_UTC
drwxrwx--- 2 tutln01 facstaff 4096 Feb 24 12:36 homedir_2023-04-24_07_00_00_UTC
```

### Locate Missing Files/Directories

Choose desired snapshot date. 

For example, assume I accidentally deleted a file from this directory on 2023-04-20, I would check both `homedir_2023-04-20_07_00_00_UTC` from 2023-04-20 as well as `homedir_2023-04-19_07_00_00_UTC` from 2023-04-19 for the desired version of the file. Repeat the following steps for both dates if needed.

Pick a snapshot date, and list the contents (our target directory is `/cluster/home/tutln01/work` in this case)

```
[tutln01@login-prod-01 .snapshot]$ cd homedir_2023-04-20_07_00_00_UTC
[tutln01@login-prod-01 homedir_2023-04-20_07_00_00_UTC]$ pwd
/cluster/home/tutln01/work/.snapshot/homedir_2023-04-20_07_00_00_UTC
[tutln01@login-prod-01 homedir_2023-04-20_07_00_00_UTC]$ ll
```

### Recovery Files/Directories

Find and verify the file/directory you are looking for, then **COPY** it back to your target directory under a different name (to avoid overwriting exisiting files).

- `-i` (Interactive): Prompts for confirmation before overwriting files.
- `-r` (Recursive): Copies directories and their contents recursively.
```
[tutln01@login-prod-01 homedir_2023-04-20_07_00_00_UTC]$ pwd
/cluster/home/tutln01/work/.snapshot/homedir_2023-04-20_07_00_00_UTC
[tutln01@login-prod-01 homedir_2023-04-20_07_00_00_UTC]$ cp -i myfile ~/work/myfile_recovered
```

If you are recovering directories, copy the directory recursively.

```
[tutln01@login-prod-01 homedir_2023-04-20_07_00_00_UTC]$ cp -i -r mydir ~/work/mydir_recovered
```

Now you can go back to your target directroy and check if the file/directory has been copied over

```
[tutln01@login-prod-01 homedir_2023-04-20_07_00_00_UTC]$ cd /cluster/home/tutln01/work
[tutln01@login-prod-01 work]$ ls -lrt
```

**If you have multiple files/directoires need to be recovered, repeat the above steps.**



