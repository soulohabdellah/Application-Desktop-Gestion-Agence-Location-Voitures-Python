from tkinter import *
from tkinter import ttk
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox
from datetime import date
root = Tk()

root1 = Tk()
root2 = Tk()
root3=Tk()
root4=Tk()
root5=Tk()
root6=Tk()
root7=Tk()
root8=Tk()
root9=Tk()
root10=Tk()
root11=Tk()
root.config(bg='#33FCFF')
root1.config(bg='#33FCFF')
root11.config(bg='#33FCFF')
root10.config(bg='#33FCFF')
root9.config(bg='#33FCFF')
root8.config(bg='#33FCFF')
root5.config(bg='#33FCFF')
root7.config(bg='#33FCFF')
root6.config(bg='#33FCFF')
root3.config(bg='#33FCFF')
root2.config(bg='#33FCFF')
root4.config(bg='#33FCFF')

def rechercheclient():
    def Fncrech():
        marque = entry_4.get()
        voiture = entry_5.get()
        coleur = entry_6.get()
        connexion = sqlite3.connect("Location_des_voitures_database.db")
        cur = connexion.cursor()
        Request = "select nom_de_marque,nom_de_modele,Coleur,Prix_location_par_jour from vehicule,modele where vehicule.Modele_id=modele.Id_modele and Disponibilite=1 and vehicule.Coleur='"+coleur+"' and nom_de_marque='"+marque+"' and nom_de_modele='"+voiture+"'"

        # # Debut de programme
        cur.execute(Request)
        data = cur.fetchall()
        data.insert(0, ('Marque', 'Voiture', 'Couleur', 'Prix Location'))
        i = 0
        j = 0
        rows = []
        for ligne in data:
            cols = []
            j = 0

            for colonne in ligne:

                z = Entry(root3,relief=GROOVE)
                z.grid(row=i + 1, column=j + 1, sticky=NSEW)

                z.insert(END, '%s' % (colonne))

                cols.append(z)
                j += 1
            rows.append(cols)
            i += 1
        connexion.commit()
        connexion.close()

        root3.mainloop()




    root3.deiconify()
    root.withdraw()
    root3.geometry('700x500')
    root3.title("Recherche voiture ")
    Button(root3, text='Recherche', width=20, bg='green', fg='white', command=Fncrech).place(x=500, y=140)
    Button(root3, text='Cancel', width=20, bg='brown', fg='white', command=menuprincipale).place(x=500, y=170)
    label_4 = Label(root3, text="Marque",bg='#33FCFF', width=20, font=("bold", 10))
    label_4.place(x=50, y=140)

    entry_4 = Entry(root3, width=40)
    entry_4.place(x=200, y=140)
    label_5 = Label(root3, text="Voiture",bg='#33FCFF', width=20, font=("bold", 10))
    label_5.place(x=50, y=170)

    entry_5 = Entry(root3, width=40)
    entry_5.place(x=200, y=170)
    label_6 = Label(root3, text="Coleur",bg='#33FCFF', width=20, font=("bold", 10))
    label_6.place(x=50, y=200)
    entry_6 = Entry(root3, width=40)
    entry_6.place(x=200, y=200)

    # it is use for display the registration form on the window
    root3.mainloop()

