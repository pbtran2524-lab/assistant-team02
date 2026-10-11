def can_register_thesis (credits, gpa) :
    return credits >= 120 and gpa >= 2.0


def missing(credits, gpa) :

    list=[];


    if credits < 120 and gpa < 2.0:
        list.append( "Bạn cần hoàn thành thêm {} tín chỉ và nâng GPA lên ít nhất 2.0 để đủ điều kiện đăng ký luận văn.".format(120 - credits))
    elif credits < 120:
        list.append( "Bạn cần hoàn thành thêm {} tín chỉ để đủ điều kiện đăng ký luận văn.".format(120 - credits))
    elif gpa < 2.0:
        list.append( "Bạn cần nâng GPA lên ít nhất 2.0 để đủ điều kiện đăng ký luận văn.")

    return list

test_credits = 115
test_gpa = 1.9
    
print("Có đủ điều kiện đăng ký khóa luận không?:", can_register_thesis(test_credits, test_gpa))
print("Các lý do chưa đạt:", missing(test_credits, test_gpa))