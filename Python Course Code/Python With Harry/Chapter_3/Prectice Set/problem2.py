Name = "Ali Rai"
Date= "08/05/2024"

letter = ''' 
Dear  <|Name|>,
Your Selected!
<|Date|>
 '''

print(letter.replace("<|Name|>" , Name).replace("<|Date|>" , Date))