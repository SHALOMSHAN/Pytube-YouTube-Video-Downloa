import pytube

link = input("Enter the link: ")

res_data = input("Enter the desired resolution (e.g. 720p): ")

print("Downloading....")

pytube.YouTube(link).streams.filter(res=res_data).first().download()

print("The video has been downloaded!")

