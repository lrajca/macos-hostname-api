
import xlrd
global serialNumber

def Find(serialNumber, wb):

	max_range = len(wb.sheets())
	Found = False
	
	for i in range(0,max_range):
		if Found is True:
			break

		else:
			iterate = 0
			sheet = wb.sheet_by_index(i)
			
			for row in sheet.col(1):
				
				if row.value == serialNumber:
					Found = True
					break
		
				iterate +=1

	if Found is False:
		return "CNF - " +serialNumber

	rowNumber, sheetName = iterate, sheet.name
	column = 1

	sh = wb.sheet_by_name(sheetName)
	
	#If Student Machine
	if (sh.name).isdigit():
		column +=1
		name = sh.cell_value(rowx=rowNumber, colx=column)
		firstLetter = name[0]
		surname = name.split(" ")
		surname = ("").join(surname[1:])
		column +=1
		graduatingYear = int(sh.cell_value(rowx=rowNumber, colx=column))
		finalName = firstLetter
		return (str(graduatingYear) + str(firstLetter) + str(surname)).lower()

	elif str(sh.name) == "staff":
		column +=1
		user = name = sh.cell_value(rowx=rowNumber, colx=column)
		firstLetter = user[0]
		user = user.split(" ")
		surname = ("").join(user[1:])
		return (str(sh.name) + str(firstLetter) + str(surname)).lower()	
	
	else:
		column += 1
		celly = str(sh.cell_value(rowx=rowNumber, colx=column))
		if ".0" in celly:
			celly = celly.strip(".0")
		return (str(sh.name) + str(celly))
	   
		
def Main(serialNumber):
	wb = xlrd.open_workbook("data.xlsx")
	Name = Find(serialNumber, wb)
	return Name

if __name__ == "__main__"
        Main(serialNumber)
		

	
	
