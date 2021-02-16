import pandas as pd
from PIL import Image, ImageDraw

df = pd.read_excel(r'C:\Python27\Copy of cards.xlsx', sheet_name = 'Sheet1', header=None)
max_r = len(df)
max_col = len(df.columns)
m = n = p = 0

option_A_col1 = option_A_col2 = option_A_col3 = option_B_col1 = option_B_col2 = option_B_col3 =option_C_col1 =option_C_col2 = option_C_col3[]
A_col2 =[]
A_col3 =[]
B_col1 = []
B_col2 =[]
B_col3 =[]
C_col1 = []
C_col2 =[]
C_col3 =[]
count_a=0
count_b=0
count_c=0
text=''
for k in range(0, max_r-3):
 for i in range(0, max_col):
     if df.iat[k,i] == "A":
        count_a=count_a+1
     elif df.iat[k,i] == "B":
         count_b=count_b+1
     elif df.iat[k,i] == "C":
         count_c=count_c+1
x=0
y=count_a
for k in range(0, max_r-3):
 for i in range(0, max_col):
     if df.iat[1,i] == "A":
         A_col1.append("A")
         A_col2.append(df.iat[0, i])
         A_col3.append(df.iat[k+3,i])
         m = m + 1
     elif df.iat[1,i] == "B":
         B_col1.append("B")
         B_col2.append(df.iat[0, i])
         B_col3.append(df.iat[k+3,i])
         n = n + 1
     elif df.iat[1,i] == "C":
         C_col1.append("C")
         C_col2.append(df.iat[0, i])
         C_col3.append(df.iat[k+3,i])
         p = p + 1


for j in range(3, max_r):
 img = Image.new('RGBA', (500, 600), color=(0,0,0,0))
 for k in range(x, y):
  text = text + ((A_col2[k] + " | " + str(A_col3[k])) +"\n")

  d = ImageDraw.Draw(img)
  d.multiline_text((10,10), text, fill='black', font=None, anchor=None, spacing=0, align='left')


 img.save('c:\Python27\images\option_A_'+str(j-3)+'.png')
 text=''
 x=x+count_a
 y=y+count_a
x=0
y=count_b
text=''
for j in range(3, max_r):
 img = Image.new('RGBA', (500, 600), color=(0,0,0,0))
 for k in range(x, y):
  text = text + ((B_col2[k] + " | " + str(B_col3[k])) +"\n")

  d = ImageDraw.Draw(img)
  d.multiline_text((10,10), text, fill='black', font=None, anchor=None, spacing=0, align='left')


 img.save('c:\Python27\images\option_B_'+str(j-3)+'.png')
 text=''
 x=x+count_b
 y=y+count_b
x=0
y=count_c
text=''
for j in range(3, max_r):
 img = Image.new('RGBA', (500, 600), color=(0,0,0,0))
 for k in range(x, y):
  text = text + ((C_col2[k] + " | " + str(C_col3[k])) +"\n")

  d = ImageDraw.Draw(img)
  d.multiline_text((10,10), text, fill='black', font=None, anchor=None, spacing=0, align='left')


 img.save('c:\Python27\images\option_C_'+str(j-3)+'.png')
 text=''
 x=x+count_c
 y=y+count_c