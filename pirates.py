from collections import defaultdict




SCRIPT_PATH = "pirates.txt"

main_characters = defaultdict(lambda: 0)

text = open(SCRIPT_PATH).read().split("\n")
for line in text:
    char = ""
    for x in line:
        if str.isupper(x):
            char += x
        elif x == " ":
            char += " "
        else:
            break
    if char:
        main_characters[char] += 1
        if char == "JACK SPARROW":
            print line

mc_list = sorted(main_characters.items(), key=lambda x: x[1], reverse=True)

#for x in mc_list:
#    print x[0] + "\t\t" + str(x[1])
