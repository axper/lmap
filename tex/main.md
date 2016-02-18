# Lmap

# Abbreviations
lmap - local nmap
TCP -
UDP -
IDS - Intrusion detection system
psutil - process utilities

# Preface

## Current approach of system vulnerability detection
It is a common job of system administrators to perform port scans of their systems.
Such scans help the administrators to find vulnerabilities in the system earlier than a possible attacker.
To perform such scans administrators use tools like nmap, nessus, accunetix etc. Network port scanning process looks
like this:

1. The administrator determines the address and port range(s) for scanning
2. He points the port scanning program to these ranges and starts the scan
3. The program probes every possible IP address and port combination
4. If a port is detected to be open, a special script is run which tries to guess details about that service
(name, version, configuration, available usernames etc)
5. Results are reported to the administrator in chosen format (xml or console output for nmap)

However, this approach has a few downsides:

- Scanning every TCP and UDP port requires a lot of time
- It consumes network resources and might make some systems unavailable during the scan process
- In certain scenarios port scanning might trigger a false alarm in IDS
- False positives and incorrect service detections are possible
- If the service is using an unusual port, it might not be discovered during the scan

## An alternative
In this document, we present an alternative way of evaluating server vulnerabilities which scans the system for
vulnerabilities from the inside

This program is partially inspired by Microsoft Baseline Security Analyzer

This program leaves a lot of thinking to the user,

This program automatically scans configuration files of running services and reports known misconfigurations to the
user.

# How it works
Firstly the program discovers all open TCP and UDP ports on current system. Then for every open port it scans
the configuration file of the service for known security misconfigurations and blank passwords and reports them to
the user.

Besides determining whether a port is open or not, it checks to see whether it is filtered by a firewall.

# Common configuration mistakes
- Blank passwords
- Path traversal
- Usage of SSL (1.0 – 3.0) and TLS 1.0
- Using SSH passphrase

# Updates
The script checks the last time the system was updated. If it was updated more than the amount given in lmap's config
file, a warning is issued.

## Debian/APT-based systems
[8] Lmap checks for last access date of `/var/cache/apt/` directory to determine the last time `sudo apt-get update`
command was run.

## Red Hat/YUM based systems
[9] Lmap checks the last time the `sudo yum update` command was run by grep'ing the output of `yum history`

## Arch/Pacman based systems
[10] Lmap checks the last time the `sudo pacman -Syu` command was run by parsing the output of `/var/lob/pacman.log`

# Logging in as root
Lmap checks whether the current user's session is login and it has admin privileges. If yes, then a warning is issued
. [12]
If the user runs `lmap` with sudo, the program detects that and no warning is issued.

# Empty passwords
If the server is externally accessible by services which use local linux user accounts, then Lmap checks whether there
are any users who blank passwords. [13] This is done by:

    awk -F: '($2=="") {print}' /etc/shadow
    
## Make Sure No Non-Root Accounts Have UID Set To 0
[15]
awk -F: '($3 == "0") {print}' /etc/passwd

# Services

## SSHd
The SSH server config file is located at:

- /etc/ssh/sshd_config

1. Most dangerous misconfiguration is enabling SSH v1 protocol. It's vulnerability was exploited in the wild by the
WOOT project [7].
2. Checks whether SSH password login is enabled. If it is, a weak warning is issued [11]:

    cat PasswordAuthentication no

## MySQL
MySQL is one of the most popular relational database engines in the world. [4]
The program scans the following configuration files for errors:

- /etc/my.cnf
- /etc/mysql/my.cnf
- ~/.my.cnf

## Telnet
If running telnet instance is found, a warning is issued. [13]

## FTP
If running FTP daemon is not:

- read-only
- anonymous (no password)

then a warning is issued against using FTP. FTP is insecure because the username/password is transmitted in clear 
text. [14]

# Apache HTTPD

# Requirements
The project requires:

Python 3.5.1
psutil library

# Sources:
[1]http://sectools.org/
[2]https://docs.python.org/2/library/socket.html
[3]https://pythonhosted.org/psutil/
[4]http://db-engines.com/en/ranking
[5]http://www.yolinux.com/TUTORIALS/LinuxTutorialInternetSecurity.html
[6]http://www.yolinux.com/TUTORIALS/LinuxTutorial-woot-project.html
[7]http://www.iss.net/threats/advise100.html
[8]http://serverfault.com/questions/20747/find-last-time-update-was-performed-with-apt-get
[9]http://serverfault.com/questions/389650/how-to-check-when-yum-update-was-last-run
[10]https://bbs.archlinux.org/viewtopic.php?id=150428
[11]https://www.digitalocean.com/community/tutorials/7-security-measures-to-protect-your-servers
[12]http://askubuntu.com/questions/16178/why-is-it-bad-to-login-as-root
[13]http://www.tecmint.com/linux-server-hardening-security-tips/
[14]https://www.digitalocean.com/community/tutorials/an-introduction-to-securing-your-linux-vps
[15]http://www.cyberciti.biz/tips/linux-security.html
