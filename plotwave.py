import matplotlib.pyplot as plt
import numpy, wave
from pylab import*
from scipy.io import wavfile
from pydub import AudioSegment

def get_amplitude():
    #Location of WaVE files
    folder = 'C:/Users/lenovo/Documents/LearnPython/output/'
    
    #Reading the WAVE file
    file_data = wave.open(folder+'temp.wav', 'r')
    signal = file_data.readframes(-1)
    
    #Converting the data in 16-bit integer for plotting
    signal = numpy.frombuffer(signal, 'Int16')
    
    #sample_freq = 44110                          #Sample frequency
    
    signal = signal / (2.**15)                   #Converting data into floating point
    #print(max(signal))                           #Debug: Getting Amplitude
    return max(signal)


    #Location of WaVE files
folder = 'C:/Users/lenovo/Documents/LearnPython/Sounds/'
    
    #Reading the WAVE file
file_data = wave.open(folder+'Gul1.wav', 'r')
signal = file_data.readframes(-1)
    
    #Converting the data in 16-bit integer for plotting
signal = numpy.frombuffer(signal, 'Int16')
    
signal = signal / (2.**15)                   #Converting data into floating point
norm_amp = max(signal)
print(norm_amp)
signal = signal / norm_amp
#print(signal.shape[0]/sample_freq)           #Debug: Printing time in seconds  

#demo
max_energy = energy(max(signal))
print("Energy" + max_energy)  
#Amplitude plotting
timeArray = arange(0, signal.shape[0], 1)    #Shape[0] gives total points to be plotted(Y-axis)
timeArray = timeArray / sample_freq          #Getting maximum time on scale in seconds
timeArray = timeArray * 1000                 #Converting time in milisecond
    
    #print(max(timeArray))                        #Debug: Getting max time on axis'''
    
    
plot(timeArray, signal, color='k')           #Plotting Amplitude vs Time graph
ylabel('Amplitude')
xlabel('Time (ms)')

'''#Plotting  the signal
plt.figure(1)
plt.plot(signal)
plt.title('Signal Wave')
plt.show()'''
#print(signal)
#new_signal = signal[:,1]
#print(new_signal)

'''#Getting the length of signal for plotting frequency
signal_length = len(signal)
fourier_points = fft(signal)    #Correct, giving imaginary output, for magnitude and phase

points = int(ceil((signal_length + 1) / 2))  #Calculating Unique Points

fourier_points = fourier_points[0:points]
fourier_points = abs(fourier_points)

#Scaling by number of points
fourier_points = fourier_points / float(signal_length)
fourier_points = fourier_points**2   #Squaring

if signal_length % 2 > 0:  #Number of odd points
	fourier_points[1:len(fourier_points)] = fourier_points[1:len(fourier_points)] * 2

else:  #Number of even points
	fourier_points[1:len(fourier_points)-1] = fourier_points[1:len(fourier_points)-1] * 2'''


'''#Plotting Frequency Graph
freq_array = arange(0, points, 1.0) * (freq/signal_length)
plot(freq_array*1000, 10*log10(fourier_points), color='k')
xlabel('Frequency (kHz)')
ylabel('Power (dB)')

rms_val = sqrt(mean(signal**2))
print(rms_val)
print(sqrt(sum(fourier_points)))
rms_freq = sqrt(mean(freq_array**2))
print(rms_freq)
print(freq_array)'''

#Trimming leading and ending silence
def detect_leading_silence(sound, silence_threshold):
	trim_ms = 0 # ms
	chunk_size = 5 # to avoid infinite loop

	while sound[trim_ms:trim_ms+chunk_size].dBFS > silence_threshold and trim_ms < len(sound):
	        trim_ms += chunk_size

	return trim_ms

sound = AudioSegment.from_file(folder+'Badam1.wav', format="wav")
avg = mean(signal)
print(avg)
start_trim = detect_leading_silence(sound, avg)
end_trim = detect_leading_silence(sound.reverse(), avg)

duration = len(sound)
print(start_trim)
print(end_trim)
print(duration)
'''trimmed_sound = sound[start_trim:duration-end_trim]

trimmed_sound.export("Trim.wav", format="wav")'''
print("Created...")
