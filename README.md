# Wazuh SOC Analyst Project

![Wazuh](https://img.shields.io/badge/Wazuh-SIEM-blue)
![Python](https://img.shields.io/badge/Python-Automation-yellow)
![Windows](https://img.shields.io/badge/Windows-Endpoint-blue)
![SOC](https://img.shields.io/badge/SOC-Analyst-green)

## Project Overview

This project demonstrates the deployment and use of a Security Information and Event Management (SIEM) platform using Wazuh for security monitoring, log analysis, and threat detection. The lab simulates a SOC environment where security events are collected, analyzed, and investigated.

## Objectives

* Deploy and configure a Wazuh SIEM environment.
* Connect a Windows endpoint to Wazuh.
* Collect and analyze Windows event logs.
* Detect suspicious activities such as PowerShell execution and failed login attempts.
* Perform threat hunting and incident investigation.

---

## Lab Environment

| Component      | Details                 |
| -------------- | ----------------------- |
| SIEM Platform  | Wazuh                   |
| Server OS      | Ubuntu Server 24.04 LTS |
| Endpoint OS    | Windows                 |
| Virtualization | VMware Workstation      |
| Log Collection | Wazuh Agent + Sysmon    |
| Dashboard      | Wazuh Dashboard         |

---

## Architecture

```text
Windows Endpoint (Wazuh Agent + Sysmon)
                 │
                 ▼
           Wazuh Manager
                 │
                 ▼
           Wazuh Indexer
                 │
                 ▼
          Wazuh Dashboard
```

---

## Detection Scenarios

### 1. Wazuh Server Health Status

Verified the operational status of the Wazuh Manager, Indexer, and Dashboard services.

### 2. Wazuh Dashboard

Accessed and monitored security events using the Wazuh web dashboard.

### 3. Agent Connected

Successfully registered and connected the Windows endpoint to the Wazuh server.

### 4. Threat Hunting – Windows Event Logs

Performed searches and investigations on Windows security events.

### 5. PowerShell Detection

Generated PowerShell activity and observed its detection within Wazuh.

### 6. Failed Windows Login Attempts

Simulated failed login attempts and analyzed authentication events.

### 7. Suspicious Windows CMD Shell Execution

Executed command prompt activities and investigated the generated alerts.

### 8. Wazuh SOC Architecture Diagram

Created an architecture diagram to demonstrate the flow of logs and alerts within the SIEM environment.

---

## Screenshots

* SS1 – Wazuh Server Health Status
* SS2 – Wazuh Dashboard
* SS3 – Agent Connected
* SS4 – Threat Hunting – Windows Event Logs
* SS5 – PowerShell Detection
* SS6 – Failed Windows Login Attempts
* SS7 – Suspicious Windows CMD Shell Execution
* SS8 – Wazuh SOC Architecture Diagram

---

## Skills Demonstrated

* Security Monitoring
* SIEM Administration
* Log Analysis
* Threat Hunting
* Incident Investigation
* Windows Event Analysis
* Endpoint Monitoring
* SOC Operations

---

## Tools Used

* Wazuh
* Ubuntu Server
* VMware Workstation
* Windows
* Sysmon
* PowerShell
* Command Prompt

---

## MITRE ATT&CK Techniques

| Technique | Description                         |
| --------- | ----------------------------------- |
| T1059.001 | PowerShell                          |
| T1059.003 | Windows Command Shell               |
| T1110     | Brute Force / Failed Login Attempts |
| T1082     | System Information Discovery        |
| T1005     | Data from Local System              |

---

## Key Learning Outcomes

* Deployment and management of a SIEM solution.
* Security event collection and correlation.
* Detection of suspicious activities on Windows endpoints.
* Investigation and analysis of security alerts.
* Understanding of SOC workflows and incident response processes.

---

## Future Improvements

* Add custom Sigma detection rules.
* Integrate additional endpoints.
* Create automated incident response scripts.
* Develop advanced threat-hunting use cases.

## Author

**Chaitanya**
MSc Cybersecurity Student | Aspiring SOC Analyst | Learning Threat Detection and Incident Response.
