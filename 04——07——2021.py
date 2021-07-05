mix=[1,2,3,4,5]
mix.append(6)       # insert number using append
# the last one in the row

mix.extend([7,8])   # insert more than one number into the array
s=len(mix)
mix.insert(0,0)     # insert 0 in the zero place

mix.remove(0)    # remove number from array
del mix[0]      # remove fisrt number from array
name = mix.pop() # name the last value and take it out from the array(last in fisrt out)
print(mix)
print(s)
print(name)
#insert numbers into form['fish', 88, 'darkness', 90, 'mix', 85, 'jing', 90, 'fall', 88]
#from member = ['fish', 'darkness', 'mix', 'jing', 'fall']
member = ['fish', 'darkness', 'froggy way', 'jing', 'falling sun']
member.insert(1,88)
member.insert(3,90)
member.insert(5,85)
member.insert(7,90)
member.insert(9,88)
print(member)

for i in range(len(member)):
    print(member[i])

for i in range(0,len(member),2):
    print(member[i],member[i+1])

s=member.count(88) # count the number of the variable appear in the array
print(member)
print(s)
s1=member.index(88)# find the indix of the variable
print(s1)
s2 = member.index(88,0,len(member)) #find varable in certain range, hoever only return the first index postion
print(s2)
member.reverse()
print(member) # reverse the order of the array

list=[1,34,35,34,223,234,5]
list.sort()
print(list) # sort the number from small to largerst
list.sort(reverse=True)
print(list)