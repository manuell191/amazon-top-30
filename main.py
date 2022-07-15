import io
import re
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure

fileList = ["7-5-22-amazon.txt", "6-25-22-amazon.txt", "6-15-22-amazon.txt", "6-11-22-amazon.txt", "6-2-22-amazon.txt", "5-24-22-amazon.txt", "5-17-22-amazon.txt", "5-10-22-amazon.txt", "5-5-22-amazon.txt", "4-29-22-amazon.txt"]

big_counter = 1

week1 = {}
week2 = {}
week3 = {}
week4 = {}
week5 = {}
week6 = {}
week7 = {}
week8 = {}
week9 = {}
week10 = {}

for j in fileList:
  name = j
  file = open(name, "r", encoding='utf-8')
  reference = file.readlines()

  for o in range (0, len(reference)):
    x = re.search("CardsClient\-\-\>\<div id", reference[o])
    if x:
      y = re.findall("(?<=\<span\>\<div class\=)(.*?)(?=div\>)", reference[o])
      for ia in range(0, len(y)):
        z = re.findall("(?<=\"\>)(.*?)(?=\<\/)", y[ia])
        for i in range(0, len(z)):
          z[i] = z[i].replace("&#x27;", "'")

        a = re.findall("(?<=\<span class\=\"zg-bdg-text\"\>\#)(.*?)(?=\<\/span\>\<\/div\>\<div class\=\"a-section zg-bdg-tri zg-bdg-clr-tri aok-float-left\"\>)", reference[o])

        b = re.findall("(?<=\<span class\=\"\_cDEzb\_p13n-sc-price\_3mJ9Z\"\>\$)(.*?)(?=\<\/span\>)", reference[o])
        if b == []:
          b = re.findall("(?<=\<span class\=\"p13n-sc-price\"\>\$)(.*?)(?=\<\/span\>)", reference[o])

        if big_counter == 1:
          if z[0] in week1:
            pass
          else:
            week1[z[0]] = {
                "Name": z[0],
                "Placement": a[ia],
                "Price": b[ia],
            }
        elif big_counter == 2:
          if z[0] in week2:
            pass
          else:
            week2[z[0]] = {
                "Name": z[0],
                "Placement": a[ia],
                "Price": b[ia],
            }
        elif big_counter == 3:
          if z[0] in week3:
            pass
          else:
            week3[z[0]] = {
                "Name": z[0],
                "Placement": a[ia],
                "Price": b[ia],
            }
        elif big_counter == 4:
          if z[0] in week4:
            pass
          else:
            week4[z[0]] = {
                "Name": z[0],
                "Placement": a[ia],
                "Price": b[ia],
            }
        elif big_counter == 5:
          if z[0] in week5:
            pass
          else:
            week5[z[0]] = {
                "Name": z[0],
                "Placement": a[ia],
                "Price": b[ia],
            }
        elif big_counter == 6:
          if z[0] in week6:
            pass
          else:
            week6[z[0]] = {
                "Name": z[0],
                "Placement": a[ia],
                "Price": b[ia],
            }
        elif big_counter == 7:
          if z[0] in week7:
            pass
          else:
            week7[z[0]] = {
                "Name": z[0],
                "Placement": a[ia],
                "Price": b[ia],
            }
        elif big_counter == 8:
          if z[0] in week8:
            pass
          else:
            week8[z[0]] = {
                "Name": z[0],
                "Placement": a[ia],
                "Price": b[ia],
            }
        elif big_counter == 9:
          if z[0] in week9:
            pass
          else:
            week9[z[0]] = {
                "Name": z[0],
                "Placement": a[ia],
                "Price": b[ia],
            }
        elif big_counter == 10:
          if z[0] in week10:
            pass
          else:
            week10[z[0]] = {
                "Name": z[0],
                "Placement": a[ia],
                "Price": b[ia],
            }
  big_counter += 1

name_list = []

for i in week1:
  name_list.append(week1[i]['Name'])
for i in week2:
  name_list.append(week2[i]['Name'])
for i in week3:
  name_list.append(week3[i]['Name'])
for i in week4:
  name_list.append(week4[i]['Name'])
for i in week5:
  name_list.append(week5[i]['Name'])
for i in week6:
  name_list.append(week6[i]['Name'])
for i in week7:
  name_list.append(week7[i]['Name'])
for i in week8:
  name_list.append(week8[i]['Name'])
for i in week9:
  name_list.append(week9[i]['Name'])
for i in week10:
  name_list.append(week10[i]['Name'])

def countX(lst, x):
  count = 0
  for ele in lst:
    if (ele == x):
      count = count + 1
  return count

name_list_occured = []

for i in name_list:
  if i not in name_list_occured:
    name_list_occured.append(i)

occurences = {
    
}

for i in name_list_occured:
  count = countX(name_list, i)
  occurences[i] = count

counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
counter6 = 0
counter7 = 0
counter8 = 0
counter9 = 0
counter10 = 0

