from tkinter import messagebox, ttk
import customtkinter
from tkinter import *
from PIL import ImageTk, Image
from app.libs.admin_libs import Admin_Libs
from app.dbms.admin_login import adminLogin
from app.admin import admin_dashboard

class Login(customtkinter.CTk):
    def __init__(self, root):
        self.root=root
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
        self.root.screen_width=root.winfo_screenwidth()
        self.root.screen_height=root.winfo_screenheight()
        self.root.minsize(self.root.screen_width, self.root.screen_height)
        self.root.state('zoomed')
        self.root.title("LC Security Login")

        self.root.bind('<Escape>', lambda e: root.destroy())

        # -----------------------------Font------------------------------------------
        font1 = customtkinter.CTkFont(family='Times New Roman', size=20, weight='normal')

        # -----------------------------Top Frame------------------------------------------
        north_frame = customtkinter.CTkFrame(master=root, height=100)
        north_frame.pack(side=TOP, fill=BOTH)

        # -----------------------------Top frame title------------------------------------------
        title_label = customtkinter.CTkLabel(master=north_frame, text="LC Security SYSTEM", font=('Times New Roman', 35, 'bold'))
        title_label.place(x=650, y=40)

        # -----------------------------Top frame Left frame------------------------------------------
        frame1 = customtkinter.CTkFrame(master=root, width=400, height=400, corner_radius=20)
        frame1.pack(side=LEFT, padx=20)

        # -----------------------------Left frame image------------------------------------------
        canvas = Canvas(frame1, width=900, height=900, bg="#212325", borderwidth=0, bd=0, highlightthickness=0)
        image=ImageTk.PhotoImage(Image.open("image/Tablet login-rafiki.png"))
        canvas.create_image(120, 120, image=image)
        canvas.pack()

        # -----------------------------Login image sign in image------------------------------------------
        Cover_Image = Image.open('image/Tablet login-rafiki.png')
        photo1 = ImageTk.PhotoImage(Cover_Image)
        Cover_Image_label = Label(frame1, image=photo1, bg="#212325")
        Cover_Image_label.image = photo1
        Cover_Image_label.place(x=10, y=0)

        # frame2 = customtkinter.CTkFrame(master=root, width=750, height=600, corner_radius=20)
        # frame2.pack(side=RIGHT, padx=30)

        # -----------------------------Signin and create account tab------------------------------------------
        parent_tab=customtkinter.CTkTabview(self.root, width=750, height=600)
        parent_tab.pack(side=RIGHT, padx=30)

        parent_tab.add('Sign In')

        # -----------------------------Image------------------------------------------
        sign_in_image = Image.open('image/hyy.png')
        photo = ImageTk.PhotoImage(sign_in_image)
        sign_in_image_label = Label(master=parent_tab.tab('Sign In'), image=photo, bg="#2b2b2b")
        sign_in_image_label.image = photo
        sign_in_image_label.place(x=380, y=40)

        # -----------------------------Signin label------------------------------------------
        signin_lbl = customtkinter.CTkLabel(master=parent_tab.tab('Sign In'), text="Sign In", font=font1)
        signin_lbl.place(x=330, y=150)

        # -----------------------------Email label------------------------------------------
        email_lbl = customtkinter.CTkLabel(master=parent_tab.tab('Sign In'), text="Email: ", font=font1)
        email_lbl.place(x=200, y=205)
        # -----------------------------Email textfield------------------------------------------
        email_txt1 = customtkinter.CTkEntry(master=parent_tab.tab('Sign In'), corner_radius=10, font=font1, width=200)
        email_txt1.place(x=330, y=200)

        # -----------------------------Password Label------------------------------------------
        password_lbl = customtkinter.CTkLabel(master=parent_tab.tab('Sign In'), text="Password: ", font=font1)
        password_lbl.place(x=200, y=255)

        # -----------------------------Show password function------------------------------------------
        def show_password():
            if i.get()==1:
                password_txt1.configure(show='')
            else:
                password_txt1.configure(show='*')

        i=customtkinter.IntVar()

        # -----------------------------Password Entry Widget------------------------------------------
        password_txt1 = customtkinter.CTkEntry(master=parent_tab.tab('Sign In'), show="*", corner_radius=10, font=font1, width=200)
        password_txt1.place(x=330, y=250)

        # -----------------------------Sow password checkbox widget------------------------------------------
        password_show = customtkinter.CTkCheckBox(master=parent_tab.tab('Sign In'), text="Show password", variable=i, command=show_password)
        password_show.place(x=330, y=290)

        # ----------------------------admin login function------------------------------------------
        def login_admin():
            # Tạo đối tượng Admin_Libs từ dữ liệu nhập vào
            login720 = Admin_Libs(email=email_txt1.get(), password=password_txt1.get())

            # Kiểm tra xem email hoặc mật khẩu có trống không
            if email_txt1.get() == "" or password_txt1.get() == "":
                messagebox.showerror("LC Security SYSTEM", "Please enter email and password!")
            else:
                adminresult = adminLogin(login720)  # Gọi hàm kiểm tra đăng nhập

                if adminresult is not None:  # Nếu đăng nhập thành công
                    self.root.destroy()  # Đóng cửa sổ hiện tại
                    root = customtkinter.CTk()  # Tạo cửa sổ mới
                    admin_dashboard.Admin_Dashboard(root)  # Mở bảng điều khiển
                    root.mainloop()  # Bắt đầu vòng lặp chính
                else:  # Nếu đăng nhập thất bại
                    messagebox.showerror("LC Security SYSTEM", "Incorrect email and password!")

        #-----------------------------Login Button------------------------------------------
        add_login_image = customtkinter.CTkImage(light_image=Image.open("image/login.png").resize((50, 50)))
        button = customtkinter.CTkButton(master=parent_tab.tab('Sign In'),command=login_admin, text="Login", image=add_login_image,
                                         corner_radius=10,
                                         text_color="white", font=('',18, 'bold'), hover_color="black")
        button.place(x=340, y=350)

        signup_lbl = customtkinter.CTkLabel(master=parent_tab.tab('Sign In'), text="No account yet")
        signup_lbl.place(x=320, y=420)

        # -----------------------------Signup GUI function------------------------------------------
        def signup():
            self.root.destroy()
            root=customtkinter.CTk()

            root.mainloop()

        signup_btn = customtkinter.CTkButton(master=parent_tab.tab('Sign In'), text="SIGN UP NOW", width=50, height=20,
                                             hover_color="black", command=signup)


        signup_btn.place(x=410, y=420)

        parent_tab.add('Sign Up')

        # -----------------------------Signup Frmae------------------------------------------
        signupframe=customtkinter.CTkFrame(master=parent_tab.tab('Sign Up'), height=70,)
        signupframe.pack(side=TOP, fill=BOTH, pady=(20,0))

        signuptitle=customtkinter.CTkLabel(master=signupframe, text="CUSTOMER REGISTRATION FORM", font=('Times New Roman',20, 'bold'))
        signuptitle.place(x=200, y=20)

        # ===========================All Variables===========
        self.name_txt = StringVar()
        self.mobile_txt = StringVar()
        self.gender_txt = StringVar()
        self.email_txt = StringVar()
        self.address_txt = StringVar()
        self.password_txt = StringVar()
        self.credit_txt = StringVar()

        # -----------------------------Name Label------------------------------------------
        name_lbl = customtkinter.CTkLabel(parent_tab.tab('Sign Up'), text="Name: ",font=font1)
        name_lbl.place(x=20, y=150)

        # -----------------------------Name Entry Widget------------------------------------------
        name_txt = customtkinter.CTkEntry(parent_tab.tab('Sign Up'), font=font1,width=200)
        name_txt.configure(textvariable=self.name_txt)
        name_txt.place(x=110, y=150)




        # -----------------------------Gender Label Widget------------------------------------------
        gender_lbl = customtkinter.CTkLabel(parent_tab.tab('Sign Up'), text="Gender: ", font=font1)
        gender_lbl.place(x=20, y=200)

        # -----------------------------Gender Optionmenu Widget------------------------------------------
        gender_txt = customtkinter.CTkOptionMenu(master=parent_tab.tab('Sign Up'),  variable=self.gender_txt,values=['Male', 'Female', 'Others'], font=font1, width=200)
        gender_txt.set('Male')
        gender_txt.place(x=110, y=200)

        # -----------------------------Password Label------------------------------------------
        password_lbl = customtkinter.CTkLabel(parent_tab.tab('Sign Up'), text="Password: ",font=font1)
        password_lbl.place(x=20, y=250)

        # -----------------------------Password Entry------------------------------------------
        password_txt = customtkinter.CTkEntry(master=parent_tab.tab('Sign Up'), font=font1, width=200)
        password_txt.configure(textvariable=self.password_txt)
        password_txt.place(x=110, y=250)

        # -----------------------------Mobile Label------------------------------------------
        mobile_lbl = customtkinter.CTkLabel(parent_tab.tab('Sign Up'), text="Mobile: ", font=font1)
        mobile_lbl.place(x=400, y=150)

        # -----------------------------Mobile Entry------------------------------------------
        mobile_txt = customtkinter.CTkEntry(master=parent_tab.tab('Sign Up'), font=font1,width=200)
        mobile_txt.configure(textvariable=self.mobile_txt)
        mobile_txt.place(x=480, y=150)

        # -----------------------------Address Label------------------------------------------
        address_lbl = customtkinter.CTkLabel(parent_tab.tab('Sign Up'), text="Address: ",font=font1)
        address_lbl.place(x=400, y=200)

        # -----------------------------Address Entry------------------------------------------
        address_txt = customtkinter.CTkEntry(master=parent_tab.tab('Sign Up'), font=font1, width=200)
        address_txt.configure(textvariable=self.address_txt)
        address_txt.place(x=480, y=200)

        # -----------------------------Email Label------------------------------------------
        email_lbl = customtkinter.CTkLabel(parent_tab.tab('Sign Up'), text="Email: ",font=font1)
        email_lbl.place(x=400, y=250)

        # -----------------------------Email Entry------------------------------------------
        email_txt = customtkinter.CTkEntry(master=parent_tab.tab('Sign Up'),font=font1,width=200)
        email_txt.configure(textvariable=self.email_txt)
        email_txt.place(x=480, y=250)







        # -----------------------------Rehistration button------------------------------------------
        register_btn_image = customtkinter.CTkImage(light_image=Image.open("image/edit.png"))
        register_btn = customtkinter.CTkButton(master=parent_tab.tab('Sign Up'), text="Register",image=register_btn_image,hover_color='black', font=('Tahoma', 20, 'bold'))
        register_btn.place(x=150, y=400)

        # -----------------------------Clear entry field------------------------------------------
        def clear():
            self.name_txt.set('')
            self.mobile_txt.set('')
            self.gender_txt.set('')
            self.address_txt.set('')
            self.password_txt.set('')
            self.email_txt.set('')

            if (name_txt.get()=='') or (mobile_txt.get()=='')  or \
               (address_txt.get()=='') or (password_txt.get()=='') or \
                (email_txt.get()==''):
                msg1=messagebox.showinfo("Taxi Booking System","All fields are cleared!")

            else:
                msg2=messagebox.showerror("Error!","Error ocurred!")

        # -----------------------------Clear Button------------------------------------------
        clear_btn_image = customtkinter.CTkImage(light_image=Image.open("image/cleaning.png"))
        clear_btn = customtkinter.CTkButton(master=parent_tab.tab('Sign Up'),command=clear,  text="Clear", image=clear_btn_image,hover_color='black', font=('Tahoma', 20, 'bold'))
        clear_btn.place(x=300, y=400)



if __name__ == '__main__':
    root = customtkinter.CTk()
    Login(root)
    root.mainloop()