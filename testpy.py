from csv import DictWriter
  
name_input = input("what is your name?: " )
age_input = input("how old are u? : ")
add_input = input("wher do you live?: ")
field_names = ['ID','NAME','AGE',
               'ADDRESS']

# Dictionary
dict={'ID':3,'NAME': name_input,'AGE':age_input,
      'ADDRESS': add_input}
  
# Open your CSV file in append mode
# Create a file object for this file
with open('testdata.csv', 'a') as f_object:
      
    # Pass the file object and a list 
    # of column names to DictWriter()
    # You will get a object of DictWriter
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
  
    #Pass the dictionary as an argument to the Writerow()
    dictwriter_object.writerow(dict)
  
    #Close the file object
    f_object.close()
