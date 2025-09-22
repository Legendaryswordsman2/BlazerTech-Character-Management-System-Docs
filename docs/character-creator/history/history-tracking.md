---
uid: history-tracking-System
---

# History Tracking System
The **History Tracking System** tracks every change made to the character in the Character Creation Menu whlie the menu is open. Changes can then be undone at anytime.

---

## Features

| Feature | Description |
|---------|-------------|
| **Automatic Tracking** | Every change to the character is recorded as a snapshot. |
| **Undo/Redo** | Step backward or forward through the snapshot list. |
| **Direct Selection** | Select any snapshot to instantly restore the character. |
| **Snapshot Limit** | Configurable maximum number of snapshots (1-100, default = 30). |

---

## History Tracker Component

The [CCMHistoryTracker](xref:BlazerTech.CharacterManagement.CharacterCreator.CCMHistoryTracker) component can be added to any game object inside the contents of the Character Creation Menu.
- Tracks all layer changes made to the character and saves them as a snapshot.
- A snapshot contains all information required to restore the character to that exact state.
- Snapshots are saved in a list.
- Max Snapshots can be set anywhere between 1-100 (Default is 30).
- When the max amount of snapshots is met, oldest snapshots will start being replaced.
- The **Preserve First Snapshot** bool can be toggled which will stop the first snapshot created from being deleted or replaced.

---

## UI Integration

1. **Undo/Redo Buttons:**
   - Buttons can be added which can undo or redo changes you've made.  
   - [Read More → History Undo/Redo](xref:history-undo-redo)
2. **History Panels:**
   - Multiple types of panels can be added which display every change made in a clean list.
   - [Read More → History Panels](xref:history-panels)