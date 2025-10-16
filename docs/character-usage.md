---
uid: character-usage
summary: Included components for rendering and animating characters.
---

# Character Usage

The following scripts can be used to load and render characters

- **[Layered Character Group Renderer](#layered-character-group-renderer)** - Load and render a pre-existing Layered Character from a group.
- **[Layered Character Template Renderer](#layered-character-template-renderer)** - Create/load and render a layered character from a template.
- **[Unified Character Template Renderer](#unified-character-template-renderer)** - Create/Load and render a Unified Character from a template.

---

## The Character Shader

A **shader** is how the final character is displayed. Sprites from the **Base Spritesheet** in a **Character Type** are rendered in a component such as a **Sprite Renderer** or used in an **Animator Controller**.

If a **Unified Character** is used, the shader takes the single spritesheet of the character and shows that over the **Base Spritesheet**.  
If a **Layered Character** is used, the shader combines all layers into the final rendered character.  

> [!NOTE]
> If a **Character Renderer** component is used the shader will be applied automatically.

---

## Character Renderers

Character Renderer components can be used to load and display any character you've created regardless of the type. All **Character Renderers** have the following fields:

### References
| Field                       | Type       | Description                                                                                                                  |
| --------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Renderer**                | `Renderer` | Reference to a **Renderer** component such as a **Sprite Renderer**. Used to apply shader.                                   |
| **Set Animator Controller** | `Bool`     | Toggle if the **Animator Controller** referenced in the **Character Type** should be applied to animate the character.       |
| **Animator**                | `Animator` | Reference to an **Animator** component to apply the animator controller. Only shown if  **Set Animator Controller** is true. |

### Loading Settings
| Field                       | Type   | Description                                                                   |
| --------------------------- | ------ | ----------------------------------------------------------------------------- |
| **Loading Mode**            | `Enum` | Option to load character asynchronously or synchronously.                     |
| **Load Character On Start** | `Bool` | if true the the character will be loaded when the **Start** method is called. |

---

## Unified Character Template Renderer
Requirements:  
Have a [Unified Character Type](xref:unified-character-type) and at least one [Unified Character Template](xref:character-templates#unified-character-template) Setup.

The [Unified Character Renderer](xref:BlazerTech.CharacterManagement.Components.UnifiedCharacterTemplateRenderer) component can be used to create and load a character from a **Unified Character Template**.  
- Add the script to a game object.
- Set **Renderer** and optionally **Animator** references.
- Set Loading Settings.
- Reference the **Unified Character Template** you want to load.
- Play your game and if **Load Character On Start** is toggled, your character will be displayed.

---

## Layered Character Renderers

### Layered Character Group Renderer
Requirements:  
Have a [Layered Character Type](xref:layered-character-type) setup and at least one **Layered Character** saved in a group.

[Read More → Character Groups](xref:character-grouping-system)

The [Layered Character Group Renderer](xref:BlazerTech.CharacterManagement.Components.LayeredCharacterGroupRenderer) component can be used to load **Layered Characters** from a **Character Group**.
- Add the script to a game object.
- Set **Renderer** and optionally **Animator** references.
- Set Loading Settings.
- Reference the **Character Type** you want to load a character from.
- Set the **Character Group** you want to load your character from within the **Character Type**.

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
| **Character Load Method** | `Enum`   | Determines how a character is selected from the group: <br> - **Character Name** → Load a character by its saved name. <br> - **Character Index** → Load a character by its index position in the group. <br> - **Randomized** → Randomly load a character from the group. |

---

### Layered Character Template Renderer
Requirements:  
Have a [Layered Character Type](xref:layered-character-type) and at least one [Layered Character Template](xref:character-templates#layered-character-template) Setup.

The [Layered Character Template Renderer](xref:BlazerTech.CharacterManagement.Components.LayeredCharacterTemplateRenderer) component can be used to create and load a character from a  **Layered Character Template**.  
- Add the script to a game object.
- Set **Renderer** and optionally **Animator** references.
- Set Loading Settings.
- Reference the **Layered Character Template** you want to load.
- Play your game and if **Load Character On Start** is toggled, your character will be displayed.
