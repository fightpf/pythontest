import selenium
import time
from selenium import webdriver
import time 
import os 
import traceback

options = webdriver.ChromeOptions()
#options.add_argument("--headless")
browser = webdriver.Chrome('chromedriver.exe', chrome_options=options)
#browser = webdriver.Chrome('F:\Desktop\lable\chromedriver.exe', chrome_options=options)
browser.get('http://labms.ehs.fju.edu.tw/Laboratory/Login.aspx')
browser.maximize_window()
username=[]
with open("username.txt") as fopen:
    for i in fopen:
        username.append(i.strip())
    
username_input= username[0]
password_input= username[1]

UN = browser.find_element_by_id('ContentPlaceHolder1_LoginWindow_UserName')
UN.send_keys(username_input)
PS = browser.find_element_by_id('ContentPlaceHolder1_LoginWindow_Password')
PS.send_keys(password_input)
LI = browser.find_element_by_id('ContentPlaceHolder1_LoginWindow_LoginButton')
LI.click()


browser.execute_script("return __doPostBack('ctl00$ContentPlaceHolder1$GridView1','Select$0')")
LII = browser.find_element_by_css_selector('li:nth-child(5)')
LII.click()

time.sleep(4)
recordin305first=browser.find_element_by_xpath('//*[@id="home"]/div[2]/div[2]/div[2]')
recordin305first.click()
time.sleep(1)
# recordin305second=browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[1]/ul/li[2]/p/a')
# recordin305second.click()
go_to_daily_record=browser.find_element_by_xpath('//*[@id="record_page"]/div[2]/div[2]/div[2]/div[2]/a[1]/button')
go_to_daily_record.click()
localtime = time.localtime(time.time())
x=localtime.tm_mday
y=localtime.tm_wday
y=(y+2)%7
if y == 0 :
    y=7
z=(x-1)%7
if z == 0:
    z=7
firstday_wday=((y-z)+7)%7
if firstday_wday==0:
    firstday_wday=7    
week_series=(x-1+firstday_wday-1)//7+1
print(x,y,firstday_wday,week_series)
def autoclick_day():
    time.sleep(2)
    thisday='//*[@id="daliy-table"]/tbody/tr[{temp_week}]/td[{temp_day}]/i'
    thisday=thisday.format(temp_week=week_series+2,temp_day=y)
    try:
        thisday_get=browser.find_element_by_xpath(thisday)
        check_compeleornon=thisday_get.get_attribute('class')
        check_compeleornon=="ivu-icon ivu-icon-checkmark-round checkmark"
    except:

        dayselection='//*[@id="daliy-table"]/tbody/tr[{temp_week}]/td[{temp_day}]/span[2]/button'
        today_string=dayselection.format(temp_week=week_series+2,temp_day=y)
        go_to_today_list=browser.find_element_by_xpath(today_string)
        go_to_today_list.click()
        time.sleep(2)
        for numberseries in range (1,4):
            click_day='//*[@id="app"]/div/div[2]/div[2]/div[2]/div[{temp_day}]/p[1]'
            click_day=click_day.format(temp_day=numberseries)
            click_day=browser.find_element_by_xpath(click_day)
            click_day.click()
            time.sleep(2)
            if numberseries!=3:
                for j in range (1,11):
                    click_day='//*[@id="app"]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[3]/div[{temp_day}]/div/div[1]/input'   
                    click_day=click_day.format(temp_day=j)
                    click_day=browser.find_element_by_xpath(click_day)
                    click_day.click()
                    time.sleep(0.2)
                click_finish=browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[3]/div[3]/div[2]/button[1]')
                click_finish.click()
                time.sleep(1)
                alert = browser.switch_to.alert
                time.sleep(1)
                print (alert.text)  #打印警告對話框內容
                alert.accept()   #alert對話框屬於警告對話框，我們這裏只能接受彈窗
                time.sleep(1) 
    
        
            else:
                for j in range (1,9):
                    click_day='//*[@id="app"]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div[{temp_day}]/div/div[1]/input'
                    click_day=click_day.format(temp_day=j)
                    click_day=browser.find_element_by_xpath(click_day)
                    click_day.click()
                    time.sleep(0.2)
                click_finish=browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[3]/div[3]/div[2]/button[1]')
                click_finish.click()
                time.sleep(1)
                alert = browser.switch_to.alert
                time.sleep(1)
                print (alert.text)  #打印警告對話框內容
                alert.accept()   #alert對話框屬於警告對話框，我們這裏只能接受彈窗
                time.sleep(1)
        change_type=browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[3]/div[3]/div[2]/button[3]')#下面四行切回週檢點表
        change_type.click()
    change_type=browser.find_element_by_xpath('//*[@id="sidebar"]/div[2]/div[2]')
    change_type.click()
    time.sleep(1)
                                            

