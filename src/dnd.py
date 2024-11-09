#ask to fully random generate or input fields

#if random generate
    #random choose race 
    #random generate name from dict list for race
    #random choose class (consider probability based on race?)
    #random choose alignment

#if input fields
    #what field would you like to input? (provide list) 
        #name
        #race
        #class
        #alignment
        #stats
        # cancel
    #ask for imput for specified field. store. 
    #repeat "what field would you like to input? 
        #name
        #race
        #class
        #alignment
        #stats
        # done (select to random generate unspecified fields)
    #if "done" selected: "Y/N to confirm: unspecified fields will be randomly generated"
        #Y = randomly generate and compile file  
        #N = repeat from line 18 "what field would you like to input"

#calculate stats
    #strength
    #dexterity
    #constitution
    #intelligence
    #wisdom
    #charisma

#generate character sheet file with info
    #place and format information in character sheet
    #save as character name.jpg