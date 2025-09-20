class pattern:
  def __init__(self,num,arr) -> None:
    self.num = num
    self.arr = arr

  '''
          *   *   *  
          *   *   *
          *   *   *
          *   *   *
          *   *   *
  '''
  
  def skip_star(self):
    for rows in range(1, self.num+1):
      for colomn in range(1,self.num+1):

        ''' using urary operator(used only when you printing/ getting single value)
        print(" ",end="") if(colomn %2 == 0) else print("*",end=" ") '''

        if(colomn %2 == 0):
          print(" ",end=" ")
        else:
          print("*",end=" ")
      print(" ")


  # Top right triangle

  '''   * * * * * 
          * * * *
            * * *
              * *
                *     
  '''
  
  def top_right_triangle(self):
    count = 0
    for rows in range(1, self.num+1):
      for coloumn in range(1,self.num+1):
        if(coloumn > count):
          print("*",end=" ")
        else:
          print(" ",end=" ")
      count += 1
      print("")

  # reverse left angle triangle

  '''   * * * * *  
        * * * *  
        * * *  
        * *  
        *
  '''
  def reverse_left_triangle(self):
    count = self.num
    for rows in range(1, self.num+1):
      for coloumn in range(1,count+1):
        print("*",end=" ")
      count -= 1
      print(" ")

# left angle triangle
  '''
        * 
        * *
        * * *
        * * * *
        * * * * *
  '''
  def left_triangle(self):
    for i in range(1, self.num + 1):
      for j in range(1,i+1):
        print("*",end=" ")
      print("")

# Right angle Triangle
  '''
              *  
            * *
          * * *
        * * * *
      * * * * *
  '''

  def right_triangle(self):
    count = self.num
    for i in range(1,self.num + 1):
      for j in range(1,self.num+1):
        if(j >= count):
         print("*",end=" ")
        else:
          print(" ",end=" ")
  
      print(" ",end="")
      count -= 1
      print("")

# printing "*" for given array element

  '''
      * * 
      * * * * * 
      * * * * 
      * * * * * 
      * *
      * * * * * *
      * * * * * * * *
  '''

  def arr_pattern(self):
    for arr_items in self.arr:
      print("* " * arr_items)


  # Border Star Pattern
  '''
        * * * * * 
        *       * 
        *       * 
        *       * 
        * * * * *
  '''

  def edge_pattern(self):
    for rows in range(1,self.num+1):
      for coloum in range(1,self.num+1):

        '''we can use below condition in single line or use if and elif 
        # if(rows == 1 or rows == self.num or coloum == 1 or coloum == self.num):'''

        if(rows == 1 or rows == self.num):
          print("*" ,end=" ")
        elif(coloum == 1 or coloum == self.num):
          print("*" ,end=" ")
        else:
          print(" ",end=" ")
      print('')
  

  # pyramid pattern

  '''
              * 
            * * *
          * * * * *
        * * * * * * *
      * * * * * * * * *

  '''
  def praymid_pattern(self):
    count = 1
    for rows in range(1, self.num+1):
      for space in range(self.num - rows):
        print(' ',end=" ")
      
      for stars in range(count):
        print("*",end=" ")

      count += 2
      print("")

        


my_patterns = pattern( 5,[2,5,4,5,2,6,8])
# my_patterns.right_triangle()
# my_patterns.arr_pattern()
# my_patterns.left_triangle()
# my_patterns.reverse_left_triangle()
# my_patterns.top_right_trianle()
# my_patterns.skip_star()
# my_patterns.edge_pattern()
# my_patterns.praymid_pattern()
