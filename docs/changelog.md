---
uid: changelog
summary: All notable changes made to the **BlazerTech Character Management System**.
---

# Changelog

All notable updates, improvements, and fixes to the **BlazerTech Character Management System** are listed below.  
This log follows the [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) convention and uses [Semantic Versioning](https://semver.org/).

---

## [0.2.0] - 10-23-2025

### Added
- Added [Top-Down Character Physics Animator Handler component](xref:character-usage#top-down-character-physics-animator-handler). Uses the direction and speed of the game object to set parameters within an Animator Controller.
- Added [Random Layered Character Renderer component](xref:character-usage#random-layered-character-renderer). Automatically creates a new layered character at runtime using the selected Character Type and random layer options.
- Added randomized NPCs sample scene (Sample 2).
- Added [Built-In Character documentation page](xref:built-in-characters). Explains wha's included and how to use the built-in modular characters.
- Added [Character Animation Setup documentation page](xref:character-animation-setup). Explains the setup process for setting up animations and an animator controller for your characters.

### Changed
- Renamed `PlayerMovementController` to `TopDownMovementController`.
- Renamed all Character Loader components to **Character Renderers** (e.g., `Layered Character Template Renderer`).
- Renamed `CharacterAnimatorHandler` to `TopDownCharacterAnimatorHandler`.
- Exposed animator parameters in Character Animator Handler components.
- Changed Animator Controller `Speed` float to `Is Moving` bool.
- Revised [Quick Start Guide](xref:quick-start).
- Revised entire site layout and structure (The site you're on right now!).

---

### Legend
- 🆕 **Added** — New features or systems.
- 🔄 **Changed** — Updates, improvements, or refactors.
- 🐛 **Fixed** — Bug or issue resolution.
- ⚙️ **Internal** — Refactoring or technical improvements not visible to the user.