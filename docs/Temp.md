---
uid: temp
summary: Components for rendering, animating, and controlling characters.
---

# Character Usage

The **Character Usage System** provides the runtime components needed to **load**, **render**, **animate**, and **control** characters.  
Whether using pre-made unified sprites or fully modular layered characters, these components work together to display, animate, and move your characters in-game.

---

## 📦 Overview

| Component Type | Purpose | Works With |
|----------------|----------|------------|
| **Character Renderers** | Display and load characters at runtime. | Unified / Layered |
| **Animator Handlers** | Control and update animator parameters based on player movement or physics. | Any animated character |
| **Character Controllers** | Handle player input and movement logic. | Any Character Renderer |

---

## 🧩 The Character Shader

A **Character Shader** defines how the final character is rendered.

- **Unified Characters:** Use a single spritesheet rendered directly onto the base texture.
- **Layered Characters:** Combine multiple texture layers (body, outfit, hair, etc.) into one composite texture.

> [!NOTE]
> If you’re using a **Character Renderer** component, the shader is applied automatically.  
> You can also manually assign your own compatible shader for custom rendering.

---

## 🎨 Character Renderer Components

All **Character Renderer** components share similar fields and behavior.

### References

| Field | Type | Description |
|-------|------|-------------|
| **Renderer** | `Renderer` | Reference to a **Sprite Renderer** or other renderer component used to display the character. |
| **Set Animator Controller** | `bool` | Automatically assigns the **Animator Controller** from the referenced **Character Type**. |
| **Animator** | `Animator` | Reference to an Animator component used to animate the character. Shown only if the above option is enabled. |

### Loading Settings

| Field | Type | Description |
|-------|------|-------------|
| **Loading Mode** | `Enum` | Choose between **Synchronous** or **Asynchronous** character loading. |
| **Load Character On Start** | `bool` | If true, automatically loads the character when the component starts. |

---

## 🧍 Unified Character Template Renderer

