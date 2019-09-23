# List basics :D

#1 - Define a bucket list with 10 items
bucket_list = [ 'Abseil Down a Waterfall', 'Air Boat Across an Alligator Infested Swamp', 'Arrive By Seaplane', 'Catch a Wave Surfing', 'Dog Sled', 'Ride a Zip Line', 'Eat Fire', 'Explore a Cave', 'Flip on a Trampoline', 'Flyboarding']

#2 - Print the entire list

print(bucket_list)

#3 - Check the length of the list / how many items inside the list?

print(bucket_list.__len__())

#4 - print the first item

print(bucket_list[0])

#5 - Print the second item

print(bucket_list[1])

#6 - add one more item to the list

bucket_list.append('Indoor Skydive')

#7 - print the last item in the list

print(bucket_list[-1])

#8 - Re assign an item and print all of the list again

bucket_list[3] = "Arrive by Seaplane and don't fall into the sea"
print(bucket_list)