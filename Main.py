from cgitb import text
from fileinput import filename
from inspect import EndOfBlock
from logging import root
from msilib.schema import Font
from posixpath import split
from random import randint, random
import tempfile
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import color, st
from PIL import Image,ImageTk
from pip import main
import random,os
from PIL import Image





class Bill_App:
 
        def __init__(self,root):   
                self.root=root        
                self.root.geometry("1530x790+0+0")     
                self.root.title("Billing Software") 
                
                




                #varibles
                self.c_name=StringVar()
                self.c_phon=StringVar()
                self.bill_no=StringVar()
                z=random.randint(1000,9999)
                self.bill_no.set(z)
                self.c_email=StringVar()
                self.search_bill=StringVar()
                self.product=StringVar()
                self.prices=IntVar()
                self.qty=IntVar()
                self.sub_total=StringVar()
                self.tax_input=StringVar()
                self.total=StringVar()


                #Product details

                self.Category=["Select Option","Clothing","LifeStyle","Mobiles"]

                self.SubCatClothing=["Pant","T-shirt","Shirt"]
                self.pant=["Levis",'Ok','spayker']
                self.price_Levis=5000
                self.price_Ok=700
                self.price_spayker=8000


                self.T_shirt=['polo','Roadster','Jack&Jones']
                self.price_polo=1500
                self.price_Roadster=1800
                self.price_JackJones=1700

                self.Shirt=['Peter England','Louis Phillipe','Park Avenue']
                self.price_Peter=2100
                self.price_Louis=2700
                self.price_Park=1740


                self.SubCatLifeStyle=['Bath Soap','Face Creame','Hair Oil']

                self.Bath_soap=['LifeBuy', 'Lux', 'Santoor', 'Pearl'] 
                self.price_life=float(20)

                self.price_lux=20

                self.price_santoor=20

                self.price_pearl=30

                self.Face_creame=['Fair&Lovely', 'Ponds', 'Olay', 'Garnier']

                self.price_fair=20

                self.price_ponds=20

                self.price_olay=20

                self.price_garnier=30

                self.Hair_oil=['Parachute', 'Jashmin', 'Bajaj'] 

                self.price_para=25

                self.price_jashmin=22

                self.price_bajaj=30 

                # SubCatMobiles

                self.SubCatMobiles=['Iphone', 'Sumsung', 'Xiome', 'RealMe', "One+"]

                self.Iphone=['Iphone X', 'Iphone_11', 'Iphone_12']

                self.price_ix=40000

                self.price_i11=60000

                self.price_i12=85000



                self.Samsung=['Samsung M16', 'Sumsung M12', 'Sumsung M21']

                self.price_sm16=16000

                self.price_sm12=12000

                self.price_sm21=18000

                self.Xiome=['Red11', 'Redme-12', 'RedmePro']

                self.price_r11=11000

                self.price_r12=12000

                self.price_rpro=9000

                self.RealMe=['RealMe 12', 'RealMe 13', 'RealMe Pro']

                self.price_rel12=25000

                self.price_re113=22000

                self.price_relpro=30000

                self.OnePlus=['OnePlus1', 'OnePlus2', 'OnePlus3']

                self.price_one1=45000

                self.price_one12=60000

                self.price_one3=45800
                
                
























                img=Image.open(r"D:\Billing\Photo\a.png")
                img=img.resize((1530,150),Image.LANCZOS)# resizing the images and reduces the size of the images
                self.indreniimg=ImageTk.PhotoImage(img)


                f_lbl=Label(self.root,image=self.indreniimg) #settimg the image on the windoes screen
                f_lbl.place(x=0,y=0,width=1530,height=150)



                lbl_title=Label(self.root,text="Billing Software",font=("times new roman",36,"bold"),bg="white",fg="Black")
                lbl_title.place(x=0,y=150,width=1530,height=55)



        


                Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
                Main_Frame.place(x=0,y=205,width=1530,height=580)



                #1st frame

                Cust_Frame=LabelFrame(Main_Frame,text="-----------------Customer-------------------",font=("times new roman",15,"bold"),bg="white",fg="Black")
                Cust_Frame.place(x=10,y=5,width=350,height=140)


                self.lbl_mob=Label(Cust_Frame,text="Mobile No:",font=("times new roman",12,"bold"),bg="white",fg="Black")
                self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

                self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("times new roman",12,"bold"),width=24)
                self.entry_mob.grid(row=0,column=1,sticky=W,padx=5,pady=5)


                self.lbl_name=Label(Cust_Frame,text="Name:",font=("times new roman",12,"bold"),bg="white",fg="Black")
                self.lbl_name.grid(row=1,column=0,sticky=W,padx=5,pady=2)

                self.entry_name=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("times new roman",12,"bold"),width=24)
                self.entry_name.grid(row=1,column=1,sticky=W,padx=5,pady=5)


                self.lbl_email=Label(Cust_Frame,text="Email:",font=("times new roman",12,"bold"),bg="white",fg="Black")
                self.lbl_email.grid(row=2,column=0,sticky=W,padx=5,pady=2)

                self.entry_email=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("times new roman",12,"bold"),width=24)
                self.entry_email.grid(row=2,column=1,sticky=W,padx=5,pady=5)




                #product frame

                Product_Frame=LabelFrame(Main_Frame,text="-----------------Product-------------------",font=("times new roman",15,"bold"),bg="white",fg="Black")
                Product_Frame.place(x=370,y=5,width=690,height=140)



                self.lbl_Category=Label(Product_Frame,text="Select Categories",font=("times new roman",12,"bold"),bg="white",fg="Black")
                self.lbl_Category.grid(row=0,column=0,sticky=W,padx=5,pady=2)

                self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=("times new roman",12,"bold"),width=24,state="readonly")
                self.Combo_Category.current(0)
                self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=5)
                self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)


                self.lbl_SubCategory=Label(Product_Frame,text="Select Sub-Category",font=("times new roman",12,"bold"),bg="white",fg="Black")
                self.lbl_SubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

                self.Combo_SubCategory=ttk.Combobox(Product_Frame,value=[""],font=("times new roman",12,"bold"),width=24,state="readonly")
                self.Combo_SubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=5)
                self.Combo_SubCategory.bind("<<ComboboxSelected>>",self.Product_add)


                self.lbl_ProductName=Label(Product_Frame,text="Product Name",font=("times new roman",12,"bold"),bg="white",fg="Black")
                self.lbl_ProductName.grid(row=3,column=0,sticky=W,padx=5,pady=2)


                self.Combo_productName=ttk.Combobox(Product_Frame,textvariable=self.product,font=("times new roman",12,"bold"),width=24,state="readonly")
                self.Combo_productName.grid(row=3,column=1,sticky=W,padx=5,pady=5)
                self.Combo_productName.bind("<<ComboboxSelected>>",self.price)


                self.lbl_ProducPrice=Label(Product_Frame,text="Price:",font=("times new roman",12,"bold"),bg="white",fg="Black")
                self.lbl_ProducPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)


                self.Combo_productPrice=ttk.Combobox(Product_Frame,textvariable=self.prices,font=("times new roman",12,"bold"),width=24,state="readonly")
                self.Combo_productPrice.grid(row=0,column=4,sticky=W,padx=5,pady=5)


                self.lbl_Quntity=Label(Product_Frame,text="Quantity:",font=("times new roman",12,"bold"),bg="white",fg="Black")
                self.lbl_Quntity.grid(row=1,column=3,sticky=W,padx=5,pady=2)


                self.entry_Quntity=ttk.Entry(Product_Frame,textvariable=self.qty,font=("times new roman",12,"bold"),width=24)
                self.entry_Quntity.grid(row=1,column=4,sticky=W,padx=5,pady=5)



                Search_Frame=LabelFrame(Main_Frame,bd=0,bg="white")
                Search_Frame.place(x=1069,y=0,width=500,height=70)




                self.searchnn=Button(Main_Frame,text="Costumer Bill No.",font=('times new roman',13,'bold'),bg="light green",fg="Black")
                self.searchnn.grid(row=0,column=0,sticky=W,padx=1070,pady=9)

                self.entry_serch=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("times new roman",13,"bold"),width=20)
                self.entry_serch.grid(row=0,column=2,sticky=W,padx=170,pady=13)


                self.searchnn=Button(Main_Frame,command=self.find_bill,text="Search",font=('times new roman',13,'bold'),bg="light green",fg="Black")
                self.searchnn.grid(row=0,column=0,sticky=W,padx=1440,pady=9)












                # frame
                #right Lable frasme

                RightLabelFrame=LabelFrame(Main_Frame,text="Costumer Bill",font=("times new roman",15,"bold"),bg="white",fg="Black")
                RightLabelFrame.place(x=1070,y=50,width=440,height=350)

                scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
                self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="Black")
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_y.config(command=self.textarea.yview)
                self.textarea.pack(fill=BOTH,expand=1)


                #boytoom frame part


                BottomLabelFrame=LabelFrame(Main_Frame,text="Costumer Bill",font=("times new roman",15,"bold"),bg="white",fg="Black")
                BottomLabelFrame.place(x=0,y=420,width=1530,height=150)


                self.lbl_subtotal=Label(BottomLabelFrame,text="Sub Total",font=("times new roman",12,"bold"),bg="white",fg="Black")
                self.lbl_subtotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

                self.entry_subtotall=ttk.Entry(BottomLabelFrame,textvariable=self.sub_total,font=("times new roman",12,"bold"),width=24)
                self.entry_subtotall.grid(row=0,column=1,sticky=W,padx=5,pady=5)


                self.lbl_tax=Label(BottomLabelFrame,text="Tax",font=("times new roman",12,"bold"),bg="white",fg="Black")
                self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

                self.entry_tax=ttk.Entry(BottomLabelFrame,textvariable=self.tax_input,font=("times new roman",12,"bold"),width=24)
                self.entry_tax.grid(row=1,column=1,sticky=W,padx=5,pady=5)



                


                
                self.lbl_Totalamount=Label(BottomLabelFrame,text="Total Amount",font=("times new roman",12,"bold"),bg="white",fg="Black")
                self.lbl_Totalamount.grid(row=2,column=0,sticky=W,padx=5,pady=2)

                self.entry_Totalamount=ttk.Entry(BottomLabelFrame,textvariable=self.total,font=("times new roman",12,"bold"),width=24)
                self.entry_Totalamount.grid(row=2,column=1,sticky=W,padx=5,pady=5)




                #buttoframe

                Bttn_Frame=Frame(BottomLabelFrame,border=3,bg="white")
                Bttn_Frame.place(x=320,y=0)

                self.addtoCart=Button(Bttn_Frame,command=self.AddItem,text="Add To Cart",font=('times new roman',17,'bold'),bg="light green",fg="Black")
                self.addtoCart.grid(row=0,column=0,sticky=W,padx=23,pady=20)

                self.generatebill=Button(Bttn_Frame,command=self.gen_bill,text="Generate Bill",font=('times new roman',17,'bold'),bg="light green",fg="Black")
                self.generatebill.grid(row=0,column=1,sticky=W,padx=23,pady=20)

                self.SaveBill=Button(Bttn_Frame,command=self.save_bill,text="Save Bill",font=('times new roman',17,'bold'),bg="light green",fg="Black")
                self.SaveBill.grid(row=0,column=2,sticky=W,padx=23,pady=20)

                self.PrintBill=Button(Bttn_Frame,text="Print Bill",command=self.iprint,font=('times new roman',17,'bold'),bg="light green",fg="Black")
                self.PrintBill.grid(row=0,column=3,sticky=W,padx=23,pady=20)


                self.Cleardata=Button(Bttn_Frame,command=self.clear,text="Clear Data",font=('times new roman',17,'bold'),bg="light green",fg="Black")
                self.Cleardata.grid(row=0,column=4,sticky=W,padx=23,pady=20)


                self.Exit=Button(Bttn_Frame,command=self.root.destroy,text="Exit",font=('times new roman',17,'bold'),bg="light green",fg="Black")
                self.Exit.grid(row=0,column=5,sticky=W,padx=23,pady=30)
                self.welcome()

                self.l=[]

                
        #function



        def AddItem(self):
                Tax=1
                self.n=self.prices.get()
                self.m=self.qty.get()*self.n
                self.l.append(self.m)
                if self.product.get()=="":
                        messagebox.showerror("error")
                else:
                        
                        self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
                        self.sub_total.set(str('Rs.%2f'%(sum(self.l))))
                        self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
                        self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax))))))




        def gen_bill(self):
                if self.product.get()=="":
                        messagebox.showerror("error please select")
                else:
                        
                        
                        text=self.textarea.get(10.0,(10.0+float(len(self.l))))
                        self.welcome()
                        self.textarea.insert(END,text)
                        
                        self.textarea.insert(END,"\n==================================================")
                        self.textarea.insert(END,f"\nSub Amount:\t\t\t{self.sub_total.get()}")
                        self.textarea.insert(END,f"\nTax Amount:\t\t\t{self.tax_input.get()}")
                        self.textarea.insert(END,f"\nTotal Amount:\t\t\t{self.total.get()}")
                        self.textarea.insert(END,"\n===================================================\n")



        def save_bill(self):
                op=messagebox.askyesno("Save Bill","Do You Want To Save The Bill?")
                if op>0:
                        self.bill_data=self.textarea.get(1.0,END)
                        f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
                        f1.write(self.bill_data)
                        op=messagebox.showinfo("Saved",f"{self.bill_no.get()} Saved Sucessfully")

                        f1.close()
                        
        def iprint(self):
                q=self.textarea.get(1.0,"end-1c")
                filename=tempfile.mktemp('.txt')
                open(filename,'w').write(q)
                os.startfile(filename,"print")
        


        def find_bill(self):
                found="no"
                for i in os.listdir("bills/"):
                        if i.split('.')[0]==self.search_bill.get():
                                f1=open(f'bills/{i}','r')
                                self.textarea.delete(1.0,END)
                                for d in f1:
                                        self.textarea.insert(END,d)
                                f1.close()
                                found="yes"
                if found=='no':
                        messagebox.showerror("Error","Error On Bill")


        def clear(self):
                self.textarea.delete(1.0,END)
                self.c_name.set("")


                self.textarea.delete(1.0, END)
                self.c_name.set("")
                self.c_phon.set("")
                self.c_email.set("")
                x=random.randint(1000, 9999)

                self.bill_no.set(str(x))

                self.search_bill.set("")

                self.product.set("")

                self.prices.set(0)

                self.qty.set(0)

                self.l=[0]

                self.total.set("")

                self.sub_total.set("")

                self.tax_input.set('')

                self.welcome()





        def welcome(self):
                self.textarea.delete(1.0,END)
                
                self.textarea.delete(1.0, END)
                self.textarea.insert(END, "\t    Welcome Project Mini Mall")
                self.textarea.insert(END, f"\n Bill Number:{self.bill_no.get()}")
                self.textarea.insert(END, f"\n Costumer Name:{self.c_name.get()}")
                self.textarea.insert(END, f"\n Phone Number:{self.c_phon.get()}")
                self.textarea.insert(END, f"\n Costumer Email:{self.c_email.get()}")


                self.textarea.insert(END,"\n===================================================")
                self.textarea.insert(END,f"\nProducts\t\t\tQTY\t\tPrice")
                self.textarea.insert(END,"\n===================================================\n")






        def Categories(self,event=""):
                if self.Combo_Category.get()=="Clothing":
                        self.Combo_SubCategory.config(value=self.SubCatClothing)
                        self.Combo_SubCategory.current(0)




                if self.Combo_Category.get()=="LifeStyle":
                        self.Combo_SubCategory.config(value=self.SubCatLifeStyle)
                        self.Combo_SubCategory.current(0)



                if self.Combo_Category.get()=="Mobiles":
                        self.Combo_SubCategory.config(value=self.SubCatMobiles)
                        self.Combo_SubCategory.current(0) 



        def Product_add(self,event=""):
                if self.Combo_SubCategory.get()=="Pant":
                        self.Combo_productName.config(value=self.pant)      
                        self.Combo_productName.current(0)  



                if self.Combo_SubCategory.get()=="T-shirt":
                        self.Combo_productName.config(value=self.T_shirt)      
                        self.Combo_productName.current(0)



                



                if self.Combo_SubCategory.get()=="Shirt":
                        self.Combo_productName.config(value=self.Shirt)      
                        self.Combo_productName.current(0)  





                if self.Combo_SubCategory.get()=="Bath Soap":

                        self.Combo_productName.config(value=self.Bath_soap) 
                        self.Combo_productName.current(0)

                if self.Combo_SubCategory.get()=="Face Creame":

                        self.Combo_productName.config(value=self.Face_creame)

                        self.Combo_productName.current(0)

                if self.Combo_SubCategory.get()=="Hair Oil": 
                        self.Combo_productName.config(value=self.Hair_oil)

                        self.Combo_productName.current(0)

                # Mobile

                if self.Combo_SubCategory.get()=="Iphone":

                        self.Combo_productName.config(value=self.Iphone)

                        self.Combo_productName.current(0)

                if self.Combo_SubCategory.get() == "Sumsung":

                        self.Combo_productName.config(value=self.Samsung)

                        self.Combo_productName.current(0)

                if self.Combo_SubCategory.get()=="Xiome":

                        self.Combo_productName.config(value=self.Xiome)

                        self.Combo_productName.current(0)

                if self.Combo_SubCategory.get()=="RealMe":

                        self.Combo_productName.config(value=self.RealMe)

                        self.Combo_productName.current(0)

                if self.Combo_SubCategory.get()=="One+":

                        self.Combo_productName.config(value=self.OnePlus)

                        self.Combo_productName.current(0)




        def price(self,event=""):
                #pant
                if    self.Combo_productName.get()=="Levis":
                        self.Combo_productPrice.config(valu=self.price_Levis) 
                        self.Combo_productPrice.current(0)   
                        self.qty.set(1) 



                if    self.Combo_productName.get() == "Ok": 
                
                        self.Combo_productPrice.config(value=self.price_Ok)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)

                if    self.Combo_productName.get()=="spayker":
                        self.Combo_productPrice.config(value=self.price_spayker)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)


                
                        # T-Shirt

                if    self.Combo_productName.get()=="polo":

                        self.Combo_productPrice.config(value=self.price_polo)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)  



                        
                if    self.Combo_productName.get()=="Roadster":
                        self.Combo_productPrice.config(value=self.price_Roadster)
                

                        self.Combo_productPrice.current(0)
                        self.qty.set(1)


                if self.Combo_productName.get()=="Jack&Jones":

                        self.Combo_productPrice.config(value=self.price_JackJones)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)

                        # Shirt

                if    self.Combo_productName.get() == "Peter England":

                        self.Combo_productPrice.config(value=self.price_Peter)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)

                if    self.Combo_productName.get() == "Louis Phillipe":

                        self.Combo_productPrice.config(value=self.price_Louis)

                        self.Combo_productPrice.current(0)
                        self.qty.set(1)

                if    self.Combo_productName.get() == "Park Avenue":

                        self.Combo_productPrice.config(value=self.price_Park)

                        self.Combo_productPrice.current(0)
                        self.qty.set(1)


                if    self.Combo_productName.get()=="LifeBuy":

                        self.Combo_productPrice.config(value=self.price_life)
                        self.Combo_productPrice.current(0)

                        self.qty.set(1)



                if    self.Combo_productName.get()=="Lux":

                        self.Combo_productPrice.config(value=self.price_lux)
                        self.Combo_productPrice.current(0)

                        self.qty.set(1)

                if    self.Combo_productName.get() == "Santoor":

                        self.Combo_productPrice.config(value=self.price_santoor)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)

                if    self.Combo_productName.get()=="Pearl":

                        self.Combo_productPrice.config(value=self.price_pearl)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)

                if    self.Combo_productName.get()=="Fair&Lovely":

                        self.Combo_productPrice.config(value=self.price_fair)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)

                if    self.Combo_productName.get()=="Ponds":

                        self.Combo_productPrice.config(value=self.price_ponds)

                        self.Combo_productPrice.current(0)
                        self.qty.set(1)





                if    self.Combo_productName.get()=="Olay":

                        self.Combo_productPrice.config(value=self.price_olay) 
                        self.Combo_productPrice.current(0)

                        self.qty.set(1)

                if    self.Combo_productName.get()=="Garnier":

                        self.Combo_productPrice.config(value=self.price_garnier)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)

                if    self.Combo_productName.get()=="Parachute":

                        self.Combo_productPrice.config(value=self.price_para)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)

                if    self.Combo_productName.get()=="Jashmin":

                        self.Combo_productPrice.config(value=self.price_jashmin)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)

                if    self.Combo_productName.get()=="Bajaj":

                        self.Combo_productPrice.config(value=self.price_bajaj)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)





                if    self.Combo_productName.get()=="Iphone X":

                        self.Combo_productPrice.config(value=self.price_ix) 
                        self.Combo_productPrice.current(0)

                        self.qty.set(1)

                if    self.Combo_productName.get()=="Iphone_11":

                        self.Combo_productPrice.config(value=self.price_i11)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)

                if    self.Combo_productName.get() == "Iphone_12":

                        self.Combo_productPrice.config(value=self.price_i12)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)

                if    self.Combo_productName.get() == "Samsung M16":

                        self.Combo_productPrice.config(value=self.price_sm16)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)

                if    self.Combo_productName.get()=="Sumsung M12":

                        self.Combo_productPrice.config(value=self.price_sm12)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)





                if      self.Combo_productName.get() == "Sumsung M21":

                        self.Combo_productPrice.config(value=self.price_sm21)
                        self.Combo_productPrice.current(0)

                        self.qty.set(1)

                if      self.Combo_productName.get()=="Red11":

                        self.Combo_productPrice.config(value=self.price_r11)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)

                if      self.Combo_productName.get()=="Redme-12":

                        self.Combo_productPrice.config(value=self.price_r12)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)

                if      self.Combo_productName.get() == "RedmePro":

                        self.Combo_productPrice.config(value=self.price_rpro)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)


                if      self.Combo_productName.get()=="RealMe 12":

                        self.Combo_productPrice.current(0)
                        self.Combo_productPrice.config(value=self.price_rel12)

                        self.qty.set(1)

                if      self.Combo_productName.get()=="RealMe 13":

                        self.Combo_productPrice.config(value=self.price_re113)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)

                if      self.Combo_productName.get() == "RealMe Pro":

                        self.Combo_productPrice.config(value=self.price_relpro)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)

                if      self.Combo_productName.get() == "OnePlus1":

                        self.Combo_productPrice.config(value=self.price_one1)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)


                if      self.Combo_productName.get()=="OnePlus2":

                        self.Combo_productPrice.config(value=self.price_one12)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)

                if      self.Combo_productName.get()=="OnePlus3":

                        self.Combo_productPrice.config(value=self.price_one3)

                        self.Combo_productPrice.current(0)

                        self.qty.set(1)














                                        



                                        







                                    















                    











                    






                    




                    





if __name__ == "__main__": #calling the main

    root=Tk()   #calling the root with the toolkit

    obj=Bill_App(root) 
    root.mainloop() 


    


       
