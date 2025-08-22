# Layered Character Type
A layered character is character made from multiple layers, these layers are stacked upon each other to form the final character.  
Ex: **Body > Eyes > Outfit > Hairstyle > Accessory** - Each layer is added one by one in order.

---

## Creating a Layered Character Type
to create a new layered character type right click the **Project** window and navigate to **Create > BlazerTech Character Management System > Layered Character Type**.

> [!IMPORTANT]
> The **Layered Character Type Scriptable Object** MUST be placed inside a folder named **Resources**! This is need for runtime initialization.

---

### Setting up a Layered Character Type
The following properties must be set:

| Property                | Type                      | Description
|-----------------------------------------------------------------------------|---------------------------|---------------------------
| **[CharacterTypeID](character-type-properties.md#charactertypeid)**         | String                    | A **unique** identifer
| **[BaseSpritesheet](character-type-properties.md#basespritesheet)**         | Sprite                    | The default character spritesheet
| **[CharacterController](character-type-properties.md#charactercontroller)** | RuntimeAnimatorController | The Animator Controller used

---

### Setting up Character Layers

At the bottom of your layered character type is a list of **Character Piece Collections**. You can think of each collection as a layer of your character.

To create a **Character Piece Collection** once again right click the Project window and navigate to **Create > BlazerTech Character Management System > Character Piece Collection**.

After the **Character Piece Collection** has been created make sure to add it to the **Character Piece Collections** list inside your **Layered Character Type**.

> [!IMPORTANT]
> Only the **Layered Character Type** must be placed in a **Resources** folder. Everything else including **Character Piece Collections** should be placed outside the **Resources** folder!

Refer to [Character Piece Collections](character-piece-collections.md) for how to setup your newely created collections.