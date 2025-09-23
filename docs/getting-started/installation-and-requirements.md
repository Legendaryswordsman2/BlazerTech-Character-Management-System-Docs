# Installation and Requirements

This guide covers the **requirements** and **installation steps** for the **BlazerTech Character Management System** (BT-CMS).

---

## Requirements

> [!NOTE]  
> All required packages must be installed and correctly configured **before importing BT-CMS**.

| Package | Purpose | Notes / Links |
|---------|---------|---------------|
| **Addressables** | Dynamically load/unload character spritesheets. | Found in the **Unity Registry** via Package Manager. |
| **Naughty Attributes** | Adds additional attributes to the Unity Inspector. | [Installation Guide](https://dbrizov.github.io/na-docs/general/installation.html) <br> [Unity Asset Store Link](https://assetstore.unity.com/packages/tools/utilities/naughtyattributes-129996) |

> [!IMPORTANT]  
> **Addressables Settings file** must be created **before** importing BT-CMS. If not created beforehand the included characters will not be functional.
> To create the settings file navigate to: `Window > Asset Management > Addressables > Groups > Create Addressables Settings`.

---

## Installation Steps

### prerequisites
Make sure **Naughty Attributes** and **Addressables** are both installed and the **Addressables Settings file** has been creeated ([See above^^](#requirements)).

### Importing
**Itch.io:**
- If bought from Itch.io, download `BlazerTech Character Management System.unitypackage` and drag and drop it into your project.

**Unity Asset Store:**
- If bought from the Unity Asset Store, navigate to `Window > Package Manager > My Assets` and find `BlazerTech Character Management System` from within the list. Click `Download` if not already downloaded and then `Import`.

**Import Popup:**
- Regardless of the installation method a popup will appear prompting you to import the `BlazerTech Character Management System` into your project. Make sure all assets are selected and click the `Import` button.  
![Import Popup](~/images/setup/import-popup.png)

### After Installtion
Here's some things to do after installing the **BlazerTech Character Management System**:
1. **Play sample scenes** - Go into the **Samples** folder and run some of the sample scenes to make sure everything is functioning properly.
2. **Create your own character type** - make a new character type to use your own spritesheets or third party ones.  
[🔗 Read More → Character Types](xref:character-types)
3. **Implement a character creation menu** - Use the modular Character Creator System to create your own in-game character creation menu..  
[🔗 Read More → Character Creator Overview](xref:character-creator-overview)