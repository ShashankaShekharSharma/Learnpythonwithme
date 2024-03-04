#This code will download 5 random pics from the link given. You can change the resolution of the picture
#Better to run in Replit
import multiprocessing
import requests
if __name__ == "__main__":
    def downloadFile(url,name):
        response = requests.get(url)
        open(f"file{name}.jpg","wb").write(response.content)
    url = "https://picsum.photos/2000/3000"
    pros = []
    for i in range(5):
        p =multiprocessing.Process(target=downloadFile,args= [url,i])
        p.start()
        pros.append(p)
    for p in pros:
        p.join()