---
uid: ccm-character-preview
---

# Character Preview

The **character preview** shows a live view of the character the player is customizing. Whenever a layer of the character is modifed, the preview is refreshed automatically.

> [!TIP]
> Prefabs Location: **Prefabs > Character Creator > Character Preview**

## Core Character Preview

![Core Character Preview](~/images/ccm-character-preview/core-character-preview.png)

Inside the base **Character Preview** folder is the core prefab as well variations. the core prefab can be used on it's own, or combined with add-on prefabs which add extra functioanlity such as rotation or animation switching button.

The Core Character Preview contains the [CCMCharacterPreviewHandler](xref:BlazerTech.CharacterManagement.CharacterCreator.CCMCharacterPreviewHandler) component which is responsible for handling and updating the preview.

### Preview Mode
The preview mode determines how the character preview is displayed.

1. **Static**
   - Uses the **Character Preview Sprite** assigned in the **Character Creator Settings** section of the **Layered Character Type**.
2. **Animated**
   - Uses the **Character Preview Controller** assigned in the **Character Creator Settings** section of the **Layered Character Type** to animate the character preview.

---

## Character Preview Rotation

![Character Preview Rotation Buttons](~/images/ccm-character-preview/character-preview-rotation-buttons.png)

located in the **/Character Rotation** subfolder are prefabs which add rotation controls to the preview.  
**Setup Instructions:**
1. Add the prefab to your scene.
2. Assign the **OnClick** event for each button to the method  
   `CCMCharacterPreviewHandler.RotateCharacterPreview(bool rotateLeft)`.
   - `true` → rotate left  
   - `false` → rotate right  

> [!NOTE]
> Rotation Controls only work with animated character previews.

---

## Character Preview Animation Buttons

![Character Preview Animation Buttons](~/images/ccm-character-preview/character-preview-animation-buttons.png)

Located in the **/Animation Control** subfolder are prefabs for switching between character animations.  
Three prefabs exist:
1. **Animation Buttons [Auto Create]**
   - automatically creates a button for each animation in the assigned Character Type at runtime.
2. **Animation Buttons [Initialize Existing]**
   - Uses animation buttons already in the prefab hierarchy.
   - Logs a warning if not enough buttons exist.
   - Can optionally disable or hide unused buttons.
3. **Animation Button**
   - Prefab used by the other two prefabs. Cannot be used on it's own.

---

## Complete Character Previews

![Character Preview Complete](~/images/ccm-character-preview/character-preview-complete.png)

Located in the **/Complete Previews** subfolder are prefabs which combine all elements of the character preview.
- The core preview.
- Rotation Buttons
- Animation Switching Buttons.

These **Complete Previews** are already setup and completely functional. All you need to do is add them to your Character Creation Menu.