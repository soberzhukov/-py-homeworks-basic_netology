class Album:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.track_list = list()

    def add_track(self, track):
        self.track_list.append(track)
        print(self.track_list)

    def get_duration(self):
        count = 0
        for track in self.track_list:
            count += track.duration
        print(count)

    def __str__(self):
        map_list = list(map(str, self.track_list))
        aaa = '\n\t'.join(map_list)
        result = f'Name group: {self.group}\n' \
                 f'Name album: {self.name}\n' \
                 f'Tracks:\n' \
                 f"\t{aaa}"
        return result


class Track:
    def __init__(self, name, duration: int):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f'{self.name}-{self.duration}min'

    def __lt__(self, other):
        if not isinstance(other, Track):
            return
        return self.duration < other.duration


oxygen_track = Track('oxygen', 182)
rate_track = Track('rate', 199)
molly_track = Track('molly', 205)
pick_track = Track('pick', 105)

my_love_album = Album('my_love', 'little_big')
my_love_album.track_list = [oxygen_track, rate_track]
girls_album = Album('girls', 'oxymiron')
girls_album.track_list = [molly_track]




