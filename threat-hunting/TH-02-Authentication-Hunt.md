# Threat Hunt 02 – Failed Login Investigation

## Objective

Identify failed authentication attempts on the Windows endpoint.

## Data Source

* Windows Security Logs
* Wazuh SIEM

## Hunt Query

Search for:

* Event ID 4625

## Findings

Multiple failed login events were identified and reviewed in the Wazuh Dashboard.

## Analysis

The failed login attempts were intentionally generated within the lab environment and did not result in unauthorized access.

## MITRE ATT&CK

* T1110 – Brute Force

## Conclusion

The investigation confirmed that Wazuh successfully collects and displays authentication-related security events.
