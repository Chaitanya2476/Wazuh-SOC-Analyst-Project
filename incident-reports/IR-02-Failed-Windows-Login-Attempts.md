# Incident Report 02 – Failed Windows Login Attempts

## Incident Summary

Multiple failed login attempts were detected on the monitored Windows endpoint. The activity was intentionally generated in the lab environment to validate authentication monitoring and alert generation capabilities within Wazuh.

## Severity

Medium

## Detection Source

* Wazuh SIEM
* Windows Security Event Logs

## Date

15-07-2026

## Description

Several incorrect login attempts were performed on the Windows endpoint. The failed authentication events were collected by the Wazuh agent and forwarded to the Wazuh Manager, where alerts were generated and reviewed.

## Timeline

1. Incorrect credentials were entered on the Windows system.
2. Windows generated failed authentication events.
3. Wazuh agent collected the logs.
4. Wazuh Manager analyzed the events and generated alerts.
5. Alerts were reviewed in the Wazuh Dashboard.

## Indicators of Compromise (IOCs)

* Event Type: Failed Logon
* Source: Windows Security Logs
* Event ID: 4625

## MITRE ATT&CK Mapping

* T1110 – Brute Force

## Investigation Findings

The failed login attempts were intentionally generated for testing and validation purposes. No unauthorized access was achieved.

## Remediation

* Monitor repeated authentication failures.
* Configure alert thresholds for excessive failed logins.
* Investigate repeated failures from unknown sources in production environments.

## Lessons Learned

* Wazuh successfully detected failed authentication attempts.
* Windows Event ID 4625 is useful for identifying brute-force activity.
* SIEM monitoring provides visibility into authentication-related events.