def autoclick_week() : 
    weekselection='//*[@id="weekly"]/div/div/div[{week_get}]/div[@class]'
    thisweek=weekselection.format(week_get=week_series) #抓取週數
    try :
        thisweek_get=browser.find_element_by_xpath(thisweek)
        check_compeletornon=thisweek_get.get_attribute('class')
        if check_compeletornon=='compelet'or check_compeletornon=='holiday':
            print("週檢點表已填")
    except :
        clikck_weekselection='//*[@id="weekly"]/div/div/div[{week_temp}]/button'
        clikck_weekselection=clikck_weekselection.format(week_temp=week_series)
        click_in_week=browser.find_element_by_xpath(clikck_weekselection)
        click_in_week.click()
        for i in range (1,5) :
            time.sleep(1)
            click_in_week='//*[@id="app"]/div/div[2]/div[2]/div[2]/div[{tempweek}]/p[1]'
            click_in_week=click_in_week.format(tempweek=i)           
            click_in_week=browser.find_element_by_xpath(click_in_week)
            click_in_week.click()
            for j in range (1,13) :
                time.sleep(0.2)
                click_in_week='//*[@id="app"]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[3]/div[{tempweek2}]/div/div[1]/input'
                click_in_week=click_in_week.format(tempweek2=j)           
                click_in_week=browser.find_element_by_xpath(click_in_week)
                click_in_week.click()
            click_finish=browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[3]/div[3]/div[2]/button[1]')
            click_finish.click()
            time.sleep(1)
            alert = browser.switch_to.alert
            time.sleep(1)
            print (alert.text)  
            alert.accept()   
            time.sleep(1)
        click_in_week='//*[@id="app"]/div/div[2]/div[2]/div[2]/div[5]/p[1]'           
        click_in_week=browser.find_element_by_xpath(click_in_week)
        click_in_week.click()
        for j in range (1,11) :
            time.sleep(1)
            click_in_week='//*[@id="app"]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[3]/div[{tempweek}]/div/div[1]/input'
            click_in_week=click_in_week.format(tempweek=j)           
            click_in_week=browser.find_element_by_xpath(click_in_week)
            click_in_week.click()
            time.sleep(0.2)
        for j in range (1,5) :
            click_in_week='//*[@id="app"]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[4]/div[{tempweek}]/div/div[1]/input'
            click_in_week=click_in_week.format(tempweek=j)           
            click_in_week=browser.find_element_by_xpath(click_in_week)
            click_in_week.click()
            time.sleep(0.2)
        click_finish=browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[3]/div[3]/div[2]/button[1]')
        click_finish.click()
        time.sleep(1)
        alert = browser.switch_to.alert
        time.sleep(1)
        print (alert.text)  #打印警告對話框內容
        alert.accept()   #alert對話框屬於警告對話框，我們這裏只能接受彈窗
        time.sleep(1)
            
   
##day    
autoclick_day()

##week
autoclick_week()
browser.quit()
    

