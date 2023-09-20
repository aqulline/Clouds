import os
import string
import shutil

for root, dirs, files, rootfd in os.fwalk('/media/alpha/E08C-B7DC/audio'):
    print(root, "consumes", end="")
    print(sum(os.stat(name, dir_fd=rootfd).st_size for name in files),
          end="")
    print("bytes in", len(files), "non-directory files")
    # os.makedirs("a")

let = string.ascii_lowercase

# shutil.copy('/media/alpha/E08C-B7DC/audio/jason_derulo_swalla_lyrics_feat._nicki_minaj_amp_ty_dolla_ign_mp3_78581.mp3', "a")

def move(le, files):
    os.makedirs(f'/media/alpha/E08C-B7DC/audio/{le}')
    for file in files:
        shutil.copy(f'/media/alpha/E08C-B7DC/audio/{file}', f'/media/alpha/E08C-B7DC/audio/{le}')

for i in range(26):
    we = [x for x in files if x[0] == let[i]]
    print(we)
    move(let[i], we)
    we.clear()



