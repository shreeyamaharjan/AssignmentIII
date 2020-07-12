import csv

with open('details.csv','w',newline='') as file:
    writer =csv.writer(file)
    writer.writerow(['Name','Email','Address'])
    writer.writerow(['Ram', 'ram@gmail.com', 'Lalitpur'])
    writer.writerow(['Sita', 'sita004@gmail.com', 'Dang'])
    writer.writerow(['Geeta', 'geeta123@yahoo.com', 'Bhaktapur'])
    writer.writerow(['Rameshwor', 'ramesh_wor55@gmail.com', 'Kavre'])
    writer.writerow(['Sarita', 'sarita_s5@gmail.com', 'Lalitpur'])
    writer.writerow(['Purnima', 'puru55@gmail.com', 'Kathmandu'])