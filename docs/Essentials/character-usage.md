---
uid: character-usage
---

# Character Usage

The following scripts can be used to load and use characters

- **Layered Character Loader** - Load pre-existing Layered Characters.
- **Layered Character Template Loader** - Create/load a layered character from a template.
- **Unified Character Loader** - Load a Unified Character from a template.

---

## Character Loaders

Character loading scripts can be used to load any character you've created regardless of the type. All Character Loaders have these fields:

### References:
| Field | Type | Description |
|-------|------|-------------|
| **Renderer** | `Renderer` | Reference to a **Render** component such as a **Sprite Renderer**. Used to apply shader. |
| **Set Animator Controller** | `Bool` | Toggle if an **animator controller** should be applied to animate the character.  |
| **Animator** | `Animator` | Reference to an **Animator** component to apply the animator controller. Only shown if  **Set Animator Controller** is true. |

### Loading Settings:
| Field | Type | Description |
|-------|------|-------------|
| **Loading Mode** | `Enum` | Option to load character asynchronously or synchronously. |
| **Load Character On Start** | `Bool` | Toggles if the character should be loaded when the **Start** method is called. |

---

## Loading Unified Characters
Requirements:
Have a **Unified Character Type** and at least one **Unified Character Template** Setup.

The **Unified Character Loader** component can be used to create and load a **Unified Character Template**.  
- Add the script to a game object.
- Set **Render** and optionally **Animator** references.
- Set Loading Settings.
- Reference the **Unified Character Template** you want to load.
- Play your game and if **Load Character On Start** is toggled, your character will be displayed.