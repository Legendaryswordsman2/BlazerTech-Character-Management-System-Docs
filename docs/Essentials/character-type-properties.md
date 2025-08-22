---
uid: character-type-properties
---

# Character Type Properties
The following are properties that are shared across all **character type** [Scriptable Objects](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ScriptableObject.html).    

## CharacterTypeID
Type: **String**.
> A unique identifier used to reference this character type. Must be unique across all character types.  

[API](xref:BlazerTech.CharacterManagement.Characters.CharacterTypeBaseSO.CharacterTypeID)

---

## BaseSpritesheet
Type: **Spritesheet**.
> Defines the **required base sprite sheet** for the character type.  
Set this spritesheets **Sprite Mode** to **Multiple** and slice it.  
Whenever this character is used the sprites in the **BaseSpritesheet** will be used and a shader will then  override them with the finalized character.  
Character spritesheets with mismatched dimensions will be rejected when validated.

[API](xref:BlazerTech.CharacterManagement.Characters.CharacterTypeBaseSO.BaseSpritesheet)

---

## CharacterController
Type: **RuntimeAnimatorController**.
> The animator controller asset assigned to characters of this type.  
> Animations inside this controller should use sprites in the [BaseSpritesheet](#basespritesheet).

[API](xref:BlazerTech.CharacterManagement.Characters.CharacterTypeBaseSO.CharacterController)