def Reservation():
    def funreser():

     try:#client
        cin = entry_1.get()
        prenom = entry_2.get()
        nom = entry_3.get()
        email = entry_4.get()
        telephone = entry_5.get()
        paypalcode= entry_6.get()
        requete_client="insert into client values ('"+cin+"','"+nom+"','"+prenom+"','"+email+"','"+telephone+"','"+paypalcode+"')"
        connexion = sqlite3.connect("Location_des_voitures_database.db")
        cur = connexion.cursor()

        cur.execute(requete_client)


        #Voiture
        marque = entry_7.get()
        voiture = entry_8.get()
        coleur = entry_9.get()
        jourdep = entry_14.get()
        moisdep= entry_15.get()
        anneedep = entry_16.get()
        jourfin = entry_17.get()
        moisfin = entry_18.get()
        anneefin = entry_19.get()
        ddep = date(int(anneedep), int(moisdep), int(jourdep))
        dfin = date(int(anneefin), int(moisfin), int(jourfin))
        du = dfin - ddep
        duree=du.days
        #duree=(int(anneefin)-int(anneedep))*365+(int(moisfin)-int(moisdep))*30+int(jourfin)-int(jourdep)
        matricule=cur.execute("select Matricule from vehicule,modele where Modele_id=Id_modele and Disponibilite=1 and Coleur='"+coleur+"'and nom_de_marque='"+marque+"' and nom_de_modele='"+voiture+"'")
        obj=matricule.fetchall()
        obj1=obj[0]
        matricule1=obj1[0]
        prixjr = cur.execute("select Prix_location_par_jour from vehicule where Matricule='"+matricule1+"'")
        obj = prixjr.fetchall()
        obj1 = obj[0]
        prix = obj1[0]
        prixtotal = duree * float(prix)

        requete_voiture="update vehicule set Disponibilite=0 where Matricule="+matricule1+""
        cur.execute(requete_voiture)
        #Contrat partie:
        requete_contrat="insert into contrat (Vehicule_Matricule,Client_cin,DateDep,DateFin,LaDuree,montant)values('"+matricule1+"','"+cin+"','"+jourdep+"/"+moisdep+"/"+anneedep+"','"+jourfin+"/"+moisfin+"/"+anneefin+"',"+str(duree)+","+str(prixtotal)+")"
        cur.execute(requete_contrat)
        connexion.commit()
        connexion.close()
        messagebox.showinfo(title='Felecitation !', message='Felecitation vous avez reserver une voiture')
     except:
         messagebox.showerror(title='Error !', message='Les informations erronées')

    root2.deiconify()
    root.withdraw()
    root2.geometry('700x500')
    root2.title("Locater voiture ")
    label_0 = Label(root2, text="Client autentification",bg='#33FCFF', width=20, font=("bold", 15))
    label_0.place(x=40, y=5)

    label_1 = Label(root2, text="CIN", width=20,bg='#33FCFF', font=("bold", 10))
    label_1.place(x=50, y=35)

    entry_1 = Entry(root2, width=40)
    entry_1.place(x=200, y=35)

    label_2 = Label(root2, text="Prénom",bg='#33FCFF', width=20, font=("bold", 10))
    label_2.place(x=50, y=65)

    entry_2 = Entry(root2, width=40)
    entry_2.place(x=200, y=65)
    label_3 = Label(root2, text="Nom",bg='#33FCFF', width=20, font=("bold", 10))
    label_3.place(x=50, y=95)

    entry_3 = Entry(root2, width=40)
    entry_3.place(x=200, y=95)
    label_4 = Label(root2, text="Email",bg='#33FCFF', width=20, font=("bold", 10))
    label_4.place(x=50, y=125)

    entry_4 = Entry(root2, width=40)
    entry_4.place(x=200, y=125)
    label_5 = Label(root2, text="Téléphone",bg='#33FCFF', width=20, font=("bold", 10))
    label_5.place(x=50, y=155)

    entry_5 = Entry(root2, width=40)
    entry_5.place(x=200, y=155)
    label_6 = Label(root2, text="PayPal code",bg='#33FCFF', width=20, font=("bold", 10))
    label_6.place(x=50, y=185)

    entry_6 = Entry(root2, width=40,show="*")
    entry_6.place(x=200, y=185)
    label_12 = Label(root2, text="Voiture caracteristique",bg='#33FCFF', width=20, font=("bold", 15))
    label_12.place(x=40, y=215)
    label_7 = Label(root2, text="Marque",bg='#33FCFF', width=20, font=("bold", 10))
    label_7.place(x=50, y=245)

    entry_7 = Entry(root2, width=40)
    entry_7.place(x=200, y=245)
    label_8 = Label(root2, text="Voiture",bg='#33FCFF', width=20, font=("bold", 10))
    label_8.place(x=50, y=275)

    entry_8 = Entry(root2, width=40)
    entry_8.place(x=200, y=275)
    label_9 = Label(root2, text="Couleur",bg='#33FCFF', width=20, font=("bold", 10))
    label_9.place(x=50, y=305)

    entry_9 = Entry(root2, width=40)
    entry_9.place(x=200, y=305)
    label_13 = Label(root2, text="Date location",bg='#33FCFF', width=20, font=("bold", 15))
    label_13.place(x=40, y=335)
    label_14 = Label(root2, text="Date depart",bg='#33FCFF', width=20, font=("bold", 10))
    label_14.place(x=50, y=365)

    entry_14 = Entry(root2, width=3)
    entry_14.place(x=200, y=365)
    entry_15 = Entry(root2, width=3)
    entry_15.place(x=230, y=365)
    entry_16 = Entry(root2, width=8)
    entry_16.place(x=260, y=365)
    label_16 = Label(root2, text="Date fin",bg='#33FCFF', width=20, font=("bold", 10))
    label_16.place(x=300, y=365)
    entry_17 = Entry(root2, width=3)
    entry_17.place(x=450, y=365)
    entry_18 = Entry(root2, width=3)
    entry_18.place(x=480, y=365)
    entry_19 = Entry(root2, width=8)
    entry_19.place(x=510, y=365)



    Button(root2, text='Reserver', width=20, bg='green', fg='white', command=funreser).place(x=240, y=400)
    Button(root2, text='Cancel', width=20, bg='brown', fg='white', command=menuprincipale).place(x=240, y=440)

    # it is use for display the registration form on the window
    root2.mainloop()


