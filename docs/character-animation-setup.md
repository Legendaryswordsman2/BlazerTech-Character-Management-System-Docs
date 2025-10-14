---
uid: character-animation-setup
---

# Character Animation Setup

This page goes over how to create and properly configure an **Animator Controller** to be used by your **Character Types**.

## Overview

Every Character Type can include an **Animator Controller**.
This controller provides uesable animations from the sprites contained within the Base Spritesheet set in the **Character Type**

The setup for the **Animator Controller** is the same regardless of if you're using a **Unified** or **Layered Character Type**.

The most important requirement is that all animations **MUST** only use sprites from the **Base Spritesheet** otherwise they won't be renderered correctly when used with the [Character Shader](xref:character-usage#the-character-shader)

If you already have your own movement and animator handling scripts, you can setup the Animator Controller however you need for you project. That means you can create your own Parameters, animations, blend trees, etc.

## Integration With Included Movement And Animator Handling Scripts
The included scripts contain support for the following movement animations:
- Idle
- Walk
- Sprint
- Crouch-Idle
- Crouch-Moving

Additional animations can be triggered through the PlayAnimation(AnimationName) method on all **Character Animation Handler components**.