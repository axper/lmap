Server security measuring software
==================================

TOC
===

    Abbreviations
    Preface
        Why information security matters
        Aspects of information security
        Current approach of securing servers
            Antivirus
            Port scanning
    Requirements
        The problem
        An alternative
        Common configuration mistakes
    Implementation
        Updates
        Logging in as root
        Empty passwords
        Make Sure No Non-Root Accounts Have UID Set To 0
        Service-specific checks
            ...
        Software requirements
    P.S.
    Sources

Abbreviations
=============

Lmap - Local Nmap
TCP - Transmission control protocol
UDP - User datagram protocol
IDS - Intrusion detection system
psutil - python system and process utilities

Preface
=======

Why security matters
--------------------

### What is information security?

[20]
Information security is the process of preventing and detecting the unauthorized use of a computer. 

Prevention is the process of stopping unauthorized malicious people (also known as "attackers", "intruders", "hackers") of accessing
a part of the software or data they are not authorized to access.

Detection is the process of determining whether an attempt unauthorized access has took place, and if so, whether it was
successful and what exactly has been done.

### Why should we care about information security?

Nowadays we use computers in almost every aspect of our life. From banking and investing to shopping and communication,
computers have become an unseparable part of every business. It is hard to pinpoint a field which has not benefited
from the rise of information technology.

Although not all data stored by business can be considered "Top secret", administrators probably don't want strangers
looking at their internal communications, examining their personal information, and making changes in their computer.

### Why would anyone want to break into the system?

Attackers often do not care about about a user's or organization's identity.
Having control of a server not only puts the organization at a risk, but also visitors of the website. Attackers can also
use a compromised server to launch attacks on other organizations without discovering their true identity.
Having control over compromised server helps attackers carry out DDoS attacks.
An attacker has several reasons to break into a server:

* Monetary gain - Stealing details of your bank account and credit card
* Business disruption - An organization might pay hackers to cause chaos in their rival's network
* Information leakage - An organization might pay hackers to gain competitive advantage over a rival company by accessing it's secrets
* DDoS - To carry out distributed denial of service (DDoS) attacks on other servers
* SEO - A hacked website might be used to increase SEO of other sites by placing links to that site on the hacked website
* Base for further attacks - A hacked server might be used for broader attacks, having more servers helps them cover their true identity

* Fun - An attacker might do it for fun or amusement

Aspects of server security
--------------------------

Information security remains one of the most important issues businesses have to tackle today.[21]

1. Remove unnecessary services
Default operating system installations and configurations, are not secure. Many default services are installed, but not used,
such as print servers, samba shares etc. These services increase the attack surface by opening more ways for the
malicious user to abuse the system.

Administrators must disable or secure all unnecessary services via firewall.

2. Remote access
Connecting to the server using an unsecured, public network connection makes it possible for hackers to perform
attacks such as man-in-the-middle and data stealing.

Administrators must make sure that all remote connections to the servers are secured properly using encryption and
security tokens.

5. Permissions and privileges
Proper permissions management has an important role in server security. If a malicious user or process is given more privileges
than he needs to carry out his job, he can use that to compromise the server.

Administrators must make sure that all system users have only access to files and resources which are required to carry out their job.

6. Installing security updates on time
It is important to update the operating system and and the software with latest updates and security patches.
While installing updates can be somewhat dangerous, in means that it might introduce stability issues, administrators
must ensure that they are installed in a timely manner.

7. Monitoring and log audit
Logs are produces by every piece of software - the operating system, web applications, all kinds of services, databases, network, routers, switches etc.

These logs must be monitored and frequently checked, because logs can often indicate an upcoming attack. Even in case
of a successfully compromised system logs server as the only way to perform forensic analysis.

8. User accounts
Unused user accounts, such as of a laid off employee should be disabled along with accounts created by various services.

Every administrator accessing the server needs to have his own account and his own password, and correct privileges. Passwords should not be shared.

9. Remove unused modules and extensions
Applications such as web servers often contain a number of pre-defined default extensions and modules.
These modules can contain vulnerabilities and can increase the possible attack surface for the attacker.

Administrators must ensure that, whenever possible, only modules required by the web application are enabled.

11. Stay informed
Nowadays information about software and operating system, including security can be found freely on the internet.

Administrators must make sure that they and the users are constantly informed about latest news about attacks and vulnerabilities.

12. Use security scanners
Scanners are pieces of software which help automate and ease the process of securing a server and applications.

Software static/dynamic analysis tools such as Sonar for java, Valgrind for C etc help find bugs and vulnerabilities early
in application lifecycle.
Network security scanners help administrators to ensure the security of their servers. These tools are able to find open ports, 
vulnerabile services and even viruses.
A list of well known network scanners includes:
    1. Nmap
    2. Nessus
    3. Accunetix

