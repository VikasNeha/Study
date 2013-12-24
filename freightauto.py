#-*- coding: UTF-8 -*-
#from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import random
import time
import sys

#------------------------------------Freightauto v2.00------------------------------------


def turkishCharacters(str):

	str = str.encode('utf_8','ignore')
	str = str.replace("ç", "c")
	str = str.replace("Ç", "C")
	str = str.replace("ö", "o")
	str = str.replace("Ö", "O")
	str = str.replace("İ", "I")
	str = str.replace("ı", "i")
	str = str.replace("ü", "u")
	str = str.replace("Ü", "U")
	str = str.replace("Ğ", "G")
	str = str.replace("ğ", "g")
	str = str.replace("Ş", "S")
	str = str.replace("ş", "s")

	return str;

def disableImages():

	firefoxProfile = FirefoxProfile()
	firefoxProfile.set_preference('permissions.default.stylesheet', 2)
	firefoxProfile.set_preference('permissions.default.image', 2)
	firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','false')

	return firefoxProfile

def find_between_r(s, first, last ):
	try:
		start = s.rindex( first ) + len( first )
		end = s.rindex( last, start )
		return s[start:end]
	except ValueError:
		return ""

def loginGIT(browser,username,password):

	browser.get('https://www.gittigidiyor.com/uye-girisi')

	#Login to the page
	browser.find_element_by_name("kullanici").send_keys(username)
	browser.find_element_by_name("sifre").send_keys(password + Keys.RETURN)

	return browser

def loginTAOBAO(browser,username,password):

	browser.get('https://login.taobao.com/member/login.jhtml')

	#Login to the page
	browser.find_element_by_name('TPL_username').send_keys(username)
	browser.find_element_by_name('TPL_password').send_keys(password + Keys.RETURN)

	return browser

def login4PX(browser,username,password):

	browser.get('http://en.4px.com')

	#Login to the page
	browser.find_element_by_name('objUDto.username').send_keys(username)
	browser.find_element_by_name('objUDto.password').send_keys(password+Keys.RETURN)

	time.sleep(10)

	windows = browser.window_handles
	browser.close()
	browser.switch_to_window(windows[1])
	browser.maximize_window()

	return browser

def CreateOrders(browser,orders,products):

	Trorder = []

	for row in orders:
		if row['frgtnumbercn'] != '':
			y = row['ggordernumbers'].split(',')
			for x in products:
				if (x['ggordernumber'] == y[0]) and (row['albordernumber'] == x['albordernumber']) and (x['READY']== True):
					Trorder.append({'albordernumber':row['albordernumber'],'frgtnumbercn':row['frgtnumbercn'],'weight':row['weight'],'quantity':row['quantity'],'ggordernumbers':row['ggordernumbers'],'ad':x['ad'],'soyad':x['soyad'],'adres':x['adres'],'semt':x['semt'],'sehir':x['sehir'],'telefon':x['telefon'],'ceptelefon':x['ceptelefon'],'postakodu':x['postakodu'],'freightnumbertr':''})
					break

	if len(Trorder) > 0:
		for order in Trorder:
			browser.get('http://order.4px.com/gotoCreateOrder.html')
			try:
				browser.find_element_by_xpath('//div[@class="dialog-content"]/div[@style="width:100%;"]/a').click()
			except NoSuchElementException:
				pass

			browser.find_element_by_id('orderNo').send_keys(order['frgtnumbercn'])

			select = Select(browser.find_element_by_id("productDictionary"))
			select.select_by_visible_text(u"新加坡小包挂号  Singapo SPack IMAIR")

			browser.find_element_by_id('customerWeight').send_keys(order['weight'])
			browser.find_element_by_id('consignee_name').send_keys(order['ad'].decode('utf_8','ignore')+' '+order['soyad'].decode('utf_8','ignore'))

			select = Select(browser.find_element_by_id('CountryDictionary'))
			select.select_by_visible_text(u"TURKEY 土耳其")

			browser.find_element_by_id('txt_code').send_keys(order['postakodu'].decode('utf_8','ignore'))
			browser.find_element_by_id('consignee_address').send_keys(order['adres'].decode('utf_8','ignore')+' '+order['semt'].decode('utf_8','ignore')+'/'+order['sehir'].decode('utf_8','ignore')+'/TURKEY'+' '+order['ceptelefon'].decode('utf_8','ignore'))
			browser.find_element_by_id('consignee_tel').send_keys('+90'+order['telefon'].decode('utf_8','ignore'))
			browser.find_element_by_id('di_ename').send_keys('CLOTH')
			browser.find_element_by_id('di_piece').send_keys(order['quantity'])
			browser.find_element_by_id('di_unit_price').send_keys(str(random.randint(30,55)))
			browser.find_element_by_id('di_name').send_keys(order['albordernumber']+' - '+order['ggordernumbers'])

			browser.find_element_by_id('btn_save_down').click()


	returnArray = []
	returnArray.append(browser)
	returnArray.append(Trorder)
	return returnArray




