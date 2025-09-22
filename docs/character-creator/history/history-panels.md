---
uid: history-panels
---

# History Panels

A History Panel displays a list of snaphots saved in the [History Tracker component](xref:history-tracking-system#history-tracker-component) for the player to view and restore any changes they've made.

> [!TIP]
> Prefabs Location: **Prefabs > Character Creator > History > History Panels**

## Panel Type Prefabs

1. **History Panel [Text, Vertical List]**
   - A vertical, text based list. Each entry displays text containing what changed in the assigned character snapshot.
   - ![History Panel Text](/images/history-panels/history-panel-text.png)
2. **History Panel [Sprite, Horizontal List]** 
   - A horizontal, sprite based list. Each entry contains a list of sprites, each sprite displays a layer in the assigned character snapshot.
   - ![History Panel Sprite Preview](/images/history-panels/history-panel-sprite-preview.png)

---

## Entry Prefabs

The following are entries used in the above mentioned panels.

1. **History Panel Entry [Text]**
   - Entry displaying text which describes what changed in the assigned snapshot.
2. **History Panel Entry [Sprite]**
   - Entry containing a dynmaic list of sprites. Each sprite displays a layer in the assigned character snapshot.

> [!TIP]
> Entry prefabs live in the **/History List Entries** subfolder.

### Custom Prefabs
You can create your own history panel entry easily. Here are the steps
1. Create a new game object and add the [HistoryPanelEntry](xref:BlazerTech.CharacterManagement.CharacterCreator.HistoryPanelEntry) component.
2. Set the display mode:
   - Text - Requires reference to a text objcet.
   - Sprite - Requires reference to layer preview sprites parent. (The parent game object sprites will be instantiated to)
   - Text And Sprite - Requires both aforementioned references.
3. Add the `Toggle` component and reference it in the `HistoryPanelEntry` component.
4. Add an `Image` component - This will be the background image.
5. Set the `Target Graphic` on the `toggle` to the image component.
6. Add a new child game object and add another `Image` component to it.
7. Name the new child game object something like **Highlight**. - This game object will only be active when the entry is selected.
8. Set the `Graphic` on the `toggle` to the image component on the **Highlight** game object.
9. Turn your game object into a prefab by dragging it into a folder in the project window.
10. Finally, on the [CCMHistoryPanel](xref:BlazerTech.CharacterManagement.CharacterCreator.CCMHistoryPanel) component which lives on all **History Panels**, set the `Entry Prefab` to reference your new prefab.

**Confused?**  
Checkout one of the pre-existing entry prefabs to see how they're setup.