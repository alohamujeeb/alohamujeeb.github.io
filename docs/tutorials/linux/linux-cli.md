---
tags:
  - Linux
---

# Linux CLI Reference
This page provides quick-access cheat sheets for Linux CLI commands.

---
## Files and Directories
??? "Files and Directories (click to view)"
	
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
## File Searching
??? "File/Content Searching (click to view)"

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
		|```find /tmp -type f -name "*.tmp" -exec rm {} \;```| Delete all .tmp files|
		|```find . -type f -empty -exec rm {} \;```| Delete empty files|
		|```find /backup -type f -mtime +30 -exec rm {} \;```| Delete files older than 30 days|
		|```find ~/Downloads -type f -mtime +30 -exec rm {} \;```| Delete files older than 30 days|
		

	Note: **-exec** is not the same as the shell’s built-in **exec** command — they're totally different things, even though they share the word "exec."
	
	- exec some_command  (this is part of shell itself)
	- The -exec Option in the find Command is not same as exec...It is just an option of the 'find command itself"
	

---
## execute a command (exec vs -exec)
??? "File/Content Searching (click to view)"

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
	
### exec vs -exec

- **-exec** is not the same as the shell’s built-in exec command — they're totally different things, even though they share the word "exec."

- **exec some_command** (this is part of shell itself)
The -exec Option in the find Command is not same as exec...It is just an option of the 'find command itself"

### When to use "exec"
??? note "When to use **exec** (click to find out about various scenarios/use-cases)"
	- It is used to **Replace the Shell with Another Program**: Useful in scripts or login environments where you want to run a program instead of a shell — and don’t need to return.
	
	
	- To Save Memory in Scripts: In long-running scripts, especially daemons, using exec prevents spawning a new process. It replaces the shell, saving memory and process overhead.
	
	
	- To Redirect Input/Output for the Entire Shell or Script: exec can be used to change stdin, stdout, or stderr at the shell level — affecting all commands that follow.
	
	- To Replace the Shell in System Startup Scripts: In init or systemd environments, exec is used so that the shell process doesn’t hang around. This is cleaner and avoids zombie processes.
	- To Chain Commands with Replacement: You can use it at the end of a script to "handoff" control to another process, especially for chaining tools or launching shells.

### When NOT to use "exec"
??? warning "When NOT to use **exec** (click to find out)"
	
	- Once executed, the shell is gone. If you accidentally use exec instead of running a command normally, your terminal may close (especially with GUI apps).
	
	- For most everyday tasks (like ls, rm, etc.), you should just run the command normally, not with exec.

---
## Finding text in file(s)
WIP

---
## User and Permission Managment
WIP


---
## File Compression and Archiving
WIP

---
## System Monitoring and Process Management
WIP

---
## Package Management
WIP

---
## Networking
WIP
