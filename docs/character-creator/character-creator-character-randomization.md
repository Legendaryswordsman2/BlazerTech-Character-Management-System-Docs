---
uid: ccm-character-randomization
---

# Character Randomization

The character in the Character Creation Menu can be completely randomized by randomizing every layer or randomize only specific layers. 

## Complete Character Randomization
This is the simplest option. A button can be setup with the `CCM Relay` component. The button should call the `RandomizeEntireCharacter` method on the `CCM Relay` which will then randomize all layers of the character.

> [!TIP]
> A complete randomization button prefab can be located in **Prefabs > Character Creator > Randomization > Randomize Character Button**
> 
---

## Single Layer Randomization
Some Layer Selectors include a variant that contains a randomize button that when pressed will randomize that layer of the character.

If a Layer Selector does **not** include a variant with a randomize button; one can be added easily.  
Add a button component that **On Click** calls **[CharacterLayerSelector.RandomizeLayer()](xref:BlazerTech.CharacterManagement.CharacterCreator.CharacterLayerSelector#BlazerTech_CharacterManagement_CharacterCreator_CharacterLayerSelector_RandomizeLayer)**

---

## Controlled Randomization
A controlled randomization button contains extra options to only randomize the selected layers.

![Controlled Randomization](~/images/ccm-character-randomization/controlled-randomization-example.png)

> [!TIP]
> A prefab is locatated in **Prefabs > Character Creator > Randomization > Controlled Randomization Button**