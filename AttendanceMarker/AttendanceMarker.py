import csv
def ReadCSV():
    path= input("Enter the complete path of the attendance file:")
    lines_seen=set();
    with open(path,'r+',newline='') as file_obj:
        p=[]
        csv_reader= csv.reader(file_obj)
        for i in file_obj:
            i=i.replace('"',",")
            i=i.replace("\r\n"," ")
            i=i.split(",") 
            p.append(i)
        print(p[8][9])
        spamwriter = csv.writer(file_obj, delimiter=' ',quotechar=' ')
        count=int(p[1][1])
        for i in range(8, (8+count)):
            if p[i][0] not in lines_seen:
                spamwriter.writerow(p[i][0]+","+p[i][10]+",present")
                lines_seen.add(p[i][0])
         
 
           
         
            
ReadCSV()


