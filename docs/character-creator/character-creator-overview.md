---
uid: character-creator-overview
---

# Character Creator

The Character Creator is a modular system for creating a Character Creation Menu inside your game. Combine different parts together to create a menu you want.

---

## Layer Selectors

A layer selector is any UI that lets the user change a layer of the character. These selectors come in many shapes and size.

1. Dropdown Layer Selector - A dropdown containg all options for a single layer of the character.
2. Carousel Layer Selector - Text showing the currently selected layer option and two arrows that let you scroll between the different options.
3. Grid Layer Selector - A grid with each element containing a preview of the layer option. Clicking an element applies it.
4. List Layer Selector - A list containg all options for a layer. Can optional also include a preview image. Clicking an element in the list applies it.
5. Tab Layer Selector - This is meant to be used with another layer selector. When clicked it changes another pre-setup layer selector to the layer assigned to the tab layer selector.

---

## Character Preview

A preview of the character you're editing in the character creation menu can be shown. The character preview contains the following options:

- Static Sprite Preview - The simplest option. Displays a sprite defined in the Character Type which is automatically updated with the applied layers.
- Animated Preview - An animator controller can be setup to show animations for the character preview.
- Animation Swapping - If an animated preview is used; Additional animations can be defined in the Character Type and a set of buttons can be automatically generated allowing the user to switch between animations.
- Rotate Character - Buttons can be added which when pressed will show different sizes of the character.

---

## Character History

The CCM History Tracker component can be used to keep track of every change made to the character. each time a character layer is made a snapshot is made. The History Tracker can hold anywhere between 1-100 snapshots (Configurable) with the default being 30.

Addiotnally the first snapshot created can be preserved so it won't be overitten when the snapshots cap is met.

### Undo/Redo Support

Buttons can be setup and use the CCM Undo Redo Button Handler component to communicate with the History Track and undo/redo changes.

### History Panels

A history panel displays a list of all created snapshots and lets the user click on them to revert back to that version.

Two versions of the the panel exists.
1. Text Based - Each element contains text describing what was changed (Usually a vertical list)
2. Sprite Based - A preview of the snapshot is shown in each entry making it easy to see what changed visually (Usually a horizontal list)
3. Text and Sprite Based panels can be combined to display both text and sprites.

---

## Other Features

- Mid Play character editing - the Character Creation Menu can be used while a character is already and it will automatically be updated when editing the same character in the Character Creation Menu.
- Optioanl Display Name - A field can be added to the menu to allow the user to input a display name which can be shown for each character.
- Reset Button - A reset button can be added to the menu which resets the character to the state it was in when the Character Creation Menu was first opened.