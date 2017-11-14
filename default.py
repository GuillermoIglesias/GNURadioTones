# generate wav file containing sine waves
# FB36 - 20120617
import math, wave, array
duration = 1 # seconds
#freq = 440 # of cycles per second (Hz) (frequency of the sine waves)
freq = 1209 # of cycles per second (Hz) (frequency of the sine waves)
volume = 100 # percent
data = array.array('h') # signed short integer (-32768 to 32767) data
sampleRate = 44100 # of samples per second (standard)
numChan = 1 # of channels (1: mono, 2: stereo)
dataSize = 2 # 2 bytes because of using signed short integers => bit depth = 16
numSamplesPerCyc = int(sampleRate / freq)
numSamples = sampleRate * duration

'''for i in range(numSamples):
    sample = 32767 * float(volume) / 100
    sample *= math.cos(math.pi * 2 * (i % numSamplesPerCyc) / numSamplesPerCyc)
    data.append(int(sample))

for i in range(23):
    sample = 32767 * float(volume) / 100
    sample = 0
    data.append(int(sample))'''

#freq = 697
for i in range(numSamples):
    sample = 32767 * float(volume) / 100
    sample *= math.cos(math.pi * 2 * (i % numSamplesPerCyc) / numSamplesPerCyc)
    data.append(int(sample))

f = wave.open('SineWave_' + str(freq) + 'Hz.wav', 'w')
f.setparams((numChan, dataSize, sampleRate, numSamples, "NONE", "Uncompressed"))
f.writeframes(data.tostring())
f.close()
