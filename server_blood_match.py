import requests
import json


r= requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/kjt31")


dict_message=json.loads(r.text)
recipient=dict_message["Recipient"]
Donor=dict_message["Donor"]

r_patient= requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/{}".format(recipient))
r_donor=requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/{}".format(Donor))

if r_patient.text==r_donor.text:
    answer="yes"
else:
    answer="no"
    
    
out_data={"Name": "kjt1", "Match": answer}
r_post = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json=out_data) 



print(r_post.status_code)# blood match server code


