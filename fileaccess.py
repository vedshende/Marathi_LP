import glob

folder = 'C:/Users/lenovo/Documents/LearnPython/Sounds2/'

def fetch_location():
    location = glob.glob(folder+"*.wav")
    return location

'''
def file_rename():
    for fname in os.listdir(folder):
        input_file = os.path.join(folder, fname)
        if not os.path.isfile(input_file):
            continue
        #old_file = os.path.splittext(fname)
        new_name = input_file.replace('.amr', '.wav')
        os.rename(input_file, new_name)
		'''