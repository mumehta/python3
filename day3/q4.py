# Import external module for text to speech and use it to greet yourself.

# pip install pyttsx3

import pyttsx3

engine = pyttsx3.init()
# I would like to hear twinkle twinkle poem
poem = '''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav’ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav’ller in the dark,
Tho' I know not what you are,
Twinkle, twinkle, little star.
'''
engine.say(poem)
engine.runAndWait()