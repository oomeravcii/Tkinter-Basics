
#! Tkinter penceresi ve pencere adı oluşturma:

import tkinter

window = tkinter.Tk() #? Pencere açma komutudur.

window.title("Tkinter Test") #? Pencerenin adını yazdırır.

#---------------------------------

#! Pencereye yazı yazdırma: 

text1 = tkinter.Label(window,text="Hello World!") #? Pencereye yazı yazdırma komutudur.
text1.pack() #? Yazıyı yazdırmak için paketleme zorunludur.

text2 = tkinter.Label(window,text="Hello!",fg="red") #? "fg" ile yazının rengi değiştirilir.
text2.pack()

text3 = tkinter.Label(window,text="World!",fg="white",bg="black") #? "bg" ile yazının arkaplan rengi değiştirilir.
text3.pack()

text4 = tkinter.Label(window,text="New Text",font="Times 15 italic") #? "font" ile yazı tipi, büyüklüğü, kalınlığı, değiştirilir.
text4.pack()

text5 = tkinter.Label(window,text="New Text",font="Roboto 20 bold")
text5.pack()

#----------------------------------

#! Pencereye giris ekleme:

entry = tkinter.Entry(background="green")
entry.pack()

def verial():
    text_on_screen.config(text=entry.get())  #? veri alma fornksiyonumuzu oluşturuyoruz. altındaki satirdaki kod aynı işe yarıyor.
    # text_on_screen["text"] = entry.get()

button = tkinter.Button(text="Verileri Al",fg="red",bg="green",command=verial)  #? veriyi almak için buton kullanıyoruz.
button.pack()

text_on_screen = tkinter.Label(text="veriler buraya gelecek.")  #? verileri yazacağımız yazı kısmını oluşturuyoruz.
text_on_screen.pack()

def sil():
    entry.delete(0,"end") #? entrynin içindeki yazıları silmek için kullanılan fonksiyon.

button_sil = tkinter.Button(text="Verileri Sil",fg="green",bg="red",command=sil) #? verileri silme komutunu veren buton.
button_sil.pack()

#! Şifre giriş ekranı yapma:

entry2 = tkinter.Entry(background="green",show="*") #? show= komutu girilen karakterleri ekranda nasıl istersek öyle gösterir.
entry2.pack()

#----------------------------------

#! Pencereye buton ekleme ve konumlandırma:

def topla():
    pass

button = tkinter.Button(window,text="topla!",fg="white",bg="black",command=topla) #?renkli buton ekleme ve komut atama.
button.pack(side=tkinter.BOTTOM,fill=tkinter.X) #?butonun konumunu oluşturma ve doldurma.

button2 = tkinter.Button(window,text="test")
button2.pack(anchor="ne") #? "n" yukarı, "s" aşşağı, "e" sağ, "w" sol, "center" orta.

button3= tkinter.Button(window,text="hello")
button3.pack(padx="20",pady="100")  #? buton konumunu x ve y düzleminde değiştirme.
button3.pack(ipadx="30",ipady="20") #? buton büyüklüğünü x ve y düzleminde değiştirme.

button4 = tkinter.Button(window,text="This is a test.")
button4.place(x=150,y=40) #? butonumuzu ekrande herhangi yere x ve y düzleminde koymamızı sağlar. pencere boyutu değişince haraket etmez.

button5 = tkinter.Button(window,text="This is another test.")
button5.place(relx=0.3,rely=0.5) #? Butonu x ve y ekseninde orantısal olarak konumlandırma. Pencere boyutu değişirse, butonun konumunu değiştirir.

#----------------------------------

#! Pencereyi boyutlandırma ve renklendirme:

window.geometry("500x400+500+200") #? Genişlik X Yükseklik + Ekranda çıkacağı yerin kordinati (x+y)

window.minsize(300,300)  #? Minimum pencere boyutunu ayarlama.

window.maxsize(10000,100000)  #? Maxsimum pencere boyutunu ayarama.

window.resizable(False,False)  #? X ve Y eksenleri ile oynanıp oynanmamasını ayarlama.

window.state("normal") #? "pencere durumu normal/iconic/zoomed" olarak ayarlanabilir.

window.config(background="yellow") #? Pencereyi renklendirir.

#----------------------------------

#! Pencerede checkbutton oluşturma:

x = tkinter.IntVar()
x.set(0)

def kontrol():
    if x.get() == 0:
        print("Onaylanmadı!")
    else:
        print("Onaylandı!")

check = tkinter.Checkbutton(window,text="Onay",fg="pink",bg="aqua",variable=x,command=kontrol)
check.pack()

#----------------------------------

#! Radio Butonu Oluşturma:

def control():
    if x.get() == "1":
        print("Buton 1 seçildi.")
    elif x.get() == "2":
        print("Buton 2 seçildi.")
    else:
        print("Buton 1 ve 2 seçildi.")

button = tkinter.Button(window,text="Click",foreground="black",background="aqua",activebackground="green",command=control)
button.pack()

x = tkinter.StringVar()

radio1 = tkinter.Radiobutton(window,text="radio1",activebackground="red",value="1",variable=x)
radio1.pack()   

radio2 = tkinter.Radiobutton(window,text="radio2",activebackground="red",value="2",variable=x)
radio2.pack()  

#----------------------------------

#! Ekrana MessageBox Çıkartma:

from tkinter import messagebox #? Messagebox modülümüzü import etmemiz gerekiyor.

def message():
    messagebox.showinfo(title="Başlık",message="Bu bir mesaj!") #?  Ekrana başka pencere içinde mesaj çıkartır.
    messagebox.askretrycancel(title="Başlık2",message="Bu bir mesaj! ") #? Ekrana yeniden dene butonlu mesaj çıkartır.
    messagebox.askyesno(title="Başkık3",message="Bu bir mesaj!") #? Ekrana yes no butonlu mesaj çıkartır.
    messagebox.askquestion(title="Başlık4",message="Bu bir mesaj!") #? Ekrana yes no butonlu mesaj çıkartır.

button = tkinter.Button(window,text="Mesajı görmek için tıklayın.",command=message).pack()

#----------------------------------

#! ComboBox Oluşturma:

from tkinter.ttk import Combobox

sehirler = ["Ankara","İstanbul","Balıkesir","İzmir","Burdur"]
kutu = Combobox(window,values=sehirler,height=3) #? values=("1","2","3") şeklinde liste kullanmadan yazılabilir.
kutu.pack() 
#? height= ilk olarak gözükecek değer sayısıdır.
#? Kutudaki değeri almak için "kutu.pack()" ayrı satırda yazıldıktan sonra "kutu.get" kullanılır.

#----------------------------------

#! SpinBox Oluşturma:

spin = tkinter.Spinbox(from_=10,to=100)
spin.pack()

#----------------------------------

#! Pencereyi çalıştırma: 

tkinter.mainloop() #? Penceremizi döngüye sokarak her zaman ekranda kalmasını sağlar.
