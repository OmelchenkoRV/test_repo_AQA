def generate_song(strings=3, units=3, exclamation=0):
    return " ".join(['-'.join(['la'] * strings)] * units) + '.!'[exclamation]


print(generate_song(5, 5, 0))
