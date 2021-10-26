import qrcode

name = input("Enter name ")
enroll = input("Enrollment ")
age = input("Age ")
mn = input("MothersName ")
fn = input("FathersName ")
branch = input("Branch ")
dob = input("DOB ")
address = input("Address ")
course = input("Course ")
mobileno = input("Mobile Number ")
email = input("Email ")
college = input("College ")

st = "Name:{}\n Enrollment:{}\n Age:{}\n MothersName:{}\n FathersName:{}\n Branch:{}\n DOB:{}\n Address:{}\n Course:{}\n MobileNo.:{}\n Email:{}\n College:{}\n"
st.format(name,enroll,age,mn,fn,branch,dob,address,course,mobileno,email,college)


img = qrcode.make(enroll)
img.save(f"C:/Users/SAKSHAM ASATI/Desktop/Sakshi/Python/Coding/qr code/New folder/{enroll}.jpg")



