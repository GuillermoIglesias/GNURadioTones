import math, wave, array, sys

print ("\n 1 2 3 A \n" 
" 4 5 6 B \n" 
" 7 8 9 C \n"
" * 0 # D \n")

toneInput = raw_input("Select tone: ")

tones = [['1','2','3','A'],['4','5','6','B'],['7','8','9','C'],['*','0','#','D']]
tones2 = ['1','2','3','A','4','5','6','B','7','8','9','C','*','0','#','D']

#if not toneInput in tones:
#	print "\nERROR: Input is not valid\n"
#	sys.exit()
print tones
print tones2
print tones2.index(toneInput)
	
lower = [697, 770, 852, 941]
upper = [1209, 1336, 1477, 1633]


duration = 1 # seconds
freq = 1209 # of cycles per second (Hz) (frequency of the sine waves)
volume = 100 # percent
data = array.array('h') # signed short integer (-32768 to 32767) data
sampleRate = 44100 # of samples per second (standard)
numChan = 1 # of channels (1: mono, 2: stereo)
dataSize = 2 # 2 bytes because of using signed short integers => bit depth = 16
numSamplesPerCyc = int(sampleRate / freq)
numSamples = sampleRate * duration

for i in range(numSamples):
    sample = 32767 * float(volume) / 100
    sample *= math.cos(math.pi * 2 * (i % numSamplesPerCyc) / numSamplesPerCyc)
    data.append(int(sample))

f = wave.open('SineWave_' + str(freq) + 'Hz.wav', 'w')
f.setparams((numChan, dataSize, sampleRate, numSamples, "NONE", "Uncompressed"))
f.writeframes(data.tostring())
f.close()