def menuprincipale():

    root1.withdraw()
    root2.withdraw()
    root3.withdraw()
    root4.withdraw()
    root5.withdraw()
    root1.withdraw()
    root2.withdraw()
    root3.withdraw()
    root5.withdraw()
    root6.withdraw()
    root7.withdraw()
    root8.withdraw()
    root9.withdraw()
    root10.withdraw()
    root11.withdraw()
    root.deiconify()
    connexion = sqlite3.connect("Location_des_voitures_database.db")
    cur = connexion.cursor()
    Request = "select nom_de_marque,nom_de_modele,Coleur,Prix_location_par_jour from vehicule,modele where vehicule.Modele_id=modele.Id_modele and Disponibilite=1 "
    # Debut de programme
    cur.execute(Request)
    data = cur.fetchall()
    data.insert(0,('Marque', 'Voiture', 'Couleur','Prix Location'))
    root.geometry('700x500')
    root.title("Location voitures menu")
    image1 = Image.open("C:/Users/Solouh/Desktop/pfa/imgvoiture.jpg")
    test = ImageTk.PhotoImage(image1)

    label4 = Label(root,image=test,width=150,height=150)
    label4.image = test
    label4.place(x=520,y=10)
    def quitapp():
        root.destroy()



    Button(root, text='Mode admin', width=20, bg='green', fg='white', command=manager_autentification).place(x=520, y=200)
    Button(root, text='Reserver voiture', width=20, bg='blue', fg='white', command=Reservation).place(x=520, y=250)
    Button(root, text='Recherche', width=20, bg='blue', fg='white', command=rechercheclient).place(x=520, y=300)
    Button(root, text='Quitter', width=20, bg='brown', fg='white', command=quitapp).place(x=520, y=350)



    i=0
    j=0
    rows = []
    for ligne in data:
        cols = []
        j = 0

        for colonne in ligne:
           e = Entry(relief=GROOVE)
           e.grid(row=i+1, column=j+1, sticky=NSEW)

           e.insert(END, '%s' % (colonne))

           cols.append(e)
           j+=1
        rows.append(cols)
        i +=1


    connexion.commit()
    connexion.close()
    root.mainloop()
def Espaceadmin():
    root1.withdraw()
    root2.withdraw()
    root3.withdraw()
    root.withdraw()
    root5.withdraw()
    root6.withdraw()
    root7.withdraw()
    root8.withdraw()
    root9.withdraw()
    root10.withdraw()
    root11.withdraw()
    root4.deiconify()
    root4.geometry('900x500')
    root4.title("Manager espace")

    connexion = sqlite3.connect("Location_des_voitures_database.db")
    cur = connexion.cursor()
    Request = "select Matricule,nom_de_marque,nom_de_modele,Coleur,Prix_location_par_jour,Disponibilite from vehicule,modele where vehicule.Modele_id=modele.Id_modele "
    # Debut de programme
    cur.execute(Request)
    data = cur.fetchall()
    data.insert(0, ('Matricule','Marque', 'Voiture', 'Couleur', 'Prix Location','Disponibilite'))

    i = 0
    j = 0
    rows = []
    for ligne in data:
        cols = []
        j = 0

        for colonne in ligne:
            z = Entry(root4, relief=GROOVE)
            z.grid(row=i + 1, column=j + 1, sticky=NSEW)

            z.insert(END, '%s' % (colonne))

            cols.append(z)
            j += 1
        rows.append(cols)
        i += 1
    connexion.commit()
    connexion.close()
    Button(root4, text='Ajouter voitures', width=15, bg='green', fg='white', command=Ajoutervoiture).place(x=765,y=50)
    Button(root4, text='Archive des contrats', width=15, bg='blue', fg='white', command=listcontrat).place(x=765,y=100)

    Button(root4, text='Supprimer vehicules', width=15, bg='blue', fg='white', command=Supprimervoiture).place(x=765, y=150)
    Button(root4, text='Modifier vehicules', width=15, bg='blue', fg='white', command=Modifiervoiture).place(x=765, y=200)
    Button(root4, text='Recherche multiple', width=15, bg='blue', fg='white', command=recherchecmanager).place(x=765, y=250)
    Button(root4, text='Liste clients', width=15, bg='blue', fg='white', command=listclient).place(x=765, y=300)
    Button(root4, text='Chiffre daffaire', width=15, bg='blue', fg='white', command=chiffrdaff).place(x=765, y=350)
    Button(root4, text='Deconnexion', width=15, bg='brown', fg='white', command=menuprincipale).place(x=765, y=400)
    root4.mainloop()
