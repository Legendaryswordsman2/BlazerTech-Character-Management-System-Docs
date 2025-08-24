---
uid: basic-concepts
---

# Basic Concepts

This page introduces the **core building blocks** of the Character Management System:  
- [**Character Types**](#character-types) – Define how characters are structured.  
- [**Character Templates**](#character-templates) – Blueprints for creating characters later.  
- [***Character Usage***](#character-usage) – Scripts to load and manage characters.  
- [**Character Creator**](#character-creator) – Modular system for building customizable characters in-game.  

---

## Character Types
A **Character Type** defines how a character works. There are two kinds:

| Type | Description | Best For |
|------|-------------|----------|
| **Unified Character Type** | A single spritesheet containing a fully assembled character. No runtime customization. | Characters with fixed, pre-set appearances. |
| **Layered Character Type** | Multiple spritesheets, each containing one visual layer (body, outfit, hair, etc.). | Customizable player characters. dynamic or randomized NPCs. |

- [🔗 Read More →  Character Types](xref:character-types)  
- [🔗 Read More → Unified Character Type](xref:unified-character-type)  
- [🔗 Read More → Layered Character Type](xref:layered-character-type)  

---

## Character Templates

A character template is a [Scriptable Object](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ScriptableObject.html) and can be thought of as a blueprint that can be used to create a character later. Templates are supported for both **Unified** and **Layered Characters**.

[🔗 Read More → Character Templates](xref:character-templates)  

---

## Character Usage

Once a **Character Type** has been created it can be loaded using the following scripts

- **Layered Character Loader** - Load pre-existing Layered Characters.
- **Layered Character Template Loader** - Create/load a layered character from a template.
- **Unified Character Loader** - Load a Unified Character from a template.
  
  [🔗 Read More → Loading Characters](xref:loading-characters)  

---

## Character Creator

The **Character Creator** is a fully modular menu system designed for **Layered Characters**.  
Easily build a character creation menu into your game using the included scripts and prefabs.

> [!TIP]  
> The **Character Creator** only works with **Layered Characters**. **Unified Characters** do not support runtime customization.

### Example Use Cases
1. **Customizable Player Character** – Easily setup the menu for a single character such as the player character.  
2. **Editing a List of Characters** – Let players edit a predefined roster, or manage a dynamic list (create, edit, delete).  

### Key Features
- **Layer Selectors** – Dropdowns, carousels, tabs, etc.  
- **Character Preview** – Static or animated, with options to rotate or swap animations.  
- **History Tracking** – Every change is logged and can be shown as text or image snapshots.  
- **Randomization** – Randomize the entire character or specific layers.  
- **Character Naming** – Optional name field.  

- [🔗 Read More → Character Creator](xref:character-creator)  
