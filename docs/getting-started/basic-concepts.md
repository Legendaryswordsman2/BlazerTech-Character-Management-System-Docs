---
uid: basic-concepts
---

# Basic Concepts

## Character Types
[Read More → Character Types](xref:character-types)

A character type define how the character works. There are two types of character types:

### 1. Unified Character Type
Each character uses a single spritesheet containing the fully assembled character. No runtime customization is possible.  
- **Use Case:** Characters with fixed, pre-set appearances.  
- **Example:** Simplistic characters where their appearance is pre-determined and won't need to be changed.

[Read More → Unified Character Type](unified-character-type.md)

---

### 2. Layered Character Type
A set of separate spritesheets, each containing one visual layer of the character.  
- **Use Case:** Customizable player characters or dynamically generated NPCs.  
- **Example:** Body, Outfit, Hairstyle, Accessory  

[Read More → Layered Character Type](layered-character-type.md)

---

## Character Creator

A fully modular Character Creation Menu System for layered characters. Easily implement your own Character Creation Menu by adding pre-made scripts and prefabs.

### Use-case Examples

#### 1. Customizable Player Character
The Character Creation Menu can be easily setup for a single character such as the player character. Once made it can easily be used anywhere in-game.

#### 2. Customizing a List of Characters
Pre-created lists of charactes can be edited one by one.
Or a dynamic list can be used and allow the player to create, edit and delete characters at any time.

---

### Customizability:
- **Character Piece Selectors** - Dropdowns, Carousel Selectors, Tabs, etc.
- **Character Preview** - Static, Animated, Change Animations, Rotate Character.
- **History** - all changes are recorded and can be shown as text or image snapshots. Clicking an entry will revert to that snapshot.
- **Character Randomization** - Randomize the entire character or specific layers.
- **Character Name Field** - Optional.

[Read More → Character Creator](<xref:character-creator>)