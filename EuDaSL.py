from tkinter import *
import tkinter as tk
from tkinter.ttk import Frame, Button, Style,Treeview
from PIL import Image, ImageDraw, ImageTk, ImageFont


fields =  'Maximal Cost', 'Response Time'
nbqueries = 1
entries = []
texts=[]
Checkbuttons=[]

def run(entries,root):

   Queries={}
   print (">>>>>>>>>,",entries)
   for entry in entries[1]:
      field = entry[0]
      s  = (entry[1].get("1.0",END).splitlines())
      print('%s: "%s"' % (field, s)) 
      test=True
      i=1
      while test and i<len(s):
         start=str('Query ')+str(i)
         result = s[i-1][7:]
         if result==None:
            test=False
         else:
            print(result)
            if not result=='':
               Queries[start]=result.split(',')
            i+=1
   for entry in entries[0]:
      field = entry[0]
      if field=='Maximal Cost':
         print('oui')
         Cost=int(entry[1].get())
         print(Cost)
      elif field=='Response Time':
         print('oui')
         Time=int(entry[1].get())
         print(Time)
      text  = entry[1].get()
      print('%s: "%s"' % (field, text)) 
   for entry in entries[2]:
      field = entry[0]
      text  = entry[1].get()
      if text==1:
         print('%s: "%s"' % (field, text)) 
   data= Cost
   ##data is a dictionnary of all results that will be appeared in Page2
   
   p2 = Page2(data)
   p2.place(in_=root, x=0, y=0, relwidth=1, relheight=1)
   

def reset(ents):
   for entry in ents[0]:
      entry[1].delete(0,END)
   for entry in ents[1]:
      entry[1].delete('1.0', END)
      for i in range(1,9): 
         entry[1].insert(END, "Query %d\n"%i, 'RED')
         entry[1].tag_config('RED', foreground='grey',font=('verdana', 16))
   for entry in ents[2]:
      entry[1].set(0)



class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()



class Page1(Page):
   def __init__(self, buttonframe,container):        
       Page.__init__(self)
       cwgt=Canvas(self)
       cwgt.pack(expand=True, fill=BOTH)
       image1=PhotoImage(file="background.png")
       cwgt.img=image1
       cwgt.create_image(10, 1, anchor=NW, image=image1)
      
       self.container = container
       self.buttons = buttonframe
       Checkbuttons=[]
       queriesRow=Frame(self)
       queriesRow.pack(side=TOP, fill=X, padx=5, pady=5)

       ent = Text(queriesRow, height=15, width=50)
       lab = Label(queriesRow, width=15,  text='Data Queries', anchor='w')
       lab.pack(side=LEFT)
       buttonAddquerry = Button(queriesRow, text='Add Querry',command=(lambda e=[]: addQuery(queriesRow,self)))
       buttonAddquerry.pack(side=RIGHT)
       
       addQuery(queriesRow,self)
       
       queriesRow=Frame(self)
       queriesRow.pack(side=TOP, fill=X, padx=5, pady=5)

       ent = Text(queriesRow, height=15, width=50)
       lab = Label(queriesRow, width=15,  text='Data Queries', anchor='w')
       lab.pack(side=LEFT)
       addQuery(queriesRow,self)
       texts.append(('Data Queries',ent))

       for field in fields:
         row = Frame(self)
         lab = Label(row, width=15, text=field, anchor='w')
         ent = Entry(row)
         row.pack(side=TOP, fill=X, padx=5, pady=5)
         lab.pack(side=LEFT)
         ent.pack(side=RIGHT, expand=YES, fill=X)
         entries.append((field, ent))
         row=Frame(self)

       lab1=Label(self, text="",width=68, anchor='w') 
       lab=Label(self, text="Selection Method:",width=18, anchor='w')   
       row.pack(side=LEFT, fill=X, padx=5, pady=5)
       lab1.pack(side=LEFT)
       lab.pack(side=LEFT)

       v1 = 1
       v3 = IntVar()
       v2 = IntVar()
       m1 = Checkbutton(self, text="Optimal Plan", variable=v1)
       m2 = Checkbutton(self, text="Knapsack M.", variable=v2)
       m3 = Checkbutton(self, text="All possible Plans", variable=v3)
       m1.var=v1
       m2.var=v2
       m3.var=v3
       m2.select()

       m1.pack(side=LEFT)
       m2.pack(side=LEFT)
       m3.pack(side=LEFT)
       Checkbuttons.append(('Optimal Plan', v1))
       Checkbuttons.append(('Knapsack M.', v2))
       Checkbuttons.append(('All possible Plans', v3))

       ents=[]
       ents.append(entries)
       ents.append(texts)
       ents.append(Checkbuttons)
       b3 = Button(self, text='Quit', command=root.quit,cursor='X_cursor')
       b3.pack(side=RIGHT, padx=5, pady=5)
       b2 = Button(self, text='Run', command=(lambda e=ents: run(e,self.container,self.buttons)),cursor='sb_right_arrow')
       b2.pack(side=RIGHT, padx=5, pady=5)
       b1 = Button(self, text='Reset',
          command=(lambda e=ents: reset(e)), cursor='exchange')
       b1.pack(side=RIGHT, padx=5, pady=5)
      
