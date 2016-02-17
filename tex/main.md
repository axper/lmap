# Lmap

# Abbreviations
lmap - local nmap
TCP -
UDP -
IDS - Intrusion detection system
psutil - process utilities

# Preface

## Current approach
It is a common job of system administrators to perform port scans of their systems.
Such scans help the administrators to find vulnerabilities in the system earlier than a possible attacker.
To perform such scans administrators use tools like nmap, nessus, accunetix which scan all possible ports from the
outside and report the open ports and found vulnerabilities to the administrator. However, this has a few downsides:

- Scanning every TCP and UDP often requires a lot of time
- It consumes network resources and might make some systems unavailable during the scan process
- in certain scanning might even trigger a false alarm in IDS.

## An alternative
In this document, we present an alternative way of evaluating server vulnerabilities which scans the system for
vulnerabilities from the inside, as opposed to the outside.

This program is partially inspired by Microsoft Baseline Security Analyzer

This program leaves a lot of thinking to the user,

This program automatically scans configuration files of running services and reports known misconfigurations to the
user.

# How it works
Firstly the program discovers all open TCP and UDP ports on current system. Then for every open port it scans
the configuration file of the service for known security misconfigurations and blank passwords and reports them to
the user.

# Common configuration mistakes
- Blank passwords
- Path traversal
- Usage of SSL (1.0 – 3.0) and TLS 1.0
- Using SSH passphrase

# Services

## MySQL
MySQL is one of the most popular relational database engines in the world. [4]
The program scans the following configuration files for errors:

- /etc/my.cnf
- /etc/mysql/my.cnf
- ~/.my.cnf

# Apache HTTPD

# Requirements
The project requires:

Python 3.5.1
psutil library

# Sources:
http://sectools.org/
https://docs.python.org/2/library/socket.html
https://pythonhosted.org/psutil/
[4] http://db-engines.com/en/ranking