# 



## Instructor Notes

Windows -- Git Bash (Cygwin, PowerShell, Windows Subsystem for Linux (WSL))

Mac OSX -- Terminal

Linux -- Shell

### Setup

https://swcarpentry.github.io/shell-novice/setup.html

Download [shell-lesson-data.zip](https://swcarpentry.github.io/shell-novice/data/shell-lesson-data.zip) and store the file on your __Desktop__



You can follow the lecture writeup, but do focus on the shell (terminal) :) 

### Introducing the Shell (10:10)

GUI vs CLI

for a literature search, you have to copy the third line of one thousand text files in one thousand different directories and paste it into a single file.

BASH

```
$ cat /etc/shells
```

Change Shell:

```
$ chsh -s /bin/bash
```

prompt -- $ (#, %) -- shell is waiting for input/command

```
$ Command + Options + Argument
```

```
$ ls
```



__senario:__

Nelle, biologist

She has 1520 samples that she’s run through an assay machine to measure the relative abundance of 300 proteins. 

She needs to run these 1520 files through an imaginary program called `goostats.sh` she inherited.

write a paper

use gui is mundane task 



In order to achieve her task, Nelle needs to know how to:

- navigate to a file/directory
- create a file/directory
- check the length of a file
- chain commands together
- retrieve a set of files
- iterate over files
- run a shell script containing her pipeline

### Navigating Files and Directories (10:50)

file system

```
$ pwd
```

```
$ ls
$ ls -F

```

- a trailing `/` indicates that this is a directory
- `@` indicates a link
- `*` indicates an executable

```
$ clear
```

Help!

```
$ ls --help
$ man ls
```



```
$ cd /path
$ cd ..
$ cd
$ cd -

```

```
$ ls -s
$ ls -S
$ ls -F /
```

```
tab completion
```



### Working With Files and Directories (11:30)

```
$ mkdir
```

```
$ mkdir -p
```

```
$ ls -FR 
```



### Pipes and Filters

### Loops

### Shell Scripts

### Finding Things









Commands:

$ command + flag/option + argument(s)



Case Sensitive

print working directory



https://librarycarpentry.org/lc-shell/02-navigating-the-filesystem/index.html



Wildcard -- * or ?

watch out for -- rm

