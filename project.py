from PIL import Image
import customtkinter
import datetime
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import random
import threading
from ensta import Mobile as Host


def calcTime():
    license_over_date_day = 7
    license_over_date_month = 7
    license_over_date_year = 2025

    current_year = datetime.date.today().year
    current_month = datetime.date.today().month
    current_day = datetime.date.today().day

    if current_month < 10:
        current_month_str = "0" + str(current_month)
    else:
        current_month_str = str(current_month)

    if current_day < 10:
        current_day_str = "0" + str(current_day)
    else:
        current_day_str = str(current_day)

    current_date_str = f"{current_year}-{current_month_str}-{current_day_str}"
    license_over_date_str = f"{license_over_date_year}-{license_over_date_month:02d}-{license_over_date_day:02d}"

    current_date = datetime.datetime.strptime(current_date_str, "%Y-%m-%d").date()
    license_over_date = datetime.datetime.strptime(license_over_date_str, "%Y-%m-%d").date()

    remaining_days = (license_over_date - current_date).days

    return remaining_days

emergency_exit_signin = 0

def signIn(tried_sign_in):

    def on_close():
        global emergency_exit_signin
        emergency_exit_signin = 1
        app.destroy()


    def save_inputs():
        global username,password
        username = entry_1.get()
        password = entry_2.get()
        app.destroy()


    app = customtkinter.CTk()
    app.geometry("600x400")
    app.title("Sosyal Medya Yazılımı")
    
    app.protocol("WM_DELETE_WINDOW", on_close)


    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    xforapp = (screen_width - 600) / 2
    yforapp = (screen_height - 400) / 2


    app.geometry("+%d+%d" % (xforapp, yforapp))



    frame = customtkinter.CTkFrame(master=app)
    frame.pack(pady=20,padx=60,fill="both",expand=True)


    space_label = customtkinter.CTkLabel(frame, text="", height=50)
    space_label.pack()

    img = customtkinter.CTkImage(dark_image=Image.open(r'assets/instagram.png'), size=(75,75))

    lab = customtkinter.CTkLabel(frame,image=img,text="")
    lab.pack()
    
    space_label = customtkinter.CTkLabel(frame, text="", height=30)
    space_label.pack()

    entry_1 = customtkinter.CTkEntry(master = frame, placeholder_text="Kullanıcı adı", width=200)
    entry_1.pack(pady=10, padx=10)

    entry_2 = customtkinter.CTkEntry(master = frame, placeholder_text="Şifre", width=200, show="*")
    entry_2.pack(pady=10, padx=10)

    if tried_sign_in==1:
        label_not_signed = customtkinter.CTkLabel(master = frame, text="Giriş yapılamadı. Tekrar deneyin!", text_color="#CF3626")
        label_not_signed.pack()

    button_1 = customtkinter.CTkButton(master=frame, text="Giriş Yap", command=save_inputs)
    button_1.pack(pady=12, padx=10)

    label_infos = customtkinter.CTkLabel(
        master=app,
        text=f"Lisansınızın bitmesine {calcTime()} gün kaldı.")
    label_infos.pack(side="bottom")

    app.mainloop()

def liveTime():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S - %d/%m/%Y")
    return current_time




