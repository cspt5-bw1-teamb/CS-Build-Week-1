from adventure.models import Player, Room

room_list = []

for room in Room.objects.all():
    room_list.append({"id":room.id, "title":room.title, "description": room.description, "n_to":room.n_to, "s_to":room.s_to, "e_to":room.e_to, "w_to":room.w_to})


print(room_list)

