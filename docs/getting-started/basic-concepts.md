---
uid: basic-concepts
---

# Basic Concepts

This page introduces the **core building blocks** of the Character Management System:  
- **Character Types** – Define how characters are structured.  
- **Character Creator** – A system for building and customizing characters in-game.  

---

## Character Types
A **Character Type** defines how a character works. There are two kinds:

| Type | Description | Best For |
|------|-------------|----------|
| **Unified Character Type** | A single spritesheet containing a fully assembled character. No runtime customization. | Characters with fixed, pre-set appearances. |
| **Layered Character Type** | Multiple spritesheets, each containing one visual layer (body, outfit, hair, etc.). | Customizable player characters or dynamic/randomized NPCs. |

- [🔗 Read More →  Character Types](xref:character-types)  
- [🔗 Read More → Unified Character Type](xrefunified-character-type)  
- [🔗 Read More → Layered Character Type](xreflayered-character-type)  

---

## Character Creator

The **Character Creator** is a fully modular menu system designed for **Layered Characters**.  
Easily build a character creation menu into your game using the included scripts and prefabs.

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
