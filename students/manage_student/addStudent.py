def addNewStudent(sid,sinfo):
    get_id = input('Enter student Id: ')
    get_name = input("Enter student Name :")
    get_branch = input("Enter branch : ")
    get_year = input("Enter year : ")
    sid.add(get_id)
    sinfo[get_id] = {'name':get_name,'branch':get_branch,'year':get_year}
    # print(student_info[get_id])
    return [sid,sinfo]