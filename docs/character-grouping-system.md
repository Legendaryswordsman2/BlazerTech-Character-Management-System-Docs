---
uid: character-grouping-system
---
[EnableMenu_PrimaryCharacterSlot]: xref:BlazerTech.CharacterManagement.CharacterCreator.CharacterCreationMenuManager#BlazerTech_CharacterManagement_CharacterCreator_CharacterCreationMenuManager_EnableMenu_PrimaryCharacterSlot_BlazerTech_CharacterManagement_Characters_LayeredCharacterTypeSO_System_Boolean_

# Character Grouping System

Character groups are a convenient way to store/sort characters. They are for [Layered Characters](xref:layered-character-type) only.
Characters in a group are automatically saved to disk and loaded again next session.

## The Primary Character Slot

Every Character Type contains a **Primary Character Slot** which can hold a singular character. This is useful for simple setups where only one character is used.  

The main use for the **Primary Character Slot** is for use with the [Character Creation Menu](xref:character-creator-overview).  
The menu can be opened using the character contained within the **Primary Character Slot**.

## Group Types

**There are two types of groups:** 

### Flexible Group Type

A dynamic list. Characters can be added, removed or edited at any time.

Flexibe Groups are great when you want the player to have full control of the list. 
For example a list of playable characters with the ability for the player to create new characters.

[API](xref:BlazerTech.CharacterManagement.Characters.FlexibleCharacterGroup)
### Fixed Group Type

A list of a pre-determined amount of characters. The number is set when the list is created and all characters are created immedietely. Characters within the list can be edited at anytime but cannot be removed and new characters cannot be added.

Best for situations where an immutable list is needed. Such as a set of pre-created characters the player can edit the designs of but not change the count. Or a set of playable characters the player can choose from.

[API](xref:BlazerTech.CharacterManagement.Characters.FixedCharacterGroup)

---
## Character Group Registries
The [CharacterGroupRegistry](xref:BlazerTech.CharacterManagement.Characters.CharacterGroupRegistry) is a wrapper class. An instance of this class exists for each **Layered Character Type**.
This wrapper class holds the [Primary Character Slot](#the-primary-character-slot) as well as all flexible and fixed groups created for the same **Layered Character Type**.

## Character Group Manager

The [LayeredCharacterGroupManager](xref:BlazerTech.CharacterManagement.Characters.LayeredCharacterGroupManager) is a static class which handles all groups.

The Layered Character Group Manager contains a dictionary of type `CharacterGroupRegistry`. One entry for each **Layered Character Type** used.

The `LayeredCharacterGroupManager.GetGroupRegistryForType(LayeredCharacterTypeSO type)` method can be used to retrieve the registry for a specific **Character Type**.