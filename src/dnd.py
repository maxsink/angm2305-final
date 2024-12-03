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
        race = input(f"Enter your race ({', '.join(races)}): ").strip()
        character_class = input(f"Enter your class ({', '.join(classes)}): ").strip()
        alignment = input(f"Enter your alignment ({', '.join(alignments)}): ").strip()
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

#collect generation & store
def random_generate(races, classes, alignments):
    race = random.choice(races)
    character_class = random.choice(classes)
    alignment = random.choice(alignments)
    print(f"Randomly generated character details:")
    print(f"Race: {race}")
    print(f"Class: {character_class}")
    print(f"Alignment: {alignment}")


def input_fields(races, alignments, classes):
    #if input fields
        #what field would you like to input? (provide list) 
            #race
            #class
            #alignment
            #stats
            # cancel
        #ask for imput for specified field. store. 
        #repeat "what field would you like to input? 
            #race
            #class
            #alignment
            #stats
            # done (select to random generate unspecified fields)
        #if "done" selected: "Y/N to confirm: unspecified fields will be randomly generated"
            #Y = randomly generate and compile file  
            #N = repeat from line 18 "what field would you like to input"


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