def getOrders(browser):

	browser.get('http://www.gittigidiyor.com/BanaOzel/durum.php?type=satis&filter=2#sattiklarim')

	time.sleep(2)

	orders = []

	albordernumbers = browser.find_elements_by_xpath('//div[@style="border:1px solid #FFCC00;padding:3px;background-color:#FFFFCC;"]/table[@width="100%"]//tr/td[2]/small')
	ggordernumbersX = browser.find_elements_by_xpath('//div[@style="border:1px solid #FFCC00;padding:3px;background-color:#FFFFCC;"]/table[@width="100%"]//tr/td[1]/a[@href]')

	for k,albo in enumerate(albordernumbers):
		newalbo = []
		newalbo.append(str(albo.text))
		newalbo.append(find_between_r(str(ggordernumbersX[k].get_attribute("href")),"?delNote=","&noteType=S").strip())
		orders.append(newalbo)


	dicOrders 	= []
	dicProducts = []

	for order in orders:
		if order[0].strip().isdigit():
			ggordernumbers = str(order[1])
			for xequal in orders:
				if (order[0] == xequal [0]) and (order[1] != xequal[1]) and (order[1] != -1):
					ggordernumbers = ggordernumbers + "," + str(xequal[1])
					xequal[1] = -1

			if order[1] != -1:
				y = ggordernumbers.split(',')
				if len(y) > 1:
					for yproduct in y:
						dicProducts.append({'albordernumber':str(order[0]),'ggordernumber':str(yproduct),'ad':'','soyad':'','adres':'','semt':'','sehir':'','postakodu':'','telefon':'','ceptelefon':'','READY':False})
				elif len(y) == 1:
					dicProducts.append({'albordernumber':str(order[0]),'ggordernumber':str(order[1]),'ad':'','soyad':'','adres':'','semt':'','sehir':'','postakodu':'','telefon':'','ceptelefon':'','READY':False})

				dicOrders.append({'albordernumber':str(order[0]),'frgtnumbercn':'','weight':'','quantity':'','ggordernumbers':ggordernumbers,'freightnumbertr':''})
		else:
			print 'NO digits'

	returnArray = []
	returnArray.append(browser)
	returnArray.append(dicOrders)
	returnArray.append(dicProducts)
	return returnArray


