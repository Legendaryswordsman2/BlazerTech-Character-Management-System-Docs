# Character Layers
A Character Layer is a [Scriptable Object](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ScriptableObject.html) that contains all available character spritesheets for a specific layer of a character.

## Character Layer Options
A [Character Layer Option](xref:BlazerTech.CharacterManagement.Characters.CharacterLayerOption) is a wrapper for a character spritesheet which allows for easy loading/unloading of the spritesheet when needed.

A list of Layer Options is kept in every Character Layer. The list represents all valid character spritesheets for a specific layer of a character.

![Character Layer Options List](~/images/character-types/character-layers/character-layer-options-list.png)

---

## Fields

### Attached Character Type
The **Layered Character Type** the layer is meant to be used for.

### Layer Name
The name of the layer. Used in the [Character Creator](xref:character-creator-overview) when displaying character layer names.  
Does **NOT** need to be unique.

### Layer Asset Label
The **Addressables label** used to collect spritesheets and load them into **Layer Options**. The **Character Management System** uses Unitys **Addressables package** to dynamically load/unload sprites when needed. Select the label you'd like to use and make sure all character spritesheets meant to be used for this layer are marked as Addressable and have the same label.

### Include None Option
if toggled a blank option will be added to the list of **Layer Options**. This will essentially allow a character to be created without using that layer since if the blank option is chosen, an empty sprite will be used.

![Character Layer](~/images/character-types/character-layers/character-layer.png)

---

## Buttons

### Collect Layer Options
Finds all sprites matching the **Layer Asset Label** and are the same size as the **Base Spritesheet**. If so it gets added it to the [Layer Options](#character-layer-options) list.

### Clear Options List
Clears the Layer Options list.

> [!TIP]
> Can be undo using **control/command + Z**