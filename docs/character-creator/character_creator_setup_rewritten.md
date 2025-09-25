---
uid: character-creator-setup-rewrite
---

# Character Creator Setup

This page walks you through adding a **Character Creation Menu** to your game—either by dropping in a premade menu or assembling your own from modular prefabs.

> [!NOTE]
> The **Character Creator** works with **Layered Characters**. Make sure you have a valid **Layered Character Type** set up first. See: [Layered Character Type](xref:layered-character-type).

---

## 1) Core Concepts & Required Components

The **Character Creation Menu** is orchestrated by a single component:

### CharacterCreationMenuManager
- Lives **outside** the menu UI and should remain **enabled** while your game runs.
- Two key fields:
  - **Default Character Type** — Fallback character type used if none is supplied when opening the menu.
  - **Menu Contents** — The root GameObject that holds the actual menu UI (selectors, preview, buttons, etc.).

> [!TIP]
> Keep your scene tidy by creating two objects:
> 1) **CCM_Manager** – Has `CharacterCreationMenuManager` attached (enabled at runtime).
> 2) **CCM_MenuContents** – Your menu UI (can be initially disabled). Assign this to **Menu Contents** on the manager.

---

## 2) Enabling the Menu (Choose a Flow)

`CharacterCreationMenuManager` exposes four entry points. Pick the one that fits your UX:

| Method | Use When | Effect |
|---|---|---|
| `EnableMenuSingleGroup(LayeredCharacterTypeSO characterType = null, bool enableMenuContents = true)` | You have a **Single** group per type and want to open it (auto‑create if missing). | Uses the provided `characterType` or the **Default Character Type**. If a single‑group character exists, opens a **copy** for editing; otherwise, creates a new one.
| `EnableMenuNewSingleGroup(LayeredCharacterTypeSO characterType, bool enableMenuContents = true)` | You want to **force a brand‑new** character into the **Single** group. | Creates a new character draft and targets the Single group for saving.
| `EnableMenuPreExistingCharacter(LayeredCharacter character, bool enableMenuContents = true)` | You want to edit a **specific existing** character (e.g., from a roster). | Opens a **copy** of the provided character for safe editing. Saving writes back.
| `EnableMenuNewFlexibleCharacter(string characterName, FlexibleCharacterGroup group, bool enableMenuContents = true)` | You want to create a **new** character and add it to a **Flexible** group (lists/rosters). | Creates a new character draft; saving appends to the given flexible group.

> [!IMPORTANT]
> When the menu opens, the system preloads all **character pieces** for the active type (with progress). Provide a loading screen (below) to hide the menu while it initializes.

---

## 3) Menu Lifecycle & Events

### UnityEvent (Inspector‑friendly)
- **CharacterSaved** — Invoked after a successful **Save** within the menu. Wire buttons, SFX, or close logic here.

### C# Events (script‑hookable)
- **OnMenuEnabledAndSetup** — Raised when the menu is fully opened **and** finished loading.
- **OnMenuDisabled** — Raised after the menu is closed and cleaned up.
- **OnMenuLoadingProgressUpdated (float progress)** — Raised repeatedly during asset preloading (0–1). Perfect for progress bars/text.
- **static OnCharacterSaved (LayeredCharacter)** — Global event also fired on save; useful for autosave systems and external listeners.

> [!TIP]
> To close the menu after saving, subscribe to `CharacterSaved` or `OnCharacterSaved` and call `CharacterCreationMenuManager.Instance.DisableMenu()`.

---

## 4) Premade Menus (Fastest Start)

Drop‑in prefabs that include all essentials. Each premade menu includes:

- **Layer Selectors** — UI to change each character layer (dropdowns, carousels, grids, etc.).
- **Character Preview** — Static or animated preview of the current character.
- **Loading Screen** — Hides UI while assets load (progress bar/text included in complete variants).
- **Save & Back Buttons** — Basic control flow out of the box.

> [!TIP]
> **Location:** `Prefabs > Character Creator > Premade Menus`

### Included Example
1) **Simplistic**
   - **Dropdown Selectors (Initialize Existing)** – 6 pre‑wired dropdowns.
   - **Character Preview** – With rotation buttons.
   - **Loading Screen** – Progress bar + text.
   - **Save & Back Buttons**

---

## 5) Build Your Own Menu (Modular)

Use this checklist to assemble a menu from parts. Everything is prefab‑based and can be placed **anywhere** under **Menu Contents**.

### Essentials
1. **Layer Selectors**  
   Let the player choose an option for each layer (Body, Outfit, Hair, etc.).  
   **Location:** `Prefabs > Character Creator > Layer Selectors`  
   - Use the **/Pre‑Setup** variants for instant wiring.  
   - Learn more: [Layer Selector Setup](xref:ccm-layer-selector-setup)

2. **Character Preview**  
   Live preview of the character (static or animated).  
   **Location:** `Prefabs > Character Creator > Character Preview`  
   - Add rotation/animation‑swap add‑ons as needed.  
   - Learn more: [Character Preview](xref:ccm-character-preview)

