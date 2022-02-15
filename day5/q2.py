# Write a program to fill in a letter template given below with name and date​

# Letter = '''Dear <|Name|>,​
#                          You are selected!​
#                                        <|Date|>'''
#  today()
from datetime import date
name = input("Enter the name: ")

template = '''Dear <|Name|>,​
You are selected!​
<|Date|>'''

print(template.replace('<|Name|>', name).replace('<|Date|>', str(date.today())))

#
# 'Dear Johnathan,​
# You are selected!​
# <|Date|>'

#
# 'Dear Johnathan,​
# You are selected!​
# 31/01/2022'

