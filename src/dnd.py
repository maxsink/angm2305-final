import random

def main():
    #ask to fully random generate or input fields
    print("Welcome to the D&D Character Sheet Generator!")
    name = input("Name your character: ")
    mode = input("Would you like to (1) Input your character manually or (2) Randomize your character? (Enter 1 or 2): ")
 
    # Load the options from the text files
    races = get_txt_from_file("races.txt")
    classes = get_txt_from_file("classes.txt")
    alignments = get_txt_from_file("alignments.txt")

    #initialize variables as empty
    race = None
    character_class = None
    alignment = None
    ability_scores = {}

    if mode == "1":
        # Self-input phase
        print("\nSelf-Input Mode:")
        race, character_class, alignment, ability_scores = input_fields(races, alignments, classes)
    elif mode == "2":
        # Randomization phase
        print("\nRandomization Mode:")
        race, character_class, alignment, ability_scores = random_generate()
    else:
        print("Invalid input. Please try again")
        return None
    
    # Return the character details as a dictionary
    return {
        "Name": name,    
        "Race": race,
        "Class": character_class,
        "Alignment": alignment,
        "Ability Scores": ability_scores
    }

def get_txt_from_file(filename):
    try:
        file = open(filename, 'r')
        lines = file.readlines()
        return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found. Creating Empty File.")
        file = open(filename, 'w')
        quit() #exits code - code cannot execute without dictionary files
    finally:
        file.close()


#if mode 2: collect generation & store
def random_generate():
    #load options
    races = get_txt_from_file("races.txt")
    classes = get_txt_from_file("classes.txt")
    alignments = get_txt_from_file("alignments.txt")

    #random generation
    race = random.choice(races)
    character_class = random.choice(classes)
    alignment = random.choice(alignments)
    ability_scores = {
        "Strength": roll_ability_score(),
        "Dexterity": roll_ability_score(),
        "Constitution": roll_ability_score(),
        "Intelligence": roll_ability_score(),
        "Wisdom": roll_ability_score(),
        "Charisma": roll_ability_score()
    }
   
    #show generated character details
    print(f"Randomly generated character details:")
    print(f"Race: {race}")
    print(f"Class: {character_class}")
    print(f"Alignment: {alignment}")
    print(f"Stats: {ability_scores}")

    return race, character_class, alignment, ability_scores
 

#use 4d6 method to calculate stats
def roll_ability_score():
    rolls = [random.randint(1, 6) for _ in range(4)]  # Roll 4d6
    rolls.sort()  # Sort the rolls to drop the lowest
    return sum(rolls[1:])  # Sum the highest 3 rolls


#if mode 1: input fields
def input_fields(races, alignments, classes):
    #race input
    race_input = input(f"Enter your race ({', '.join(races)}) or press Enter to randomize: ").strip()
    if race_input:
        race = race_input
    else:
        race = random.choice(races)
        print(f"Randomly generated race: {race}")
   
    #class input
    class_input = input(f"Enter your class ({', '.join(classes)}) or press Enter to randomize: ").strip()
    if class_input:
        character_class = class_input
    else:
        character_class = random.choice(classes)
        print(f"Randomly generated class: {character_class}")

    #alignment input
    alignment_input = input(f"Enter your alignment ({', '.join(alignments)}) or press Enter to randomize: ").strip()
    if alignment_input:
        alignment = alignment_input
    else:
        alignment = random.choice(alignments)
        print(f"Randomly generated alignment: {alignment}")
    
    #stat input
    ability_scores = {}
    print("\nFor Ability Scores (Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma):")
    for stat in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]:
        score_input = input(f"Enter your {stat} score (or press Enter to randomize): ").strip()
        if score_input:
            ability_scores[stat] = int(score_input)
        else:
            ability_scores[stat] = roll_ability_score()
            print(f"Randomly generated {stat} score: {ability_scores[stat]}")

    return race, character_class, alignment, ability_scores

#print character sheet to terminal
def print_character_sheet(character, name):
    if character:
        print(f"\n--- {name} ---\n--- Character Sheet ---")
        for key, value in character.items():
            if key == "Ability Scores":
                print(f"{key}:")
                for stat, score in value.items():
                    print(f"  {stat}: {score}")
            else:
                print(f"{key}: {value}")
        print("\nCharacter sheet generated successfully!")


#def txtfile_generation():
    #generate character sheet file with info
        #place and format information in character sheet
        #save as character name.txt
def save_character_sheet(character, name ):
    filename=(f"{name}_CharacterSheet.txt")
    with open(filename, 'w') as file:
        file.write("--- Character Sheet ---\n")
        for key, value in character.items():
            if key == "Ability Scores":
                file.write(f"{key}:\n")
                for stat, score in value.items():
                    file.write(f"  {stat}: {score}\n")
            else:
                file.write(f"{key}: {value}\n")
    print(f"\nCharacter sheet saved to {filename}")


if __name__ == "__main__":
    character = main()
    if character:
        print_character_sheet(character, character['Name'])
        save_character_sheet(character, character['Name'])