occurences_dict = {
    
}

for i in occurences:
  if occurences[i] == 1:
    counter1 += 1
  elif occurences[i] == 2:
    counter2 += 1
  elif occurences[i] == 3:
    counter3 += 1
  elif occurences[i] == 4:
    counter4 += 1
  elif occurences[i] == 5:
    counter5 += 1
  elif occurences[i] == 6:
    counter6 += 1
  elif occurences[i] == 7:
    counter7 += 1
  elif occurences[i] == 8:
    counter8 += 1
  elif occurences[i] == 9:
    counter9 += 1
  elif occurences[i] == 10:
    counter10 += 1

occurences_dict["1"] = counter1
occurences_dict["2"] = counter2
occurences_dict["3"] = counter3
occurences_dict["4"] = counter4
occurences_dict["5"] = counter5
occurences_dict["6"] = counter6
occurences_dict["7"] = counter7
occurences_dict["8"] = counter8
occurences_dict["9"] = counter9
occurences_dict["10"] = counter10

new_list = []
old_list = []
for i in occurences_dict:
  old_list.append(i)
  new_list.append(occurences_dict[i])

x = np.array(old_list)
y = np.array(new_list)

plt.bar(x, y)
plt.xlabel("Number of weeks")
plt.ylabel("Number of occurences")
plt.title("Weeks in the top 30")
plt.show()

top_ten_movement = {
    
}

for i in occurences:
  if occurences[i] == 10:
    top_ten_movement[i] = {
        "week1": week1[i]['Placement'],
        "week2": week2[i]['Placement'],
        "week3": week3[i]['Placement'],
        "week4": week4[i]['Placement'],
        "week5": week5[i]['Placement'],
        "week6": week6[i]['Placement'],
        "week7": week7[i]['Placement'],
        "week8": week8[i]['Placement'],
        "week9": week9[i]['Placement'],
        "week10": week10[i]['Placement'],

    }

new_top_ten_movement = {

}

counter = 1

for i in range(10):
  if counter == 1:
    new_top_ten_movement["week 1"] = {
        
    }
    for n in top_ten_movement:
      new_top_ten_movement["week 1"][n] = int(top_ten_movement[n]["week1"])
  elif counter == 2:
    new_top_ten_movement["week 2"] = {
        
    }
    for n in top_ten_movement:
      new_top_ten_movement["week 2"][n] = int(top_ten_movement[n]["week2"])
  elif counter == 3:
    new_top_ten_movement["week 3"] = {
        
    }
    for n in top_ten_movement:
      new_top_ten_movement["week 3"][n] = int(top_ten_movement[n]["week3"])
  elif counter == 4:
    new_top_ten_movement["week 4"] = {
        
    }
    for n in top_ten_movement:
      new_top_ten_movement["week 4"][n] = int(top_ten_movement[n]["week4"])
  elif counter == 5:
    new_top_ten_movement["week 5"] = {
        
    }
    for n in top_ten_movement:
      new_top_ten_movement["week 5"][n] = int(top_ten_movement[n]["week5"])
  elif counter == 6:
    new_top_ten_movement["week 6"] = {
        
    }
    for n in top_ten_movement:
      new_top_ten_movement["week 6"][n] = int(top_ten_movement[n]["week6"])
  elif counter == 7:
    new_top_ten_movement["week 7"] = {
        
    }
    for n in top_ten_movement:
      new_top_ten_movement["week 7"][n] = int(top_ten_movement[n]["week7"])
  elif counter == 8:
    new_top_ten_movement["week 8"] = {
        
    }
    for n in top_ten_movement:
      new_top_ten_movement["week 8"][n] = int(top_ten_movement[n]["week8"])
  elif counter == 9:
    new_top_ten_movement["week 9"] = {
        
    }
    for n in top_ten_movement:
      new_top_ten_movement["week 9"][n] = int(top_ten_movement[n]["week9"])
  elif counter == 10:
    new_top_ten_movement["week 10"] = {
        
    }
    for n in top_ten_movement:
      new_top_ten_movement["week 10"][n] = int(top_ten_movement[n]["week10"])
  counter+=1

top_ten_movement_list = []
title_list = []

for i in new_top_ten_movement:
  top_ten_movement_list.append(i)

counter = 1

figure(figsize=(15, 5))

for p in top_ten_movement:
  title_list.append(p)
  xpointlabels = []
  ypointlabels = []
  for n in new_top_ten_movement:
    ypointlabels.append(int(new_top_ten_movement[n][p]))
    xpointlabels.append(n)

  xpoint = np.array(xpointlabels)
  ypoint = np.array(ypointlabels)
  plt.plot(xpoint, ypoint, marker = 'o')
  plt.xticks(rotation = 45)
  counter += 1

plt.xlabel("Weeks")
plt.ylabel("Placement (1st, 2nd, etc.)")
plt.title("Most occuring books on amazon top 30 through the weeks")
plt.legend(title_list)
plt.show()