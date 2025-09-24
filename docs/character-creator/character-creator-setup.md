---
uid: character-creator-setup
---

# Character Creator Setup
This page will guide you through the process of implementing your own **Character Creation Menu** into your game.

## The Character Creation Menu Manager

The `CharacterCreationMenuManager` is the beating heart of the menu.

It lives outside the contents of the menu and should be enabled at all times.  
It requires two things.
1. **Default Character Type** - The character type used when enabling the menu. Can be overridden.
2. **Menu Contents** - Parent game object of the actual Character Creation Menu contents.

### How to Enable the Menu
The `Character Creation Menu Manager` provides 4 methods to open the menu.  
Most methods use the Character Grouping System.  
Learn more about the [Character Grouping System here](xref:character-groups).  

| Method                                                                                                                   | Descripion                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| [EnableMenu_PrimaryCharacterSlot]                                                                                        | Opens the menu using the Primary Character Slot of the Character Type Used.                  |
| [EnableMenu_EditCharacter]                                                                                               | Open the menu to edit a layered character that already exists.                               |
| [EnableMenu_NewPrimaryCharacterSlot]                                                                                     | Opens the menu with a new character that overrides the Primary Character slot.               |
| [<span style="white-space:nowrap">EnableMenu_NewCharacterInFlexibleGroup</span>][EnableMenu_NewCharacterInFlexibleGroup] | Opens the menu with a new character & puts it inside the provided Flexible Group when saved. |

### Character Creation Menu Events

Two Unity Events are exposted in the `Character Creation Menu Manager` component.

1. **On Character Saved**
   - Called when the character in the **Character Creation Menu** is saved.
   - Provides the charater that was saved as an argument.
   - For example you can hook up to this event, when it's invoked call `CharacterCreationMenuManager.DisableMenu` to disable and close the menu.
2. **On Menu Disabled**
   - Called after the **Character Creation Menu** is disabled and closed. You can hook up to this event and when invoked open any other menu you'd like using your own menu system.

---

## Premade Character Creation Menus

The easiest solution is to use a **premade character creation menu**. These prefabs contain everything needed for a functional Character Creation Menu.
At bare minimum they contain the following:  

| Content                 | Descripion                                                       |
| ----------------------- | ---------------------------------------------------------------- |
| **Layer Selectors**     | Used to change layers of the character.                          |
| **Character preview**   | Used to preview the character while editing.                     |
| **Loading Screen**      | Displayed over the Character Creation Menu while it's loading.   |
| **Save & Back Buttons** | Used to save character changes or close the menu without saving. |

> [!TIP]
> Premade Character Creation Menu prefabs location: **Prefabs > Character Creator > Premade Menus**  

### Premade Menus:  
1. **Simplistic**:
   - **Dropdown Selectors [Initialize Existing]**. - Includes 6 dropdown selectors.
   - **Character Preview** - Includes rotation controls.
   - **Loading Screen** - Includes progress bar and text.
   - **Save & Back Buttons**.
   - <img src="~/images/premade-character-creation-menus/premade-character-creation-menu-1.png" alt="Premade Character Creation Menu #1" width="500" />

---


---
## Creating Your Own Character Creation Menu

[EnableMenu_PrimaryCharacterSlot]: xref:BlazerTech.CharacterManagement.CharacterCreator.CharacterCreationMenuManager#BlazerTech_CharacterManagement_CharacterCreator_CharacterCreationMenuManager_EnableMenu_PrimaryCharacterSlot_BlazerTech_CharacterManagement_Characters_LayeredCharacterTypeSO_System_Boolean_
[EnableMenu_EditCharacter]: xref:BlazerTech.CharacterManagement.CharacterCreator.CharacterCreationMenuManager#BlazerTech_CharacterManagement_CharacterCreator_CharacterCreationMenuManager_EnableMenu_EditCharacter_BlazerTech_CharacterManagement_Characters_LayeredCharacter_System_Boolean_
[EnableMenu_NewPrimaryCharacterSlot]: xref:BlazerTech.CharacterManagement.CharacterCreator.CharacterCreationMenuManager#BlazerTech_CharacterManagement_CharacterCreator_CharacterCreationMenuManager_EnableMenu_NewPrimaryCharacterSlot_BlazerTech_CharacterManagement_Characters_LayeredCharacterTypeSO_System_Boolean_
[EnableMenu_NewCharacterInFlexibleGroup]: xref:BlazerTech.CharacterManagement.CharacterCreator.CharacterCreationMenuManager#BlazerTech_CharacterManagement_CharacterCreator_CharacterCreationMenuManager_EnableMenu_NewCharacterInFlexibleGroup_System_String_BlazerTech_CharacterManagement_Characters_FlexibleCharacterGroup_System_Boolean_
