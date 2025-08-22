---
tags:
  - RM530N-GL
  - at commands
---
Under Construction

# Quectel AT Command Reference

Applicable to following Quectel models:

- RG520N
- RG52xF
- RG530F
- RM520N
- RM530N


---
## 1. Reference manaul 
Source:  [Quectel_AT_Commands_Manual_PDF](Quectel_RG520N&RG52xF&RG530F&RM520N&RM530N_Series_AT_Commands_Manual_V1.0.0_Preliminary_20220812.pdf)

---
## 2. Command categories

### SIM-related AT commands
???+ "SIM Card"
	|AT Command|Purpose|Example|Expected Output|
	|---|---|---|---|
	|```AT+CPIN?```|Check SIM card status|```AT+CPIN?```|``` +CPIN: READY``` (SIM is already unlocked)|
	|```AT+CPIN=<pin>```|Enter SIM PIN to unlock SIM|```AT+CPIN="1234"```|```OK``` or ```ERROR``` if PIN wrong|
	|```AT+CSIM```|	Send raw APDU commands to SIM (advanced use only)|```AT+CPIN?```|+CPIN: READY (SIM is already unlocked)|
	|```AT+QCCID```|Read SIM card ICCID (serial number)|```AT+QCCID```|+QCCID: 898600xxxxxxxxxxxx OK|
	|```AT+CLCK```|Enable/disable SIM lock (PIN protection)|```AT+CLCK="SC",0,"1234"```|OK – disables SIM lock|
	|```AT+CPWD```|Change SIM PIN code|```AT+CPWD="SC","1234","5678"```|OK|
	|```AT+CLCK?```|Check if SIM PIN lock is enabled|```AT+CLCK="SC",2```|	+CLCK: 1 (enabled), +CLCK: 0 (disabled)|
	



---
## Some useful links

[Quectel_AT_Commands_Manual_PDF](Quectel_RG520N&RG52xF&RG530F&RM520N&RM530N_Series_AT_Commands_Manual_V1.0.0_Preliminary_20220812.pdf)
