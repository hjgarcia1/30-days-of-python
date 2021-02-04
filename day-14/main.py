with open("./iris.csv", "r") as iris_file:
	iris_data = iris_file.readlines()

headers = iris_data[0].strip().split(",")

irises = []

for row in iris_data[1:]:
	iris = row.strip().split(",")
	iris_dict = dict(zip(headers, iris))

	irises.append(iris_dict)

print(irises)
