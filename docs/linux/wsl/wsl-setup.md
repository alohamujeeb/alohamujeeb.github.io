---
tags:
  - WSL
  - Windows Subsystem for LInux
---

# Windows Subsystem for Linux (WSL) Quick Reference
This page provides quick-access cheat sheets for WSL installation and setup.

**Note: This is not an exhaustive guide—just a concise reference for commonly used commands.**

---
## 1. What is WSL
- Windows Subsystem for Linux (WSL) allows us to run a Linux environment directly on Windows without needing a virtual machine or dual boot.

- It lets us install and use Linux distributions (such as Ubuntu) alongside Windows tools, making it easy to run Linux commands, develop software, and manage files.

- WSL is lightweight, starts quickly, and integrates well with Windows, allowing **seamless switching between environments**.

- This document is a quick reference of commands for installing and setting up WSL using Windows PowerShell.

---
## 1. Installation 

| Description | Command / Method |
|------------|-----------------|
| Install WSL with default distro | `wsl --install` |
| Install a specific distro (PowerShell) | `wsl --install -d Ubuntu-20.04` |
| Install another distro (PowerShell) | `wsl --install -d Ubuntu-22.04` |
| Install another distro (PowerShell) | `wsl --install -d Ubuntu-24.04` |
| Install distro with custom name | `wsl --install -d Ubuntu-24.04 --name u24-mdc` |
| Install distro via Microsoft Store | Open Store → search distro → Click Get / Install |


---
## 2. General commands

| Description | Command |
|------------|--------|
| List all installed distros (detailed: state + version) | `wsl -l -v` |
| List all installed distros (simple) | `wsl -l` |
| Launch a specific distro | `wsl -d Ubuntu-22.04` |
| Run a Linux command from Windows | `wsl ls -la` |
| Run a command in a specific distro | `wsl -d Ubuntu-22.04 ls -la` |
| Shut down all running distros | `wsl --shutdown` |
| Terminate a specific distro | `wsl --terminate Ubuntu-20.04` |
| Set default distro | `wsl --set-default Ubuntu-24.04` |
| Set default distro (custom name) | `wsl --set-default u24-mdc` |
| Set WSL version for a distro (1 or 2) | `wsl --set-version Ubuntu-22.04 2` |
| Set default WSL version for new installs | `wsl --set-default-version 2` |
| Show WSL status | `wsl --status` |
| Export a distro to a backup file | `wsl --export Ubuntu-22.04 backup.tar` |
| Import a distro from a backup | `wsl --import NewDistro C:\WSL\NewDistro backup.tar` |
| Unregister (delete) a distro ⚠️ | `wsl --unregister Ubuntu-20.04` |






