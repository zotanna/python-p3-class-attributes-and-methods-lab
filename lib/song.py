class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genre(self.genre)
        self.add_to_artist(self.artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genre(cls, genre):
            if genre not in cls.genres:
                cls.genres.append(genre)

    @classmethod
    def add_to_artist(cls, artist):
         if artist not in cls.artists:
              cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre):
              cls.genre_count[genre] += 1
        else:
             cls.genre_count[genre] = 1
         
    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
             cls.artist_count[artist] = 1

    pass