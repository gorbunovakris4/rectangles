from Selection import Selection
from Rectangle import Rectangle
from Field import Field

field = Field(10, 10)
field.locate_rectangles([Rectangle(1, 1), Rectangle(4, 4), Rectangle(8, 8)])
print(field)

###
Вывод:
  
2 2 2 2 1 1 1 1 1 _ 
1 2 2 2 1 1 1 1 1 _ 
1 2 2 2 1 1 1 1 1 _ 
1 2 2 2 1 1 1 1 1 _ 
_ 1 1 1 1 1 1 1 1 _ 
_ 1 1 1 1 1 1 1 1 _ 
_ 1 1 1 1 1 1 1 1 _ 
_ 1 1 1 1 1 1 1 1 _ 
_ _ _ _ _ _ _ _ _ _ 
_ _ _ _ _ _ _ _ _ _ 
###
