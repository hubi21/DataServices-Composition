from Tkinter import *
import Tkinter as tk
#from Tkinter.ttk import Frame, Button, Style,Treeview
from PIL import Image, ImageDraw, ImageTk, ImageFont


fields =  'Maximal Cost', 'Response Time'
nbqueries = 1

class Placeholder_State(object):
     __slots__ = 'normal_color', 'normal_font', 'placeholder_text', 'placeholder_color', 'placeholder_font', 'with_placeholder'

def add_placeholder_to(entry, placeholder, color="grey", font=None):
    normal_color = entry.cget("fg")
    normal_font = entry.cget("font")
    
    if font is None:
        font = normal_font

    state = Placeholder_State()
    state.normal_color=normal_color
    state.normal_font=normal_font
    state.placeholder_color=color
    state.placeholder_font=font
    state.placeholder_text = placeholder
    state.with_placeholder=True

    def on_focusin(event, entry=entry, state=state):
        if state.with_placeholder:
            entry.delete(0, "end")

            entry.config(fg = state.normal_color, font=state.normal_font)
            #entry.config(state='disabled')
        
            state.with_placeholder = False

    def on_focusout(event, entry=entry, state=state):
        if entry.get() == '':
            entry.insert(5, state.placeholder_text)
            entry.config(fg = state.placeholder_color, font=state.placeholder_font)
            
            state.with_placeholder = True

    entry.insert(0, placeholder)
    entry.config(fg = color, font=font)

    entry.bind('<FocusIn>', on_focusin, add="+")
    entry.bind('<FocusOut>', on_focusout, add="+")
    
    entry.placeholder_state = state

    return state


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
   print("Queries:")
   for el in Queries:
      print(el)
      print(Queries[el])
   for entry in entries[0]:
      field = entry[0]
      if field=='Maximal Cost':
         if not entry[1].get()=='Maximal Cost...':
           print('oui')
           Cost=int(entry[1].get())
           print(Cost)
      elif field=='Response Time':
         if not entry[1].get()=='Response Time...':
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
   def __init__(self, ):
      pass
      
class Page2(Page):
   def __init__(self, data):
       Page.__init__(self)
       # tree = Treeview(self)
       self.data = data
       print('>>>>>>>>>>>>>>>>>>>',self.data)
       from defuse import knap
       a,b,s,Plans=knap(data)
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
       i=0
       for planid in s:
        i=i+1
        for plan in Plans:
          if plan.ide==planid:
            rep=plan.reputation
            cost=plan.cost
            tree.insert('', 'end', text = "Plan"+str(i), values=(cost,"----",rep,"--"))
        

       tree.insert('', 'end', text = "Total", values=(b,"----",a,"--"), tags = ('oddrow',))
       tree.tag_configure('oddrow', background='light blue')

       tree.pack()

       save = Button(self, text='Save Results', cursor='exchange')
       save.pack(side=TOP, padx=5, pady=5)

       b1 = Button(self, text='Run', cursor='exchange')
       b1.pack(side=RIGHT, padx=5, pady=5)
       b2 = Button(self, text='Select Plans', cursor='exchange')
       b2.pack(side=RIGHT, padx=5, pady=5)
       b3 = Button(self, text='Confirm', cursor='exchange')
       b3.pack(side=RIGHT, padx=5, pady=5)


class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)


class MainView(tk.Frame):
    def __init__(self, row,root):
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
      for i in range(1,3): 
       ent.insert(END, "Query %d " %i,"RED")
       ent.tag_config('RED', foreground='grey',font=('black', 20))
       ent.insert(END, ":    First User Query \n","NED")
       ent.tag_config('NED', foreground='black',font=('black', 20))



       texts.append(('Data Queries',ent))

      #Separator
      seperatorFrame=Frame(root)
      seperatorFrame.pack(side=TOP, fill=X, padx=5, pady=10)


      buttonAddquerry = Button(seperatorFrame, text='Add Querry',command=(lambda e=[]: addquery1(ent)))
      buttonAddquerry.pack(side=RIGHT, padx=700, pady=1)

      seperatorFrame=Frame(root)
      seperatorFrame.pack( fill=X, padx=5, pady=10)


      #Fields
      for field in fields:
       seperatorFrame=Frame(root)
       seperatorFrame.pack( fill=X, padx=5, pady=10)
       row = Frame(root)
       lab = Label(row, width=15, text=field, anchor='w')
       ent1 = Entry(row)
       add_placeholder_to(ent1, field+str('...'))
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



      #root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
      b3 = Button(root, text='Quit', command=root.quit,cursor='X_cursor')
      b3.pack(side=RIGHT, padx=5, pady=5)
      b2 = Button(root, text='Run', command=(lambda e=inputRun: run(e,root)),cursor='sb_right_arrow')
      b2.pack(side=RIGHT, padx=5, pady=5)
      b1 = Button(root, text='Reset',
        command=(lambda e=inputRun: reset(e)), cursor='exchange')
      #b1.place(relx=-0.5, rely=0.5, anchor=CENTER)

      b1.pack(side=RIGHT, padx=5, pady=5)
      #main = MainView(root)





entries = []
texts=[]
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

    #s.pack(side=RIGHT, fill=Y)

    ent.config(yscrollcommand=s.set)
    ent2.config(yscrollcommand=s.set)
    ent.insert(END, "new Query" , 'RED')
    ent2.insert(END, "New Query" , 'RED')

     #ent.insert(END, '')
    ent.tag_config('RED', foreground='grey',font=('verdana', 16))
    ent2.tag_config('RED', foreground='black',font=('verdana', 16))
    texts.append(('Data Queries',ent))

def addquery1(ent):
    value = len(texts)+1
    ent.insert(END, "Query %d\n"%value, 'RED')
    ent.tag_config('RED', foreground='grey',font=('verdana', 16))
    texts.append(('Data Queries',ent))


if __name__ == "__main__":
    root2 = tk.Tk()
    root2.geometry("1500x1000")
    root2.title("EuDaSL: On Enriching User-Centered Data Integration Schemas in Service Lakes")  
    ### Background canvas
    root=Canvas(root2)
    root.pack(expand=True, fill=BOTH)
    image1=PhotoImage(file="").zoom(2)
    root.img=image1
    root.create_image(400, 150, anchor=NW, image=image1)
 


    Checkbuttons=[]

    #Main Page 

    ## Dauphine image 
    tiltleFrame=Frame(root)
    tiltleFrame.pack(side=TOP, padx=10, pady=10)
    photo = tk.PhotoImage(file="")

    w = tk.Label (tiltleFrame,height=150,width=1000,image =photo)
    w.pack(fill=Y)
    
    #Separator
    seperatorFrame=Frame(root)
    seperatorFrame.pack(side=TOP, fill=X, padx=5, pady=10)

    #frame for Queries
    queriesFrame=Frame(root)
    queriesFrame.pack(side=TOP, fill=X, padx=5, pady=5)


    #Separator
    seperatorFrame=Frame(root)
    seperatorFrame.pack(side=TOP, fill=X, padx=5, pady=10)

    MainView(queriesFrame,root)

    root.mainloop()