def getOrdersChange(browser):

	browser.get('http://www.gittigidiyor.com/BanaOzel/durum.php?type=satis&filter=0#sattiklarim')

	time.sleep(2)

	orders = []

	albordernumbers = browser.find_elements_by_xpath('//div[@style="border:1px solid #FFCC00;padding:3px;background-color:#FFFFCC;"]/table[@width="100%"]//tr/td[2]/small')
	ggordernumbersX = browser.find_elements_by_xpath('//div[@style="border:1px solid #FFCC00;padding:3px;background-color:#FFFFCC;"]/table[@width="100%"]//tr/td[1]/a[@href]')

	for k,albo in enumerate(albordernumbers):
		newalbo = []
		newalbo.append(str(albo.text))
		newalbo.append(find_between_r(str(ggordernumbersX[k].get_attribute("href")),"?delNote=","&noteType=S").strip())
		orders.append(newalbo)


	dicOrders 	= []
	dicProducts = []

	for order in orders:
		if 'CHANGE' in order[0].strip():
			ggordernumbers = str(order[1])
			for xequal in orders:
				if (order[0] == xequal [0]) and (order[1] != xequal[1]) and (order[1] != -1):
					ggordernumbers = ggordernumbers + "," + str(xequal[1])
					xequal[1] = -1

			if order[1] != -1:
				y = ggordernumbers.split(',')
				rightOrderNum = str(order[0])
				rightOrderNum = rightOrderNum[rightOrderNum.rindex(' ')+1:]
				if len(y) > 1:
					for yproduct in y:
						dicProducts.append({'albordernumber':rightOrderNum,'ggordernumber':str(yproduct),'ad':'','soyad':'','adres':'','semt':'','sehir':'','postakodu':'','telefon':'','ceptelefon':'','READY':False,'TYPE':'CHANGE'})
				elif len(y) == 1:
					dicProducts.append({'albordernumber':rightOrderNum,'ggordernumber':str(order[1]),'ad':'','soyad':'','adres':'','semt':'','sehir':'','postakodu':'','telefon':'','ceptelefon':'','READY':False,'TYPE':'CHANGE'})

				dicOrders.append({'albordernumber':rightOrderNum,'frgtnumbercn':'','weight':'','quantity':'','ggordernumbers':ggordernumbers,'freightnumbertr':'','TYPE':'CHANGE'})
		else:
			#print 'NO Change'
			pass

	returnArray = []
	returnArray.append(browser)
	returnArray.append(dicOrders)
	returnArray.append(dicProducts)
	return returnArray


def getOrdersExtra(browser):

	browser.get('http://www.gittigidiyor.com/BanaOzel/durum.php?type=satis&filter=2#sattiklarim')

	time.sleep(2)

	orders = []

	albordernumbers = browser.find_elements_by_xpath('//div[@style="border:1px solid #FFCC00;padding:3px;background-color:#FFFFCC;"]/table[@width="100%"]//tr/td[2]/small')
	ggordernumbersX = browser.find_elements_by_xpath('//div[@style="border:1px solid #FFCC00;padding:3px;background-color:#FFFFCC;"]/table[@width="100%"]//tr/td[1]/a[@href]')

	for k,albo in enumerate(albordernumbers):
		newalbo = []
		newalbo.append(str(albo.text))
		newalbo.append(find_between_r(str(ggordernumbersX[k].get_attribute("href")),"?delNote=","&noteType=S").strip())
		orders.append(newalbo)


	dicOrders 	= []
	dicProducts = []

	for order in orders:
		if 'EXTRA' in order[0].strip():
			ggordernumbers = str(order[1])
			for xequal in orders:
				if (order[0] == xequal [0]) and (order[1] != xequal[1]) and (order[1] != -1):
					ggordernumbers = ggordernumbers + "," + str(xequal[1])
					xequal[1] = -1

			if order[1] != -1:
				y = ggordernumbers.split(',')
				rightOrderNum = str(order[0])
				rightOrderNum = rightOrderNum[rightOrderNum.rindex(' ')+1:]
				if len(y) > 1:
					for yproduct in y:
						dicProducts.append({'albordernumber':rightOrderNum,'ggordernumber':str(yproduct),'ad':'','soyad':'','adres':'','semt':'','sehir':'','postakodu':'','telefon':'','ceptelefon':'','READY':False,'TYPE':'EXTRA_RIGHT'})
				elif len(y) == 1:
					dicProducts.append({'albordernumber':rightOrderNum,'ggordernumber':str(order[1]),'ad':'','soyad':'','adres':'','semt':'','sehir':'','postakodu':'','telefon':'','ceptelefon':'','READY':False,'TYPE':'EXTRA_RIGHT'})

				dicOrders.append({'albordernumber':rightOrderNum,'frgtnumbercn':'','weight':'','quantity':'','ggordernumbers':ggordernumbers,'freightnumbertr':'','TYPE':'EXTRA_RIGHT'})

				leftOrderNum = str(order[0])
				leftOrderNum = leftOrderNum[:leftOrderNum.index(' ')]
				if len(y) > 1:
					for yproduct in y:
						dicProducts.append({'albordernumber':leftOrderNum,'ggordernumber':str(yproduct),'ad':'','soyad':'','adres':'','semt':'','sehir':'','postakodu':'','telefon':'','ceptelefon':'','READY':False,'TYPE':'EXTRA_LEFT'})
				elif len(y) == 1:
					dicProducts.append({'albordernumber':leftOrderNum,'ggordernumber':str(order[1]),'ad':'','soyad':'','adres':'','semt':'','sehir':'','postakodu':'','telefon':'','ceptelefon':'','READY':False,'TYPE':'EXTRA_LEFT'})

				dicOrders.append({'albordernumber':leftOrderNum,'frgtnumbercn':'','weight':'','quantity':'','ggordernumbers':ggordernumbers,'freightnumbertr':'','TYPE':'EXTRA_LEFT'})


		else:
			#print 'NO Extra'
			pass

	returnArray = []
	returnArray.append(browser)
	returnArray.append(dicOrders)
	returnArray.append(dicProducts)
	return returnArray