def listcontrat():
    root4.withdraw()
    root11.deiconify()
    root11.geometry('900x500')
    root11.title("Liste contrat")

    connexion = sqlite3.connect("Location_des_voitures_database.db")
    cur = connexion.cursor()
    Request = "select id_contrat,montant,DateDep,DateFin,Client_cin,Vehicule_Matricule from contrat "
    # Debut de programme
    cur.execute(Request)
    data = cur.fetchall()
    data.insert(0, ('Id contrat', 'Montant', 'Date debut', 'Date fin', 'CIN client', 'Vehicule matricule'))

    i = 0
    j = 0
    rows = []
    for ligne in data:
        cols = []
        j = 0

        for colonne in ligne:
            z = Entry(root11, relief=GROOVE)
            z.grid(row=i + 1, column=j + 1, sticky=NSEW)

            z.insert(END, '%s' % (colonne))

            cols.append(z)
            j += 1
        rows.append(cols)
        i += 1
    connexion.commit()
    connexion.close()
    Button(root11, text='OK', width=15, bg='green', fg='white', command=listcontrat).place(x=765, y=50)
    Button(root11, text='Chifrre daffaire', width=15, bg='green', fg='white', command=chiffrdaff).place(x=765, y=100)

    Button(root11, text='Cancel', width=15, bg='brown', fg='white', command=Espaceadmin).place(x=765, y=150)

    root11.mainloop()
