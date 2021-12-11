#giman.py
# Calculate the mean number of hours it will take to ascend a character to level 80 for AR 8 in Genshin Impact
from time import sleep
from math import ceil

CHARACTERS = ["Albedo", "Jean", "Klee", "Lisa"]

print("Initializing Genshin Impact Level-Up Manager. . .") ; sleep(.3)
print()
print("Welcome!")

def main():
    #input the name of the character you want stats on

    print("----")
    print("Enter the name of a character.")
    infilename = input("Character in question (first name only): ") ; sleep(.3)
    infilename = infilename.lower()



    #Convert the character name input into the corresponding file name
    if infilename == "albedo":
        infilename = "albedo.txt" 

    elif infilename == "jean":
        infilename = "jean.txt"

    elif infilename == 'klee':
        infilename = "klee.txt"

    elif infilename == "lisa":
        infilename = "lisa.txt"

    elif infilename == "whomst":
        print()
        print("The availible characters are:")
        for item in CHARACTERS: #tells you what characters are availible
            if item == CHARACTERS[-1]:
                print(item, end="")
            else:
                print(item, end=", ")
        print()
        main()
    else:
        print()
        print("Sorry, that is not a registered character name.") ; sleep(.6)
        print('Please try again, or check the list of names by entering "whomst"') ; sleep (.6)
        main()
    outfilename = "item_list.txt"

    

    #the file with the character/ item names in it
    infile = open(infilename, "r")
    #the file that is gonna have the processed stats in it
    outfile = open(outfilename, "w")



    #each charaacter needs this much of each item variety
    mora = 300000
    books1 = 3
    books2 = 21
    rock1 = 1
    rock2 =  9
    rock3 =  9
    localspe = 108 
    mons1 = 18
    mons2 = 30
    mons3 = 12
    bossdrop = 26



    for line in infile:
		#assign display name to mora, it'll be the same for every character
        mora_name = "Mora"
        
        #assign display names to the items
        name, books1_name, books2_name, rock1_name, rock2_name, rock3_name, localspe_name, mons1_name, mons2_name, mons3_name, bossdrop_name  = line.split(",")
        
        bossdrop_name = bossdrop_name
        #print the list of materials
        print(name, "Materials", file=outfile)
        print("-------------------------------", file=outfile)
        #mora
        print(mora_name, "x", mora, file=outfile)
        print(file=outfile)
        #books
        print(books1_name, "x", books1, file=outfile)
        print(books2_name, "x", books2, file=outfile)
        print(file=outfile)
        #boss drop
        print(bossdrop_name, "x", bossdrop, file=outfile)
        print(file=outfile)
        #rocks
        print(rock1_name, "x", rock1, file=outfile)
        print(rock2_name, "x", rock2, file=outfile)
        print(rock3_name, "x", rock3, file=outfile)
        print(file=outfile)
        #local specialty
        print(localspe_name, "x", localspe, file=outfile)
        print(file=outfile)
        #monster drop
        print(mons1_name, "x", mons1, file=outfile)
        print(mons2_name, "x", mons2, file=outfile)
        print(mons3_name, "x", mons3, file=outfile)
    infile.close()
    outfile.close()
    print("----")
    print(name + ", " + 'nice choice!') # Their item list is in "item_list.txt"')
    print("----")
    



    #CONVERT ITEMS FROM LOWER TIERS TO HIGHER TIER
    print()
    print()
    print("\_/\_ Convert Materials _/\_/")
    print("-------------------------------")

    #Initialize values
    print("Please input how much of each item you have currently.")
    print("-------------------------------")
    mora_rn = int(input("Mora: "))
    #books
    books1_rn = int(input( books1_name + ": "))
    books2_rn = int(input( books2_name + ": "))
    print()
    #boss drops
    bossdrop_rn = int(input(bossdrop_name + ": "))
    print()
    #rocks
    rock1_rn = int(input( rock1_name + ": "))
    rock2_rn = int(input( rock2_name + ": " ))
    rock3_rn = int(input( rock3_name + ": " ))
    print()
    #local specialties
    localspe_rn = int(input( localspe_name + ": " ))
    print()
    #monster drop
    mons1_rn = int(input( mons1_name + ": " ))
    mons2_rn = int(input( mons2_name + ": "))
    mons3_rn = int(input( mons3_name + ": " ))
    print("-------------------------------")




    rate = 3 #conversion rate for all materials is 3
    #Convert those values
    #MORA
    mora_new = mora_rn #needs no conversion
    bossdrop_new = bossdrop_rn #needs no conversion
    #BOOKS
    #convert the tier 1 books to tier 2 books
    if books1_rn >= books1:
        books1_remain = (books1_rn - books1) % rate
        books1_conv = (books1_rn - books1) // rate
        books1_new = books1 + books1_remain
        books2_new = books1_conv + books2_rn

    else: #if there are less than books1 books, don't convert anything
        books1_new = books1_rn
        books2_new = books2_rn

    #ROCKS
    #convert the tier 1 rocks to tier 2 rocks
    if rock1_rn >= rock1:
        rock1_remain = (rock1_rn - rock1) % rate #the remainder of the conversion
        rock1_conv = (rock1_rn - rock1) // rate #the conversion of 1 -> 2, so this is the tier 2 materials
        rock1_new = rock1_remain + rock1 #add the remainder to the current # of 'rock1's
        rock2_new = rock1_conv + rock2_rn  # add the converted rocks to the current # of 'rock2's
    else: #if there are less than rocks1 rocks1s, don't convert anything
        rock1_new = rock1_rn 
        rock2_new = rock2_rn
    #convert the tier 2 rocks into tier 3 rocks
    if rock2_new >= rock2:
        rock2_remain = (rock2_new - rock2) % rate
        rock2_conv = (rock2_new - rock2) // rate
        rock2_new = rock2_remain + rock2
        rock3_new = rock2_conv + rock3_rn
    else:
        rock2_new = rock2_new
        rock3_new = rock3_rn

    #LOCAL SPECIALTIES
    localspe_new = localspe_rn #needs no conversion

    #MONSTER DROPS
    #convert the tier 1 monster drops into tier 2 monster drops
    if mons1_rn >= mons1:
        mons1_remain = (mons1_rn - mons1) % rate
        mons1_conv = (mons1_rn - mons1) // rate
        mons1_new = mons1_remain + mons1
        mons2_new = mons1_conv + mons2_rn
    else:
        mons1_new = mons1_rn
        mons2_new = mons2_rn
    #convert the tier 2 monster drops into tier 3 monster drops
    if mons2_new >= mons2:
        mons2_remain = (mons2_new - mons2) % rate
        mons2_conv = (mons2_new - mons2) // rate
        mons2_new = mons2_remain + mons2
        mons3_new = mons2_conv + mons3_rn
    else:
        mons2_new = mons2_new
        mons3_new = mons3_rn





    #Write the converted materials in a new text file
    #open the file, write in the file, exit the file
    convertfilename = "converted_materials.txt"
    convertfile = open(convertfilename, "w")
    print("Converted Materials", file=convertfile)
    print("-------------------------------", file=convertfile)
    #mora
    print(mora_name, "x", mora_new, "out of", mora, file=convertfile)
    print(file=convertfile)
    #books
    print(books1_name, "x", books1_new, "/", books1, file=convertfile)
    print(books2_name, "x", books2_new, "/", books2, file=convertfile)
    print(file=convertfile)
    #boss drop
    print(bossdrop_name, "x", bossdrop_new, "/", bossdrop, file=convertfile)
    print(file=convertfile)
    #rocks
    print(rock1_name, "x", rock1_new, "/", rock1, file=convertfile)
    print(rock2_name, "x", rock2_new, "/", rock2, file=convertfile)
    print(rock3_name, "x", rock3_new, "/", rock3, file=convertfile)
    print(file=convertfile)
    #local specialty
    print(localspe_name, "x", localspe_new, "/", localspe, file=convertfile)
    print(file=convertfile)
    #monster drops
    print(mons1_name, "x", mons1_new, "/", mons1, file=convertfile)
    print(mons2_name, "x", mons2_new, "/", mons2, file=convertfile)
    print(mons3_name, "x", mons3_new, "/", mons3, file=convertfile)



    convertfile.close()

    #let the user know the conversion has been stored
    print('Your information is stored in "converted_materials.txt"')
    print("-------------------------------")
    print()
    print()


    #\_/\_ HOW MUCH RESIN/ HOW MANY DAYS _/\_/#
    #-------------------------------------------------------

    print("\_/\_ Resin Costs/ Days til lvl 80 _/\_/")
    print("-------------------------------")


    #library of local specialty's frequency in the overworld per 3 days
    SPECIAL = {'types': ['Wolfhook', 'Valberry', 'Cecilia', 'Windwheel Aster', 'Philanemo Mushroom', 'Small Lamp Grass', 'Calla Lily', 'Dandelion Seed',
                'Jueyun Chili', 'Noctilucous Jade', 'Silk Flower', 'Glaze Lily', 'Qingxin', 'Starconch', 'Violetgrass', 'Cor Lapis',
                'Onikabuto', 'Sakura Bloom', 'Crystal Marrow', 'Dendrobium', 'Naku Weed', 'Sea Ganoderma', 'Sango Pearl', 'Amakumo Fruit', 'Fluorescent Fungus'],
                
                'Wolfhook': {'num': 33}, 'Valberry': {'num': 81}, 'Cecilia': {'num': 50}, 'Windwheel Aster': {'num': 83}, 'Philanemo Mushroom': {'num': 54}, 'Small Lamp Grass': {'num': 72}, 'Calla Lily': {'num': 52}, 'Dandelion Seed': {'num': 53},
                'Jueyun Chili': {'num': 90}, 'Noctilucous Jade': {'num': 45}, 'Silk Flower': {'num': 38}, 'Glaze Lily': {'num': 36}, 'Qingxin': {'num': 48}, 'Starconch': {'num': 71}, 'Violetgrass': {'num': 50}, 'Cor Lapis': {'num': 51},
                'Onikabuto': {'num': 45}, 'Sakura Bloom': {'num': 55}, 'Crystal Marrow': {'num': 66}, 'Dendrobium': {'num': 55}, 'Naku Weed':{'num': 46}, 'Sea Ganoderma': {'num': 46}, 'Sango Pearl': {'num': 44}, 'Amakumo Fruit': {'num': 110}, 'Fluorescent Fungus': {'num': 65}}

    #the number of items you can get per one attempt at getting them

    #one run of a book domain (20 resin)
    books1_per = 2.20
    books2_per = 1.97
    #one run of a boss fight (40 resin)
    rock1_per = 2.15
    rock2_per = 1.60
    rock3_per = 0.14
    bossdrop_per = 2.55

    #this many per local_respawn
    localspe_per = SPECIAL[localspe_name]['num']

    #while you have not enough items, go into this

    #while you have less books than you need, spend more resin until you do...
    #worry about low level items first so that you can convert items-
    #reassign the "new" variables
    resin = 0
    spe_days = 0
    #resin = 160 #initialize resin per day
    days = 0 #initialize days' allowances of resin used
    domain = 20 #cost of domain
    boss = 40 #cost of boss

    #BOSS DROPS
    #get more boss drops
    while bossdrop_new < bossdrop:
        resin += boss

        bossdrop_new += bossdrop_per
        rock1_new += rock1_per
        rock2_new += rock2_per
        rock3_new += rock3_per


    #BOOKS
    #get more books1
    while books1_new < books1:
        resin += domain
        books1_new += books1_per
        books2_new += books2_per
        #convert the tier 1 books to tier 2 books
        if books1_new >= books1:
            books1_remain = (books1_new - books1) % rate
            books1_conv = (books1_new - books1) // rate
            books1_new = books1 + books1_remain
            books2_new = books1_conv + books2_new
        else: #if there are less than books1 books, don't convert anything
            books1_new = books1_new
            books2_new = books2_new

    #get more books2
    while books2_new < books2:
        resin += domain
        books1_new += books1_per
        books2_new += books2_per

        #convert the tier 1 books to tier 2 books
        if books1_new >= books1:
            books1_remain = (books1_new - books1) % rate
            books1_conv = (books1_new - books1) // rate
            books1_new = books1 + books1_remain
            books2_new = books1_conv + books2_new
        else: #if there are less than books1 books, don't convert anything
            books1_new = books1_new
            books2_new = books2_new


    #ROCKS
    #get more rock1
    while rock1_new < rock1:
        resin += boss
        bossdrop_new += bossdrop_per
        rock1_new += rock1_per
        rock2_new += rock2_per
        rock3_new += rock3_per
        #convert tier 1 rocks into tier 2 rocks
        if rock1_new >= rock1:
            rock1_remain = (rock1_new - rock1) % rate 
            rock1_conv = (rock1_new - rock1) // rate 
            rock1_new = rock1_remain + rock1 
            rock2_new = rock1_conv + rock2_new  

    #get more rock2
    while rock2_new < rock2:
        resin += boss
        bossdrop_new += bossdrop_per
        rock1_new += rock1_per
        rock2_new += rock2_per
        rock3_new += rock3_per

        #convert tier 1 rocks into tier 2 rocks    
        if rock1_new > rock1:
            rock1_remain = (rock1_new - rock1) % rate 
            rock1_conv = (rock1_new - rock1) // rate 
            rock1_new = rock1_remain + rock1 
            rock2_new = rock1_conv + rock2_new  

        #convert tier 2 rocks into tier 3 rocks
        if rock2_new >= rock2:
            rock2_remain = (rock2_new - rock2) % rate 
            rock2_conv = (rock2_new - rock2) // rate 
            rock2_new = rock2_remain + rock2
            rock3_new = rock2_conv + rock3_new 

                
    #get more rock3
    while rock3_new < rock3:
        resin += boss
        bossdrop_new += bossdrop_per
        rock1_new += rock1_per
        rock2_new += rock2_per
        rock3_new += rock3_per

        if rock1_new > rock1:
            rock1_remain = (rock1_new - rock1) % rate 
            rock1_conv = (rock1_new - rock1) // rate 
            rock1_new = rock1_remain + rock1 
            rock2_new = rock1_conv + rock2_new  

        #convert tier 2 rocks into tier 3 rocks
        if rock2_new >= rock2:
            rock2_remain = (rock2_new - rock2) % rate 
            rock2_conv = (rock2_new - rock2) // rate 
            rock2_new = rock2_remain + rock2
            rock3_new = rock2_conv + rock3_new 


    days1 = resin / 160
    days = ceil(days1)

    while localspe_new < localspe:
        spe_days +=3
        localspe_new += localspe_per


    resin_costname = "resin_cost.txt"
    resin_cost = open(resin_costname, "w")
    print(name + "'s", "Resin Costs/ Days til lvl 80", file=resin_cost)
    print("-------------------------------", file=resin_cost)
    #mora
    print(mora_name, "x", mora_new, "out of", mora, file=resin_cost)
    print(file=resin_cost)
    #books
    print(books1_name, "x", '{0:.0f}'.format(books1_new), "/", books1, file=resin_cost)
    print(books2_name, "x", '{0:.0f}'.format(books2_new), "/", books2, file=resin_cost)
    print(file=resin_cost)
    #boss drop
    print(bossdrop_name, "x",'{0:.0f}'.format(bossdrop_new), "/", bossdrop, file=resin_cost)
    print(file=resin_cost)
    #rocks
    print(rock1_name, "x", '{0:.0f}'.format(rock1_new), "/", rock1, file=resin_cost)
    print(rock2_name, "x", '{0:.0f}'.format(rock2_new), "/", rock2, file=resin_cost)
    print(rock3_name, "x", '{0:.0f}'.format(rock3_new), "/", rock3, file=resin_cost)
    print(file=resin_cost)
    #THIS PART IS GONNA TELL YOU HOW MANY DAYS OF RESIN THIS IS GONNA TAKE
    print("For all resin-related items, you will need {} resin. That is {} day(s) of resin.".format(resin, days), file=resin_cost)
    print(file=resin_cost)
    #local specialty
    print(localspe_name, "x", '{0:.0f}'.format(localspe_new), "/", localspe, file=resin_cost)
    print(file=resin_cost)
    #THIS PART IS GONNA TELL YOU HOW MANY DAYS OF SPAWNS THIS IS GONNA TAKE
    print("For your Local Specialties, it will take {} days to find enough".format(spe_days), localspe_name + ".", file=resin_cost)
    print(file=resin_cost)
    #monster drops
    print(mons1_name, "x", '{0:.0f}'.format(mons1_new), "/", mons1, file=resin_cost)
    print(mons2_name, "x",'{0:.0f}'.format( mons2_new), "/", mons2, file=resin_cost)
    print(mons3_name, "x", '{0:.0f}'.format(mons3_new), "/", mons3, file=resin_cost)
    print(file=resin_cost)


    resin_cost.close()

    print('Your information is stored in "resin_cost.txt"') 
    print("----")
    print('Please check your files. Happy leveling! (Press enter to close).')
    uwu = input()



if __name__ == "__main__":
    main()