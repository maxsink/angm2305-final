import random

def main():
    #ask to fully random generate or input fields

    races = get_txt_from_file("races.txt")
    classes = get_txt_from_file("classes.txt")
    alignments = get_txt_from_file("alignments.txt")

    print("Welcome to the D&D Character Sheet Generator!")
    mode = input("Would you like to (1) Input your character manually or (2) Randomize your character? (Enter 1 or 2): ")

    if mode == "1":
        # Self-input phase
        print("\nSelf-Input Mode:")
        input_fields()
    elif mode == "2":
        # Randomization phase
        print("\nRandomization Mode:")
        random_generate()
    else:
        print("Invalid input. Please try again")
        return None



def get_txt_from_file(filename):
    try:
        file = open(filename, 'r')
        lines = file.readlines()
        return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
         file = open(filename, 'w')
    finally:
        file.close()

def stat_calc():
    rolls = [random.randint(1, 6) for _ in range(4)]  # Roll 4d6
    rolls.sort()  # Sort the rolls to easily drop the lowest
    return sum(rolls[1:])  # Sum the highest 3 rolls

#if mode 2: collect generation & store
def random_generate(races, classes, alignments):
    race = random.choice(races)
    character_class = random.choice(classes)
    alignment = random.choice(alignments)
    print(f"Randomly generated character details:")
    print(f"Race: {race}")
    print(f"Class: {character_class}")
    print(f"Alignment: {alignment}")

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

    #alignment
    alignment_input = input(f"Enter your alignment ({', '.join(alignments)}) or press Enter to randomize: ").strip()
    if alignment_input:
        alignment = alignment_input
    else:
        alignment = random.choice(alignments)
        print(f"Randomly generated alignment: {alignment}")
    
    #stats
    print("\nFor Ability Scores (Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma):")
    for stat in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]:
        score_input = input(f"Enter your {stat} score (or press Enter to randomize): ").strip()
        if score_input:
            ability_scores[stat] = int(score_input)
        else:
            ability_scores[stat] = roll_ability_score()
            print(f"Randomly generated {stat} score: {ability_scores[stat]}")



def stat_assign():
    ability_scores = {
        "Strength": stat_calc(),
        "Dexterity": stat_calc(),
        "Constitution": stat_calc(),
        "Intelligence": stat_calc(),
        "Wisdom": stat_calc(),
        "Charisma": stat_calc()
    }    

def sheet_generation():
    #generate character sheet file with info
        #place and format information in character sheet
        #save as character name.jpg

if __name__ == "__main__":
    main()