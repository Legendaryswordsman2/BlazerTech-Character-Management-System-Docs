---
_layout: landing
---

# **BlazerTech Character Management System Docs**

A Character Handler for Unity.

### Features:
1. Modular Layered Characters
2. Layered Characters can be customized at runtime
3. Unified Characters (Characters that are one complete spritesheet and can't be changed at runtime)
   
4. Characters are defined by a character type (Which is a scriptable object), either unified or layered. Both character types require a character tpye id, base spritesheet which defines the size of every character spritesheet of that character type (All frames of a character must be contained within a single spritesheet). And finally the character controller which is a runtime animator controller which will be used to play the animations of the character. All animations within the controller must use frames from the Base Spritesheet. When a character is used it will use a shader to override the base spritesheet and display the character instead of the default spritesheet, this happens the same for both Unified and layered characters. the only difference is for layered characters multiple spritesheets are layered on top of each other one by one witin the shader to display the final character.
   
5. To use a unified character you must first create the Unifed Character Type and define the things previously listed. Then create a Unified Character Template (It's a scriptable Object). A Unified Character Template requires a reference to the Unifed Character Type it's meant to be a template for. A Character Name and a reference to the spritesheet for that template. Now that template can be used to create that character. Whenever that character is used the shader will replace the Base Spritesheet in the Character Type with the Character Spritesheet in the template.
   
6. Layered Character Types must be placed inside a "Resources' folder to be properly initialized. They require the same three things the Unified Character Type Requires (Character Type ID. base Spritesheet and Character Controller). A layered character type contains a list of Character Piece Collections. Each collection can be thought of as a layer for the character. The order of the list determins the order the layers are layered on top of each other.
   
7. A Character Piece Collection is a Scriptable Object that contains a list of Spritesheets (Character Pieces Definitions) that can be used as a layer for that Character Type. A Character Piece Collection requires a reference to the Layered Character Type it's meant for, a Collection Name and A Character Piece Label. This label will be used to fetch every single Spritesheet that is marked as an Addressable and contains the same label. It also must be the same size as the Base Spritesheet in order for it to be valid. The Character Piece Collection will only fetch these spritesheets when the "Get Character Piece" button is pressed within the editor.
   
8. A Character Piece Definition is a class which contains a reference to a spritesheet for that layer of the character. the Name ofthe Spritesheet, Addressable Key used to load the spritesshet, index, reference to the character piece collection it's in and character type the collection is for.
   
9.  Usage Scripts are premade scripts which make using characters easy. To use a Unifed Character Type simply add the "Unifed Character Loader' component, assign it's spriterender so it knows where to replace the material to apply the shader. A reference to the animator to set the animator controller. Set the loading mod to eith Synchronous or Async and choose if you want the character to be loaded on Start using the "Load Character On Start" bool. Finally give it a reference to the Unifed Character template you want to use. When the character is loaded it will apply the animator controller and the shader. The aniamtor controller will use the frames in the Base Spritesheet from the Character Type referenced in the Character Template. The shader will then replace the spritesheet with the one referenced in the Unifed Character Type. If both spritesheets are the same size (Which they will be otherwise an error will be thrown) then the new spritesheet will be shown visually while the Base Spritesheet is the one actually being used.
    
10. The Character Creator allows developers to add their own Character Creation Menu within their game. To start add the "Characer Creation Menu Manager" component anywhere in your scene. The first variable is the "Menu Contents" which takes a game object and should be the base game object that is the parent of the Character Creation Menu. Then reference the Character Type the menu will use. The Character Creation Menu can now be used by players to create their own Characters.
    
11. The Character Creator has a ton of customizability. You can change how you select character pieces in each layer, for example you could use dropdowns, or carousel selectors, or tabs, or any number of other options. You can customize how the character is previewed, it could be static, animated with a predetermined animation, or the animation could be changeable. You could also include buttons that allow you to rotate the character to see all sides. If you choose to include it you could also include a history list that shows every single modification that was made to the character and by clicking on any entry in the list you can go back to that version of the character. The list could have names of the things that were changed, or static frames of what the characer looked like. Or both.
    
12. Within the Character Creation Menu if you don't know what kind of character you like you can randomize the character. You can randomize all layers or only some layers.
    
13. Because Layered Character can be edited at any time you can also include a Character Creation Menu in the main game, for example the pause menu. Whenever you modify the character all instances of that character will automatically be updated.
    
14. When a character is created in the Character Creation Menu it usually needs to be put in a group. There are three types of groups that are separate and unique for each Layered Character Type. The groups are Single Group, Fixed Group and Flexible Group.
    
15. A Single Group is meant for one character and is for simple situations like when the Character Creation Menu is only going to be used for one character such as the player character. It can then be easily loaded from the Single Group in the Layered Character loader Component.
    
16. A Fixed Group is a group that when first created has a pre-set number of characters in it. All characters are automatically created when the group is created and can then be modified.
    
17. A Flexible Group is a group that can hold any number of characters. When first created it contains no characters and characters can be added, removed and modified freely.
    
18. The "Layered Charcter Loader" works the same as the "Unifed Character Loader" except instead of referencing a Character Template you reference the Layered Character Type you want to use, then the Character Group you want to look for a character in, the options are Single Group, Fixed Group or Flexible Group. The Singe Group can only have one character so nothing else is needed to setup. The other two groups can have any amount of characters so you have three ways to find a specific one. You can search by name, index or choose one randomly. Whatever you select, once the character is loaded it will do the same thing as the Unified Character Loader, set the animator controller and shader. The shader works similarly to the Unified Character Shader except it takes all the layeres of the Character (Defined with each Character Piece Collection) and it will combine each layer together one by one to then be displayed as a finalized character. an example of a layerd character could look like this; Body, Eyes, Outfit, Hairstyle and an optional Acessory.
    
19. A Layered Character Template can be used to create premade Layered Characters. They are scriptable objects just like the Unied Character Template. First reference the Layered Character Type it's meant for, then give the Character Name. Once a reference to a Layered Character Type is given, a list will then be shown, one entry for ever Character Piece Collection (Layer of the character). You can select the Character Piece Definition used for each layer out of the options provided with inthe Character Piece Collection for each layer.
    
20. A Layered Character Template Loader can be used to load Layered Characters from a template. All settings are the same as the Unified and Layered Character Loader however you instead need to reference a Layered Character Template. When the Character Loader component is ran it will create a new character using the Template to create each layer of the character.
    
21. Layered Characters can be created at runtime throughcode by providing a list of character piece names for each layer in the character.
    
22. Other usage scripts include a Player Movement Controller component which can be used to control the main character player. You can adjust the character speed and optionally allow for Sprint and Crouch controls.
    
23. A Layered Character Randomizer Component can be used to generate completely randomized characters at runtime, restrictions can be applied to only randomize specific layers or not include specific options. This is perfect for random NPCs.
    
24. A "Character Animator" component can be used to animate the character if the Player Movement Controller component is being used and the Character Animator Controller is setup a particular way.
    
25. A really IMPORTANT part of this Unity Asset is that it contains it's own character sets. A character set is a character with the following layers; Body, Eyes, Outfit, Hairstyle, Accessory. These character come with the asset and can be used in both personal and commercial projects.
    
26. Another really IMPORTANT part of this asset is that it has full support for LimeZu's Modern Interiors and Exteriors asset packs and character included within them. 
        
> [!WARNING]
> THIS WEBSITE IS UNDER CONSTRUCTION AND NOT YET FINISHED!