---
uid: layered-character-type
---

# Layered Character Type
A layered character is made from multiple layers, these layers are stacked upon each other to form the final character.  
Ex: **Body > Outfit > Hairstyle > Accessory** - Each layer is added one by one in order.

---

## Creating a Layered Character Type
to create a new layered character type right click the **Project** window and navigate to **Create > BlazerTech > Character Management System > Layered Character Type**.

> [!IMPORTANT]
> The **Layered Character Type Scriptable Object** MUST be placed inside a folder named **Resources**! This is need for runtime initialization.

---

### Setting up a Layered Character Type
The following properties must be set:

| Property                                                                 | Type                      | Description                       |
| ------------------------------------------------------------------------ | ------------------------- | --------------------------------- |
| **[CharacterTypeID](xref:character-type-core#character-type-id)**        | String                    | A **unique** identifer            |
| **[BaseSpritesheet](xref:character-type-core#base-spritesheet)**         | Sprite                    | The default character spritesheet |
| **[CharacterController](xref:character-type-core#character-controller)** | RuntimeAnimatorController | The Animator Controller used      |

---

### Setting up Character Layers

At the bottom of your **Layered Character Type** is a list of **Character Layers**. Each layer is a **Scriptable Object** that contains all available options for that layer of your character.

To create a **Character Layer**, once again right click the **Project window** and navigate to **Create > BlazerTech ? Character Management System > Layered Character Type > Character Layer**.

After the **Character Layer** has been created make sure to add it to the **layers** list inside your **Layered Character Type**.

> [!IMPORTANT]
> Only the **Layered Character Type** must be placed in a **Resources** folder. Everything else including **Character Layers** should be placed outside the **Resources** folder!

Refer to [Character Layers](character-layers.md) for how to setup your newely created layers.