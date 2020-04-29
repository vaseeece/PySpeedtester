from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
from importlib import reload
import speedtest

st = speedtest.Speedtest()

dowload_speed = st.download() / 1000.0 / 1000.0
dnld_mpbs = "{:.2f}".format(dowload_speed)
upload_speed = st.upload() / 1000.0 / 1000.0
upld_mpbs = "{:.2f}".format(upload_speed)
ping = st.results.ping
isp = st.results.client['isp']
country = st.results.client['country']
ip = st.results.client['ip']
server = st.results.server['sponsor']
sever_location = st.results.server['name']

window = Tk()
window.title("PySpeedTester")
window.geometry('400x300')
window.iconbitmap('speedtest.ico')
#window.configure(bg='white')

style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='green', justify='center')
style.configure("BW.TLabel", foreground="black", background="white")
label = Label(window, text="    python based internet speed tester  \n ", justify=CENTER, anchor=NW).grid()

Network_det_label = Label(window, text='Network : '+isp+'          Test server : '+server+
	              '  \n \ncountry : '+country+'             Region : '+sever_location+
	              ' \n \nip address : '+ip+' \n \nPing Time : '+str(round(ping, 0))+
	              ' ms  \n ', justify=LEFT, anchor=NW
	              ).grid()

bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar', mode="determinate")
bar['value'] = dnld_mpbs
bar.grid()
dnld_label = Label(window, text='Download speed : '+str(dnld_mpbs)+' Mbps \n  ', justify=LEFT, anchor=NW).grid()

bar1 = Progressbar(window, length=200, style='black.Horizontal.TProgressbar', mode="determinate")
bar1['value'] = upld_mpbs
bar1.grid()
upld_label = Label(window, text='Upload speed : '+str(upld_mpbs)+' Mbps', justify=LEFT, anchor=NW).grid()

window.mainloop()
