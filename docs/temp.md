---
uid: temp
summary: Configure global settings for the **BlazerTech Character Management System**.
---

# Project Settings

All global settings for the **BlazerTech Character Management System** are managed through the Project Settings window:  
**`Edit → Project Settings → BlazerTech → Character Management System`**

![Project Settings](~/images/project-settings.png)

---

## ⚙️ Overview

The Project Settings panel provides control over **how characters and groups are saved**, and includes **debugging options** for monitoring internal CMS events.

---

## 💾 Saving Settings

Configure how and when **Character Groups** are automatically saved to disk.

### **Auto Save Triggers**

A multi-select dropdown defining the events that trigger automatic saves.

| Option | Description |
|---------|--------------|
| **Game Exit** | Saves all character groups when the application quits. |
| **Character Creator Save** | Saves whenever a character is saved from the Character Creation Menu. |
| **Scene Change** | Saves when the active scene changes. |

> [!TIP]
> Multiple triggers can be active simultaneously.

---

### **Save Format**

Select how character groups are serialized to disk.

| Format | Description |
|---------|-------------|
| **JSON** | Human-readable format (`.json`). Easy to open and manually edit. |
| **Binary** | Compact binary format (`.bin`). Much harder to read or modify manually. |

> [!NOTE]
> Binary saves are more secure against tampering, while JSON saves are ideal during development and debugging.

---

## 🧩 Debug Options

These settings control which CMS logs appear in the Unity Console — useful for diagnosing issues or monitoring runtime behavior.

### **Logs To Show**

A multi-select dropdown defining which types of logs are displayed.

| Log Type | Description |
|-----------|--------------|
| **Character Group Save Trigger Logs** | Logs when character groups are saved. |
| **New Character Created Logs** | Logs when new characters are created. |
| **Character Recreated From DTO Logs** | Logs when a character is reconstructed from saved data (DTO). |
| **Loaded Character Updated Logs** | Logs when an already loaded character is modified. |
| **Character Creation Menu Logs** | Logs events within the Character Creation Menu (UI, randomization, saves, etc.). |

> [!TIP]
> Disable unneeded log types in release builds to reduce console noise.

---

## 🧠 Related Topics
- [Character Groups](xref:character-groups)
- [Character Creation Menu](xref:character-creator)
- [Saving & Loading System](xref:saving-and-loading)