def recherchecmanager():
    root4.withdraw()
    def Fncreccontrat():
        idcontrat1 = entry_6.get()
        idcontrat=int(idcontrat1)
        connexion = sqlite3.connect("Location_des_voitures_database.db")
        cur = connexion.cursor()
        Request = "select id_contrat,montant,DateDep,DateFin,Client_cin,Vehicule_Matricule from contrat where id_contrat="+str(idcontrat)+""
        # Debut de programme
        cur.execute(Request)
        data = cur.fetchall()
        data.insert(0, ('Id contrat', 'Montant', 'Date debut', 'Date fin', 'CIN client', 'Vehicule matricule'))

        i = 0
        j = 0
        rows = []
        for ligne in data:
            cols = []
            j = 0

            for colonne in ligne:
                z = Entry(root10, relief=GROOVE)
                z.grid(row=i + 1, column=j + 1, sticky=NSEW)

                z.insert(END, '%s' % (colonne))

                cols.append(z)
                j += 1
            rows.append(cols)
            i += 1
        connexion.commit()
        connexion.close()
        root10.mainloop()

    def Fncrechclient():
        cin = entry_5.get()

        connexion = sqlite3.connect("Location_des_voitures_database.db")
        cur = connexion.cursor()
        Request = "select * from client where Cin='"+cin+"'"
        # Debut de programme
        cur.execute(Request)
        data = cur.fetchall()
        data.insert(0, ('CIN', 'Nom', 'Prénom', 'Email', 'Telephone', 'Paypal'))

        i = 0
        j = 0
        rows = []
        for ligne in data:
            cols = []
            j = 0

            for colonne in ligne:
                z = Entry(root10, relief=GROOVE)
                z.grid(row=i + 1, column=j + 1, sticky=NSEW)

                z.insert(END, '%s' % (colonne))

                cols.append(z)
                j += 1
            rows.append(cols)
            i += 1
        connexion.commit()
        connexion.close()

        root10.mainloop()


    def Fncrechveh():
        matricule = entry_4.get()
        connexion = sqlite3.connect("Location_des_voitures_database.db")
        cur = connexion.cursor()
        Request = "select Matricule,nom_de_marque,nom_de_modele,Coleur,Prix_location_par_jour,Disponibilite from vehicule,modele where vehicule.Modele_id=modele.Id_modele and Matricule ='"+matricule+"'"
        # Debut de programme
        cur.execute(Request)
        data = cur.fetchall()
        data.insert(0, ('Matricule', 'Marque', 'Voiture', 'Couleur', 'Prix Location', 'Disponibilite'))

        i = 0
        j = 0
        rows = []
        for ligne in data:
            cols = []
            j = 0

            for colonne in ligne:
                z = Entry(root10, relief=GROOVE)
                z.grid(row=i + 1, column=j + 1, sticky=NSEW)

                z.insert(END, '%s' % (colonne))

                cols.append(z)
                j += 1
            rows.append(cols)
            i += 1
        connexion.commit()
        connexion.close()
        root10.mainloop()

    root10.deiconify()
    root4.withdraw()
    root10.geometry('900x500')
    root10.title("Recherche multiple ")
    label_12 = Label(root10, text="Recherche vehicule",bg='#33FCFF', width=20, font=("bold", 15))
    label_12.place(x=40, y=100)
    label_4 = Label(root10, text="Matricule",bg='#33FCFF', width=20, font=("bold", 10))
    label_4.place(x=50, y=140)

    entry_4 = Entry(root10, width=40)
    entry_4.place(x=200, y=140)
    Button(root10, text='Recherche', width=20, bg='green', fg='white', command= Fncrechveh).place(x=500, y=140)
    Button(root10, text='Cancel', width=20, bg='brown', fg='white', command=Espaceadmin).place(x=700, y=140)
    label_13 = Label(root10, text="Recherche client",bg='#33FCFF', width=20, font=("bold", 15))
    label_13.place(x=40, y=180)

    label_5 = Label(root10, text="CIN",bg='#33FCFF', width=20, font=("bold", 10))
    label_5.place(x=50, y=220)
    entry_5 = Entry(root10, width=40)
    entry_5.place(x=200, y=220)
    Button(root10, text='Recherche', width=20, bg='green', fg='white',command=Fncrechclient).place(x=500, y=220)
    Button(root10, text='Cancel', width=20, bg='brown', fg='white', command=Espaceadmin).place(x=700, y=220)
    label_14 = Label(root10, text="Recherche contrat",bg='#33FCFF', width=20, font=("bold", 15))
    label_14.place(x=40, y=260)


    label_6 = Label(root10, text="Id contrat",bg='#33FCFF', width=20, font=("bold", 10))
    label_6.place(x=50, y=300)
    entry_6 = Entry(root10, width=40)
    entry_6.place(x=200, y=300)
    Button(root10, text='Recherche', width=20, bg='green', fg='white',command= Fncreccontrat).place(x=500, y=300)
    Button(root10, text='Cancel', width=20, bg='brown', fg='white', command=Espaceadmin).place(x=700, y=300)

    # it is use for display the registration form on the window
    root10.mainloop()


def chiffrdaff():
    root11.withdraw()
    root4.withdraw()
    root9.deiconify()
    root9.geometry('900x300')
    root9.title("Chiffre d'affaire")
    Button(root9, text='OK', width=15, bg='green', fg='white', command=chiffrdaff).place(x=765, y=50)
    Button(root9, text='Cancel', width=15, bg='brown', fg='white', command=Espaceadmin).place(x=765, y=100)
    connexion = sqlite3.connect("Location_des_voitures_database.db")
    cur = connexion.cursor()
    Request = "select sum(montant) from contrat "
    # Debut de programme
    cur.execute(Request)
    data = cur.fetchall()
    data.insert(0, ('Chiffre daffaire en DH',''))


    i = 0
    j = 0
    rows = []
    for ligne in data:
        cols = []
        j = 0


        for colonne in ligne:
            z = Entry(root9, relief=GROOVE)
            z.grid(row=i + 1, column=j + 1, sticky=NSEW)

            z.insert(END, '%s' % (colonne))

            cols.append(z)
            j += 1
        rows.append(cols)
        i += 1
    connexion.commit()
    connexion.close()

    root9.mainloop()
