import librosa
import matplotlib.pyplot as plt
from IPython.display import HTML  

filename = librosa.example('trumpet')
filename

HTML(librosa.util.example_info("trumpet", html=True))

y, sr = librosa.load(filename)

plt.figure(figsize= (10,7))
plt.plot(y)
plt.show()

