
startrange = int(input("Enter the starting number: "))
endrange = int(input("Enter the ending number: "))
        
squares = [i ** 2 for i in range(startrange, endrange + 1)]
        

even = [sq for sq in squares if sq % 2 == 0]
odd = [sq for sq in squares if sq % 2 != 0]
     
print(f"\nEven Squares: {even}")
print(f"Odd Squares: {odd}")
        
    


