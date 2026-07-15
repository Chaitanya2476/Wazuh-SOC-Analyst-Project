# Incident Report 03 – Suspicious CMD Shell Execution

## Incident Summary

A Command Prompt (CMD) process execution was detected on the monitored Windows endpoint. The activity was intentionally generated in the lab environment to validate process monitoring and alert generation capabilities within Wazuh.

## Severity

Medium

## Detection Source

* Wazuh SIEM
* Sysmon Process Creation Events

## Date

14-07-2026

## Description

A Command Prompt session was executed on the Windows endpoint. The event was captured by Sysmon and forwarded by the Wazuh agent to the Wazuh Manager, where an alert was generated and investigated.

## Timeline

1. Command Prompt was executed on the Windows endpoint.
2. Sysmon generated a process creation event.
3. Wazuh agent collected the event logs.
4. Wazuh Manager analyzed the logs and generated an alert.
5. The alert was reviewed in the Wazuh Dashboard.

## Indicators of Compromise (IOCs)

* Process: `cmd.exe`
* Event Source: Sysmon Process Creation
* Host: Windows Endpoint

## MITRE ATT&CK Mapping

* T1059.003 – Windows Command Shell

## Investigation Findings

The CMD execution was intentionally generated for lab testing and validation purposes. No malicious commands or unauthorized activities were identified.

## Remediation

* Monitor unusual or unexpected command shell executions.
* Restrict command shell access where appropriate.
* Investigate suspicious parent-child process relationships in production environments.

## Lessons Learned

* Wazuh successfully detected command shell activity.
* Sysmon provides valuable visibility into process execution.
* Process monitoring is essential for identifying potentially malicious behavior.
