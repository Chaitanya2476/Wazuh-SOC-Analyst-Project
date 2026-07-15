# Incident Report 01 – PowerShell Activity Detection

## Incident Summary

A PowerShell process execution was detected on the monitored Windows endpoint. The activity was generated intentionally within the lab environment to validate Wazuh's ability to detect and log PowerShell execution events.

## Severity

Medium

## Detection Source

* Wazuh SIEM
* Windows Endpoint (Wazuh Agent + Sysmon)

## Date

15-07-2026

## Description

PowerShell was executed on the Windows endpoint and corresponding events were collected by the Wazuh agent. The Wazuh Manager processed the logs and generated an alert indicating PowerShell process activity.

## Timeline

1. User executed PowerShell on the Windows endpoint.
2. Sysmon generated process creation events.
3. Wazuh agent collected the logs.
4. Wazuh Manager analyzed the events and generated an alert.
5. The alert was reviewed in the Wazuh Dashboard.

## Indicators of Compromise (IOCs)

* Process: `powershell.exe`
* Host: Windows endpoint
* Event Source: Sysmon Process Creation

## MITRE ATT&CK Mapping

* T1059.001 – PowerShell

## Investigation Findings

The activity was determined to be authorized and intentionally generated for lab validation purposes. No malicious activity was identified.

## Remediation

No remediation required. Continue monitoring PowerShell usage and implement alert tuning for production environments.

## Lessons Learned

* Wazuh successfully detected PowerShell execution events.
* Sysmon integration improves endpoint visibility.
* SIEM platforms can effectively monitor administrative scripting activity.