def getData(browser,orders,products):

	time.sleep(20)

	for row in orders:
		try:
			browser.get('http://trade.1688.com/order/unify_buyer_detail.htm?orderId='+row['albordernumber']+'&tracelog=20120313bscentertologisticsbuyer&#logisticsTabTitle')

			row['frgtnumbercn'] = browser.find_element_by_xpath('//div[@class="order-detail"]/ul[@class="cell-detail-list last-list"]/li[3]/span[@class="gray-light right-con"]').text.strip()

			weightList = browser.find_elements_by_xpath('//div[@class="weight-left weight"]')
			weight = 0

			for w in weightList:
				weight = weight + float(re.findall(r"[-+]?\d*\.\d+|\d+",w.text.strip())[0])
			row['weight'] = str(float(weight) - 0.05)

			quantity = 1
			row['quantity'] = str(quantity)

		except NoSuchElementException:
			pass

	time.sleep(2)
	print 'Step5 : Get 8 data items'

	for row in products:
		executethis = False

		for x in orders:
			if (x['albordernumber'] == row['albordernumber']) and (x['frgtnumbercn'] != ''):
				executethis = True

		if executethis:
			try:
				browser.get('http://www.gittigidiyor.com/BanaOzel/kargo_bilgisi.php?satis_code='+row['ggordernumber'])
				row['ad'] 		  = turkishCharacters(browser.find_element_by_xpath('//tbody/tr[2]/td[2]/font').text.strip())
				row['soyad'] 	  = turkishCharacters(browser.find_element_by_xpath('//tbody/tr[3]/td[2]/font').text.strip())
				row['adres'] 	  = turkishCharacters(browser.find_element_by_xpath('//tbody/tr[4]/td[2]/font').text.strip())
				row['semt']	  	  = turkishCharacters(browser.find_element_by_xpath('//tbody/tr[5]/td[2]/font').text.strip())
				row['sehir']	  = turkishCharacters(browser.find_element_by_xpath('//tbody/tr[6]/td[2]/font').text.strip())
				row['telefon']	  = turkishCharacters(browser.find_element_by_xpath('//tbody/tr[7]/td[2]/font').text.strip())
				row['ceptelefon'] = turkishCharacters(browser.find_element_by_xpath('//tbody/tr[8]/td[2]/font').text.strip())
				row['postakodu']  = turkishCharacters(browser.find_element_by_xpath('//tbody/tr[9]/td[2]/font').text.strip())
				row['READY'] = True

			except NoSuchElementException:
				continue


	returnArray = []
	returnArray.append(browser)
	returnArray.append(orders)
	returnArray.append(products)

	return returnArray



def gotoAvailableOrders(browser):

	browser.get('http://order.4px.com/gotoAvailableOrder.html')
	time.sleep(5);
	try:
		browser.find_element_by_id('all').click()
		browser.find_element_by_id('postOrder').click()
	except NoSuchElementException:
		pass

	return browser


def getFreightnumbertr(browser,executedOrders):

	browser.get('http://order.4px.com/queryPostOrder.html')
	time.sleep(5)
	select = Select(browser.find_element_by_id('setpagesize'))
	select.select_by_visible_text(u"500")

	for row in executedOrders:
		counter = 1
		while True:
			counter = counter + 1
			try:
				fn = browser.find_element_by_xpath('//table[@id="orderResults"]/tbody/tr['+str(counter)+']/td[2]/a').text.strip()
				if fn == row['frgtnumbercn']:
					row['freightnumbertr'] = browser.find_element_by_xpath('//table[@id="orderResults"]/tbody/tr['+str(counter)+']/td[6]/div').text.strip()
					break
				else:
					continue
			except NoSuchElementException:
				break

	returnArray = []
	returnArray.append(browser)
	returnArray.append(executedOrders)

	return returnArray

