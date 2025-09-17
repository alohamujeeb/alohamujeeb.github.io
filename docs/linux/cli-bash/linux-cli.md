---
tags:
  - linux 
  - linux commands reference
  - linux cheat sheet
---

# Linux Commands Reference
This page provides quick-access cheat sheets for Linux CLI commands.

---
## 1. Files and Directories
???+ "Files and Directories (click to view)"
	
	=== "Navigation and Listing"
		|command|description|
		|---|---|
		|```ls```|List files and folders in the current directory|
		|```ls -l```|List with detailed info (permissions, size, date)|
		|```ls -a```|List all files, including hidden ones (. files)|
		|```pwd```|Show current directory path|
		|```cd [directory]```|Change directory|
		|```cd ..```|Go up one directory level|
		|```cd```|Go to home directory of the logged-in user|
		
	=== "Creating & Removing"
		|command|description|
		|---|---|
		|```mkdir [foldername```|Create a new folder|
		|```rmdir [foldername]```| Remove an empty folder|
		|```rm -r [foldername]```| Remove a folder and its contents recursively|
		|```touch [filename]```|Create an empty file or update timestamp|
		|```rm [filename]```|Remove a file|
		
	=== "Copying & Moving"
		|command|description|
		|---|---|
		|```cp [source] [destination]```|Copy file|
		|```cp -r [source_folder] [destination_folder]```|Copy folder recursively|
		|```mv [source] [destination]```| Move or rename files/folders|
		

	=== "Viewing"
		|command|description|
		|---|---|
		|```cat [filename]```|Display file content|
		|```less [filename]```|View file content page by page|
		|```head [filename]```|Show first 10 lines of a file|
		|```tail [filename]```|Show last 10 lines of a file|
		
	=== "File Info"
		|command|description|
		|---|---|
		|```file [filename]```|Show file type|
		|```stat [filename]```|Detailed info about a file or folder|
		
		
---
## 2. File Searching
???+ "File Searching (click to view)"

	=== "Navigation and Listing"
		|command|description|
		|---|---|
		|```find [path] -name "[pattern]"```| Search for files by name|
		|```locate [filename]```| Quickly find a file by name (database-based))|
		|```grep "[text]" [filename]```|Search for text inside a file|

	=== "Basic example"
		|command|description|
		|---|---|
		|```find . -name "*.txt"```| Find all .txt files in the current directory and subdirectories|
		|```locate [filename]```| Quickly find a file by name (database-based))|
		|```find /home/user -name "notes.md"```|Find a file named notes.md anywhere in /home/user|
		|```find /tmp -name "*.tmp" -exec rm {} \;```|Find and delete all .tmp files in /tmp|

	=== "More examples of find"
		|command|description|
		|---|---|
		|```find /etc -type f -name "*.conf" -exec realpath {} \;```| List full path of all .conf files|
		|```find /var/log -type f -name "*.log" -exec du -h {} \;```| Print file size of .log files|
        |```find /var/log -type f -name "*.log" -size +1M -exec rm {} \;```| Delete log files of size above 1MB (using rm shell command)|
        |```find /var/log -type f -name "*.log" -size +1M -delete```| Delete log files of size above 1MB (using -delete flag)|
		|```find /tmp -type f -name "*.tmp" -exec rm {} \;```| Delete all .tmp files|
		|```find . -type f -empty -exec rm {} \;```| Delete empty files|
		|```find /backup -type f -mtime +30 -exec rm {} \;```| Delete files older than 30 days|
		|```find ~/Downloads -type f -mtime +30 -exec rm {} \;```| Delete files older than 30 days|
		

	Note: **-exec** is not the same as the shell’s built-in **exec** command — they're totally different things, even though they share the word "exec."
	
	- exec some_command  (this is part of shell itself)
	- The -exec Option in the find Command is not same as exec...It is just an option of the 'find command itself"
    - to delete log files "-delete" option is better than "rm", because it is a built-in parameter of "find" command. It's generally faster and uses less system resources because it doesn’t need to spawn a new rm process for each file.
    (both ways are mentioned in above examples)

---
## execute a command (```exec``` vs ```-exec```)
???+ "File/Content Searching (click to view)"

	=== "exec command"
		``` bash
		exec command [arguments]
		```
	=== "Description"
		- The exec command is a shell builtin that replaces the current shell process with a specified command, running that command directly without creating a new process.
		- After exec runs, the original shell session is replaced and does not return to the previous shell.
		
		
	=== "Some Examples"
		``` bash
		#This replaces the current shell with the ls -l command.
		#Once ls finishes listing files, the session ends (you won’t get a prompt back).
		exec ls -l
		
		
		#Delete all .bak files in the current directory and subdirectories
		find . -type f -name "*.bak" -exec rm {} \;
		```
	
### ```exec``` vs ```-exec```

- **-exec** is not the same as the shell’s built-in exec command — they're totally different things, even though they share the word "exec."

- **exec some_command** (this is part of shell itself)
The -exec Option in the find Command is not same as exec...It is just an option of the 'find command itself"

### When to use ```exec```
???+ note "When to use **exec** (click to find out about various scenarios/use-cases)"
	- It is used to **Replace the Shell with Another Program**: Useful in scripts or login environments where you want to run a program instead of a shell — and don’t need to return.
	
	
	- To Save Memory in Scripts: In long-running scripts, especially daemons, using exec prevents spawning a new process. It replaces the shell, saving memory and process overhead.
	
	
	- To Redirect Input/Output for the Entire Shell or Script: exec can be used to change stdin, stdout, or stderr at the shell level — affecting all commands that follow.
	
	- To Replace the Shell in System Startup Scripts: In init or systemd environments, exec is used so that the shell process doesn’t hang around. This is cleaner and avoids zombie processes.
	- To Chain Commands with Replacement: You can use it at the end of a script to "handoff" control to another process, especially for chaining tools or launching shells.

