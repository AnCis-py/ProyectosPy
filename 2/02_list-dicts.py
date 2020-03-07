# Create a list of the BRICS countries
country = [ 
            "Brazil", 
            "Russia", 
            "India", 
            "China", 
            "South Africa"
          ]

"""Create a dictionary of BRICS capitals.
Note that South Africa has 3 capitals. Therefore, we embed a list inside
the dictionary.
"""

capitals = {
    "Brazil": "Brasilia",
    "Russia": "Moscow",
    "India": "New Delhi",
    "China": "Beijing",
    "South Africa": [
                        "Pretoria",
                        "Cape Town",
                        "Bloemfontein"  
                    ]
           }

# Print the list and dictionary
print( country )
print( capitals )
"""
What response did you get?
Why did the list and dictionary contents not print?
Fix the code and run the script again.
"""

print( capitals["South Africa"][1] )
"""
Why did you get an error for the 2nd capital of South Africa?
Hint: Check the syntax for the index value.
"""


Datos = input("Ingrese nombre, apellido,ubicación y teléfono: ")
div=Datos.split("Anabel","Inga","Guamani","34")
r0=div[0]
r1=div[1]
r2=div[2]
r3=div[3]
space=" "
print(r0+space+r1+space+r2+space+r3)