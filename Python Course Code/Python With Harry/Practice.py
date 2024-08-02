# Problem1
# print("""Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the traveler in the dark
# Thanks you for your tiny spark,
# How could he see where to go,
# If you did not twinkle so?

# In the dark blue sky you keep,
# Often through my curtains peep
# For you never shut your eye,
# Till the sun is in the sky.

# As your bright and tiny spark
# Lights the traveler in the dark,
# Though I know not what you are,
# Twinkle, twinkle, little star.""")

#Problem2
# import pyttsx3
# engine = pyttsx3.init()
# engine.say("how Are You and What are You Doing")
# engine.runAndWait()


#Problem3 

import os

# Specify the directory path
dir_path = '/'

# List all files in the directory and subdirectories
for root, dirs, files in os.walk(dir_path):
    for file in files:
        print(os.path.join(root, file))

