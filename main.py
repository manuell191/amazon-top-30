import io
import re


#Upload the txt file.
name = "7-5-22-amazon.txt"
file = open(name, "r", encoding='utf-8')
reference = file.readlines()
rxns = {}
week1 = {
    
}
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

      if z[0] in week1:
        pass
      else:
        week1[z[0]] = {
            "Name": z[0],
            "Placement": a[ia],
            "Price": b[ia],
        }