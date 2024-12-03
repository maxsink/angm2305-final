import random

def main():
    #ask to fully random generate or input fields
    start_msg = ("Enter 'r' to fully randomly generate a character sheet or 'i' to input fields.")

    races = get_txt_from_file("races.txt")
    classes = get_txt_from_file("classes.txt")
    alignments = get_txt_from_file("alignments.txt")

    while True:
        print() #for cleanliness
        choice = input(f"{start_msg}").lower()
        if choice == "r":
            random_generate()
        elif choice == "i":
            input_fields()
        else:
            print("Invalid input. Please try again")


def get_txt_from_file(filename):
    try:
        file = open(filename, 'r')
        lines = file.readlines()
        return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
         file = open(filename, 'w')
    finally:
        file.close()


#collect generation & store
def random_generate(races, classes, alignments):
    race = random.choice(races)
    character_class = random.choice(classes)
    alignment = random.choice(alignments)
    print(f"Randomly generated character details:")
    print(f"Race: {race}")
    print(f"Class: {character_class}")
    print(f"Alignment: {alignment}")

def random_race(races):
        #random choose race 
        races = get_txt_from_file("races.txt")
        return random.choice(races)

def random_alignment(alignments):
        #random choose alignments 
        alignments = get_txt_from_file("alignments.txt")
        return random.choice(alignments)

def random_class(classes):
        #random choose class (consider probability based on race?)
        classes = get_txt_from_file("classes.txt")
        return random.choice(classes)



def input_fields():
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

def stat_calc():
    #calculate stats
        #strength
        #dexterity
        #constitution
        #intelligence
        #wisdom
        #charisma

def sheet_generation():
    #generate character sheet file with info
        #place and format information in character sheet
        #save as character name.jpg

if __name__ == "__main__":
    main()