def listclient():
    root4.withdraw()
    root8.deiconify()
    root8.geometry('900x500')
    root8.title("Liste client")

    connexion = sqlite3.connect("Location_des_voitures_database.db")
    cur = connexion.cursor()
    Request = "select * from client "
    # Debut de programme
    cur.execute(Request)
    data = cur.fetchall()
    data.insert(0, ('CIN', 'Nom', 'Prénom', 'Email', 'Telephone', 'Paypal'))

    i = 0
    j = 0
    rows = []
    for ligne in data:
        cols = []
        j = 0

        for colonne in ligne:
            z = Entry(root8, relief=GROOVE)
            z.grid(row=i + 1, column=j + 1, sticky=NSEW)

            z.insert(END, '%s' % (colonne))

            cols.append(z)
            j += 1
        rows.append(cols)
        i += 1
    connexion.commit()
    connexion.close()
    Button(root8, text='OK', width=15, bg='green', fg='white', command=listclient).place(x=765, y=50)
    Button(root8, text='Cancel', width=15, bg='brown', fg='white', command=Espaceadmin).place(x=765, y=100)


    root8.mainloop()
def Modifiervoiture():
    root1.withdraw()
    root2.withdraw()
    root3.withdraw()
    root4.withdraw()
    root5.withdraw()
    root.withdraw()
    root6.withdraw()
    root7.deiconify()
    def Updatevoitur():
     try:
        matricule = entry_4.get()
        nvcolor = entry_5.get()
        nvprix1 = entry_6.get()
        nvprix=float(nvprix1)
        connexion = sqlite3.connect("Location_des_voitures_database.db")
        cur = connexion.cursor()
        requete_update = "update vehicule set Coleur = '"+nvcolor+"' , Prix_location_par_jour = "+str(nvprix)+" where Disponibilite=1 and Matricule=" + matricule + ""

        cur.execute(requete_update)
        connexion.commit()
        connexion.close()
        messagebox.showinfo(title='Felecitation !', message='Voiture modifier')

     except:
        messagebox.showerror(title='Error !', message='Les informations erroées')
    root7.geometry('700x500')
    root7.title("Modifier voiture")
    label_12 = Label(root7, text="Modifier vehicule",bg='#33FCFF', width=20, font=("bold", 15))
    label_12.place(x=40, y=100)
    Button(root7, text='Modifier', width=20, bg='green', fg='white', command=Updatevoitur).place(x=500, y=140)
    Button(root7, text='Cancel', width=20, bg='brown', fg='white', command=Espaceadmin).place(x=500, y=170)
    label_4 = Label(root7, text="Matricule",bg='#33FCFF', width=20, font=("bold", 10))
    label_4.place(x=50, y=140)

    entry_4 = Entry(root7, width=40)
    entry_4.place(x=200, y=140)
    label_5 = Label(root7, text="Nouveau Couleur",bg='#33FCFF', width=20, font=("bold", 10))
    label_5.place(x=50, y=190)

    entry_5 = Entry(root7, width=40)
    entry_5.place(x=200, y=190)
    label_6 = Label(root7, text="Nouveau prix",bg='#33FCFF', width=20, font=("bold", 10))
    label_6.place(x=50, y=220)

    entry_6 = Entry(root7, width=40)
    entry_6.place(x=200, y=220)
    root7.mainloop()


def Supprimervoiture():
    root1.withdraw()
    root2.withdraw()
    root3.withdraw()
    root4.withdraw()
    root5.withdraw()
    root.withdraw()
    root6.deiconify()
    def Deletevoitur():
     try:
        matricule = entry_4.get()
        connexion = sqlite3.connect("Location_des_voitures_database.db")
        cur = connexion.cursor()
        requete_supp="delete from vehicule where Disponibilite=1 and Matricule="+matricule+""

        cur.execute(requete_supp)
        connexion.commit()
        connexion.close()
        messagebox.showinfo(title='Felecitation !', message='Vehicule supprimer')

     except:
        messagebox.showerror(title='Error !', message='Les informations erroées')
    root6.geometry('700x500')
    root6.title("Supprimer voiture")
    label_12 = Label(root6, text="Supprimer vehicule",bg='#33FCFF', width=20, font=("bold", 15))
    label_12.place(x=40, y=100)
    Button(root6, text='Supprimer', width=20, bg='green', fg='white', command=Deletevoitur).place(x=500, y=140)
    Button(root6, text='Cancel', width=20, bg='brown', fg='white', command=Espaceadmin).place(x=500, y=170)
    label_4 = Label(root6, text="Matricule",bg='#33FCFF', width=20, font=("bold", 10))
    label_4.place(x=50, y=140)

    entry_4 = Entry(root6, width=40)
    entry_4.place(x=200, y=140)
    root6.mainloop()

