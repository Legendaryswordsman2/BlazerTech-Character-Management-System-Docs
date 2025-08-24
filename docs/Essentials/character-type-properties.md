---
uid: character-type-properties
---

# Character Type Properties
The following are properties that are shared across all **Character Type** [Scriptable Objects](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ScriptableObject.html).  

Don't know what a Character Type is?  
[🔗 Read More → Character Types](xref:character-types).

---

## CharacterTypeID
Type: **String**.  
A unique identifier used to reference this character type. Must be unique across all character types.  
> [!WARNING]
> A **Character Type ID** with the same **ID** as another will fail to initialize and all characters of that type will also fail to load.

[API](xref:BlazerTech.CharacterManagement.Characters.CharacterTypeBaseSO.CharacterTypeID)

---

## BaseSpritesheet
Type: **Spritesheet**.
All characters part of the same **Character Type** must have a character spritesheet the same exact size as the **Base Spritesheet**.
> [!WARNING]
> Spritesheets of a different size will be rejected and a warning will be logged.

### Properly Setting up the Base Spritesheet
The **Sprite Mode** of the Base Spritesheet should be set to **Multiple**. This allows the sprite to be split into slices, with each slice being a frame of the character.  
When you want to use a character from a **Character Type** make sure to use the sprites from the **Base Spritesheet**. When the character is loaded a shader will be applied that will display the correct character over the **Base Spritesheet**.

[API](xref:BlazerTech.CharacterManagement.Characters.CharacterTypeBaseSO.BaseSpritesheet)

---

## CharacterController
Type: **RuntimeAnimatorController**.
> The animator controller asset assigned to characters of this type.  
> Animations inside this controller should use sprites in the [BaseSpritesheet](#basespritesheet).

[API](xref:BlazerTech.CharacterManagement.Characters.CharacterTypeBaseSO.CharacterController)