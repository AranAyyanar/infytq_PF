def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    countP=0
    countE=0
    countO=0
    for speci in patient_medical_speciality_list:
        if speci=="P":
            countP=countP+1
        elif speci=="O":
            countO=countO+1
        elif speci=="E":
            countE=countE+1
    if countP>countE and countP>countO:
        speciality=medical_speciality["P"]
    elif countE>countO:
        speciality=medical_speciality["E"]
    else:
        speciality=medical_speciality["O"]
    return speciality
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
