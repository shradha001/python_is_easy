"""
Homework Assignment  # 2: Functions

"""

# defining the song name
song_name = "What Hurts the Most"

# returns the Artist name
def artist():
    artist = "Rascal Flatts"
    return artist

# returns the released year
def year():
    released_year = 2006
    return released_year

# returns the genre
def genre():
    genre = "country"
    return genre


# checks if the song name is listed or not
def is_song_listed(name):
    if name == song_name:
        return True
    else:
        return False

if(is_song_listed("What Hurts the Most")):
    artist = artist()
    year = year()
    genre = genre()
    print("Artist: ",artist)
    print("Year: ",year)
    print("Genre: ",genre)
else:
    print('Song not found in our records.')
