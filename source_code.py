import pyttsx3
import PyPDF2

'''firstly, we have to download the pdf in this "Audio_Book" folder.
   then we'll call the name of the document in the open function.
   we can make it read a specific page by entering the page number'''

# input part

# here 'pdf name' should be replaced with the saved document
book = open('Audio_Book_Sample.pdf', 'rb')

# the variable should be called in the PdfReader parameter
reader = PyPDF2.PdfReader(book)    # this is our reader variable

# gets the total pages of the saved document
pages = len(reader.pages)


# processing part

# initiating text to speech
speaker = pyttsx3.init()

''' the specific page number has to be called in the getPage function.
    the index starts from 0.
    as per the index rule, we have to enter 1 less from the specific page number.'''

# using for loop to read multiple pages
for page_num in range(pages):
    specific_page = reader.pages[page_num]

    # extracts the contents of the page
    speech = specific_page.extract_text()

    # output part

    # speech variable can also be replaced by some text
    speaker.say(speech)   # makes the speaker talk

    speaker.runAndWait()
