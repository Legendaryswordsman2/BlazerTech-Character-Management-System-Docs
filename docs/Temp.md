---
uid: temp
summary: Components for rendering, animating, and controlling characters.
---

# Character Usage

The **Character Usage System** provides the core runtime components that let you **load**, **render**, **animate**, and **control** characters.  
From displaying pre-made characters to handling player movement and animation blending — these systems form the foundation of runtime character behavior.

---

## 📦 Overview

| Component Type | Purpose | Works With |
|----------------|----------|------------|
| **Character Renderers** | Load and display characters at runtime. | Unified & Layered |
| **Animator Handlers** | Update Animator parameters based on player or physics movement. | Any animated character |
| **Character Controllers** | Handle user input and movement logic. | All character types |

---

## 🧩 The Character Shader

A **Character Shader** determines how the final sprite(s) are combined and displayed.  

- **Unified Characters:** A single spritesheet overrides the base spritesheet defined in the **Character Type**.  
- **Layered Characters:** Multiple textures (Body, Outfit, Hair, etc.) are merged into one composite using the shader.  

> [!NOTE]
> When using a **Character Renderer**, the shader is automatically applied at runtime. You can override it manually if needed.

---

## 🎨 Character Renderer Components

Each **Character Renderer** handles loading and displaying characters of a specific type or source.

### Shared Fields

| Field | Type | Description |
|-------|------|-------------|
| **Renderer** | `Renderer` | The component (usually a **Sprite Renderer**) used to display the character. |
| **Set Animator Controller** | `bool` | If enabled, automatically applies the **Animator Controller** from the **Character Type**. |
| **Animator** | `Animator` | Reference to the Animator component. Only visible if **Set Animator Controller** is enabled. |

### Loading Settings

| Field | Type | Description |
|-------|------|-------------|
| **Loading Mode** | `Enum` | Load characters synchronously or asynchronously. |
| **Load Character On Start** | `bool` | If true, loads the character automatically when the component starts. |

---

## 🧍 Unified Character Template Renderer

