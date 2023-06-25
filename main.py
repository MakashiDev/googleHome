from googlehomepush import GoogleHome
from gtts import gTTS

import time
import pychromecast

host = ["192.168.0.34", 8009,
        "3853ec2a-3087-e15e-2fd5-10e12f19fd7b",  "Google Home Mini", "Boys Bedroom Speaker"]

cast = pychromecast._get_chromecast_from_host(host)

mc = cast.media_controller
# play the mp3 file oooh.mp3 on the chromecast
mc.play_media(
    "https://soundboardguy.com/wp-content/uploads/2022/04/Whats_up_guys_its_Quandale_dingle_getmp3.pro_.mp3", "audio/mp3")
mc.block_until_active()
time.sleep(3.3)
mc.pause()

# wait for the mp3 to start playing