class Page2(Page):
   def __init__(self, data):
       Page.__init__(self)
       self.data = data
       print('>>>>>>>>>>>>>>>>>>>',self.data)
       from defuse import knap
       a,b=knap(data)
       print('>>>>>>>>>>>> a , b',a,b)
       label = tk.Label(self, text="The set of executable query plans:")
       tree = Treeview(self, columns=('Execution Cost','Response Time','Reputation','Results number'))
       tree.heading('#0', text='Data Services')
       tree.heading('#1', text='Execution Cost')
       tree.heading('#2', text='Response Time')
       tree.heading('#4', text='Results number')
       tree.heading('#3', text='Reputation')
       tree.column('#4',stretch=tk.YES)
       tree.column('#3', stretch=tk.YES)
       tree.column('#1', stretch=tk.YES)
       tree.column('#2', stretch=tk.YES)
       tree.column('#0', stretch=tk.YES)
       tree.grid(row=4, columnspan=6, sticky='nsew')
       tree.insert('', 'end', text = "Data_Servcie1", values=(b,"----",a,"--"))
       tree.pack()

       b1 = Button(self, text='Execute', cursor='exchange')
       b1.pack(side=RIGHT, padx=5, pady=5)
       b2 = Button(self, text='Select', cursor='exchange')
       b2.pack(side=RIGHT, padx=5, pady=5)
       b3 = Button(self, text='Confirm', cursor='exchange')
       b3.pack(side=RIGHT, padx=5, pady=5)


class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p3 = Page3(self)
        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        buttonframe.pack(side="top", fill="x", expand=False)
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)        
        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)
        b3.pack(side="right")
        b1.pack(side="right")
        p1.show()

def addnewQuery(queriesFrame,totalqueries):
    newqueriesFrame2=Frame(queriesFrame)
    newqueriesFrame2.pack(side=TOP, fill=X, padx=3, pady=3)
    lab = Label(newqueriesFrame2, width=15,  text='Data Queries'+str(totalqueries), anchor='w')
    lab.pack(side=LEFT)
  
    print("Add query")
    s =Scrollbar(newqueriesFrame2)
    ent = Text(newqueriesFrame2, height=2, width=3)
    ent2 = Text(newqueriesFrame2, height=2, width=3)
    ent2.pack(side=RIGHT, expand=YES, fill=X)
    ent.pack(side=RIGHT, expand=YES, fill=X)
    s.config(command=ent.yview)
    ent.config(yscrollcommand=s.set)
    ent2.config(yscrollcommand=s.set)
    ent.insert(END, "new Query" , 'RED')
    ent2.insert(END, "New Query" , 'RED')
    ent.tag_config('RED', foreground='grey',font=('verdana', 16))
    ent2.tag_config('RED', foreground='black',font=('verdana', 16))
    texts.append(('Data Queries',ent))

def addquery1(i,ent):
    value = len(texts)+1
    ent.insert(END, "Query %d\n"%value, 'RED')
    ent.tag_config('RED', foreground='grey',font=('verdana', 16))
    texts.append(('Data Queries',ent))


