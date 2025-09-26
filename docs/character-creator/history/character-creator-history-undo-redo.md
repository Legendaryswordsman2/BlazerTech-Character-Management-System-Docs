---
uid: ccm-history-undo-redo
---

# History Undo/Redo

With the [History Tracker component](xref:ccm-history-tracking-system#history-tracker-component) setup you can include buttons in your Character Creation Menu that undo or redo changes you've previously setup.

## Setup

Setup is extremely simple:  
1. Add the `button` and [CCMTimelineButtonHandler](xref:BlazerTech.CharacterManagement.CharacterCreator.CCMTimelineButtonHandler) component to any game object.
2. Assign the `Button` reference to the `CCMTimelineButtonHandler` component.
3. Set the mode to either Undo or Redo.
4. Set the buttons **On Click** event to call `CCMTimelineButtonHandler.UndoOrRedo`.

> [!NOTE]
> A `CCM History Tracker` component **must** be present somewhere in the menu contents for the Undo/Redo buttons to be functional.

If the undo or redo action is invalid the button will be disabled until valid again.  

A prefab already exists where everything is already setup.

![History Undo/Redo Buttons](~/images/ccm-history/history-undo-redo-buttons.png)

> [!TIP]
> Prefabs Location: **Prefabs > Character Creator > History > Undo-Redo**