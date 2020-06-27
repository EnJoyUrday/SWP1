html = b"""
<html>
   <body>
      <form action=""> 
          input two numbers : (<input type="number" name="a">, 
             <input type="number" name="b">)<br><br>
          <input type="submit">
      </form>
      x + y = %(sum)s<br>
      x * y = %(mul)s<br> 
   </body>
</html>
""" 