13. Choose proper encryption and hashing algorithms
Use of broken encryption, communication and hashing protocols such as DES, SSL, MD5 should be avoided.

Weaknesses of these algorithms opens an attack vector for an attacker to exploit them.

Current approach of securing servers
------------------------------------

### Antivirus

For Windows-based servers, it is necessary to install antivirus software. [16]

The Antivirus scans the system during:

1. Scheduled/full scans
2. Runtime, i.e. when data is transmitted into the system

Antiviruses use different virus detection technologies:

1. Signature-based detection, when a file is compared with known virus code
2. Heuristic-based detection, when a file's execution behaviour is compared with common malicious patterns
3. Behaviour-based detection, . This is commonly used in IDS.

For Linux-based systems an antivirus is not commonly used. [17]
For Linux systems, an antivirus might be necessary when it is used to share files to windows hosts [19]

### Port scanning

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

Requirements
============

The purpose of this program is to scan server systems for:

- Misconfigurations
- Blank/Vulnerable passwords
- Insecure and broken protocols, algorithms and hashes

The program reports all the findings to the user.

The problem
-----------

The requirement of this document is to write a piece of software which will measure a Linux-based system's
security and given detailed report to the user

An alternative
--------------

In this document, we present an alternative way of evaluating server vulnerabilities which scans the system for
vulnerabilities from the inside

This program is partially inspired by Microsoft Baseline Security Analyzer

This program leaves a lot of thinking to the user,

This program automatically scans configuration files of running services and reports known misconfigurations to the
user.

Firstly the program discovers all open TCP and UDP ports on current system. Then for every open port it scans
the configuration file of the service for known security misconfigurations and blank passwords and reports them to
the user.

Besides determining whether a port is open or not, it checks to see whether it is filtered by a firewall.

Common configuration mistakes
-----------------------------

- Blank passwords
- Path traversal
- Usage of SSL (1.0 – 3.0) and TLS 1.0
- Using SSH passphrase

Implementation
==============

Updates
-------

The script checks the last time the system was updated. If it was updated more than the amount given in lmap's config
file, a warning is issued.

### Debian/APT-based systems

[8] Lmap checks for last access date of `/var/cache/apt/` directory to determine the last time `sudo apt-get update`
command was run.

### Red Hat/YUM based systems

[9] Lmap checks the last time the `sudo yum update` command was run by grep'ing the output of `yum history`

### Arch/Pacman based systems

[10] Lmap checks the last time the `sudo pacman -Syu` command was run by parsing the output of `/var/lob/pacman.log`

Logging in as root
------------------

Lmap checks whether the current user's session is login and it has admin privileges. If yes, then a warning is issued. [12]
If the user runs `lmap` with sudo, the program detects that and no warning is issued.

Empty passwords
---------------

If the server is externally accessible by services which use local linux user accounts, then Lmap checks whether there
are any users who blank passwords. [13] This is done by:

    awk -F: '($2=="") {print}' /etc/shadow
    
Make Sure No Non-Root Accounts Have UID Set To 0
------------------------------------------------

[15]
awk -F: '($3 == "0") {print}' /etc/passwd

Service-specific checks
-----------------------

### SSHd

The SSH server config file is located at:

- /etc/ssh/sshd_config

1. Most dangerous misconfiguration is enabling SSH v1 protocol. It's vulnerability was exploited in the wild by the
WOOT project [7].
2. Checks whether SSH password login is enabled. If it is, a weak warning is issued [11]:

    cat PasswordAuthentication no

### MySQL

MySQL is one of the most popular relational database engines in the world. [4]
The program scans the following configuration files for errors:

- /etc/my.cnf
- /etc/mysql/my.cnf
- ~/.my.cnf

### Telnet

If running telnet instance is found, a warning is issued. [13]

### FTP

If running FTP daemon is not:

- read-only
- anonymous (no password)

then a warning is issued against using FTP. FTP is insecure because the username/password is transmitted in clear 
text. [14]

### Apache HTTPD

Software requirements
------------

The project requires:

Any Unix-based system which can execute Python 3 files

- Python 3.5.1
- The `psutil` Python library library

P.S.
====

At the end of the day, the most important aspect of security is the people.
No monitoring, scanning and security system can protect from negligence and overlooking of security practices.

Sources
=======

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
[16]http://serverfault.com/questions/632/do-you-run-antivirus-on-your-windows-servers
[17]http://www.howtogeek.com/135392/htg-explains-why-you-dont-need-an-antivirus-on-linux-and-when-you-do/?PageSpeed=noscript
[18]https://antivirus.comodo.com/how-antivirus-software-works.php
[19]http://security.stackexchange.com/a/53462/37546
[20]http://cybercellmumbai.gov.in/html/general-tips/what_is_computer_security.html
[21]http://www.acunetix.com/websitesecurity/webserver-security/
[22]https://www.onehoursitefix.com/why-would-hackers-hack-my-website/