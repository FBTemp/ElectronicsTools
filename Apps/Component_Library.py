import os

titles = []
names = []
uses = []
urlNames = []
urls = []
descriptions = []

compRaw = []

with open("AppFiles/components.txt", "r") as components:
    length = len(components.readlines())
amount = length // 6

components = open("AppFiles/components.txt", "r")

for line in range(int(length)):
    compRaw.append(components.readline())

count = 0
for i in range(int(amount)):
    titles.append(compRaw[count])
    count += 1
    names.append(compRaw[count])
    count += 1
    uses.append(compRaw[count])
    count += 1
    urlNames.append(compRaw[count])
    count += 1
    urls.append(compRaw[count])
    count += 1
    descriptions.append(compRaw[count])
    count += 1

titles = [title.replace("\n", "") for title in titles]
names = [name.replace("\n", "") for name in names]
uses = [use.replace("\n", "") for use in uses]
urlNames = [urlName.replace("\n", "") for urlName in urlNames]
urls = [url.replace("\n", "") for url in urls]
descriptions = [description.replace("\n", "") for description in descriptions]

components.close()

def search(list, text):
    results = []
    for item in list:
        part = list[item]
        if text in part:
            results.append(item)
    return results

exit = True
while not exit:
    print("Choose where to search:")
    print("1 = Titles")
    print("2 = Names")
    print("3 = Uses")
    print("5 = Descriptions")
    print("6 = All")
    print("X = Exit")
    choice = input("Your choice: ")
    if choice == "1":
        result = search(titles, input("Enter search term: "))
