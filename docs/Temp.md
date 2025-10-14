---
uid: temp
---

# Character Animation Setup

This guide explains how to create and configure an **Animator Controller** to be used by your **Character Types** in the BlazerTech Character Management System (BT-CMS).

---

## Overview

Every **Character Type** can include an **Animator Controller** asset.  
This controller defines how your character’s sprites animate during gameplay — such as idle, walking, or interacting.

| Character Type | Animator Support | Description |
|----------------|------------------|--------------|
| **Unified Character Type** | ✅ Supported | Animations use a single pre-made spritesheet. |
| **Layered Character Type** | ✅ Supported | Each animation frame is composited from multiple layers (body, outfit, hair, etc.). |

> [!NOTE]
> While animations are optional, they are highly recommended to make your characters feel dynamic.

---

## 1. Create an Animator Controller

1. In the **Project window**, right-click and select  
   **Create → Animator Controller**.
2. Give it a clear name, such as  
   `Player_AnimatorController` or `NPC_AnimatorController`.
3. Double-click to open it in the **Animator window**.

You should now see an empty **State Machine** with an **Entry** node.

---

## 2. Add Animation States

Each state represents one animation (for example, Idle, Walk, Run).

1. Right-click the Animator graph and select **Create State → Empty**.
2. Name the state `Idle`.
3. Assign an animation clip to the state’s **Motion** field.
4. Repeat for additional animations like `Walk`, `Run`, or `Interact`.

> [!TIP]
> For pixel-based characters, ensure all clips use the same sprite dimensions as your **Base Spritesheet** defined in the Character Type.

---

## 3. Define Parameters

Parameters allow your scripts (or the built-in movement handlers) to control animations.

| Parameter | Type | Description |
|------------|------|-------------|
| **Horizontal** | Float | The current movement direction on the X axis. |
| **Vertical** | Float | The current movement direction on the Y axis. |
| **Speed** | Float | How fast the character is moving. Usually between 0 and 1. |
| **IsMoving** *(optional)* | Bool | True when the character is moving. |

> [!IMPORTANT]
> These parameter names must match **exactly** when using the built-in **Animator Handler** or **Top-Down Movement Controller** scripts.

---

## 4. Create Blend Trees (Optional)

For smoother directional animation:

1. Right-click → **Create State → From New Blend Tree**.
2. In the **Blend Tree**, set **Blend Type** to `2D Freeform Directional`.
3. Add motions for each direction (Up, Down, Left, Right).
4. Use `Horizontal` and `Vertical` as the **Blend Parameters**.

---

## 5. Assign to a Character Type

Once your Animator Controller is complete:

1. Select your **Character Type asset** (`LayeredCharacterTypeSO` or `UnifiedCharacterTypeSO`).
2. In the **Inspector**, find the **Character Controller** field.
3. Drag your new **Animator Controller** into this field.

Your setup should look similar to this:

![Animator Controller Field in Inspector](~/images/screenshots/animator-controller-field.png)

> [!NOTE]
> The Character Controller is stored directly in the Character Type.  
> Any characters created from this type will automatically use it when rendered.

---

## 6. Test Your Animation

To test your setup:

1. Place a **Character Loader** (such as `LayeredCharacterTemplateLoader`) in a scene.
2. Assign a Character Template that uses your configured **Character Type**.
3. Press **Play** and move your character (if using the built-in controller).

You should now see your animations play according to the character’s movement direction and speed.

---

## 7. Example Animator Setup

Here’s an example configuration for a top-down 4-direction character:

| State | Transition | Condition |
|--------|-------------|------------|
| Idle → Walk | Speed > 0.1 |
| Walk → Idle | Speed < 0.1 |

Each directional sprite can be controlled via a **2D Blend Tree** driven by `Horizontal` and `Vertical`.

---

## 8. Related Topics

- [Character Types](xref:character-types)
- [Character Usage](xref:character-usage)
- [Character Creator](xref:character-creator)

---

> [!TIP]
> If you’re using custom movement logic, you can still drive your Animator Controller manually:
> ```csharp
> animator.SetFloat("Horizontal", direction.x);
> animator.SetFloat("Vertical", direction.y);
> animator.SetFloat("Speed", speed);
> ```

---

