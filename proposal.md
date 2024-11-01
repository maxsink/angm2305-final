# DND 5E Character Sheet Generator

## Repository
https://github.com/maxsink/angm2305-final.git

## Description
This code will prepare and provide a completed character sheet with a randomly generated name, race, class, stats, and alignment. It will present the option of self inputting for each field, grouped by section for ease of use, and will randomly generate anything not pre-determined, outputting a complete file with the name of the character as the title. This will be an ideal tool for beginner players, short campaigns, or NPC creation. 

## Features
- Option for self input fields
	- When the program begins, the user is presented with an option to fully generate a random character or fill in choice fields. If the user chooses to fill in choice fields, they will be given a list and asked to specify a field, then given the ability to fill it in. The user will be asked if they are done with self-input or if they'd like to input another field. When the user says they are done, fields not defined in this step will be randomly generated.
- Random Generation
	- The program will access a series of dictionaries containing lists and select options randomly from those lists, generating a name, race, class, and alignment. 
- Stat and Skill calculation
	- The code will consider the determined race and class to calculate base stats and skills.  

## Challenges
- DND class and race overlaps- is there a way to adjust the probablity of outcomes for common combinations?
- Will the code be able to interpret user input for race and class correctly in a way that can calculate the base stats and skills?
- What factors should go into statistic determination? Ex: it is more useful for a tiefling rogue to have a high dexterity stat than a dwarf paladin. How can I best implement this consideration into my code?

## Outcomes
Ideal Outcome:
- The code will be able to interpret user input in a way that does not hinder the functionality of statistic calculation and will function in a user friendly way that will make it accessible to anybody who wants to use it.

Minimal Viable Outcome:
- The code randomly generates all fields with no extra consideration for class.

## Milestones

- Week 1
  1. Begin code file with pseudocode. Format and set up functions.
  2. Compile dictionary lists

- Week 2
  1. Implement code
  2. Ensure proper code and file connection

- Week N (Final)
  1. Define display and file saving path
  2. Bug fixes
