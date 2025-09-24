---
uid: basic-concepts
---

# Basic Concepts

This page introduces the **core principles** of the Character Management System:  
- [**Character Types**](#character-types) – Define how characters are structured.  
- [**Character Templates**](#character-templates) – Blueprints for creating characters later.  
- [**Character Usage**](#character-usage) – Scripts to load and manage characters.  
- [**Character Creator**](#character-creator) – Modular UI framework for building customizable characters in-game.  

---

## Character Types
A **Character Type** defines how a character works. There are two kinds:

| Type                       | Description                                                                            | Best For                                                    |
| -------------------------- | -------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Unified Character Type** | A single spritesheet containing a fully assembled character. No runtime customization. | Characters with fixed, pre-set appearances.                 |
| **Layered Character Type** | Multiple spritesheets, each containing one visual layer (body, outfit, hair, etc.).    | Customizable player characters, dynamic or randomized NPCs. |

- [Read More → Character Types](xref:character-types)  
- [Read More → Unified Character Type](xref:unified-character-type)  
- [Read More → Layered Character Type](xref:layered-character-type)  

---

## Character Templates
A **Character Template** is a [Scriptable Object](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ScriptableObject.html) that acts as a **blueprint** for creating characters later. Templates are supported for both **Unified** and **Layered Characters**.

[Read More → Character Templates](xref:character-templates)  

---

## Character Usage

### Character Loader Components
Once a **Unified or Layered Character** has been created, it can be loaded using one the following scripts:

| Loader                                                                                      | Purpose                                          |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| [Layered Character Loader](xref:character-usage#layered-character-loader)                   | Load pre-existing Layered Characters.            |
| [Layered Character Template Loader](xref:character-usage#layered-character-template-loader) | Create/load a Layered Character from a template. |
| [Unified Character Loader](xref:character-usage#unified-character-loader)                   | Create/load a Unified Character from a template. |

### Character Shader
Shaders are how the final Unified or Layered Character are rendered. Sprites from the **Base Spritesheet** defined in the **Character Type** are used in a renderer component such as a **Sprite Renderer**.

If a **Unified Character** is used, the shader takes the single spritesheet of the character and shows that over the **Base Spritesheet**.  
If a **Layered Character** is used, the shader combines all layers into the final rendered character.  

[Read More → Character Usage](xref:character-usage)  

---

## Character Creator
The **Character Creator** is a prefab based **Character Creation Menu Framework**.  
Prefabs can be combined and customized to create whatever design you want.  
It makes the process of building a **Character Creation Menu** into your game easy.  

> [!TIP]  
> The **Character Creator** only works with **Layered Characters**. **Unified Characters do not support runtime customization.**

### Example Use Cases
1. **Customizable Player Character** – Easily setup the menu for a single character such as the player character. 
2. **Editing Character Lists** – Allow players to edit a predefined roster, or manage a dynamic list (create, edit, delete).  

### Key Features
| Feature               | Description                                                         |
| --------------------- | ------------------------------------------------------------------- |
| **Layer Selectors**   | Dropdowns, carousels, tabs, etc.                                    |
| **Character Preview** | Static or animated, with options to rotate or swap animations.      |
| **History Tracking**  | Every change is logged and can be shown as text or image snapshots. |
| **Randomization**     | Randomize the entire character or specific layers.                  |
| **Loading Screens**   | Customizable loading screens which hide the menu until it's ready.  |
| **Character Naming**  | Optional name field.                                                |

[Read More → Character Creator](xref:character-creator-overview)