def finalStage(browser,executethis):

	time.sleep(2)

	for row in executethis:
		if row['freightnumbertr'] != '':
			y = row['ggordernumbers'].split(',')
			if len(y) == 1:
				browser.get('http://www.gittigidiyor.com/BanaOzel/gt.php?s_code='+str(y[0].strip()))
				select = Select(browser.find_element_by_id('kargo_brand'))
				select.select_by_visible_text(u"PTT Kargo")
				browser.find_element_by_id('ptt[gonderino]').send_keys(row['freightnumbertr'])
				browser.find_element_by_id('ptt[sube_adi]').send_keys('Yurtdisi')
				browser.find_element_by_xpath('//div/center/input[@name="ok"]').click()
			elif len(y) > 1:
				for g in y:
					browser.get('http://www.gittigidiyor.com/BanaOzel/gt.php?s_code='+str(g.strip()))
					select = Select(browser.find_element_by_id('kargo_brand'))
					select.select_by_visible_text(u"PTT Kargo")
					browser.find_element_by_id('ptt[gonderino]').send_keys(row['freightnumbertr'])
					browser.find_element_by_id('ptt[sube_adi]').send_keys('Yurtdisi')
					browser.find_element_by_xpath('//div/center/input[@name="ok"]').click()

	return browser

def finalStage2(browser,executethis):

	time.sleep(2)

	for row in executethis:
		try:
			if row['TYPE'] == 'CHANGE':
				browser.get('http://www.gittigidiyor.com/BanaOzel/durum.php?type=satis&filter=0#sattiklarim')
				browser.find_element_by_xpath("//input[@value='" + row['ggordernumbers'] + "']").click()
				browser.find_element_by_name("not").click()
				time.sleep(5)
				browser.find_element_by_tag_name("textarea").clear()
				browser.find_element_by_tag_name("textarea").send_keys(row['freightnumbertr'])
				browser.find_element_by_name("saveNotes").click()
			elif row['TYPE'] == 'EXTRA_RIGHT':
				browser.get('http://www.gittigidiyor.com/BanaOzel/durum.php?type=satis&filter=2#sattiklarim')
				browser.find_element_by_xpath("//input[@value='" + row['ggordernumbers'] + "']").click()
				browser.find_element_by_name("not").click()
				time.sleep(5)
				browser.find_element_by_tag_name("textarea").clear()
				browser.find_element_by_tag_name("textarea").send_keys(row['freightnumbertr'])
				browser.find_element_by_name("saveNotes").click()
		except KeyError:
			pass

	return browser