def Ajoutervoiture():
    root1.withdraw()
    root2.withdraw()
    root3.withdraw()
    root4.withdraw()
    root.withdraw()
    root5.deiconify()
    root5.geometry('700x500')
    root5.title("Ajouter voiture")
    def funraddmodele():
     try:
        idmodele1 = entry_7.get()
        idmodele=int(idmodele1)
        nommarque = entry_8.get()
        nomvoiture = entry_9.get()
        version = entry_10.get()
        jour=entry_14.get()
        mois = entry_15.get()
        annee = entry_16.get()
        requete_modele = "insert into modele values (" + str(idmodele )+ ",'" + nommarque + "','" + nomvoiture + "','" + version+ "','"+jour+"/"+mois+"/"+annee+"')"
        connexion = sqlite3.connect("Location_des_voitures_database.db")
        cur = connexion.cursor()

        cur.execute(requete_modele)
        connexion.commit()
        connexion.close()
        messagebox.showinfo(title='Felecitation !', message='Felecitation vous avez ajouter un modele')
     except:
        messagebox.showerror(title='Error !', message='Les informations erroées')

    def funaddvoiture():
     try:

        matricule = entry_1.get()
        couleur = entry_2.get()
        prix1 = entry_3.get()
        prix=float(prix1)
        modele1 = entry_4.get()
        modele=int(modele1)
        requete_vehicule = "insert into vehicule values ('" + matricule + "','" + couleur + "'," + str(prix) + ",1," + str(modele) + ")"
        connexion = sqlite3.connect("Location_des_voitures_database.db")
        cur = connexion.cursor()

        cur.execute(requete_vehicule)
        connexion.commit()
        connexion.close()
        messagebox.showinfo(title='Felecitation !', message='Felecitation vous avez ajouter une vehicule')
     except:
         messagebox.showerror(title='Error !', message='Les informations erroées')
    label_0 = Label(root5, text="Voiture informations",bg='#33FCFF', width=20, font=("bold", 15))
    label_0.place(x=40, y=5)

    label_1 = Label(root5, text="Matricule",bg='#33FCFF', width=20, font=("bold", 10))
    label_1.place(x=50, y=35)

    entry_1 = Entry(root5, width=40)
    entry_1.place(x=200, y=35)

    label_2 = Label(root5, text="Coleur",bg='#33FCFF', width=20, font=("bold", 10))
    label_2.place(x=50, y=65)

    entry_2 = Entry(root5, width=40)
    entry_2.place(x=200, y=65)
    label_3 = Label(root5, text="Prix de location",bg='#33FCFF', width=20, font=("bold", 10))
    label_3.place(x=50, y=95)

    entry_3 = Entry(root5, width=40)
    entry_3.place(x=200, y=95)
    label_4 = Label(root5, text="Modele id",bg='#33FCFF', width=20, font=("bold", 10))
    label_4.place(x=50, y=125)

    entry_4 = Entry(root5, width=40)
    entry_4.place(x=200, y=125)


    Button(root5, text='Ajouter voiture', width=20, bg='green', fg='white', command=funaddvoiture).place(x=100, y=155)
    Button(root5, text='Cancel', width=20, bg='brown', fg='white', command=Espaceadmin).place(x=300, y=155)

    label_12 = Label(root5, text="Modele caracteristique",bg='#33FCFF', width=20, font=("bold", 15))
    label_12.place(x=40, y=185)
    label_7 = Label(root5, text="Id modele",bg='#33FCFF', width=20, font=("bold", 10))
    label_7.place(x=50, y=215)

    entry_7 = Entry(root5, width=40)
    entry_7.place(x=200, y=215)
    label_8 = Label(root5, text="Nom de marque",bg='#33FCFF', width=20, font=("bold", 10))
    label_8.place(x=50, y=245)

    entry_8 = Entry(root5, width=40)
    entry_8.place(x=200, y=245)
    label_9 = Label(root5, text="Nom de voiture",bg='#33FCFF', width=20, font=("bold", 10))
    label_9.place(x=50, y=275)

    entry_9 = Entry(root5, width=40)
    entry_9.place(x=200, y=275)
    label_10 = Label(root5, text="Version",bg='#33FCFF', width=20, font=("bold", 10))
    label_10.place(x=50, y=305)

    entry_10 = Entry(root5, width=40)
    entry_10.place(x=200, y=305)
    label_14 = Label(root5, text="Date production",bg='#33FCFF', width=20, font=("bold", 10))
    label_14.place(x=50, y=335)

    entry_14 = Entry(root5, width=3)
    entry_14.place(x=200, y=335)
    entry_15 = Entry(root5, width=3)
    entry_15.place(x=230, y=335)
    entry_16 = Entry(root5, width=8)
    entry_16.place(x=260, y=335)

    Button(root5, text='Ajouter modele', width=20, bg='green', fg='white', command=funraddmodele).place(x=100, y=375)
    Button(root5, text='Cancel', width=20, bg='brown', fg='white', command=Espaceadmin).place(x=300, y=375)

    # it is use for display the registration form on the window
    root2.mainloop()