**Requirements:**
- [Unified Character Type](xref:unified-character-type)
- [Unified Character Template](xref:character-templates#unified-character-template)

The [`UnifiedCharacterTemplateRenderer`](xref:BlazerTech.CharacterManagement.Components.UnifiedCharacterTemplateRenderer)  
instantiates and renders a **Unified Character** directly from a template.

**Setup Steps**
1. Add the component to a GameObject.  
2. Assign a **Renderer** and optionally an **Animator**.  
3. Configure **Loading Settings**.  
4. Reference a **Unified Character Template**.  
5. Run the game — the character will load if **Load Character On Start** is enabled.

---

## 🧍‍♀️ Layered Character Renderers

### Layered Character Group Renderer

**Requirements:**
- [Layered Character Type](xref:layered-character-type)
- One or more saved **Layered Character Groups**

The [`LayeredCharacterGroupRenderer`](xref:BlazerTech.CharacterManagement.Components.LayeredCharacterGroupRenderer)  
renders **saved or existing Layered Characters** stored in a **Character Group**.

| Parameter | Type | Description |
|------------|------|-------------|
| **Character Group Type** | `Enum` | Select between **Primary**, **Flexible**, or **Fixed** groups. |
| **Character Group Name** | `string` | The group name to load from. Required for Flexible/Fixed groups. |
| **Character Load Method** | `Enum` | Select how to choose which character to load:<br>- **By Name**<br>- **By Index**<br>- **Randomized** |

> [!TIP]
> Use **Flexible Groups** for editable rosters or randomized NPCs, and **Fixed Groups** for predefined slots.

---

### Layered Character Template Renderer

**Requirements:**
- [Layered Character Type](xref:layered-character-type)
- [Layered Character Template](xref:character-templates#layered-character-template)

The [`LayeredCharacterTemplateRenderer`](xref:BlazerTech.CharacterManagement.Components.LayeredCharacterTemplateRenderer)  
creates and displays a new **Layered Character** from a template.

**Setup Steps**
1. Add to a GameObject.  
2. Assign a **Renderer** and optional **Animator**.  
3. Configure **Loading Settings**.  
4. Reference the **Layered Character Template**.  
5. Run the game to see your generated character.

---

## 🎞️ Character Animator Handlers

Animator Handlers automatically update Animator parameters each frame based on character or physics movement.  
They work with any character using a compatible **Animator Controller** and support crouch, sprint, and directional animations.

---

### 🧠 Character Animator Handler Base

[`CharacterAnimatorHandlerBase`](xref:BlazerTech.CharacterManagement.Components.CharacterAnimatorHandlerBase)  
provides the shared functionality used by all animator handlers.

| Field | Description |
|-------|--------------|
| **Animator** | The Animator component used for animation control. |
| **Is Moving Param** | The Animator bool parameter name (default: `"Is Moving"`). |
| **Horizontal Movement Param** | The Animator float parameter name for X movement (default: `"Horizontal Movement"`). |
| **Vertical Movement Param** | The Animator float parameter name for Y movement (default: `"Vertical Movement"`). |

**Key Methods**
- `UpdateAnimatorParameters()` — Sets movement and direction values each frame.  
- `ChangeDirection(FourDirectional/EightDirectional)` — Immediately updates facing direction values.  
- `PlayAnimation(string)` — Plays a specific animation state by name.  
- `PlayDefaultAnimation()` — Plays the default animation state defined in the Animator Controller.  

> [!NOTE]
> This base class isn’t meant to be used directly — use one of its specialized variants below.

---

### 🌐 Physics Character Animator Handler

[`PhysicsCharacterAnimatorHandler`](xref:BlazerTech.CharacterManagement.Components.PhysicsCharacterAnimatorHandler)  
is a **physics-driven** animator handler that updates animations based on the GameObject’s Rigidbody2D movement.

| Field | Type | Description |
|--------|------|-------------|
| **Enable Sprint** | `bool` | If true, enables sprinting animations when speed ≥ *Sprint Min Speed*. |
| **Sprint Min Speed** | `float` | Minimum speed required to trigger sprint animation. |
| **Sprint Parameter Name** | `string` | Animator bool name for sprint state (default: `"Is Sprinting"`). |
| **Enable Crouch** | `bool` | Enables crouching animations when speed ≤ *Crouch Max Speed*. |
| **Crouch Max Speed** | `float` | Maximum speed before switching out of crouch animation. |
| **Crouch Parameter Name** | `string` | Animator bool name for crouch state (default: `"Is Crouching"`). |

**How It Works**
- Calculates movement each `FixedUpdate()` by comparing current and previous positions.  
- Determines direction and speed, then updates Animator parameters.  
- Optionally toggles sprint/crouch states when enabled.  

> [!TIP]
> Ideal for physics-based player or NPC movement — simply attach it alongside a Rigidbody2D.

---

### 🧭 Top-Down Character Animator Handler

[`TopDownCharacterAnimatorHandler`](xref:BlazerTech.CharacterManagement.Components.TopDownCharacterAnimatorHandler)  
is designed for **top-down player characters**, syncing directly with a [`TopDownMovementController`](#🕹️-top-down-movement-controller).

| Field | Type | Description |
|--------|------|-------------|
| **Top Down Movement Controller** | `TopDownMovementController` | Reference to the movement controller script. |
| **Sprint Parameter Name** | `string` | Animator bool name for sprint state. |
| **Crouch Parameter Name** | `string` | Animator bool name for crouch state. |

**How It Works**
- Reads movement and state data from the linked controller (`IsMoving`, `IsSprinting`, `IsCrouching`).  
- Updates Animator floats and bools in real-time to reflect the character’s state.  
- Fully integrated with crouch and sprint systems.

> [!IMPORTANT]
> This component requires a `TopDownMovementController` on the same GameObject or a linked reference.

---

## 🎮 Character Controllers

Character Controllers handle **player input**, **movement**, and **physics** while exposing properties used by Animator Handlers.  
They can be used standalone or alongside a **Character Renderer**.

---

### 🕹️ Top-Down Movement Controller

[`TopDownMovementController`](xref:BlazerTech.CharacterManagement.Components.TopDownMovementController)  
manages player movement for top-down 2D games using **Rigidbody2D** motion and **keyboard input**.

**Features**
- Supports movement, sprinting, and crouching.  
- Adjustable movement speeds per state.  
- Exposes directional data to Animator Handlers.  

**Inspector Fields**

| Field | Type | Description |
|--------|------|-------------|
| **Move Speed** | `float` | Base walking speed. |
| **Enable Sprint** | `bool` | Allows sprinting with **Left Shift**. |
| **Sprint Speed** | `float` | Movement speed while sprinting. |
| **Enable Crouch** | `bool` | Allows crouching with **C** or **Left Ctrl**. |
| **Crouch Speed** | `float` | Movement speed while crouching. |
| **Can Move** | `bool` | Toggles whether the character can move. |

**Runtime Properties**

| Property | Type | Description |
|-----------|------|-------------|
| **IsMoving** | `bool` | True if character is currently moving. |
| **IsSprinting** | `bool` | True if sprint input is active. |
| **IsCrouching** | `bool` | True if crouch input is active. |
| **Movement** | `Vector2` | Current movement direction. |

> [!TIP]
> Combine this with a `TopDownCharacterAnimatorHandler` for complete animated top-down control.

---

### 🧱 (Coming Soon) 2D Side-Scroller Controller

Planned for future versions of BT-CMS, this controller will provide:
- Horizontal running, jumping, and crouching.  
- Full integration with **PhysicsCharacterAnimatorHandler**.  
- Optional ladder climbing, falling, and grounded animations.

Stay tuned for **v1.1+** updates.

---

## 🧠 Summary

| Task | Component | Works With |
|------|------------|------------|
| Render a pre-made character | **Unified Character Template Renderer** | Unified |
| Render a customizable character | **Layered Character Template Renderer** | Layered |
| Load saved characters | **Layered Character Group Renderer** | Layered |
| Handle animator logic (manual) | **Character Animator Handler Base** | All |
| Handle animator logic (physics) | **Physics Character Animator Handler** | All |
| Handle animator logic (top-down)** | **Top-Down Character Animator Handler** | Layered / Unified |
| Handle movement & input | **Top-Down Movement Controller** | All |

---

## 🔗 Next Steps
- [Read More → Character Animator Setup](xref:character-animation-setup)  
- [Read More → Character Creator](xref:character-creator)  
- [Read More → Character Groups](xref:character-grouping-system)  
- [Read More → Character Templates](xref:character-templates)
