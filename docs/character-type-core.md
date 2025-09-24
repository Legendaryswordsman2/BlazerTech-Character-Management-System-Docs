---
uid: core-character-type
uid: character-type-core
---

# Character Type Core

This page goes over the core functionality of a character type which both **Unified & Layered Character Types** inherit from.

Don’t know what a Character Type is?  
[Read More → Character Types](xref:character-types)

---

## Character Type ID
| Field | Type | Description |
|----------|------|-------------|
| **CharacterTypeID** | `String` | A unique identifier for this Character Type. Must be unique across all types. |
> [!WARNING]
> A **Character Type** with the same **ID** as another will fail to initialize and all characters of that type will also fail to load.

[API](xref:BlazerTech.CharacterManagement.Characters.CharacterTypeBaseSO.CharacterTypeID)

---

## Base Spritesheet
| Field | Type | Description |
|----------|------|-------------|
| **BaseSpritesheet** | `Spritesheet` | The main spritesheet used for all characters of this type. Every character spritesheet must match its dimensions exactly. |

> [!WARNING]  
> Character Spritesheets of a different size will be rejected, and a warning will be logged.

Sprites from the **Base Spritesheet** will be used whenever using any character of the same **Character Type**. A shader will be applied that visually overrides of spritesheet with the spritesheet(s) used by the assigned character.

### Setup
The **Base Sprite** has a **Sprite Mode** which defines if the image should be used as a singular sprite or split into individual sprites.  
In this case we want to set the **Sprite Mode** to **Multiple** so we can use each frame of the spritesheet individually.

Checkout the next section [#charactercontroller](#character-controller) to learn how sprites from the **Base Spritesheet** can animated.

[API](xref:BlazerTech.CharacterManagement.Characters.CharacterTypeBaseSO.BaseSpritesheet)

---

## Character Controller
| Property | Type | Description |
|----------|------|-------------|
| **CharacterController** | `RuntimeAnimatorController` | An **Animator Controller** that animates all characters of this Character Type. |

> [!NOTE]  
> This field is **optional**.  

An Animator Controller can be created and used to switch between different animations. Animation Clips inside this controller should use sprites from the [BaseSpritesheet](#base-spritesheet).

This Animator Controller can then be referenced in the **CharacterController** field inside your **Character Type**

> [!TIP]  
> When using a **Character Loader component**, this **Animator Controller** will be applied automatically if **Set Animator Controller** is enabled.  
> See [Character Usage](xref:character-usage) for more info.

[API](xref:BlazerTech.CharacterManagement.Characters.CharacterTypeBaseSO.CharacterController)