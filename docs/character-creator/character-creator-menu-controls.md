---
uid: ccm-menu-controls
---
[CCMRelay]: xref:BlazerTech.CharacterManagement.CharacterCreator.CCMRelay
[DisableMenu()]: xref:BlazerTech.CharacterManagement.CharacterCreator.CCMRelay#BlazerTech_CharacterManagement_CharacterCreator_CCMRelay_DisableMenu
[SaveCharacter()]: xref:BlazerTech.CharacterManagement.CharacterCreator.CCMRelay#BlazerTech_CharacterManagement_CharacterCreator_CCMRelay_SaveCharacter
[RandomizeEntireCharacter()]: xref:BlazerTech.CharacterManagement.CharacterCreator.CCMRelay#BlazerTech_CharacterManagement_CharacterCreator_CCMRelay_RandomizeEntireCharacter
[ResetCharacter()]: xref:BlazerTech.CharacterManagement.CharacterCreator.CCMRelay#BlazerTech_CharacterManagement_CharacterCreator_CCMRelay_ResetCharacter

# Character Creator Menu Controls

Menu Controls are buttons that enhance the functionality of the **Character Creation Menu**.  
They include the following:
- **Back/Close menu button**.
- **Save Character/Confirm changes button**.
- **Reset character button**.
- **Randomize character button**.

## The Character Creation Menu Relay Component

The [CCMRelay] component is used to relay methods to the `Character Creation Menu Manager`. The setup works like this:
1. Add the `CCM Relay` component to a game object.
2. Add a `button` component and set the `On Click` event to call a method on the `CCM Relay` component.

![CCM Relay Usage Example](~/images/character-creator-setup/ccm-relay-usage-example.png)

### CCM Relay Methods

The following are all public methods on the `CCM Relay` component:

- [DisableMenu()] - Disable and close the **Character Creation Menu** if open.
- [SaveCharacter()] - Save the character assigned in the **Character Creation Menu** and add it to a group if applicable.
- [RandomizeEntireCharacter()] - Randomize all layers of the character assigned in the **Character Creation Menu**.
- [ResetCharacter()] - Reset the character in the **Character Creation Menu** to the state it was in when the menu was first opened.

---

## Menu Control Prefabs


> [!TIP]
> Prefabs Location: **Prefabs > Character Creator > Menu Controls**

The following prefabs are pre-setup with the above mentioned controls.
- **Menu Controls (Core, Horizontal Group)** - Only contains a back and save character button.
- **Menu Controls (Full, Horizontal Group)** - Contains back, save character, randomize and reset buttons. All contained in a horizontal layout group.
- **(Menu Controls [Full + Undo_Redo])** - Contains back, save character, randomize and undo/redo buttons for use with the **History Tracker** component.
- **Menu Controls [Full]** - Contains back, save character, randomize and reset buttons in a grid shape.