---
uid: layer-selector-setup
---

# Layer Selector Setup

Not sure what a **Layer Selector** is?  
[Read More → Layer Selectors](xref:character-creator-overview#layer-selectors)

---

## Overview

A **Layer Selector** cannot function on its own.  
The most common way to use Layer Selectors is through the  
[`CCMCharacterLayerSelectionManager`](xref:BlazerTech.CharacterManagement.CharacterCreator.CCMCharacterLayerSelectionManager) component.

This manager is responsible for connecting UI Layer Selectors to the  
[Character Creation Menu](xref:character-creator-overview).

---

## Initialization Modes

The `CCMCharacterLayerSelectionManager` supports two initialization modes:

### 1. Create New
- At runtime, the manager will **instantiate new layer selectors** for each character layer.  
- Requires assigning a **Character Layer Selector Prefab**.  
- Each layer selector instance is linked automatically to the correct layer.  

### 2. Initialize Existing
- Use **pre-existing layer selectors** already placed in the scene.  
- Each selector is initialized with a character layer at runtime.  
- Extra selectors (more than the number of layers) can optionally be **hidden** or **disabled**.  

---

## Layer Selector Parent

Regardless of the initialization mode, a **Layer Selector Parent** is required:

- This should be the **parent GameObject** that contains all layer selectors.  
- In **Initialize Existing** mode, place all pre-made layer selectors as children of this parent.  
- In **Create New** mode, new selectors will be instantiated as children of this parent.  

---

## Layer Selector Prefabs

> [!TIP]
> All Layer Selector prefabs can be found under:  
> **BlazerTech Character Management System > Prefabs > Character Creator > Layer Selectors**  .
> Subfolders exist for each individual **Layer Selector**.

Each Layer Selector exists as a prefab and is organized into its own folder with the following structure:

- **Base Folder**  
  Contains the core Layer Selector prefab and any variant prefabs.  

- **Pre-Setup Folder**  
  Contains prefabs that already include a configured
[`CCMCharacterLayerSelectionManager`](xref:BlazerTech.CharacterManagement.CharacterCreator.CCMCharacterLayerSelectionManager).  
  Two versions are provided:  
  1. **Create New** – Instantiates Layer Selectors at runtime.  
  2. **Initialize Existing** – Uses Layer Selectors already present in the prefab hierarchy.  

This makes it easy to either drop in a ready-to-use prefab or build a custom setup.

---

## Example Setup

1. Add the `CCMCharacterLayerSelectionManager` component to your UI object.  
2. Assign the **Layer Selector Parent**.  
3. Choose an **Initialization Mode**:  
   - *Create New* → Provide a `Character Layer Selector Prefab`.  
   - *Initialize Existing* → Place selectors as children under the parent.  
4. Run the scene — selectors will now control the layers of the active character.  
