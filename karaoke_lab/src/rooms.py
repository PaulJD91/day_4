class Room:

    def __init__(self, room_number, max_occupancy):
        self.room_number = room_number
        self.max_occupancy = max_occupancy
        self.guests = []
        self.songs = []

    def check_in_guests(self, guests):
        for guest in guests:
            self.guests.append(guest)

    def check_out_guests(self, guests):
        for guest in guests:
            self.guests.remove(guest)

    def add_song(self, song):
        return self.songs.append(song)
    
    
        



