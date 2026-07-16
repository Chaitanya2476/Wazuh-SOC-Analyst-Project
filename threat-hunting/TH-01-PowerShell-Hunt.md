# Threat Hunt 01 – PowerShell Activity Investigation

## Objective

Identify PowerShell executions on the monitored Windows endpoint.

## Data Source

* Wazuh SIEM
* Sysmon Process Creation Events

## Hunt Query

Search for:

* powershell.exe
* rule.groups: sysmon

## Findings

PowerShell activity was identified and correlated with process creation logs collected by Wazuh.

## Analysis

The PowerShell execution was intentionally generated for lab validation purposes and no malicious behavior was observed.

## MITRE ATT&CK

* T1059.001 – PowerShell

## Conclusion

Wazuh successfully detected and logged PowerShell activity, demonstrating endpoint visibility and detection capabilities.