3. **Menu Controls**  
   You need **Save** and **Back** at minimum.  
   - **Prefab route:** `Prefabs > Character Creator > Menu Controls`  
   - **DIY route:** Add a `Button` + call the relevant relay/actions.  
   - Learn more: [Menu Controls](xref:ccm-menu-controls)

4. **Loading Screen**  
   Hide the UI while character pieces preload.  
   **Location:** `Prefabs > Character Creator > Loading Screen`  
   - Start with **Loading Screen Core** (black overlay).  
   - Add components from **/Loading Screen Components** (progress bar/text).  
   - Or drop a full solution from **/Complete Loading Screens**.  
   - Learn more: [Loading Screens](xref:ccm-loading-screens)

### Bonus Features
1. **Character Randomization**  
   - **Global** randomize button.  
   - **Controlled** randomization UI (toggle layers on/off).  
   - Some **Layer Selectors** include **per‑layer** randomize buttons.  
   **Location:** `Prefabs > Character Creator > Randomization`  
   Learn more: [Character Randomization](xref:ccm-character-randomization)

2. **History (Undo/Redo + Panels)**  
   - Add a **History Tracker** anywhere under Menu Contents to record every change.  
   - **Undo/Redo** buttons: `Prefabs > Character Creator > History > Undo‑Redo`  
   - **Panels** (text/sprite/hybrid lists): `Prefabs > Character Creator > History > History Panels`  
   Learn more: [History Tracking System](xref:ccm-history-tracking-system)

3. **Character Display Name**  
   - Add an optional input to set a display name shown elsewhere in your UI.  
   **Location:** `Prefabs > Character Creator > Character Display Name Field`

---

## 6) Wiring the Loading Screen (Progress)

When the menu opens, the manager preloads **all character pieces** for the active type. Subscribe your progress UI to:

- `CharacterCreationMenuManager.OnMenuLoadingProgressUpdated` — Receives a `float` (0–1).

Typical flow:
1. Show loading overlay just **before** calling an `EnableMenu...` method.
2. Update progress bar/text as events fire.
3. Hide overlay when you receive `OnMenuEnabledAndSetup`.

> [!TIP]
> Animated previews can start idling as soon as `OnMenuEnabledAndSetup` fires.

---

## 7) Character Lists (Edit/Create from a Roster)

Use **LayeredCharacterSelectionList** to drive a roster UI:
- Supports **Flexible** lists (add/remove/reorder) and **Fixed** lists (fixed size slots).  
- Can create new characters directly into a **Flexible** group, edit existing entries, reorder, and remove (permissions configurable on the component).

> Configure the list with:
> - **Layered Character Type**
> - **List Type** (Flexible/Fixed)
> - **Group Name** (+ **Fixed Size** if fixed)

Add entries parent, entry prefabs, and (optionally) a **New Character** entry prefab for Flexible lists. The list can open the **Character Creator** for editing or creating new characters, then refresh its entries on save.

---

## 8) Saving Behavior & Autosave

On **Save Character**, the manager:
- Commits the draft back to its target (Single/Flexible group).  
- Fires **CharacterSaved** and **OnCharacterSaved**.

For persistence across sessions, the **Character Group Manager** can autosave your groups to disk on:
- **Game Exit**  
- **Character Creator Save**  
- **Scene Change**

> You can also invoke an immediate save from your own code if desired.

---

## 9) Quick Start (Minimal Scene)

1. Create an empty **CCM_Manager** and add **CharacterCreationMenuManager**.  
2. Create a **CCM_MenuContents** object (your menu UI) and assign it to **Menu Contents**.  
3. Drag in a **Premade Menu** (or assemble: Selectors + Preview + Controls + Loading Screen).  
4. Set **Default Character Type** on the manager.  
5. Trigger one of the `EnableMenu...` methods from a button or script.

**Example (open Single group):**
```csharp
using BlazerTech.CharacterManagement.CharacterCreator;
using UnityEngine;

public class OpenCCM : MonoBehaviour
{
    [SerializeField] BlazerTech.CharacterManagement.Characters.LayeredCharacterTypeSO type;

    public void Open()
    {
        CharacterCreationMenuManager.Instance.EnableMenuSingleGroup(type);
    }
}
```

---

## 10) Troubleshooting

- **Nothing shows / blank UI**  
  Ensure **Menu Contents** is assigned and the manager GameObject is enabled.
- **Loads forever**  
  Check that your **Layered Character Type** and each **Character Layer** is **valid** and has at least one piece.
- **Preview looks wrong**  
  Confirm all spritesheets match the **Base Spritesheet** dimensions for the type, and your Animator uses the **base** sprites.
- **Save works, but changes don’t persist**  
  If relying on autosave, make sure autosave triggers are enabled in your project, or manually invoke a save after receiving `OnCharacterSaved`.

---

## See Also
- [Character Creator (Overview)](xref:character-creator-overview)
- [Layer Selector Setup](xref:ccm-layer-selector-setup)
- [Character Preview](xref:ccm-character-preview)
- [History Tracking System](xref:ccm-history-tracking-system)
- [Character Randomization](xref:ccm-character-randomization)
- [Loading Screens](xref:ccm-loading-screens)

