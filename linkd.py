venue = 'J7vn25t13'

vn = ""


def get_venue(venue):
    vn = ""
    for i in venue:
        if i == "v":
            vn = i + venue[venue.index(i) + 1] + venue[venue.index(i) + 2] + venue[venue.index(i) + 3]
    return vn
