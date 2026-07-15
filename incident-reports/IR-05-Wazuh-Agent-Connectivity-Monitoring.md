# Incident Report 05 – Wazuh Agent Connectivity Monitoring

## Incident Summary

The connectivity status of the Windows Wazuh agent was monitored to verify successful communication between the endpoint and the Wazuh server.

## Severity

Informational

## Detection Source

* Wazuh Agent Management
* Wazuh Dashboard

## Date

14-07-2026

## Description

The Windows endpoint was successfully registered and connected to the Wazuh Manager. The monitoring activity verified that logs were being transmitted and processed correctly.

## Timeline

1. Wazuh agent was installed on the Windows endpoint.
2. Agent registration was completed.
3. Connection with the Wazuh Manager was established.
4. Agent status was verified in the Wazuh Dashboard.
5. Log ingestion from the endpoint was confirmed.

## Indicators of Compromise (IOCs)

* Agent Status: Active
* Endpoint Communication: Successful
* Log Collection: Operational

## MITRE ATT&CK Mapping

* N/A – Administrative Monitoring Activity

## Investigation Findings

The Wazuh agent was functioning correctly and continuously sending logs to the server. No connectivity issues were identified.

## Remediation

* Regularly monitor agent status.
* Ensure agents remain updated.
* Investigate disconnected agents promptly.

## Lessons Learned

* Agent health monitoring is essential for SIEM visibility.
* Continuous log ingestion is critical for effective threat detection.
* Wazuh provides centralized monitoring of endpoint status.
