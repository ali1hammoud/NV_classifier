#Import the modules and functions
from tkinter import *
from bring_data_from_url import bring_data
from classifier_MultinomialNB_func import classifier_MultinomialNB
from classifier_MultinomialNB_func_iteration import classifier_MultinomialNB_Avg

#create a new window and assign it to the variable 'root'
root= Tk()
#set the title of the window
root.title("classifier")
#set the icon of the window
root.iconbitmap("Img/kubsu.ico")
#set the dimensions of the window
root.geometry("530x350")
#fixed size of window
root.resizable(0, 0)
#Create a Label widget with a text and assign it to a variable; A widget used to display text on the screen
Label_Text = Label(root, text='This code will bring the data for 40 url from wikipedia.org .\nThey belong to two categories ART and SCIENCE.')
Label_Text.grid( row=0, column=0, padx=5, pady=5)

#The fuction to read the data from a file
def bring():
    bring_data()

#Create a button widget; A button that can contain text and can perform an action 'command to run a function' when clicked
Button_bring = Button(root, text="Bring the data and save them as DATA.csv", command=bring)

#using .grid() geometry manager to put the postion of any widget
#padx adds padding in the horizontal direction.
#pady adds padding in the vertical direction.
Button_bring.grid(row=1, column=0, padx=5, pady=5)

#The function to start the multinomial naive bayes classifier
def classify():
    classifier_MultinomialNB()

Label_classify = Label(root, text='Using Multinomial Naive Bayes The code will choose 20%of dataset for testing and 80% to train it.\nThe result will be in confusion matrix.')
Label_classify.grid( row=2, column=0, padx=5, pady=5)

Button_classify = Button(root, text="Start the classification", command=classify)
Button_classify.grid(row=3, column=0, padx=5, pady=5)

#The function to calculate the mean for number of iteration of running the classifier
def get_avg():
#using .get() to retrieve the text and assign it to a variable 
    num = int(iteration.get())
    if num <= 50 and num > 0:
        avg = "{:.2f}".format(classifier_MultinomialNB_Avg(num) * 100)
        Label_iteration = Label(root, text='The avarge is : '+str(avg))
        Label_iteration.grid( row=7, column=0, padx=5, pady=5)
        
Label_iteration = Label(root, text='The code here will repeat the classification operation by the number which you write.\nThe average of accuracy of classifier will appear in the bottom.\nHow many times you want to classify? [1:50]')
Label_iteration.grid( row=4, column=0, padx=5, pady=5)

#A text entry widget that allows the user to write a text
iteration = Entry(root, width=35, borderwidth=5)
iteration.grid(row=5, column=0, padx=5, pady=5)

Button_iteration = Button(root, text="Get the average", command=get_avg)
Button_iteration.grid(row=6, column=0, padx=5, pady=5)

#window.mainloop() tells Python to run the Tkinter event loop. 
#This method listens for events, such as button clicks or keypresses
#and blocks any code that comes after it from running until the window it’s called on is closed. 
root.mainloop()
