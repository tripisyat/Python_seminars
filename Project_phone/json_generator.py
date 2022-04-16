import receive_data as ui
import json
def write():
    inserted = ui.add_new()
    data = {
        inserted[0]: {
            "Name": inserted[1],
            "Surname": inserted[2],
            "Phone Number": inserted[3]
        }
    }
    with open("data_base.json", "a") as write_file:
        json.dump(data, write_file)
        json.dumps('\\n')
                
    return data