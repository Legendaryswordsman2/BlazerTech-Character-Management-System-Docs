---
uid: character-usage-topdown-controller
title: Top Down Movement Controller
summary: Handles player movement for top-down 2D games with configurable input and sprint/crouch support.
---

# Top Down Movement Controller

**Component:** [`TopDownMovementController`](xref:BlazerTech.CharacterManagement.Components.TopDownMovementController)

The **Top Down Movement Controller** handles player movement for **top‑down 2D games** with four directional controls — **Up**, **Down**, **Left**, and **Right**.  
It supports movement, sprinting, crouching, and integrates seamlessly with the **Unity Input System**.

---

## 🎮 Input Configuration

This component uses the **Unity New Input System**, allowing all input actions to be fully configurable.  
See Unity’s [Input Actions documentation](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.15/manual/Actions.html) for setup details.

### Input Actions

| Input Action | Type | Description |
|--------------|------|--------------|
| **Move Action** | `Vector2` | Controls player movement along X and Y axes. |
| **Sprint Action** | `Button` | Enables player sprinting (if sprinting is enabled). |
| **Crouch Action** | `Button` | Enables player crouching (if crouching is enabled). |

A default **Input Actions asset** is provided under the `/Input Actions` folder.  
It includes bindings for **Move**, **Sprint**, and **Crouch** actions.

### Auto Enable Actions

If **Auto Enable Actions** is checked, the component automatically enables and disables the assigned input actions when the GameObject is enabled or disabled.  
This is useful when not using a **PlayerInput** component or a project‑wide input actions asset that handles enabling automatically.

---

## 🧭 Movement Settings

| Field | Type | Description |
|--------|------|--------------|
| **Move Speed** | `float` | Base walking speed (default: `6.5`). |
| **Can Move** | `bool` | Toggles whether the character can currently move. Can be changed via script or in the Inspector. |

---

## ⚡ Sprinting & Crouching

Optional sprinting and crouching systems can be toggled on via their corresponding booleans.  
Each system has customizable speed and button mode options.

| Setting | Type | Description |
|----------|------|--------------|
| **Speed** | `float` | Movement speed while sprinting or crouching. |
| **Mode** | `enum` (`Hold`, `Toggle`) | Determines whether the button must be held or toggled. Default: `Hold`. |

---

## 🧩 Component References

| Reference | Type | Description |
|------------|------|--------------|
| **Rigidbody2D** | `Rigidbody2D` | Required reference used for applying physics‑based movement. |

---

## 🕹️ Runtime Properties

| Property | Type | Description |
|-----------|------|--------------|
| **IsMoving** | `bool` | True if the player is currently moving. |
| **IsSprinting** | `bool` | True if the player is sprinting. |
| **IsCrouching** | `bool` | True if the player is crouching. |
| **Movement** | `Vector2` | The current normalized movement direction. |

---

> [!TIP]
> Combine with a [`Character Animator Handler`](xref:BlazerTech.CharacterManagement.Components.CharacterAnimatorHandler) for synchronized animation and movement control.
