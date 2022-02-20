import urllib.request


url1 ="https://www.iconsdb.com/icons/preview/white/whatsapp-xl.png"
url2 ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9FERS8UUHMor64KSyXdMPj63ZUsVkgyuINBpqM5OVkWl_C75i"
url3 ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVFA5QShn-47G2LQbuUrg33ldpgrEObpR8iNwHFQx8hSxoxFg6"

urllistesi =[url1,url2,url3]

say = 1

for urlq in urllistesi:
    urllib.request.urlretrieve(urlq,"Resim" + str(say)+".jpg")
    say +=1