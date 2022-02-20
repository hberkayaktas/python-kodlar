"""
Created on Wed Feb 16 04:05:52 2022

@author: hberk

pip install youtube_dl
"""

import youtube_dl

vlink= input("link giriniz:")

video_bilgisi = youtube_dl.YoutubeDL().extract_info(url= vlink,download=False) 
dosya_adi= f"{video_bilgisi['title']}.mp4"

ayarlar ={
    'outtmpl':dosya_adi,
}

with youtube_dl.YoutubeDL(ayarlar) as ydl:
    ydl.download([video_bilgisi['webpage_url']])
    
print(f"indirme tamamlandi...{dosya_adi}")