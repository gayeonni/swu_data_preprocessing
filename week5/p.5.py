import dataset

db = dataset.connect('sqlite:///friend.db')
table = db['friend_info']

friend_1 = {'friend_id' : 1, 'friend_name' : 'megan'}
table.insert(friend_1)
friend_2 = {'friend_id' : 2, 'friend_name' : 'tom'}
table.insert(friend_2)

instance = table.find_one(friend_id=2)
print("My friend's name is", instance['friend_name'])



