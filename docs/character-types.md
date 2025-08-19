# Character Types

Character Types are [Scriptable Objects](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ScriptableObject.html) that define core aspects of a character. They are the heart of the Character Management System.

> [!note]
> All Characters `Require` a `Character Type`.

---

### Character Type Base
All Character Types inherit from [CharacterTypeBaseSO](character-type-base.md), which contains the core properties shared across all Character Types.

---

## Character Type Variants

| Variant   | Modularity | Runtime Customization | Best For |
|-----------|--------------------|---------------|----------|
| **Unified** | Single spritesheet | None | Pre-rendered, fixed characters |
| **Layered** | Layered spritesheets | High | Modular, editable characters |

---

### 1. Unified Character Type
Each character uses a single spritesheet containing the fully assembled character. No runtime customization is possible.  
- **Use Case:** Characters with fixed, pre-rendered appearances.  
- **Example:** Simplistic characters where their appearance is pre-determined and won't need to be changed.

[Read More → Unified Character Type](unified-character-type.md)

---

### 2. Layered Character Type
A set of separate spritesheets, each containing one visual layer of the character.  
- **Use Case:** Customizable player characters or dynamically generated NPCs.  
- **Example:** Body, Outfit, Hairstyle, Accessory  

[Read More → Layered Character Type](layered-character-type.md)