if __name__ == "__main__":
    root2 = tk.Tk()
    root2.geometry("1500x1000")
    root2.title("EUDaSL: On Enriching User-Centered Data Integration Schemas in Service Lakes")  
    root=Canvas(root2)
    root.pack(expand=True, fill=BOTH)
    image1=PhotoImage(file="").zoom(2)
    root.img=image1
    root.create_image(400, 150, anchor=NW, image=image1)
    tiltleFrame=Frame(root)
    tiltleFrame.pack(side=TOP, padx=10, pady=10)
    #Separator
    seperatorFrame=Frame(root)
    seperatorFrame.pack(side=TOP, fill=X, padx=5, pady=10)

    queriesFrame=Frame(root)
    queriesFrame.pack(side=TOP, fill=X, padx=5, pady=5)
      #Separator
    seperatorFrame=Frame(root)
    seperatorFrame.pack(side=TOP, fill=X, padx=5, pady=10)
    row=queriesFrame
    s =Scrollbar(row)
    ent = Text(row, height=15, width=20)
    lab = Label(row, width=15,  text='Data Queries', anchor='w')
    row.pack(side=TOP, fill=X, padx=5, pady=5)
    s.pack(side=RIGHT, fill=Y)
    ent.pack(side=RIGHT, expand=YES, fill=X)
    s.config(command=ent.yview)
    ent.config(yscrollcommand=s.set)
    lab.pack(side=LEFT)
    def on_focusin(event):
      print("Mouse position: (%s %s)" % (event.x, event.y))
      print("Single Click, Button-l")
      ent.delete(0, "end")
      ent.insert(0, '') #Insert blank for user input
      ent.config(fg = 'black')
    ent.bind('<FocusIn>', on_focusin, add="+")
    totalqueries = 1
    for i in range(1,2): 
     ent.insert(END, "Query %d\n" %i, 'RED')
     ent.tag_config('RED', foreground='grey',font=('verdana', 16))
     texts.append(('Data Queries',ent))
    #Separator
    seperatorFrame=Frame(root)
    seperatorFrame.pack(side=TOP, fill=X, padx=5, pady=10)
    buttonAddquerry = Button(queriesFrame, text='Add Querry',command=(lambda e=[]: addquery1(2,ent)))
    buttonAddquerry.pack(side=BOTTOM)
    #Separator
    seperatorFrame=Frame(root)
    seperatorFrame.pack( fill=X, padx=5, pady=10)

    for field in fields:
     seperatorFrame=Frame(root)
     seperatorFrame.pack( fill=X, padx=5, pady=10)
     row = Frame(root)
     lab = Label(row, width=15, text=field, anchor='w')
     ent1 = Entry(row)
     row.pack(side=TOP, fill=X, padx=5, pady=5)
     lab.pack(side=LEFT)
     ent1.pack(side=RIGHT, expand=YES, fill=X)
     entries.append((field, ent1))
     row=Frame(root)


    lab=Label(root, text="Selection Method:",width=18, anchor='w')   
    row.pack(side=LEFT, fill=X, padx=5, pady=5)
    lab.pack(side=LEFT)

    v1 = IntVar()
    v3 = IntVar()
    v2 = IntVar()

    m1 = Checkbutton(root, text="Optimal Plan", variable=v1)
    m2 = Checkbutton(root, text="Knapsack M.", variable=v2)
    m3 = Checkbutton(root, text="All possible Plans", variable=v3)
    m1.var=v1
    m2.var=v2
    m3.var=v3
    #select
    m2.select()
    print (v1,v2,v3)
    m1.pack(side=LEFT)
    m2.pack(side=LEFT)
    m3.pack(side=LEFT)


    Checkbuttons.append(('Optimal Plan', v1))
    Checkbuttons.append(('Knapsack M.', v2))
    Checkbuttons.append(('All possible Plans', v3))

    inputRun=[]
    inputRun.append(entries)
    inputRun.append(texts)
    inputRun.append(Checkbuttons)  
    b3 = Button(root, text='Quit', command=root.quit,cursor='X_cursor')
    b3.pack(side=RIGHT, padx=5, pady=5)
    b2 = Button(root, text='Run', command=(lambda e=inputRun: run(e,root)),cursor='sb_right_arrow')
    b2.pack(side=RIGHT, padx=5, pady=5)
    b1 = Button(root, text='Reset',
      command=(lambda e=inputRun: reset(e)), cursor='exchange')
    b1.pack(side=RIGHT, padx=5, pady=5)
    root.mainloop()
