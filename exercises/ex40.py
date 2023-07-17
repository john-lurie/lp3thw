class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
        self.number_lines = len(lyrics)

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
    
    def yell_me_a_song(self):
        for line in self.lyrics:
            print(f"{line.upper()}!")

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# Study Drills 1 & 2: Write more song lyrics.
star_spangled = ["O! say can you see", 
                 "By the dawn's early light",
                 "What so proudly we hailed",
                 "At the twilight's last gleaming"]

national_anthem = Song(star_spangled)
print()
national_anthem.sing_me_a_song()

# Study Drill 3: Make the Song class do more things.
print(f"\nHappy Birthday has {happy_bday.number_lines} lines")
print(f"National Anthem has {national_anthem.number_lines} lines\n")

happy_bday.yell_me_a_song()