def main():

	#git
	usergit = 'fashionwish'
	pwgit = 'mJ76N01wLzP4H8aP'

	#tabao
	usertao = 'arifcalis'
	pwtao = 'yigidim81'

	#4px
	user4px = 'Ufuk'
	pw4px 	= '123456'

	orders 	 = []
	products = []

	print '------------Freightauto v2.00------------'

	while True:

		try:
			browser = webdriver.Firefox(disableImages())
			time.sleep(2)
			browser = loginGIT(browser,usergit,pwgit) #STEP 1
			print "Step1 : Logged in at http://www.gittigidiyor.com/";

			time.sleep(5)
			print 'Step2 : Going to http://www.gittigidiyor.com/BanaOzel/durum.php'
			step2 = getOrders(browser) #STEP 2
			browser  =  step2[0]
			orders   =  step2[1]
			products =  step2[2]

			time.sleep(5)
			print 'Step2.1 : Checking for CHANGE AND EXTRA'
			step2_1 = getOrdersChange(browser) #STEP 2
			browser  =  step2_1[0]
			orders2_1   =  step2_1[1]
			products2_1 =  step2_1[2]

			if len(orders2_1) > 0:
				for currOrder in orders2_1:
					orders.append(currOrder)
			if len(products2_1) > 0:
				for currProd in products2_1:
					products.append(currProd)

			step2_1_2 = getOrdersExtra(browser) #STEP 2
			browser  =  step2_1_2[0]
			orders2_1_2   =  step2_1_2[1]
			products2_1_2 =  step2_1_2[2]

			if len(orders2_1_2) > 0:
				for currOrder in orders2_1_2:
					orders.append(currOrder)
			if len(products2_1_2) > 0:
				for currProd in products2_1_2:
					products.append(currProd)



			if len(orders) > 0:
				for row in orders:

					try:
						if row['TYPE'] == 'CHANGE':
							print 'CHANGE  ',row['albordernumber'],'  =>  ', row['ggordernumbers']
							continue
						elif row['TYPE'] == 'EXTRA_RIGHT':
							print 'EXTRA  ',row['albordernumber'],'  =>  ', row['ggordernumbers']
							continue
					except KeyError:
							pass
					print '        ',row['albordernumber'],'  =>  ', row['ggordernumbers']



				time.sleep(5)
				browser = loginTAOBAO(browser,usertao,pwtao)# STEP 3
				print 'Step3 : Logged in at https://login.taobao.com/member/login.jhtml'

				time.sleep(5)
				print 'Step4 : Going at http://trade.1688.com/ to get data'
				step4   = getData(browser,orders,products) #STEP4
				browser = step4[0]
				orders  = step4[1]
				products =step4[2]#STEP5

				print '       --- Orders ---'


				emptyorders = False
				for order in orders:
					if order['frgtnumbercn']!= '':
						emptyorders = True
						print '       Albordernumber:',order['albordernumber'],'Frgtnumbercn:',order['frgtnumbercn'],'Weight:',order['weight'],'Quantity:',order['quantity']

				print


				if emptyorders == False:
					print 'No orders to process'
				else:
					for row in products:
						if row['ad'] != '':
							print '       ---',row['albordernumber'],'---'
							print '        Ggordernumber:',row['ggordernumber']
							print '        Adi:',row['ad']
							print '        Soyad:',row['soyad']
							print '        Adres:',row['adres']
							print '        Semt:',row['semt']
							print '        Sehir:',row['sehir']
							print '        Telefon:',row['telefon']
							print '        Ceptelefon:',row['ceptelefon']
							print '        Postakodu:',row['postakodu']
							print

					time.sleep(5)
					browser = login4PX(browser,user4px,pw4px)# STEP6
					print 'Step6 : Logged in at http://order.4px.com/signin.html'

					executedOrders = []

					time.sleep(5)
					print 'Step7 : Posting data at http://order.4px.com/gotoCreateOrder.html'
					step7 = CreateOrders(browser,orders,products)
					browser 		= step7[0] #STEP 7
					executedOrders  = step7[1]

					print 'wait 5 secs...'

					time.sleep(5) # delays for 5 seconds

					print 'Step8 : Goto http://order.4px.com/gotoAvailableOrder.html select all order and submit'
					browser = gotoAvailableOrders(browser)

					print 'wait 5 secs...'
					time.sleep(5) # delays for 5 seconds

					print 'Step9 : Goto http://order.4px.com/gotoPostOrder.html to get $freightnumbertr'
					step9 = getFreightnumbertr(browser,executedOrders)
					browser 		= step9[0]
					executedOrders  = step9[1]

					for o in executedOrders:
						print o['freightnumbertr']

					time.sleep(5)
					print 'Step10 : Goto http://www.gittigidiyor.com/BanaOzel/gt.php?s_code=xxxxxxxx'
					browser = finalStage(browser,executedOrders)

					time.sleep(5)
					print 'Step10.1 : Replacing albordernumber with freightnumbertr'
					browser = finalStage2(browser,executedOrders)

					print 'Completed.'
					print

				print 'Checking again...'
				print
			else:
				print 'No orders found.'

			browser.quit()

		except NoSuchElementException:
			print 'Error!'
			break
		except KeyboardInterrupt:
			print '\n','Bye. Cya later'
			break

if __name__ == "__main__":
	#now Firefox will run in a virtual display.
	#you will not see the browser.
	#nodisplay = Display(visible=0, size=(800, 600))
	#nodisplay.start()
	main()
	#nodisplay.stop()