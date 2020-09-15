#Yudha Prasetyo_Tugas_Pertemuan13

def listdata():
   nama1 = input("Input Nama ke-1: ")
   nilai1  = input("Input Nilai ke-1: ")
   nama2 = input("Input Nama ke-2: ")
   nilai2  = input("Input Nilai ke-2: ")
   nama3 = input("Input Nama ke-3: ")
   nilai3  = input("Input Nilai ke-3: ")
   return nama1, nilai1, nama2, nilai2, nama3, nilai3

def main():

   nama1, nilai1, nama2, nilai2, nama3, nilai3 = listdata()
   print ("====================================")
   print ("No \t Nama \t\t Nilai \t\t")
   print ("====================================")
   print ("1\t", nama1, "\t", nilai1,"\n2\t", nama2, "\t", nilai2,"\n3\t", nama3, "\t", nilai3)
   
main()