**Requirements**
- A [Unified Character Type](xref:unified-character-type)
- At least one [Unified Character Template](xref:character-templates#unified-character-template)

The [`UnifiedCharacterTemplateRenderer`](xref:BlazerTech.CharacterManagement.Components.UnifiedCharacterTemplateRenderer)  
creates and renders a **Unified Character** from a template.

**Setup Steps**
1. Add the component to a GameObject.  
2. Assign a **Renderer** (usually a Sprite Renderer).  
3. Optionally assign an **Animator**.  
4. Configure **Loading Settings**.  
5. Assign the **Unified Character Template**.  
6. Play the scene — the character will appear automatically if **Load Character On Start** is enabled.

---

## 🧍‍♀️ Layered Character Renderers

### Layered Character Group Renderer

**Requirements**
- A [Layered Character Type](xref:layered-character-type)
- At least one saved **Layered Character Group**

The [`LayeredCharacterGroupRenderer`](xref:BlazerTech.CharacterManagement.Components.LayeredCharacterGroupRenderer)  
renders **saved or existing characters** stored within a **Character Group**.

**Setup Steps**
1. Add to a GameObject.  
2. Assign a **Renderer** and optional **Animator**.  
3. Configure **Loading Settings**.  
4. Assign the **Character Type**.  
5. Select the **Group Type** (Primary, Flexible, or Fixed) and configure parameters.

#### Group Parameters

| Parameter | Type | Description |
|------------|------|-------------|
| **Character Group Name** | `string` | Name of the group to load from. |
| **Character Load Method** | `Enum` | How to select the character:<br>- **By Name**<br>- **By Index**<br>- **Randomized** |

> [!TIP]
> Use **Flexible Groups** for editable rosters, and **Fixed Groups** for predefined teams or NPC slots.

---

### Layered Character Template Renderer

**Requirements**
- A [Layered Character Type](xref:layered-character-type)
- At least one [Layered Character Template](xref:character-templates#layered-character-template)

The [`LayeredCharacterTemplateRenderer`](xref:BlazerTech.CharacterManagement.Components.LayeredCharacterTemplateRenderer)  
creates and displays a new **Layered Character** directly from a template.

**Setup Steps**
1. Add the component to a GameObject.  
2. Assign a **Renderer** and optional **Animator**.  
3. Configure **Loading Settings**.  
4. Assign the **Layered Character Template** to load.  
5. Run the game — the character will appear if **Load Character On Start** is enabled.

---

## 🎞️ Character Animator Handlers

The **Animator Handler Components** control character animation parameters during gameplay.  
They are designed to work with **any character using an Animator Controller**, updating parameters such as movement direction, idle states, and animation speed.

### ⚙️ Character Animator Handler
[`CharacterAnimatorHandler`](xref:BlazerTech.CharacterManagement.Components.CharacterAnimatorHandler)

A lightweight animator controller used for **manual or scripted movement** (e.g., controlled by AI, dialogue, or cutscenes).  
It updates the Animator parameters based on movement input provided by another script.

**Common Parameters**
| Parameter | Type | Description |
|------------|------|-------------|
| **Horizontal** | `float` | Left/right movement direction. |
| **Vertical** | `float` | Up/down movement direction. |
| **Speed** | `float` | Normalized speed used to blend between idle and movement animations. |

> [!NOTE]
> Use this when you’re handling movement manually or through non-physics systems.

---

### 🌐 Physics Character Animator Handler
[`PhysicsCharacterAnimatorHandler`](xref:BlazerTech.CharacterManagement.Components.PhysicsCharacterAnimatorHandler)

A physics-driven variant that automatically reads velocity from a **Rigidbody2D** and updates Animator parameters accordingly.  
Perfect for top-down or side-scrolling characters using physical movement.

**Additional Parameters**
| Parameter | Type | Description |
|------------|------|-------------|
| **Velocity Threshold** | `float` | Minimum movement speed before switching from idle to moving. |
| **Use Rigidbody Velocity** | `bool` | If true, animator parameters are updated from Rigidbody velocity. |

> [!TIP]
> Combine with the **Top Down Movement Controller** or future **Side-Scroller Controller** for seamless integration.

---

## 🎮 Character Controllers

Character Controllers handle movement, input, and physics.  
They are separate from Animator Handlers, allowing flexible setups where movement logic and animation logic are decoupled.

### 🧭 Top Down Movement Controller
[`TopDownMovementController`](xref:BlazerTech.CharacterManagement.Components.TopDownMovementController)

Handles movement for top-down characters using **WASD or arrow key input**.  
Automatically updates the Rigidbody2D position and integrates with Animator Handlers for directional animation.

**Features**
- Supports walking, sprinting, and diagonal movement.  
- Works with both **Layered** and **Unified** characters.  
- Can be paired with `PhysicsCharacterAnimatorHandler` for auto animation updates.  

**Inspector Fields**
| Field | Type | Description |
|--------|------|-------------|
| **Move Speed** | `float` | Base walking speed. |
| **Sprint Multiplier** | `float` | Speed multiplier when sprinting. |
| **Rigidbody2D** | `Component` | The Rigidbody2D component controlling movement. |
| **Animator Handler** | `Component` | Reference to an Animator Handler to synchronize animation. |

> [!TIP]
> Use this controller for any 2D top-down project — NPCs, player characters, or crowd systems.

---

### 🧱 (Coming Soon) Side-Scroller Movement Controller

A 2D side-scrolling movement component with support for:
- Horizontal running and jumping.  
- Rigidbody2D-based motion with gravity.  
- Optional crouch, climb, or attack parameter support.  
- Integrated animation syncing through `PhysicsCharacterAnimatorHandler`.

Stay tuned for this addition in **BT-CMS v1.1+**.

---

## 🧠 Summary

| Task | Component | Works With |
|------|------------|------------|
| Render a pre-made character | **Unified Character Template Renderer** | Unified |
| Render a customizable character | **Layered Character Template Renderer** | Layered |
| Load a saved or grouped character | **Layered Character Group Renderer** | Layered |
| Drive animations by script | **Character Animator Handler** | All |
| Drive animations via physics | **Physics Character Animator Handler** | All |
| Handle movement input | **Top Down Movement Controller** | All |

---

## 🔗 Next Steps
- [Read More → Character Creator](xref:character-creator)  
- [Read More → Character Groups](xref:character-grouping-system)  
- [Read More → Character Templates](xref:character-templates)  
- [Read More → Character Animator Setup](xref:character-animation-setup)
