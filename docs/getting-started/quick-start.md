---
uid: quick-start
---

# Quick Start Guide

![Logo](/images/blazertech-character-management-system-cover-iamge.png)

This guide should get you on your feet and teach you the basics of how to use the **BlazerTech Character Management System**.

It's recommended to read through the [Basic Concepts](xref:basic-concepts) before reading the **Quick Start Guide**.

## Creating a Character Type

If you only plan to use the built-in characters you can skip straight to [Character Usage](#character-usage)

<!-- This guide will assume you want to use Layered Characters (Characters built of multiple parts layered on top of each other). -->
This guide will show you how to create both Unified and Layered Characters.

**Create a Character Type Asset**
**Right click** the **Project window** and navigate to **Create > BlazerTech > Character Management System** and select either **Layered Character Type** or **Unified Character Type**.

> [!TIP]
> Unsure which **Character Type** to create? Read more about the difference between them [here](xref:character-types#character-type-variants)

You can name the asset whatever you'd like.

### Character Type Core Fields

Three fields are required regardless of the Character Type you chose.

**Character Type ID**:  
A **unique** identifier for this Character Type. Can be whatever you want as long as it's not the same as another Character Type.


**Base Spritesheet**:  
The core spritesheet that contains all frames that characters of this type will include.  
All future characters will need to have a spritesheet that is the exact same size as the **Base Spritesheet**.  

The Base Spritesheet should be the character in it's most barebones state without any extra clothing, hair, accessories, etc.
Set the **Sprite Mode** of the spritesheet to **Multiple**. This will let you slice the spritesheet into multiple sprites so each frame can be used individually.

- [Read More → Base Spritesheet](xref:character-type-core#base-spritesheet)  

**Character Controller**: (Optional)  
If you choose to, you can create an Animator Controller and assign it to the Character Controller field. Animation clips in the Animator Controller should use sprites from the **Base Spritesheet** otherwise the character won't be displayed correctly when the character shader is applied.  

Later in this guide when you learn how to use your character you can have the Character Controller automatically applied when the character is used.

- [Read More → Character Shader](xref:character-usage#the-character-shader)  
- [Read More → Character Controller](xref:character-type-core#character-controller)  

**No further setup is required for Unified Character Types.**

### Layered Character Specific Setup

Since Layered Characters are built of multiple layers, we need to define what those layers are.

**Create Layer Assets**
Each layer is represented as a separate scriptable object.
To create a layer once again right click the **Project window** and navigate to **Create > BlazerTech > Character Management System > Layered Character Type > Character Layer**.  

A layer asset contains all spritesheets that can be used for that specific layer. These are called Layer Options.

Read [Character Layers](xref:character-layers) to learn how to properly setup each layer and add Layer Options.


## Creating a Character Template  

Now that we have our character type created, we need an actual character.  
There are many ways to create a character from a Character Type but for this guide we'll be using the simplest one, a **character template**.  

You can think of a character template as a blueprint that lets use create a character from it later during runtime.

---

## Character Usage