### When NOT to use ```exec```
???+ warning "When NOT to use **exec** (click to find out)"
	
	- Once executed, the shell is gone. If you accidentally use exec instead of running a command normally, your terminal may close (especially with GUI apps).
	
	- For most everyday tasks (like ls, rm, etc.), you should just run the command normally, not with exec.

---
## 3. Finding text in file(s)
### **grep** command 

???+ "grep (click to view)"


	=== "Basic syntax"
		``` 
		grep [options] "pattern" [file...]
		```
		``` bash
		# for example
		grep "search_text" filename

		```

	=== "Some examples"
		
		``` bash
		#Find lines containing "TODO" in a file
		grep "TODO" myscript.py
		
		#Recursively search all files in a directory for "main()"
		grep -r "main()" /home/user1/code/
		
		#Search "error" ignoring case sensitivity
		grep -i "error" server.log

		#Show line numbers where "function" appears
		grep -n "function" script.sh
		
		#Match the whole word "init" (not "initialize", etc.)
		grep -w "init" config.yaml

		#Search all non-binary files for "password"
		# The -I option tells grep to ignore binary files. (i.e. non-text files)
		grep -I "password" *
		
		#Save results to a file (instead of displaying on the screen)
		grep "error" logfile.txt > results.txt
		
		#Suppress permission denied errors
		grep -r "password" /etc 2>/dev/null

		```
### **awk** tool

- **awk** is an alternative to **grep**
- Its an advanced tool and will be described in a separate section

---
## 4. User and Group Managment
(These commands are for Ubuntu/Debian releases only)

### **User ID (UID)**:

- In Linux, every user is assigned a unique number called a User ID (UID).
- This number is how the system identifies users internally, not by their username.
- The username is just a human-readable label for the UID.

### **Group ID (GID)**

- Just like users have UIDs, groups have Group IDs (GIDs).
- Groups are used to manage permissions for multiple users together.

### **Primary vs. Supplementary Groups**

- A user named xyz is created with a unique UID.
- A group named xyz is also created with the same name and a unique GID.
- This group becomes the user’s primary group.
- A user can be assigned to supplementary groups (additional groups)

### Typical UID ad GID ranges
| Range        | Purpose                | Description                                |
|--------------|------------------------|--------------------------------------------|
| 0            | Root user / root group | Superuser with full system privileges      |
| 1 – 99       | System users/groups    | Reserved for system accounts and services  |
| 100 – 999    | System users/groups    | Reserved for system accounts (varies by distro) |
| 1000+        | Regular users/groups   | Default range for normal user accounts and groups |



### Relevant commands
??? "User & Group Managent (click to view)"

	| Command Syntax          | Example          | Description                    |
	|-------------------------|------------------|--------------------------------|
	| `adduser <username>`    | `adduser mujeeb`    | Creates a new user named `mujeeb` |
	| `usermod -aG sudo <username>`     | `usermod -aG sudo mujeeb` | Adds user `mujeeb` to the `sudo` group |
	| `usermod -aG <group> <username>`     | `usermod -aG Lab1 mujeeb` | Adds user `mujeeb` to the `Lab1` group |
	| `deluser <username>`           | `deluser mujeeb`        | Deletes user `mujeeb`|
	| `gpasswd -d <username> sudo`      | `gpasswd -d mujeeb sudo`     | Removes user `mujeeb` from `sudo` group |
	| `deluser <username> sudo`         | `deluser mujeeb sudo`        | Alternative to remove `mujeeb` from `sudo` group |
	| `groups <username>`                | `groups mujeeb`               | Lists all groups the user belongs to |
	| `id <username>`                    | `id mujeeb`                   | Shows UID, GID, and group memberships                     |
	| `id <username>`                    | `id mujeeb`                   | Shows UID, GID, and group memberships                     |
	


---
## 5. Firewall, ```ufw```

###Firewall and ```iptables```

- A firewall is a security system (hardware or software) that monitors and controls incoming and outgoing network traffic based on predetermined security rules.

- ```iptables``` is a Linux command-line tool to configure the **netfilter** firewall built into the Linux kernel.
- It manages rules that determine how incoming and outgoing packets are handled (accept, drop, reject).
- Powerful and flexible, but can be complex for beginners.
- Works by manipulating tables of rules for packet filtering, [NAT](../linux-networking/nat1.md), and more.

### UFW

- UFW is a user-friendly frontend for managing firewall rules on Linux systems. 
- It simplifies configuring iptables (the underlying Linux firewall system) by providing easy-to-use commands to allow or deny network traffic


??? "Ubuntu Firewall (UFW) (click to view)"
	| Command                          | Description                                |
	|---------------------------------|--------------------------------------------|
	| `sudo ufw enable`               | Enable the firewall                        |
	| `sudo ufw disable`              | Disable the firewall                       |
	| `sudo ufw status`               | Show current firewall status               |
	| `sudo ufw status verbose`       | Show detailed firewall status              |
	| `sudo ufw allow 22`             | Allow incoming SSH connections (port 22)  |
	| `sudo ufw allow 80/tcp`         | Allow HTTP traffic                          |
	| `sudo ufw deny 23`              | Deny incoming connections on port 23      |
	| `sudo ufw delete allow 80/tcp` | Remove the rule allowing HTTP traffic      |
	| `sudo ufw reset`                | Reset firewall rules to default             |


---
## File Compression and Archiving
WIP

---
## System Monitoring and Process Management
WIP

---
## Package Management
WIP