class Instagram:

    def __init__(self,username,password):

        self.username = username
        self.password = password



        self.users_for_liking = []
        self.users_post_id_liking = {}
        self.users_text_for_liking = """"""
        self.process_time_liking_min = 45
        self.process_time_liking_max = 60
        self.time_stop_num_process_liking = 25
        self.quantity_like_of_user = 4
        self.time_stop_process_waiting_liking = 1250
        self.process_summary_liking = """"""
        self.value_of_liking_switch = "off"
        self.is_like_started = 0

        self.users_for_not_unfollowing = []
        self.users_text_for_unfollowing = """"""
        self.process_time_unfollowing_min = 25
        self.process_time_unfollowing_max = 45
        self.time_stop_num_process_unfollowing = 25
        self.time_stop_process_waiting_unfollowing = 950
        self.process_summary_unfollowing = """"""
        self.value_of_unfollowing_switch = "off"
        self.is_unfollow_started = 0

        self.users_for_following = []
        self.users_post_id_following = {}
        self.users_text_for_following = """"""
        self.process_time_following_min = 25
        self.process_time_following_max = 45
        self.time_stop_num_process_following = 25
        self.quantity_follow_of_user = 80
        self.time_stop_process_waiting_following = 950
        self.process_summary_following = """"""
        self.value_of_following_switch = "off"
        self.is_follow_started = 0

        self.process_summary_all = """"""

        self.emergency_exit_liking = 0
        self.emergency_exit_following = 0
        self.emergency_exit_unfollowing = 0
        self.emergency_exit_updateinfos = 0



    def signIn(self):

        try:
            self.host = Host(self.username,self.password)
            profil = self.host.profile(self.username)
            self.num_of_follow = profil.following_count
            self.num_of_follower = profil.follower_count

            return 1
        except:
            return 0


    def processesUi(self):

        def on_close():
            self.value_of_following_switch = "off"
            self.value_of_unfollowing_switch = "off"
            self.value_of_liking_switch = "off"

            self.emergency_exit_following = 1
            self.emergency_exit_unfollowing = 1
            self.emergency_exit_liking = 1
            self.emergency_exit_updateinfos = 1
            app_processes.destroy()


        app_processes = customtkinter.CTk()
        app_processes.geometry("900x600")
        app_processes.title("Sosyal Medya Yazılımı")

        app_processes.protocol("WM_DELETE_WINDOW", on_close)

        screen_width = app_processes.winfo_screenwidth()
        screen_height = app_processes.winfo_screenheight()
        xforapp = (screen_width - 900) / 2
        yforapp = (screen_height - 600) / 2


        app_processes.geometry("+%d+%d" % (xforapp, yforapp))

        frame = customtkinter.CTkScrollableFrame(master=app_processes)
        frame.pack(pady=20,padx=60,fill="both",expand=True)

        
        space_label = customtkinter.CTkLabel(frame, text="", height=20)
        space_label.pack()

        label_username_text = customtkinter.CTkLabel(master=frame, text=f"{self.username}", font=("Roboto", 24))
        label_username_text.pack()

        space_label = customtkinter.CTkLabel(frame, text="", height=20)
        space_label.pack()

        self.label_follow_text = customtkinter.CTkLabel(master=frame, text=f"{self.num_of_follower} Takipçi   {self.num_of_follow} Takip", font=("Roboto", 24))
        self.label_follow_text.pack()

        space_label = customtkinter.CTkLabel(frame, text="", height=30)
        space_label.pack()
        
        frame_2 = customtkinter.CTkFrame(master=frame, width=500, fg_color="#333333")
        frame_2.pack(pady=20,padx=60)

        label_process_text = customtkinter.CTkLabel(master=frame_2, text=f"İşlemler", font=("Roboto", 22), width=400,fg_color="#2B2B2B", height=40)
        label_process_text.pack()

        space_label = customtkinter.CTkLabel(frame_2, text="", height=20)
        space_label.pack()


        button_1 = customtkinter.CTkButton(master=frame_2, text="Takip Etme", font=("Roboto", 18), command=self.followUi, height=35, width=150)
        button_1.pack(pady=20, padx=18)

        button_2 = customtkinter.CTkButton(master=frame_2, text="Takipten Çıkma", font=("Roboto", 18),command=self.unfollowUi, height=35, width=150)
        button_2.pack(pady=20, padx=18)

        button_3 = customtkinter.CTkButton(master=frame_2, text="Beğeni", font=("Roboto", 18),command=self.likingUi, height=35, width=150)
        button_3.pack(pady=20, padx=18)

        space_label = customtkinter.CTkLabel(frame_2, text="", height=30)
        space_label.pack()


        frame_summary = customtkinter.CTkScrollableFrame(master=frame, fg_color="#333333", width=500)
        frame_summary.pack(pady=0,padx=20,fill="both",expand=True)

        label_summary_text = customtkinter.CTkLabel(master=frame_summary, text=f"İşlem Özeti", font=("Roboto", 14),fg_color="#2B2B2B", width=1000)
        label_summary_text.pack()

        space_label = customtkinter.CTkLabel(frame_summary, text="", height=20)
        space_label.pack()

        self.label_process_summary_text_all = customtkinter.CTkLabel(master=frame_summary, text=f"{self.process_summary_all}", font=("Roboto", 12))
        self.label_process_summary_text_all.pack()

        space_label = customtkinter.CTkLabel(frame, text="", height=30)
        space_label.pack()


        self.label_infos = customtkinter.CTkLabel(master=app_processes, text=f"Lisansınızın bitmesine {calcTime()} gün kaldı.")
        self.label_infos.pack(side="bottom")

        app_processes.mainloop()

    
    def likingUi(self):

        def addUsers():
            self.users_text_for_liking = """"""
            users_temp = []
            dialog = customtkinter.CTkInputDialog(text="Kullanıcı adı giriniz.", title="Kullanıcı girme")
            users_text_temp = dialog.get_input()
            users_temp.extend(users_text_temp.split(','))
            
            for user in users_temp:
                if user in self.users_for_liking:
                    self.users_for_liking.remove(user)
                    del self.users_post_id_liking[user]
                else:
                    self.users_for_liking.append(user)
                    self.users_post_id_liking[user] = []
            for x in range(len(self.users_for_liking)):
                self.users_text_for_liking+=self.users_for_liking[x]+"\n"

            if user:
                users_label.configure(text=self.users_text_for_liking)


        def changeSettings():
            input_1 = customtkinter.CTkInputDialog(  text="İşlem süresi giriniz.\nÖrnek: 10-25", title="Ayarlar")
            process_time_temp = input_1.get_input()
            if process_time_temp:
                process_time_liking_min_temp, process_time_liking_max_temp = process_time_temp.split('-')
                self.process_time_liking_min = int(process_time_liking_min_temp)
                self.process_time_liking_max = int(process_time_liking_max_temp)
                label_process_time_text.configure(text=f"İşlem süresi {self.process_time_liking_min} ile {self.process_time_liking_max} saniye arası")

            input_2 = customtkinter.CTkInputDialog(text="İşlem ve bekleme süresi giriniz.\nÖrnek: 35-900", title="Ayarlar")
            process_waiting_time_temp = input_2.get_input()

            if process_waiting_time_temp:
                time_stop_num_process_temp, time_stop_process_waiting_temp = process_waiting_time_temp.split('-')
                self.time_stop_num_process_liking = int(time_stop_num_process_temp)
                self.time_stop_process_waiting_liking = int(time_stop_process_waiting_temp)
                label_process_waiting_time_text.configure(text=f"Her {self.time_stop_num_process_liking} işlemde {self.time_stop_process_waiting_liking} saniye bekle")

            input_3 = customtkinter.CTkInputDialog(text="Kaç gönderi beğenilsin.\nMinimum 4 olmalıdır.", title="Ayarlar")
            quantity_user_like_temp = input_3.get_input()

            if quantity_user_like_temp:
                self.quantity_like_of_user = int(quantity_user_like_temp)
                label_quantity_like_of_user_text.configure(text=f"Son {self.quantity_like_of_user} gönderiyi beğen")

        def saveUsers():
            self.app_liking.withdraw()

        def switcherLiking():
            self.value_of_liking_switch = self.liking_process_start.get()
            if self.value_of_liking_switch == "on" and self.is_like_started == 0:
                self.is_like_started = 1
                thread1.start()

        def reopenWindow():
            self.app_liking.deiconify()
                

        
        if self.is_like_started==0:
            
            self.app_liking = customtkinter.CTkToplevel()
            self.app_liking.geometry("900x600")
            self.app_liking.title(f"{self.username}")

            self.app_liking.protocol("WM_DELETE_WINDOW", saveUsers)

            screen_width = self.app_liking.winfo_screenwidth()
            screen_height = self.app_liking.winfo_screenheight()
            xforapp = (screen_width - 900) / 2
            yforapp = (screen_height - 600) / 2

            self.app_liking.geometry("+%d+%d" % (xforapp, yforapp))


            
            frame_master = customtkinter.CTkScrollableFrame(master=self.app_liking)
            frame_master.pack(pady=20,padx=60,fill="both",expand=True)
            
            frame = customtkinter.CTkFrame(master=frame_master)
            frame.pack(pady=20,padx=60,fill="both",expand=True)

            frame_2 = customtkinter.CTkFrame(master=frame_master)
            frame_2.pack(pady=20,padx=60,fill="both",expand=True)


            space_label = customtkinter.CTkLabel(frame, text="", height=20)
            space_label.pack()


            label_follow_text = customtkinter.CTkLabel(master=frame, text=f"Beğeni Ayarları", font=("Roboto", 24))
            label_follow_text.pack()

            self.liking_process_start = customtkinter.StringVar(value=self.value_of_liking_switch)
            liking_switch = customtkinter.CTkSwitch(master=frame, text="Kontrol Düğmesi", command=switcherLiking, variable=self.liking_process_start, onvalue="on", offvalue="off")
            liking_switch.pack(pady=5)

            space_label = customtkinter.CTkLabel(frame, text="", height=50)
            space_label.pack()

            frame_users_name = customtkinter.CTkScrollableFrame(master=frame, fg_color="#333333")
            frame_users_name.pack(side="left", pady=0,padx=20,fill="both",expand=True)

            label_users_text = customtkinter.CTkLabel(master=frame_users_name, text=f"Kullanıcı Adları", font=("Roboto", 14),fg_color="#2B2B2B", width=1000)
            label_users_text.pack()

            button_2 = customtkinter.CTkButton(master=frame_users_name, text="Ekle/Sil", font=("Roboto", 13), command=addUsers, width=18)
            button_2.pack(pady=12, padx=2)

            users_label = customtkinter.CTkLabel(master=frame_users_name,text=f"{self.users_text_for_liking}", font=("Roboto", 12))
            users_label.pack(pady=10, padx=5)

            frame_settings = customtkinter.CTkScrollableFrame(master=frame, fg_color="#333333")
            frame_settings.pack(side="right", pady=0,padx=20,fill="both",expand=True)

            label_settings_text = customtkinter.CTkLabel(master=frame_settings, text=f"Ayarlar", font=("Roboto", 14),fg_color="#2B2B2B", width=1000)
            label_settings_text.pack()

            button_3 = customtkinter.CTkButton(master=frame_settings, text="Değiştir", font=("Roboto", 13), command=changeSettings, width=18)
            button_3.pack(pady=12, padx=2)

            space_label = customtkinter.CTkLabel(frame_settings, text="", height=20)
            space_label.pack()

            label_process_time_text = customtkinter.CTkLabel(master=frame_settings, text=f"İşlem süresi {self.process_time_liking_min} ile {self.process_time_liking_max} saniye arası", font=("Roboto", 15))
            label_process_time_text.pack()

            label_process_waiting_time_text = customtkinter.CTkLabel(master=frame_settings, text=f"Her {self.time_stop_num_process_liking} işlemde {self.time_stop_process_waiting_liking} saniye bekle", font=("Roboto", 15))
            label_process_waiting_time_text.pack()

            label_quantity_like_of_user_text = customtkinter.CTkLabel(master=frame_settings, text=f"Son {self.quantity_like_of_user} gönderiyi beğen", font=("Roboto", 15))
            label_quantity_like_of_user_text.pack()

            frame_summary = customtkinter.CTkScrollableFrame(master=frame_2, fg_color="#333333", width=500)
            frame_summary.pack(pady=0,padx=20,fill="both",expand=True)

            label_summary_text = customtkinter.CTkLabel(master=frame_summary, text=f"İşlem Özeti", font=("Roboto", 14),fg_color="#2B2B2B", width=1000)
            label_summary_text.pack()

            space_label = customtkinter.CTkLabel(frame_summary, text="", height=20)
            space_label.pack()

            self.label_process_summary_text_liking = customtkinter.CTkLabel(master=frame_summary, text=f"{self.process_summary_liking}", font=("Roboto", 12))
            self.label_process_summary_text_liking.pack()


            button_1 = customtkinter.CTkButton(master=self.app_liking, text="Kaydet", font=("Roboto", 20), command=saveUsers)
            button_1.pack(pady=18, padx=15)


            self.label_infos_liking = customtkinter.CTkLabel(master=self.app_liking, text=f"Lisansınızın bitmesine {calcTime()} gün kaldı.")
            self.label_infos_liking.pack(side="bottom")

        
        else:
            reopenWindow()


    def liking(self):


        while True:
            try:
                chrome_options = Options()
                chrome_options.add_argument("--headless")
                browser = webdriver.Chrome(options=chrome_options)
                browser.get("https://www.instagram.com")
                WebDriverWait(browser, 45).until(EC.presence_of_element_located((By.NAME, "username")))
                time.sleep(0.2)

                username_input = browser.find_element(By.NAME, "username")
                password_input = browser.find_element(By.NAME, "password")

                username_input.send_keys(self.username)
                time.sleep(0.1)
                password_input.send_keys(self.password)
                time.sleep(0.1)
                password_input.send_keys(Keys.ENTER)

                WebDriverWait(browser, 45).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button')))
                click_not_now = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
                click_not_now.click()

                counter_of_process = 0
                is_signed_before = 0
                break
            except:
                summary_text = f"{liveTime()} --> Beğeni ---> Spam algılandı. İşlemler 2 saat askıya alındı\n"
                self.process_summary_all = summary_text + self.process_summary_all
                self.label_process_summary_text_all.configure(text=self.process_summary_all)
                self.process_summary_liking = summary_text + self.process_summary_liking
                self.label_process_summary_text_liking.configure(text=self.process_summary_liking)
                counter = 0
                while counter<1440:
                    if self.emergency_exit_liking == 1 or self.value_of_liking_switch=="off":
                        break
                    time.sleep(5)
                    counter+=1
                if self.emergency_exit_liking == 1 or self.value_of_liking_switch=="off":
                        break

        while True:

            if self.emergency_exit_liking == 1:
                break

            while self.value_of_liking_switch=="on":
                if is_signed_before == 0:
                    summary_text = f"{liveTime()} --> Beğeni ---> İşlem başlatıldı\n"
                    self.process_summary_liking = summary_text + self.process_summary_liking
                    self.label_process_summary_text_liking.configure(text=self.process_summary_liking)
                    self.process_summary_all = summary_text + self.process_summary_all
                    self.label_process_summary_text_all.configure(text=self.process_summary_all)

                    is_signed_before = 1

                for user in self.users_for_liking:
                    
                    if self.value_of_liking_switch=="off":
                        break



                    browser.get(f"https://www.instagram.com/{user}")
                    post_id = []
                    is_posts_found = 0
                    counter_tried_find = 0
                    while is_posts_found == 0:

                        if counter_tried_find == 10:
                            break

                        try:
                            WebDriverWait(browser, 0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]')))
                            is_posts_found = 1
                            for column in range((self.quantity_like_of_user//3)+1):
                                if ((self.quantity_like_of_user//3)) == column:
                                    if self.quantity_like_of_user%3==0:
                                        for post in range(3):
                                            post_id.append(browser.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[3]/article/div[1]/div/div[{column+1}]/div[{post+1}]/a').get_attribute("href"))
                                        break
                                    else:
                                        for post in range(self.quantity_like_of_user%3):
                                            post_id.append(browser.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[3]/article/div[1]/div/div[{column+1}]/div[{post+1}]/a').get_attribute("href"))
                                        break
                                for post in range(3):
                                    post_id.append(browser.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[3]/article/div[1]/div/div[{column+1}]/div[{post+1}]/a').get_attribute("href"))
                            break
                        except:

                            try:
                                WebDriverWait(browser, 0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]')))
                                is_posts_found = 1
                                for column in range((self.quantity_like_of_user//3)+1):
                                    if ((self.quantity_like_of_user//3)) == column:
                                        if self.quantity_like_of_user%3==0:
                                            for post in range(3):
                                                post_id.append(browser.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[2]/article/div[1]/div/div[{column+1}]/div[{post+1}]/a').get_attribute("href"))
                                            break
                                        else:
                                            for post in range(self.quantity_like_of_user%3):
                                                post_id.append(browser.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[2]/article/div[1]/div/div[{column+1}]/div[{post+1}]/a').get_attribute("href"))
                                            break
                                    for post in range(3):
                                        post_id.append(browser.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[2]/article/div[1]/div/div[{column+1}]/div[{post+1}]/a').get_attribute("href"))
                                break
                            except:

                                try:
                                    WebDriverWait(browser, 0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[3]/div/div[1]/div[1]')))
                                    is_posts_found = 1
                                    for column in range((self.quantity_like_of_user//3)+1):
                                        if ((self.quantity_like_of_user//3)) == column:
                                            if self.quantity_like_of_user%3==0:
                                                for post in range(3):
                                                    post_id.append(browser.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[3]/div/div[{column+1}]/div[{post+1}]/a').get_attribute("href"))
                                                break
                                            else:
                                                for post in range(self.quantity_like_of_user%3):
                                                    post_id.append(browser.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[3]/div/div[{column+1}]/div[{post+1}]/a').get_attribute("href"))
                                                break
                                        for post in range(3):
                                            post_id.append(browser.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[3]/div/div[{column+1}]/div[{post+1}]/a').get_attribute("href"))
                                    break
                                except:

                                    try:
                                        WebDriverWait(browser, 0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[2]/div/div[1]/div[1]')))
                                        is_posts_found = 1
                                        for column in range((self.quantity_like_of_user//3)+1):
                                            if ((self.quantity_like_of_user//3)) == column:
                                                if self.quantity_like_of_user%3==0:
                                                    for post in range(3):
                                                        post_id.append(browser.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[2]/div/div[{column+1}]/div[{post+1}]/a').get_attribute("href"))
                                                    break
                                                else:
                                                    for post in range(self.quantity_like_of_user%3):
                                                        post_id.append(browser.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[2]/div/div[{column+1}]/div[{post+1}]/a').get_attribute("href"))
                                                    break
                                            for post in range(3):
                                                post_id.append(browser.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[2]/div/div[{column+1}]/div[{post+1}]/a').get_attribute("href"))
                                        break
                                    except:
                                        counter_tried_find += 1

                    if is_posts_found == 1:
                        for post_number in range(self.quantity_like_of_user):
                            if self.value_of_liking_switch=="off":
                                break
                            try:
                                if post_id[post_number] not in self.users_post_id_liking[user]:
                                    self.users_post_id_liking[user].append(post_id[post_number])

                                    browser.get(f"{post_id[post_number]}")
                                    WebDriverWait(browser, 45).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[3]/div[1]/div[1]/span[2]')))

                                    browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[3]/div[1]/div[1]/span[1]/div/div').click()

                                    summary_text = f"{liveTime()} --> Beğeni ---> {user} kullanıcısının gönderisi beğenildi\n"
                                    self.process_summary_liking = summary_text + self.process_summary_liking
                                    while (self.process_summary_liking.count('\n') + 1) > 100:
                                        lines = self.process_summary_liking.splitlines()
                                        if lines:
                                            lines.pop()
                                        self.process_summary_liking = '\n'.join(lines)
                                    self.label_process_summary_text_liking.configure(text=self.process_summary_liking)
                                    self.process_summary_all = summary_text + self.process_summary_all
                                    self.label_process_summary_text_all.configure(text=self.process_summary_all)

                                    counter_of_process+=1

                                    

                                    if counter_of_process == self.time_stop_num_process_liking:
                                        summary_text = f"{liveTime()} --> Beğeni ---> {self.time_stop_process_waiting_liking} saniye bekleniyor\n"
                                        self.process_summary_liking = summary_text + self.process_summary_liking
                                        self.label_process_summary_text_liking.configure(text=self.process_summary_liking)
                                        self.process_summary_all = summary_text + self.process_summary_all
                                        self.label_process_summary_text_all.configure(text=self.process_summary_all)
                                        
                                        counter = 0
                                        while counter<(self.time_stop_process_waiting_liking//5):
                                            if self.emergency_exit_liking == 1 or self.value_of_liking_switch=="off":
                                                break
                                            time.sleep(5)
                                            counter+=1
                                        if self.emergency_exit_liking == 1 or self.value_of_liking_switch=="off":
                                                break
                                        
                                        counter_of_process = 0
                                        continue
                                    
                                    
                                    process_time_liking = random.randint(self.process_time_liking_min,self.process_time_liking_max)
                                    counter = 0
                                    while counter<(process_time_liking//5):
                                        if self.emergency_exit_liking == 1 or self.value_of_liking_switch=="off":
                                            break
                                        time.sleep(5)
                                        counter+=1
                                    if self.emergency_exit_liking == 1 or self.value_of_liking_switch=="off":
                                            break
                                    time.sleep(process_time_liking%5)

                                else:
                                    summary_text = f"{liveTime()} --> Beğeni ---> {user} kullanıcısının son gönderisi zaten beğenilmiş\n"
                                    self.process_summary_liking = summary_text + self.process_summary_liking
                                    self.label_process_summary_text_liking.configure(text=self.process_summary_liking)
                                    self.process_summary_all = summary_text + self.process_summary_all
                                    self.label_process_summary_text_all.configure(text=self.process_summary_all)
                                    process_time_liking = random.randint(self.process_time_liking_min,self.process_time_liking_max)
                                    
                                    counter = 0
                                    while counter<(process_time_liking//5):
                                        if self.emergency_exit_liking == 1 or self.value_of_liking_switch=="off":
                                            break
                                        time.sleep(5)
                                        counter+=1
                                    if self.emergency_exit_liking == 1 or self.value_of_liking_switch=="off":
                                            break
                                    time.sleep(process_time_liking%5)
                            except:
                                summary_text = f"{liveTime()} --> Beğeni ---> {user} kullanıcısının gönderisi beğenilirken bir hata oluştu\n"
                                self.process_summary_liking = summary_text + self.process_summary_liking
                                self.label_process_summary_text_liking.configure(text=self.process_summary_liking)
                                self.process_summary_all = summary_text + self.process_summary_all
                                self.label_process_summary_text_all.configure(text=self.process_summary_all)
                    else:
                        summary_text = f"{liveTime()} --> Beğeni ---> {user} kullanıcısı bulunamadı\n"
                        self.process_summary_all = summary_text + self.process_summary_all
                        self.label_process_summary_text_all.configure(text=self.process_summary_all)
                        self.process_summary_liking = summary_text + self.process_summary_liking
                        self.label_process_summary_text_liking.configure(text=self.process_summary_liking)

            else:
                if is_signed_before == 1:
                    is_signed_before = 0
                    summary_text = f"{liveTime()} --> Beğeni ---> İşlem sonlandırıldı\n"
                    self.process_summary_liking = summary_text + self.process_summary_liking
                    self.label_process_summary_text_liking.configure(text=self.process_summary_liking)
                    self.process_summary_all = summary_text + self.process_summary_all
                    self.label_process_summary_text_all.configure(text=self.process_summary_all)

            time.sleep(5)
            







    def followUi(self):
        def addUsers():
            self.users_text_for_following = """"""
            users_temp = []
            dialog = customtkinter.CTkInputDialog(text="Kullanıcı adı giriniz.", title="Kullanıcı girme")
            users_text_temp = dialog.get_input()
            users_temp.extend(users_text_temp.split(','))
            
            for user in users_temp:
                if user in self.users_for_following:
                    self.users_for_following.remove(user)
                    del self.users_post_id_following[user]
                else:
                    self.users_for_following.append(user)
                    self.users_post_id_following[user] = []
            for x in range(len(self.users_for_following)):
                self.users_text_for_following+=self.users_for_following[x]+"\n"

            if user:
                users_label.configure(text=self.users_text_for_following)


        def changeSettings():
            input_1 = customtkinter.CTkInputDialog(  text="İşlem süresi giriniz.\nÖrnek: 10-25", title="Ayarlar")
            process_time_temp = input_1.get_input()
            if process_time_temp:
                process_time_following_min_temp, process_time_following_max_temp = process_time_temp.split('-')
                self.process_time_following_min = int(process_time_following_min_temp)
                self.process_time_following_max = int(process_time_following_max_temp)
                label_process_time_text.configure(text=f"İşlem süresi {self.process_time_following_min} ile {self.process_time_following_max} saniye arası")

            input_2 = customtkinter.CTkInputDialog(text="İşlem ve bekleme süresi giriniz.\nÖrnek: 35-900", title="Ayarlar")
            process_waiting_time_temp = input_2.get_input()

            if process_waiting_time_temp:
                time_stop_num_process_temp, time_stop_process_waiting_temp = process_waiting_time_temp.split('-')
                self.time_stop_num_process_following = int(time_stop_num_process_temp)
                self.time_stop_process_waiting_following = int(time_stop_process_waiting_temp)
                label_process_waiting_time_text.configure(text=f"Her {self.time_stop_num_process_following} işlemde {self.time_stop_process_waiting_following} saniye bekle")

            input_3 = customtkinter.CTkInputDialog(text="Bir hesaptan.\nKaç kişi takip edilsin.", title="Ayarlar")
            quantity_user_follow_temp = input_3.get_input()

            if quantity_user_follow_temp:
                self.quantity_follow_of_user = int(quantity_user_follow_temp)
                label_quantity_follow_of_user_text.configure(text=f"1 hesaptan {self.quantity_follow_of_user} kişi takip et")

        def saveUsers():
            self.app_following.withdraw()

        def switcherFollowing():
            self.value_of_following_switch = self.following_process_start.get()
            if self.value_of_following_switch == "on" and self.is_follow_started == 0:
                self.is_follow_started = 1
                thread3.start()

        def reopenWindow():
            self.app_following.deiconify()
                

        
        if self.is_follow_started==0:
            
            self.app_following = customtkinter.CTkToplevel()
            self.app_following.geometry("900x600")
            self.app_following.title(f"{self.username}")

            self.app_following.protocol("WM_DELETE_WINDOW", saveUsers)

            screen_width = self.app_following.winfo_screenwidth()
            screen_height = self.app_following.winfo_screenheight()
            xforapp = (screen_width - 900) / 2
            yforapp = (screen_height - 600) / 2

            self.app_following.geometry("+%d+%d" % (xforapp, yforapp))


            
            frame_master = customtkinter.CTkScrollableFrame(master=self.app_following)
            frame_master.pack(pady=20,padx=60,fill="both",expand=True)
            
            frame = customtkinter.CTkFrame(master=frame_master)
            frame.pack(pady=20,padx=60,fill="both",expand=True)

            frame_2 = customtkinter.CTkFrame(master=frame_master)
            frame_2.pack(pady=20,padx=60,fill="both",expand=True)


            space_label = customtkinter.CTkLabel(frame, text="", height=20)
            space_label.pack()


            label_follow_text = customtkinter.CTkLabel(master=frame, text=f"Takip Etme Ayarları", font=("Roboto", 24))
            label_follow_text.pack()

            self.following_process_start = customtkinter.StringVar(value=self.value_of_following_switch)
            following_switch = customtkinter.CTkSwitch(master=frame, text="Kontrol Düğmesi", command=switcherFollowing, variable=self.following_process_start, onvalue="on", offvalue="off")
            following_switch.pack(pady=5)

            space_label = customtkinter.CTkLabel(frame, text="", height=50)
            space_label.pack()

            frame_users_name = customtkinter.CTkScrollableFrame(master=frame, fg_color="#333333")
            frame_users_name.pack(side="left", pady=0,padx=20,fill="both",expand=True)

            label_users_text = customtkinter.CTkLabel(master=frame_users_name, text=f"Kullanıcı Adları", font=("Roboto", 14),fg_color="#2B2B2B", width=1000)
            label_users_text.pack()

            button_2 = customtkinter.CTkButton(master=frame_users_name, text="Ekle/Sil", font=("Roboto", 13), command=addUsers, width=18)
            button_2.pack(pady=12, padx=2)

            users_label = customtkinter.CTkLabel(master=frame_users_name,text=f"{self.users_text_for_following}", font=("Roboto", 12))
            users_label.pack(pady=10, padx=5)

            frame_settings = customtkinter.CTkScrollableFrame(master=frame, fg_color="#333333")
            frame_settings.pack(side="right", pady=0,padx=20,fill="both",expand=True)

            label_settings_text = customtkinter.CTkLabel(master=frame_settings, text=f"Ayarlar", font=("Roboto", 14),fg_color="#2B2B2B", width=1000)
            label_settings_text.pack()

            button_3 = customtkinter.CTkButton(master=frame_settings, text="Değiştir", font=("Roboto", 13), command=changeSettings, width=18)
            button_3.pack(pady=12, padx=2)

            space_label = customtkinter.CTkLabel(frame_settings, text="", height=20)
            space_label.pack()

            label_process_time_text = customtkinter.CTkLabel(master=frame_settings, text=f"İşlem süresi {self.process_time_following_min} ile {self.process_time_following_max} saniye arası", font=("Roboto", 15))
            label_process_time_text.pack()

            label_process_waiting_time_text = customtkinter.CTkLabel(master=frame_settings, text=f"Her {self.time_stop_num_process_following} işlemde {self.time_stop_process_waiting_following} saniye bekle", font=("Roboto", 15))
            label_process_waiting_time_text.pack()

            label_quantity_follow_of_user_text = customtkinter.CTkLabel(master=frame_settings, text=f"1 hesaptan {self.quantity_follow_of_user} kişi takip et", font=("Roboto", 15))
            label_quantity_follow_of_user_text.pack()

            frame_summary = customtkinter.CTkScrollableFrame(master=frame_2, fg_color="#333333", width=500)
            frame_summary.pack(pady=0,padx=20,fill="both",expand=True)

            label_summary_text = customtkinter.CTkLabel(master=frame_summary, text=f"İşlem Özeti", font=("Roboto", 14),fg_color="#2B2B2B", width=1000)
            label_summary_text.pack()

            space_label = customtkinter.CTkLabel(frame_summary, text="", height=20)
            space_label.pack()

            self.label_process_summary_text_following = customtkinter.CTkLabel(master=frame_summary, text=f"{self.process_summary_following}", font=("Roboto", 12))
            self.label_process_summary_text_following.pack()


            button_1 = customtkinter.CTkButton(master=self.app_following, text="Kaydet", font=("Roboto", 20), command=saveUsers)
            button_1.pack(pady=18, padx=15)


            self.label_infos_following = customtkinter.CTkLabel(master=self.app_following, text=f"Lisansınızın bitmesine {calcTime()} gün kaldı.")
            self.label_infos_following.pack(side="bottom")

        
        else:
            reopenWindow()

    def follow(self):

        while True:
        
            try:
                chrome_options = Options()
                chrome_options.add_argument("--headless")
                browser = webdriver.Chrome(options=chrome_options)
                browser.get("https://www.instagram.com")
                WebDriverWait(browser, 45).until(EC.presence_of_element_located((By.NAME, "username")))
                time.sleep(0.2)

                username_input = browser.find_element(By.NAME, "username")
                password_input = browser.find_element(By.NAME, "password")

                username_input.send_keys(self.username)
                time.sleep(0.1)
                password_input.send_keys(self.password)
                time.sleep(0.1)
                password_input.send_keys(Keys.ENTER)

                WebDriverWait(browser, 45).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button')))


                counter_of_process = 0
                is_signed_before = 0
                break

            except:
                summary_text = f"{liveTime()} --> Takip Etme ---> Spam algılandı. İşlemler 2 saat askıya alındı -402f-\n"
                self.process_summary_following = summary_text + self.process_summary_following
                self.label_process_summary_text_following.configure(text=self.process_summary_following)
                self.process_summary_all = summary_text + self.process_summary_all
                self.label_process_summary_text_all.configure(text=self.process_summary_all)
                counter = 0
                while counter<1440:
                    if self.emergency_exit_following == 1 or self.value_of_following_switch=="off":
                        break
                    time.sleep(5)
                    counter+=1
                if self.emergency_exit_following == 1 or self.value_of_following_switch=="off":
                        break
        
        spam_counter = 0
        while True:

            if self.emergency_exit_following == 1:
                break

            while self.value_of_following_switch=="on":
                if is_signed_before == 0:
                    summary_text = f"{liveTime()} --> Takip Etme ---> İşlem başlatıldı\n"
                    self.process_summary_following = summary_text + self.process_summary_following
                    self.label_process_summary_text_following.configure(text=self.process_summary_following)
                    self.process_summary_all = summary_text + self.process_summary_all
                    self.label_process_summary_text_all.configure(text=self.process_summary_all)

                    is_signed_before = 1

                for user in self.users_for_following:
                    if self.value_of_following_switch=="off":
                        break

                
                    try:
                        num = self.quantity_follow_of_user

                        try:
                            follows = self.host.followers(user, count=num)
                            dicti = {}
                            for element in follows:
                                dicti[element.username] = element.is_private

                        except:
                            try:
                                self.host = Host(self.username,self.password, r"assets/session.txt")
                                follows = self.host.followers(user, count=num)
                                dicti = {}
                                for element in follows:
                                    dicti[element.username] = element.is_private

                            except:
                                summary_text = f"{liveTime()} --> Takip Etme ---> Spam algılandı. İşlemler 2 saat askıya alındı -403f-\n"
                                self.process_summary_following = summary_text + self.process_summary_following
                                self.label_process_summary_text_following.configure(text=self.process_summary_following)
                                self.process_summary_all = summary_text + self.process_summary_all
                                self.label_process_summary_text_all.configure(text=self.process_summary_all)
                                counter = 0
                                while counter<1440:
                                    if self.emergency_exit_following == 1 or self.value_of_following_switch=="off":
                                        break
                                    time.sleep(5)
                                    counter+=1
                                if self.emergency_exit_following == 1 or self.value_of_following_switch=="off":
                                        break

                        """
                        follows_username = list(set(follows_username) - set(self.users_post_id_following[user]))
                        if len(follows_username) >= self.quantity_follow_of_user:
                            
                            follows_username = follows_username[:num]
                        """

                    except:
                        summary_text = f"{liveTime()} --> Takip Etme ---> {user} kullanıcı adını kontrol edin\n"
                        self.process_summary_following = summary_text + self.process_summary_following
                        self.label_process_summary_text_following.configure(text=self.process_summary_following)
                        self.process_summary_all = summary_text + self.process_summary_all
                        self.label_process_summary_text_all.configure(text=self.process_summary_all)
                        continue
                            
                    
                

                    
                    for username, privateu in dicti.items():
                        if self.value_of_following_switch=="off":
                            break
                        
                        try:
                            
                            browser.get(f"https://www.instagram.com/{username}")


                            counter = 0
                            while counter<20:
                                try:
                                    WebDriverWait(browser, 0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button')))
                                    browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button').click()
                                    break
                                except:
                                    try:
                                        WebDriverWait(browser, 0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')))
                                        browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button').click()
                                        break
                                    except:
                                        counter+=1
                            if counter > 19:
                                spam_counter+=1
                                if spam_counter == 4:
                                    summary_text = f"{liveTime()} --> Takip Etme ---> Spam algılandı. İşlemler 2 saat askıya alındı -405f-\n"
                                    self.process_summary_following = summary_text + self.process_summary_following
                                    self.label_process_summary_text_following.configure(text=self.process_summary_following)
                                    self.process_summary_all = summary_text + self.process_summary_all
                                    self.label_process_summary_text_all.configure(text=self.process_summary_all)
                                    counter = 0
                                    while counter<1440:
                                        if self.emergency_exit_following == 1 or self.value_of_following_switch=="off":
                                            break
                                        time.sleep(5)
                                        counter+=1
                                    if self.emergency_exit_following == 1 or self.value_of_following_switch=="off":
                                            break
                                if spam_counter == 8:
                                    summary_text = f"{liveTime()} --> Takip Etme ---> İleri düzey spam algılandı. İşlemler 1 gün askıya alındı -406f-\n"
                                    self.process_summary_following = summary_text + self.process_summary_following
                                    self.label_process_summary_text_following.configure(text=self.process_summary_following)
                                    self.process_summary_all = summary_text + self.process_summary_all
                                    self.label_process_summary_text_all.configure(text=self.process_summary_all)
                                    counter = 0
                                    while counter<17280:
                                        if self.emergency_exit_following == 1 or self.value_of_following_switch=="off":
                                            break
                                        time.sleep(5)
                                        counter+=1
                                    if self.emergency_exit_following == 1 or self.value_of_following_switch=="off":
                                            break
                                    spam_counter = 0
                                continue
                            
                            spam_counter = 0

                            if privateu == True:
                                summary_text = f"{liveTime()} --> Takip Etme ---> {username} kullanıcısına istek gönderildi\n"
                            else:
                                summary_text = f"{liveTime()} --> Takip Etme ---> {username} kullanıcısı takip edildi\n"
                            
                            self.process_summary_following = summary_text + self.process_summary_following
                            
                            
                            while (self.process_summary_following.count('\n') + 1) > 100:
                                lines = self.process_summary_following.splitlines()
                                if lines:
                                    lines.pop()
                                self.process_summary_following = '\n'.join(lines)
                            self.label_process_summary_text_following.configure(text=self.process_summary_following)
                            self.process_summary_all = summary_text + self.process_summary_all
                            self.label_process_summary_text_all.configure(text=self.process_summary_all)


                            counter_of_process+=1
                            process_time_following = random.randint(self.process_time_following_min,self.process_time_following_max)
                            
                            counter = 0
                            while counter<(process_time_following//5):
                                if self.emergency_exit_following == 1 or self.value_of_following_switch=="off":
                                    break
                                time.sleep(5)
                                counter+=1
                            if self.emergency_exit_following == 1 or self.value_of_following_switch=="off":
                                break
                            time.sleep(process_time_following%5)

                            try:

                                try:
                                    browser.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]')
                                except:
                                    browser.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]')
                                

                                summary_text = f"{liveTime()} --> Takip Etme ---> Spam algılandı. İşlemler 2 saat askıya alındı -404f-\n"
                                self.process_summary_following = summary_text + self.process_summary_following
                                self.label_process_summary_text_following.configure(text=self.process_summary_following)
                                self.process_summary_all = summary_text + self.process_summary_all
                                self.label_process_summary_text_all.configure(text=self.process_summary_all)
                                
                                process_time_following = random.randint(self.process_time_following_min,self.process_time_following_max)
                            
                                counter = 0
                                while counter<(process_time_following//5):
                                    if self.emergency_exit_following == 1 or self.value_of_following_switch=="off":
                                        break
                                    time.sleep(5)
                                    counter+=1
                                if self.emergency_exit_following == 1 or self.value_of_following_switch=="off":
                                    break
                                time.sleep(process_time_following%5)
                                

                            except:
                                pass
                            
                            if counter_of_process == self.time_stop_num_process_following:
                                summary_text = f"{liveTime()} --> Takip Etme ---> {self.time_stop_process_waiting_following} saniye bekleniyor\n"
                                self.process_summary_following = summary_text + self.process_summary_following
                                self.label_process_summary_text_following.configure(text=self.process_summary_following)
                                self.process_summary_all = summary_text + self.process_summary_all
                                self.label_process_summary_text_all.configure(text=self.process_summary_all)
                                
                                counter = 0
                                while counter<(self.time_stop_process_waiting_following//5):
                                    if self.emergency_exit_following == 1 or self.value_of_following_switch=="off":
                                        break
                                    time.sleep(5)
                                    counter+=1
                                if self.emergency_exit_following == 1 or self.value_of_following_switch=="off":
                                        break

                                counter_of_process = 0
                        except:
                            summary_text = f"{liveTime()} --> Takip Etme ---> {username} kullanıcısı takip edilirken bir hata oluştu\n"
                            self.process_summary_following = summary_text + self.process_summary_following
                            self.label_process_summary_text_following.configure(text=self.process_summary_following)
                            self.process_summary_all = summary_text + self.process_summary_all
                            self.label_process_summary_text_all.configure(text=self.process_summary_all)

                            counter = 0
                            while counter<(process_time_following//5):
                                if self.emergency_exit_following == 1 or self.value_of_following_switch=="off":
                                    break
                                time.sleep(5)
                                counter+=1
                            if self.emergency_exit_following == 1 or self.value_of_following_switch=="off":
                                break
                            time.sleep(process_time_following%5)

            else:
                if is_signed_before == 1:
                    is_signed_before = 0
                    summary_text = f"{liveTime()} --> Takip Etme ---> İşlem sonlandırıldı\n"
                    self.process_summary_following = summary_text + self.process_summary_following
                    self.label_process_summary_text_following.configure(text=self.process_summary_following)
                    self.process_summary_all = summary_text + self.process_summary_all
                    self.label_process_summary_text_all.configure(text=self.process_summary_all)

            time.sleep(5)







    def unfollowUi(self):
        def addUsers():
            self.users_text_for_unfollowing = """"""
            users_temp = []
            dialog = customtkinter.CTkInputDialog(text="Kullanıcı adı giriniz.", title="Beyaz liste")
            users_text_temp = dialog.get_input()
            users_temp.extend(users_text_temp.split(','))
            
            for user in users_temp:
                if user in self.users_for_not_unfollowing:
                    self.users_for_not_unfollowing.remove(user)
                else:
                    self.users_for_not_unfollowing.append(user)
            for x in range(len(self.users_for_not_unfollowing)):
                self.users_text_for_unfollowing+=self.users_for_not_unfollowing[x]+"\n"

            if user:
                users_label.configure(text=self.users_text_for_unfollowing)


        def changeSettings():
            input_1 = customtkinter.CTkInputDialog(  text="İşlem süresi giriniz.\nÖrnek: 10-25", title="Ayarlar")
            process_time_temp = input_1.get_input()
            if process_time_temp:
                process_time_unfollowing_min_temp, process_time_unfollowing_max_temp = process_time_temp.split('-')
                self.process_time_unfollowing_min = int(process_time_unfollowing_min_temp)
                self.process_time_unfollowing_max = int(process_time_unfollowing_max_temp)
                label_process_time_text.configure(text=f"İşlem süresi {self.process_time_unfollowing_min} ile {self.process_time_unfollowing_max} saniye arası")

            input_2 = customtkinter.CTkInputDialog(text="İşlem ve bekleme süresi giriniz.\nÖrnek: 35-900", title="Ayarlar")
            process_waiting_time_temp = input_2.get_input()

            if process_waiting_time_temp:
                time_stop_num_process_temp, time_stop_process_waiting_temp = process_waiting_time_temp.split('-')
                self.time_stop_num_process_unfollowing = int(time_stop_num_process_temp)
                self.time_stop_process_waiting_unfollowing = int(time_stop_process_waiting_temp)
                label_process_waiting_time_text.configure(text=f"Her {self.time_stop_num_process_unfollowing} işlemde {self.time_stop_process_waiting_unfollowing} saniye bekle")


        def saveUsers():
            self.app_unfollowing.withdraw()

        def switcherUnfollowing():
            self.value_of_unfollowing_switch = self.unfollowing_process_start.get()
            if self.value_of_unfollowing_switch == "on" and self.is_unfollow_started == 0:
                self.is_unfollow_started = 1
                thread4.start()

        def reopenWindow():
            self.app_unfollowing.deiconify()
                

        
        if self.is_unfollow_started==0:
            
            self.app_unfollowing = customtkinter.CTkToplevel()
            self.app_unfollowing.geometry("900x600")
            self.app_unfollowing.title(f"{self.username}")

            self.app_unfollowing.protocol("WM_DELETE_WINDOW", saveUsers)

            screen_width = self.app_unfollowing.winfo_screenwidth()
            screen_height = self.app_unfollowing.winfo_screenheight()
            xforapp = (screen_width - 900) / 2
            yforapp = (screen_height - 600) / 2

            self.app_unfollowing.geometry("+%d+%d" % (xforapp, yforapp))


            
            frame_master = customtkinter.CTkScrollableFrame(master=self.app_unfollowing)
            frame_master.pack(pady=20,padx=60,fill="both",expand=True)
            
            frame = customtkinter.CTkFrame(master=frame_master)
            frame.pack(pady=20,padx=60,fill="both",expand=True)

            frame_2 = customtkinter.CTkFrame(master=frame_master)
            frame_2.pack(pady=20,padx=60,fill="both",expand=True)


            space_label = customtkinter.CTkLabel(frame, text="", height=20)
            space_label.pack()


            label_follow_text = customtkinter.CTkLabel(master=frame, text=f"Takipten Çıkma Ayarları", font=("Roboto", 24))
            label_follow_text.pack()

            self.unfollowing_process_start = customtkinter.StringVar(value=self.value_of_unfollowing_switch)
            unfollowing_switch = customtkinter.CTkSwitch(master=frame, text="Kontrol Düğmesi", command=switcherUnfollowing, variable=self.unfollowing_process_start, onvalue="on", offvalue="off")
            unfollowing_switch.pack(pady=5)

            space_label = customtkinter.CTkLabel(frame, text="", height=50)
            space_label.pack()

            frame_users_name = customtkinter.CTkScrollableFrame(master=frame, fg_color="#333333")
            frame_users_name.pack(side="left", pady=0,padx=20,fill="both",expand=True)

            label_users_text = customtkinter.CTkLabel(master=frame_users_name, text=f"Beyaz Liste", font=("Roboto", 14),fg_color="#2B2B2B", width=1000)
            label_users_text.pack()

            button_2 = customtkinter.CTkButton(master=frame_users_name, text="Ekle/Sil", font=("Roboto", 13), command=addUsers, width=18)
            button_2.pack(pady=12, padx=2)

            users_label = customtkinter.CTkLabel(master=frame_users_name,text=f"{self.users_text_for_unfollowing}", font=("Roboto", 12))
            users_label.pack(pady=10, padx=5)

            frame_settings = customtkinter.CTkScrollableFrame(master=frame, fg_color="#333333")
            frame_settings.pack(side="right", pady=0,padx=20,fill="both",expand=True)

            label_settings_text = customtkinter.CTkLabel(master=frame_settings, text=f"Ayarlar", font=("Roboto", 14),fg_color="#2B2B2B", width=1000)
            label_settings_text.pack()

            button_3 = customtkinter.CTkButton(master=frame_settings, text="Değiştir", font=("Roboto", 13), command=changeSettings, width=18)
            button_3.pack(pady=12, padx=2)

            space_label = customtkinter.CTkLabel(frame_settings, text="", height=20)
            space_label.pack()

            label_process_time_text = customtkinter.CTkLabel(master=frame_settings, text=f"İşlem süresi {self.process_time_unfollowing_min} ile {self.process_time_unfollowing_max} saniye arası", font=("Roboto", 15))
            label_process_time_text.pack()

            label_process_waiting_time_text = customtkinter.CTkLabel(master=frame_settings, text=f"Her {self.time_stop_num_process_unfollowing} işlemde {self.time_stop_process_waiting_unfollowing} saniye bekle", font=("Roboto", 15))
            label_process_waiting_time_text.pack()

            frame_summary = customtkinter.CTkScrollableFrame(master=frame_2, fg_color="#333333", width=500)
            frame_summary.pack(pady=0,padx=20,fill="both",expand=True)

            label_summary_text = customtkinter.CTkLabel(master=frame_summary, text=f"İşlem Özeti", font=("Roboto", 14),fg_color="#2B2B2B", width=1000)
            label_summary_text.pack()

            space_label = customtkinter.CTkLabel(frame_summary, text="", height=20)
            space_label.pack()

            self.label_process_summary_text_unfollowing = customtkinter.CTkLabel(master=frame_summary, text=f"{self.process_summary_unfollowing}", font=("Roboto", 12))
            self.label_process_summary_text_unfollowing.pack()


            button_1 = customtkinter.CTkButton(master=self.app_unfollowing, text="Kaydet", font=("Roboto", 20), command=saveUsers)
            button_1.pack(pady=18, padx=15)


            self.label_infos_unfollowing = customtkinter.CTkLabel(master=self.app_unfollowing, text=f"Lisansınızın bitmesine {calcTime()} gün kaldı.")
            self.label_infos_unfollowing.pack(side="bottom")

        
        else:
            reopenWindow()

    def unfollow(self):

        while True:
            try:

                chrome_options = Options()
                chrome_options.add_argument("--headless")
                browser = webdriver.Chrome(options=chrome_options)
                browser.get("https://www.instagram.com")
                WebDriverWait(browser, 45).until(EC.presence_of_element_located((By.NAME, "username")))
                time.sleep(0.2)

                username_input = browser.find_element(By.NAME, "username")
                password_input = browser.find_element(By.NAME, "password")

                username_input.send_keys(self.username)
                time.sleep(0.1)
                password_input.send_keys(self.password)
                time.sleep(0.1)
                password_input.send_keys(Keys.ENTER)

                WebDriverWait(browser, 45).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button')))
                click_not_now = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
                click_not_now.click()


                counter_of_process = 0
                is_signed_before = 0
                break
            except:
                summary_text = f"{liveTime()} --> Takipten Çıkma ---> Spam algılandı. İşlemler 2 saat askıya alındı -401u-\n"
                self.process_summary_unfollowing = summary_text + self.process_summary_unfollowing
                self.label_process_summary_text_unfollowing.configure(text=self.process_summary_unfollowing)
                self.process_summary_all = summary_text + self.process_summary_all
                self.label_process_summary_text_all.configure(text=self.process_summary_all)
                counter = 0
                while counter<1440:
                    if self.emergency_exit_unfollowing == 1 or self.value_of_unfollowing_switch=="off":
                        break
                    time.sleep(5)
                    counter+=1
                if self.emergency_exit_unfollowing == 1 or self.value_of_unfollowing_switch=="off":
                        break

        while True:

            if self.emergency_exit_unfollowing == 1:
                break

            while self.value_of_unfollowing_switch=="on":
                if is_signed_before == 0:
                    summary_text = f"{liveTime()} --> Takipten Çıkma ---> İşlem başlatıldı\n"
                    self.process_summary_unfollowing = summary_text + self.process_summary_unfollowing
                    self.label_process_summary_text_unfollowing.configure(text=self.process_summary_unfollowing)
                    self.process_summary_all = summary_text + self.process_summary_all
                    self.label_process_summary_text_all.configure(text=self.process_summary_all)
                
                    is_signed_before = 1

                try:
                    try:
                        follows = self.host.followings(self.username, count=0)
                        followers = self.host.followers(self.username, count=0)
                        follows_username = [element.username for element in follows]
                        followers_username = [element.username for element in followers]
                    except:
                        try:
                            self.host = Host(self.username,self.password, r"assets/session.txt")
                            follows = self.host.followings(self.username, count=0)
                            followers = self.host.followers(self.username, count=0)
                            follows_username = [element.username for element in follows]
                            followers_username = [element.username for element in followers]
                        except:
                            summary_text = f"{liveTime()} --> Takipten Çıkma ---> Spam algılandı. İşlemler 2 saat askıya alındı -402u-\n"
                            self.process_summary_unfollowing = summary_text + self.process_summary_unfollowing
                            self.label_process_summary_text_unfollowing.configure(text=self.process_summary_unfollowing)
                            self.process_summary_all = summary_text + self.process_summary_all
                            self.label_process_summary_text_all.configure(text=self.process_summary_all)
                            counter = 0
                            while counter<1440:
                                if self.emergency_exit_unfollowing == 1 or self.value_of_unfollowing_switch=="off":
                                    break
                                time.sleep(5)
                                counter+=1
                            if self.emergency_exit_unfollowing == 1 or self.value_of_unfollowing_switch=="off":
                                    break
                            continue
                except:
                    summary_text = f"{liveTime()} --> Takipten Çıkma ---> Spam algılandı. İşlemler 2 saat askıya alındı -402u-\n"
                    self.process_summary_unfollowing = summary_text + self.process_summary_unfollowing
                    self.label_process_summary_text_unfollowing.configure(text=self.process_summary_unfollowing)
                    self.process_summary_all = summary_text + self.process_summary_all
                    self.label_process_summary_text_all.configure(text=self.process_summary_all)
                    counter = 0
                    while counter<1440:
                        if self.emergency_exit_unfollowing == 1 or self.value_of_unfollowing_switch=="off":
                            break
                        time.sleep(5)
                        counter+=1
                    if self.emergency_exit_unfollowing == 1 or self.value_of_unfollowing_switch=="off":
                            break
                    continue



                followers_username.extend(self.users_for_not_unfollowing)

                for user in follows_username:
                    try:
                        if user not in followers_username:
                            browser.get(f"https://www.instagram.com/{user}")
                            WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')))
                            browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button').click()

                            WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]')))
                            browser.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]').click()


                            summary_text = f"{liveTime()} --> Takipten Çıkma ---> {user} kullanıcısı takipten çıkıldı\n"
                            self.process_summary_unfollowing = summary_text + self.process_summary_unfollowing
                            while (self.process_summary_unfollowing.count('\n') + 1) > 100:
                                lines = self.process_summary_unfollowing.splitlines()
                                if lines:
                                    lines.pop()
                                self.process_summary_unfollowing = '\n'.join(lines)
                            self.label_process_summary_text_unfollowing.configure(text=self.process_summary_unfollowing)
                            self.process_summary_all = summary_text + self.process_summary_all
                            self.label_process_summary_text_all.configure(text=self.process_summary_all)

                            counter_of_process+=1
                            process_time_unfollowing = random.randint(self.process_time_unfollowing_min,self.process_time_unfollowing_max)
                            
                            counter = 0
                            while counter<(process_time_unfollowing//5):
                                if self.emergency_exit_unfollowing == 1 or self.value_of_unfollowing_switch=="off":
                                    break
                                time.sleep(5)
                                counter+=1
                            if self.emergency_exit_unfollowing == 1 or self.value_of_unfollowing_switch=="off":
                                    break
                            time.sleep(process_time_unfollowing%5)

                            try:
                                try:
                                    browser.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]')
                                except:
                                    browser.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]')

                                summary_text = f"{liveTime()} --> Takipten Çıkma ---> Spam algılandı. İşlemler 2 saat askıya alındı -403u-\n"
                                self.process_summary_unfollowing = summary_text + self.process_summary_unfollowing
                                self.label_process_summary_text_unfollowing.configure(text=self.process_summary_unfollowing)
                                self.process_summary_all = summary_text + self.process_summary_all
                                self.label_process_summary_text_all.configure(text=self.process_summary_all)
                                counter = 0
                                while counter<1440:
                                    if self.emergency_exit_unfollowing == 1 or self.value_of_unfollowing_switch=="off":
                                        break
                                    time.sleep(5)
                                    counter+=1
                                if self.emergency_exit_unfollowing == 1 or self.value_of_unfollowing_switch=="off":
                                        break
                                

                            except:
                                pass
                        
                        if counter_of_process == self.time_stop_num_process_unfollowing:
                            summary_text = f"{liveTime()} --> Takipten Çıkma ---> {self.time_stop_process_waiting_unfollowing} saniye bekleniyor\n"
                            self.process_summary_unfollowing = summary_text + self.process_summary_unfollowing
                            self.label_process_summary_text_unfollowing.configure(text=self.process_summary_unfollowing)
                            self.process_summary_all = summary_text + self.process_summary_all
                            self.label_process_summary_text_all.configure(text=self.process_summary_all)
                            
                            counter = 0
                            while counter<(self.time_stop_process_waiting_unfollowing//5):
                                if self.emergency_exit_unfollowing == 1 or self.value_of_unfollowing_switch=="off":
                                    break
                                time.sleep(5)
                                counter+=1
                            if self.emergency_exit_unfollowing == 1 or self.value_of_unfollowing_switch=="off":
                                    break

                            counter_of_process = 0
                    except:
                        summary_text = f"{liveTime()} --> Takipten Çıkma ---> {user} kullanıcısı takipten çıkılırken bir hata oluştu\n"
                        self.process_summary_unfollowing = summary_text + self.process_summary_unfollowing
                        self.label_process_summary_text_unfollowing.configure(text=self.process_summary_unfollowing)
                        self.process_summary_all = summary_text + self.process_summary_all
                        self.label_process_summary_text_all.configure(text=self.process_summary_all)
                
                summary_text = f"{liveTime()} --> Takipten Çıkma ---> İşlem tamamlandı. 2 saat sonra tekrar başlayacak\n"
                self.process_summary_unfollowing = summary_text + self.process_summary_unfollowing
                self.label_process_summary_text_unfollowing.configure(text=self.process_summary_unfollowing)
                self.process_summary_all = summary_text + self.process_summary_all
                self.label_process_summary_text_all.configure(text=self.process_summary_all)
                counter = 0
                while counter<1440:
                    if self.emergency_exit_unfollowing == 1 or self.value_of_unfollowing_switch=="off":
                        break
                    time.sleep(5)
                    counter+=1
                if self.emergency_exit_unfollowing == 1 or self.value_of_unfollowing_switch=="off":
                        break

            else:
                if is_signed_before == 1:
                    is_signed_before = 0
                    summary_text = f"{liveTime()} --> Takipten Çıkma ---> İşlem sonlandırıldı\n"
                    self.process_summary_unfollowing = summary_text + self.process_summary_unfollowing
                    self.label_process_summary_text_unfollowing.configure(text=self.process_summary_unfollowing)
                    self.process_summary_all = summary_text + self.process_summary_all
                    self.label_process_summary_text_all.configure(text=self.process_summary_all)

            time.sleep(5)
    

    def updateInfos(self):
        

        while True:
            counter = 0
            while counter<1440:
                if self.emergency_exit_updateinfos == 1:
                    break
                time.sleep(5)
                counter+=1
            if self.emergency_exit_updateinfos == 1:
                break
            try:
                self.label_infos.configure(text=f"Lisansınızın bitmesine {calcTime()} gün kaldı.")
            except:
                pass
            try:
                self.label_infos_liking.configure(text=f"Lisansınızın bitmesine {calcTime()} gün kaldı.")
            except:
                pass
            try:
                self.label_infos_unfollowing.configure(text=f"Lisansınızın bitmesine {calcTime()} gün kaldı.")
            except:
                pass
            try:
                self.label_infos_following.configure(text=f"Lisansınızın bitmesine {calcTime()} gün kaldı.")
            except:
                pass

            try:
                profil = self.host.profile(self.username)
                self.num_of_follow = profil.following_count
                self.num_of_follower = profil.follower_count
                self.label_follow_text.configure(text=f"{self.num_of_follower} Takipçi   {self.num_of_follow} Takip")
            except:
                pass
            
            while (self.process_summary_all.count('\n') + 1) > 500:
                lines = self.process_summary_all.splitlines()
                if lines:
                    lines.pop()
                self.process_summary_all = '\n'.join(lines)
            else:
                self.label_process_summary_text_all.configure(text=self.process_summary_all)

            if calcTime() < 0:
                self.value_of_following_switch = "off"
                self.value_of_unfollowing_switch = "off"
                self.value_of_liking_switch = "off"

                self.emergency_exit_following = 1
                self.emergency_exit_unfollowing = 1
                self.emergency_exit_liking = 1
                self.emergency_exit_updateinfos = 1
            




tried_sign_in = 0
is_sign_in = 0


while is_sign_in == 0:

    if calcTime() < 0:
        break

    signIn(tried_sign_in)
    tried_sign_in = 1

    if emergency_exit_signin == 1:
        break

    app = Instagram(username,password)

    thread1 = threading.Thread(target=app.liking)
    thread2 = threading.Thread(target=app.processesUi)
    thread3 = threading.Thread(target=app.follow)
    thread4 = threading.Thread(target=app.unfollow)
    thread5 = threading.Thread(target=app.updateInfos)

    if app.signIn()==1:
        is_sign_in = 1
        thread2.start()
        thread5.start()