def manager_autentification():
    root.withdraw()
    root1.deiconify()
    root1.geometry('700x500')
    root1.title("Manager Autentification")

    def Fnc():
        email=entry_1.get()
        password = entry_2.get()
        connexion = sqlite3.connect("Location_des_voitures_database.db")
        cur = connexion.cursor()
        Request = "select * from manager"
        # # Debut de programme
        cur.execute(Request)
        data = cur.fetchall()
        data1=data[0]
        emailmanager=data1[1]
        passwordmanager = data1[3]
        if emailmanager==email and password==passwordmanager:
            messagebox.showinfo(title='Bienvenu !', message='Bienvenu Admin !')
            Espaceadmin()
        if emailmanager!=email:
            entry_1.config(bg="red")
            messagebox.showerror(title='Error !', message='Email erroné !')

        if password!=passwordmanager:
            entry_2.config(bg="red")
            messagebox.showerror(title='Error !', message='Password erroné !')




    label_0 = Label(root1, text="Manager autentification",bg='#33FCFF', width=20, font=("bold", 20))
    label_0.place(x=170, y=60)

    label_1 = Label(root1, text="Email",bg='#33FCFF', width=20, font=("bold", 10))
    label_1.place(x=50, y=150)

    entry_1 = Entry(root1, width=40)
    entry_1.place(x=200, y=150)

    label_2 = Label(root1, text="Password",bg='#33FCFF', width=20, font=("bold", 10))
    label_2.place(x=50, y=200)

    entry_2 = Entry(root1, width=40,show="*")
    entry_2.place(x=200, y=200)


    Button(root1, text='Connexion', width=20, bg='green', fg='white', command=Fnc).place(x=240, y=250)
    Button(root1, text='Cancel', width=20, bg='brown', fg='white', command=menuprincipale).place(x=240, y=290)

    # it is use for display the registration form on the window
    root1.mainloop()




#Connexion au base de données
#import sqlite3
# connexion=sqlite3.connect("Location_des_voitures_database.db")
# cur=connexion.cursor()
#Les requetes de creations des tables de base de données
#Requeste_create_table_client="create table client (Cin VARCHAR(20) primary key,Nom VARCHAR(20),Prenom VARCHAR(20),Email VARCHAR(25),Telephone VARCHAR(20),Password VARCHAR(20))"
#Requeste_create_table_manger="create table manager(Id_manager int primary key,Email_manager VARCHAR(20),Telephone_manager VARCHAR(20),Password_manager VARCHAR(20))"
#Requeste_create_table_modele="create table modele(Id_modele int primary key,nom_de_marque VARCHAR(20),nom_de_modele VARCHAR(20),version VARCHAR(20),date_production DATE)"
#Requeste_create_table_vehicule="create table vehicule(Matricule VARCHAR(20) primary key,Coleur VARCHAR(20),Prix_location_par_jour float,Disponibilite BOOLEAN,Modele_id int,FOREIGN KEY (Modele_id) REFERENCES modele(Id_modele))"
#Requeste_create_table_contrat="create table contrat(id_contrat int primary key,montant float,DateDep DATE,DateFin DATE,LaDuree int ,Client_cin VARCHAR(20),Vehicule_Matricule VARCHAR(20),foreign key(Client_cin)references client(Cin),foreign key(Vehicule_Matricule)references vehicule(Matricule))"
#cur.execute(Requeste_create_table_contrat)
#connexion.commit()
#connexion.close()
#Debut de programme

menuprincipale()
