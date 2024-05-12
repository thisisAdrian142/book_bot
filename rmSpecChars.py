spec_chars="thi$6tr1ng1snot*th@t*speci@l"
print("String before removing any special characters: ", spec_chars)
print()

listforthisstr=[]

for item in spec_chars:
    if item.isalnum():
        listforthisstr.append(item)

no_spec_chars="".join(listforthisstr) #join the all the chars together and get rid of the space
print("String after removing all special characters: ", no_spec_chars)
print()

no_num_chars="".join((num for num in no_spec_chars if not num.isdigit()))
print("String without numbers: ", no_num_chars)

print("--- Begin report of the string ---")
for qualified_char in no_num_chars:
    print(f"The ", qualified_char, "character was found in the string")

print("--- End report ---")
