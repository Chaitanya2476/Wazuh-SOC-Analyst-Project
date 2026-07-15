# Incident Report 04 – Windows Event Log Threat Hunting

## Incident Summary

Threat hunting activities were performed on Windows event logs collected by Wazuh to identify suspicious or abnormal behavior on the monitored endpoint.

## Severity

Informational

## Detection Source

* Wazuh SIEM
* Windows Event Logs

## Date

14-07-2026

## Description

Windows event logs were reviewed through the Wazuh Dashboard to validate log collection, search capabilities, and event visibility. The exercise focused on identifying security-relevant events and understanding endpoint activity.

## Timeline

1. Windows endpoint generated system and security events.
2. Wazuh agent collected the event logs.
3. Events were forwarded to the Wazuh Manager and indexed.
4. Threat hunting queries were performed in the Wazuh Dashboard.
5. Relevant events were reviewed and analyzed.

## Indicators of Compromise (IOCs)

* Windows Security Events
* System Events
* Process Creation Events
* Authentication Events

## MITRE ATT&CK Mapping

* T1082 – System Information Discovery

## Investigation Findings

No malicious activity was identified during the threat hunting exercise. The activity confirmed that Windows event collection and log visibility were functioning correctly.

## Remediation

* Continue periodic threat hunting activities.
* Develop additional detection rules for high-risk events.
* Establish baselines for normal endpoint behavior.

## Lessons Learned

* Wazuh provides effective visibility into Windows events.
* Threat hunting improves understanding of endpoint activity.
* Continuous log analysis helps identify potential threats early.
