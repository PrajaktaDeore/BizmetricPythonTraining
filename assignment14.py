ask=input("Do you want Books(1) or NoteBook(2)")
if ask=='1':
  standard=int(input("Enter Standard: "))
  subject=input("Enter Subject: ")
  if standard >=1 and standard <=4:
    new_standard='1st-4th'
  elif standard >= 5 and standard <=8:
    new_standard='5th-8th'
  else:
    new_standard='9th-10th'

  my_dict={
    
    '1st-4th':
    {
    'Books':
    {
        'Hindi': 60,
        'Marathi':60,
        'English': 80,
        'Science':90,
        'Maths':100
    },
        
    },
    '5th-8th':
    {
    'Books':
    {
        'Hindi': 100,
        'Marathi':100,
        'English': 100,
        'Science':120,
        'Maths':140
    },
    '9th-10th':
    {
    'Books':
    {
        'Hindi': 150,
        'Marathi':150,
        'English': 150,
        'Science':200,
        'Maths':250
    },
    
         
    }
   }
  }
  price=my_dict[new_standard]['Books'][subject]
  print(price) 
else:
  pagess=int(input("Enter Pages: "))
  book_types=input("Enter Book Types: ")
  
  if pagess==100:
    new_pages='Pages100'
  else:
    new_pages='Pages200'
  
  
  my_dict_2={
            'Pages100':
            {
               'sqaure':40,
               '4lines':30,
               '2lines':20,
               'single lines':60,
               'A4 Notebook':100
            },
            'Pages200':
            {
                'sqaure':70,
                '4lines':50,
                '2lines':50,
                'single lines':100,
                'A4 Notebook':180,
            }

        }  

  price_book=my_dict_2[new_pages][book_types]
  print(price_book)





    