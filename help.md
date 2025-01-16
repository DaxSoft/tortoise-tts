yep

conda update tokenizers

then

conda install transformers==4.31.0

allowed me to install all dependencies for tortoise-tts==3.0.0

===

so the issue now is that tokenizers is at 0.20 and this is depending on tokenizers 0.13, which was never supporting more modern versions of rust nor python 3.12

I think we can update the setup.py to 'tokenizers>=0.20.0', 'transformers==4.45.1', currently ?

edit:

seems so, build finished, with just also 'numpy>=1.22,<2.1,!=1.22.2,!=1.22.1,!=1.22.0', to satisfy both librosa and numba

edit2: I am generating audio :)
