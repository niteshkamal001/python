import json 

while True:
    emp_dic = [
        {
            "firstname": input("Enter the first name:"),
            "lastname": input("Enter the first name:"),
            "empid":"2022-001",
            "age":int (input("Enter age: ")),
            "city":input("Enter city:"),
            "experience":int (input("Enter experience:")),
            "contactno":int(input("Enter contact no:"))
        }
 ]
    dic=json.dumps(emp_dic,intend=4)
    
    choice = input(" Another employee details Press 'y' if yes :")
    if choice != "y":
        break
    print(dic)