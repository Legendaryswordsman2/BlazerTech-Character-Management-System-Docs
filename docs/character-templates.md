---
uid: character-templates
---

# Character Templates

A **Character Template** is a blueprint for creating characters from a defined **Character Type**.  
They provide an easy way to use characters anywhere in your project.

---

## Shared Fields

Fields required by all **Character Templates**.

| Field | Type | Description |
|-------|------|-------------|
| **Character Type** | `UnifiedCharacterTypeSO` / `LayeredCharacterTypeSO` | Reference to the Character Type this template is based on.<br>[API](xref:BlazerTech.CharacterManagement.Characters.CharacterTemplateBaseSO`2.CharacterType) |
| **Character Name** | `String` | Name for characters created from this template (does **not** need to be unique).<br>[API](xref:BlazerTech.CharacterManagement.Characters.CharacterTemplateBaseSO`2.CharacterName) |
| **Character Display Name** | `String` | Optional display name shown for characters created from this template.<br>[API](xref:BlazerTech.CharacterManagement.Characters.CharacterTemplateBaseSO`2.CharacterDisplayName) |

---

## Unified Character Template

### Setup

A blueprint used to create a **Unified Character** at runtime. Can be used in the [Unified Character Loader](xref:character-usage#unified-character-loader) component.

> [!TIP]  
> To create a **Unified Character Template**:  
> `Right-click` in the Project window → **Create > BlazerTech > Character Management System > Character Templates > Unified Character Template**

![Unified Character Template](~/images/character-templates//unified-character-template.png)

### Fields

| Field | Type | Description |
|-------|------|-------------|
| **Character Spritesheet** | `AssetReferenceT<Texture2D>` | Reference to a spritesheet the same size as the **Base Spritesheet** in the Character Type. When referenced, the spritesheet is marked as **Addressable**, allowing it to be loaded/unloaded during runtime.<br>[API](xref:BlazerTech.CharacterManagement.Characters.UnifiedCharacterTemplateSO.CharacterSpritesheet) |

---

## Layered Character Template

### Setup

A blueprint used to create a **Layered Character** at runtime. Can be used in the [Layered Character Template Loader](xref:character-usage#layered-character-template-loader) component.

> [!TIP]  
> To create a **Layered Character Template**:  
> `Right-click` in the Project window → **Create > BlazerTech Character Management System > Layered Character Type**

![Layered Character Template](~/images/character-templates//layered-character-template.png)

Once the **Character Type** reference is set, a list of all layers from the referenced type will appear.  
Each layer includes:  
- **Dropdown** – Select which option to use for the layer.  
- **Search bar** – Narrow results if the list is large.  

### Buttons
- **Recreate List** – Rebuilds the layers list and resets all values.  
<!-- - **Validate Character Template** – Logs whether the template is valid (`true/false`). -->