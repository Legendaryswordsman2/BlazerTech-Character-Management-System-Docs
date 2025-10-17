---
uid: character-usage
summary: Included components for rendering and animating characters.
---

# Character Usage

The **BlazerTech Character Management System** includes the runtime components needed to **load**, **render**, **animate** and **control** characters.

| Component Type                            | Purpose                                                                                                  |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Character Renderer components**         | Load and render a character.                                                                             |
| **Character Animator Handler components** | Control specific **paramters** set in an **Animator Controller** used to properly animate the character. |
| **Character Movement components**         | Handle player input and movement logic.                                                                  |

---

## The Character Shader

A shader is used to visually display a character over the **Base Spritesheet**.  
Sprites from the **Base Spritesheet** assigned in a **Character Type** are rendered in a component such as a **Sprite Renderer** or used in an **Animator Controller**.

If a **Unified Character** is used, the shader takes the single spritesheet of the character and shows that over the **Base Spritesheet**.  
If a **Layered Character** is used, the shader combines all layers into the final rendered character.  

> [!NOTE]
> If a **Character Renderer** component is used the shader will be applied automatically.

---

## Character Renderer Components

Character Renderer components will load and display any character regardless of the type

### Components

| Renderer Component                                                          | Used For                                                                 |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| [Layered Character Group Renderer](#layered-character-group-renderer)       | Load a saved **Layered Character** from a group.                         |
| [Layered Character Template Renderer](#layered-character-template-renderer) | Create and render a **Layered Character** from a template.               |
| [Unified Character Template Renderer](#unified-character-template-renderer) | Create and render a **Unified Character** from a template.               |
| [Random Layered Character Renderer](#random-layered-character-renderer)     | Create a new **Layered Character** with completely random layer options. |

### Character Renderer Core Fields

All Character Renderer components have the following fields.

#### References
| Field                       | Type       | Description                                                                                                                  |
| --------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Renderer**                | `Renderer` | Reference to a **Renderer** component such as a **Sprite Renderer**. Used to apply character shader.                         |
| **Set Animator Controller** | `Bool`     | Automatically assigns the Animator Controller from the referenced Character Type.                                            |
| **Animator**                | `Animator` | Reference to an **Animator** component to apply the animator controller. Only shown if  **Set Animator Controller** is true. |

#### Loading Settings
| Field                       | Type   | Description                                                                   |
| --------------------------- | ------ | ----------------------------------------------------------------------------- |
| **Loading Mode**            | `Enum` | Option to load character **asynchronously** or **synchronously**.             |
| **Load Character On Start** | `Bool` | If true the the character will be loaded when the **Start** method is called. |

---

## Unified Character Template Renderer

- **Component**: [UnifiedCharacterTemplateRenderer](xref:BlazerTech.CharacterManagement.Components.UnifiedCharacterTemplateRenderer).  

Requirements:  
- A [Unified Character Type](xref:unified-character-type).
- At least one [Unified Character Template](xref:character-templates#unified-character-template).

The **Unified Character Template Renderer** component renderers a **Unified Character** from a **Unified Character Template**.

**Setup Steps:**
1. Add the component to a GameObject.
2. Assign **Renderer** (Usually a Sprite Renderer).
3. optionally assign **Animator**.
4. Configure Loading Settings.
5. Assign the **Unified Character Template** you want to use.
6. Play your game and if **Load Character On Start** is enabled, your character will be displayed.

---

## Layered Character Renderers

### Layered Character Group Renderer

- **Component**: [LayeredCharacterGroupRenderer](xref:BlazerTech.CharacterManagement.Components.LayeredCharacterGroupRenderer).  

**Requirements:**  
- A [Layered Character Type](xref:layered-character-type).  
- At least one **Layered Character** saved in a group.  

[Read More → Character Groups](xref:character-grouping-system)

The **Layered Character Group Renderer** component renderers a previously saved **Layered Character** from a **Character Group**.

**Setup Steps:**
1. Add the component to a GameObject.
1. Assign **Renderer** (Usually a Sprite Renderer).
2. optionally assign **Animator**.
3. Configure Loading Settings.
5. Assign the **Character Type** you want to load a character from.
6. Select the **Character Group** (Primary, Flexible or Fixed) and configure parameters.

#### Character Groups
After a **Character Type** has been referenced, you can choose which group you want to load a **Layered Character** from:

| Group Type                 | Description                                                                                           |
| -------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Primary Character Slot** | A single character contained in the Character Type. No additional parameters required.                |
| **Flexible Group**         | A group of characters that can be added, removed, or edited at any time.                              |
| **Fixed Group**            | A group with a preset number of characters. New characters cannot be added or removed after creation. |

If **Flexible Group** or **Fixed Group** is selected, the following parameters are required:

| Parameter                 | Type     | Description                                                                                                                                                                                                                                                                |
| ------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Character Group Name**  | `String` | A unique name used to find the fixed or flexible group.                                                                                                                                                                                                                    |
| **Character Load Method** | `Enum`   | Determines how a character is selected from the group: <br> - **Character Name** > Load a character by its saved name. <br> - **Character Index** > Load a character by its index position in the group. <br> - **Randomized** > Randomly load a character from the group. |

---

### Layered Character Template Renderer

- **Component**: [LayeredCharacterTemplateRenderer](xref:BlazerTech.CharacterManagement.Components.LayeredCharacterTemplateRenderer). 

**Requirements:**
- A [Layered Character Type](xref:layered-character-type).  
- At least one [Layered Character Template](xref:character-templates#layered-character-template).

The **Layered Character Template Renderer** component renderers a **Layered Character** from a **Layered Character Template**.

**Setup Steps:**
1. Add the component to a GameObject.
2. Assign **Renderer** (Usually a Sprite Renderer).
3. optionally assign **Animator**.
4. Configure Loading Settings.
5. Assign the **Layered Character Template** you want to use.
6. Play your game and if **Load Character On Start** is enabled, your character will be displayed.

---

### Random Layered Character Renderer

- **Component**: [RandomLayeredCharacterRenderer](xref:BlazerTech.CharacterManagement.Components.RandomLayeredCharacterRenderer). 

**Requirements:**
- A [Layered Character Type](xref:layered-character-type).

The **Random Layered Character Renderer** component creates and renders a **completely random Layered Character**. A random option is chosen from every layer.

**Setup Steps:**
1. Add the component to a GameObject.
2. Assign **Renderer** (Usually a Sprite Renderer).
3. optionally assign **Animator**.
4. Configure Loading Settings.
5. Assign the **Layered Character Type** you want to use.
6. Play your game and if **Load Character On Start** is enabled, a new completely randomized character will be displayed.

---

## Character Animator Handlers

---

### Character Animator Handler

---

### Physics Character Animator Handler

---

## Character Controllers

---

### Top Down Movement Controller

---

### (Coming Soon) Side-Scroller Movement Controller