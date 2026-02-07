real = float(input("Enter the real part of the number: "))
imaginary = float(input("Enter the imaginary part of the  number: "))
str_complex = f"{real} + {imaginary}j"
print(f"The complex number you entered is: {str_complex}")
complex_number = complex(real, imaginary)
print(f"The complex number you entered is: {complex_number}")