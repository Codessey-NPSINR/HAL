import customtkinter as Ctk
from PIL import Image, ImageTk

def create_image(image_path):
    img=Image.open(image_path)
    photo=ImageTk.PhotoImage(img)
    return photo


def destroy():
    for widget in window.winfo_children():
        widget.destroy()


def login_page():
    destroy()
    def login():
        destroy()
        bg2=create_image(r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\login_background.png")
        bg=Ctk.CTkLabel(window,text="",image=bg2)
        bg.place(x=0,y=0)
        login3=create_image(r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\login_btn.png")
        login_btn2=Ctk.CTkButton(window,text="",image=login3,command=lambda:print("login,to the csv file"))
        login_btn2.place(x=480,y=580)
        entry1=Ctk.CTkEntry(window,placeholder_text="Username",height=54,width=650,fg_color="white",placeholder_text_color="black",text_color="black")
        entry1.place(x=420,y=250)
        entry2=Ctk.CTkEntry(window,placeholder_text="Password",height=54,width=650,fg_color="white",placeholder_text_color="black",text_color="black")
        entry2.place(x=420,y=350)
        entry3=Ctk.CTkEntry(window,placeholder_text="Captcha",height=54,width=388,fg_color="white",placeholder_text_color="black",text_color="black")
        entry3.place(x=680,y=450)
        captcha=create_image(r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\captcha.png")
        captcha1=Ctk.CTkLabel(window,text="",image=captcha)
        captcha1.place(x=375,y=450)
        
    def sign_up():
        
        destroy()

        def next_signup():
            destroy()

            def sending_verification_code():
                pass

            
            def typeuser(choice):
                destroy()
                if choice=="User":
                    
                    def find_home():
                        pass

                    def find_services():
                        pass

                    def look_for_community():
                        pass

                    def contribute_to_ngo():
                        pass
                    
                    bg2=create_image(r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\user_page.jpg")
                    bg=Ctk.CTkLabel(window,text="",image=bg2)
                    bg.place(x=0,y=0)
                    img5=create_image(r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\find_home_btn.png")
                    find_home_btn=Ctk.CTkButton(window,text="",image=img5,command=lambda:find_home())
                    find_home_btn.place(x=15,y=550)
                    img6=create_image(r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\services_btn.png")
                    services_btn=Ctk.CTkButton(window,text="",image=img6,command=lambda:find_services())
                    services_btn.place(x=275,y=545)
                    img9=create_image(r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\community_btn.png")
                    community_btn=Ctk.CTkButton(window,text="",image=img9,command=lambda:look_for_community())
                    community_btn.place(x=590,y=550)
                    img10=create_image(r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\contribute_btn.png")
                    contribute_btn=Ctk.CTkButton(window,text="",image=img10,command=lambda:contribute_to_ngo())
                    contribute_btn.place(x=910,y=538)
                    
                elif choice=="NGO":
                    def underpriviledged():
                        pass
                    
                    def disabled():
                        pass
                    
                    bg2=create_image(r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\ngo_bg.png")
                    bg=Ctk.CTkLabel(window,text="",image=bg2)
                    bg.place(x=0,y=0)
                    img13=create_image(r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\help_underpriviledged_btn.png")
                    underpriviledged_btn=Ctk.CTkButton(window,text="",image=img13,command=lambda:underpriviledged())
                    underpriviledged_btn.place(x=45,y=480)
                    img14=create_image(r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\help_disabled_btn.png")
                    disabled_btn=Ctk.CTkButton(window,text="",image=img14,command=lambda:disabled())
                    disabled_btn.place(x=700,y=460)
                    
                elif choice=="Management":
                    #waste page has to be made again
                    #get the coordinates fixed,after that is donee...
                    def waste():
                        pass


                    bg2=create_image(r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\waste_management_bg.png")
                    bg=Ctk.CTkLabel(window,text="",image=bg2)
                    bg.place(x=0,y=0)
                    img11=create_image(r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\waste_btn.png")
                    waste_btn=Ctk.CTkButton(window,text="",image=img11,command=lambda:waste())
                    waste_btn.place(x=300,y=580)
                    
                elif choice=="Services":
                    pass
                
            bg2=create_image(r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\signup_2bg.png")
            bg=Ctk.CTkLabel(window,text="",image=bg2)
            bg.place(x=0,y=0)
            signup2=create_image(r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\signup_btn_img2.png")
            signup_btn2=Ctk.CTkButton(window,text="",image=signup2,command=lambda:print("it,finally signs up"))
            signup_btn2.place(x=445,y=550)
            entry=Ctk.CTkEntry(window,placeholder_text="Phone No",height=54,width=585,fg_color="white",placeholder_text_color="black",text_color="black")
            entry.place(x=530,y=225)
            verification=Ctk.CTkEntry(window,placeholder_text="Verification Code:",height=54,width=388,fg_color="white",placeholder_text_color="black",text_color="black")
            verification.place(x=680,y=320)
            send_verify=Ctk.CTkButton(window,text="Send Verification Code",command=lambda:sending_verification_code())
            send_verify.place(x=500,y=320)
            option_var=Ctk.StringVar(value="User")
            optionmenu=Ctk.CTkOptionMenu(window,dropdown_hover_color="black",dropdown_fg_color="black",button_hover_color="black",values=["User","NGO","Management","Services"],height=54,width=585,command=typeuser,variable=option_var)
            optionmenu.place(x=530,y=400)
            
            
            
        
        bg2=create_image(r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\signup_1bg.png")
        bg=Ctk.CTkLabel(window,text="",image=bg2)
        bg.place(x=0,y=0)
        next1=create_image(r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\next_btn_img.png")
        next_btn=Ctk.CTkButton(window,text="",image=next1,command=lambda:next_signup())
        next_btn.place(x=450,y=580)
        entry=Ctk.CTkEntry(window,placeholder_text="Email",height=54,width=760,fg_color="white",placeholder_text_color="black",text_color="black")
        entry.place(x=310,y=190)
        entry1=Ctk.CTkEntry(window,placeholder_text="Username",height=54,width=650,fg_color="white",placeholder_text_color="black",text_color="black")
        entry1.place(x=420,y=270)
        entry2=Ctk.CTkEntry(window,placeholder_text="Password",height=54,width=650,fg_color="white",placeholder_text_color="black",text_color="black")
        entry2.place(x=420,y=360)
        entry3=Ctk.CTkEntry(window,placeholder_text="Captcha",height=54,width=200,fg_color="white",placeholder_text_color="black",text_color="black")
        entry3.place(x=680,y=450)
        captcha=create_image(r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\captcha.png")
        captcha1=Ctk.CTkLabel(window,text="",image=captcha)
        captcha1.place(x=370,y=450)
        captcha_submit=Ctk.CTkButton(window,text="Submit",width=140,height=54,command=lambda:submit())
        captcha_submit.place(x=930,y=450)

        
    bg2=create_image(r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\login_page_bg.png")
    bg=Ctk.CTkLabel(window,text="",image=bg2)
    bg.place(x=0,y=0)
    login_btn=create_image(r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\Login.jpeg")
    button1=Ctk.CTkButton(window,text="",image=login_btn,command=lambda:login())
    button1.place(x=65,y=105)
    signup=create_image(r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\Sign_up.jpeg")
    button2=Ctk.CTkButton(window,text="",image=signup,command=lambda:sign_up())
    button2.place(x=685,y=428)
    
        
Ctk.set_appearance_mode("Dark")

window=Ctk.CTk()
window.geometry("1200x700")
image_path=r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\homepage.png"
img = Image.open(image_path)
photo = ImageTk.PhotoImage(img)
label =Ctk.CTkLabel(window,text="",image=photo)
label.place(x=0,y=0)
logo_img=r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\home_button(1).jpeg"
img1=Image.open(logo_img)
bg=ImageTk.PhotoImage(img1)
button1=Ctk.CTkButton(window,text="",image=bg,command=lambda:login_page())
button1.place(x=420,y=100)
utopia=r"C:\Users\SweetHome\Desktop\spandan\NPSHack\Codessey2023\tkinter3\images\utopia.png"
img2=Image.open(utopia)
home_text=ImageTk.PhotoImage(img2)
home_text1=Ctk.CTkButton(window,text="",border_color="gray100",image=home_text,command=lambda:login_page())
home_text1.place(x=320,y=460)


window.mainloop()
