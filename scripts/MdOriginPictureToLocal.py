import requests;

def parseFileAndReplace(fileName):
    count = 0
    newLines = []
    with open(fileName, "r") as f:
        lines = f.readlines()
        for line in lines:
            if(line.startswith("![")):
                count += 1
                url = line.split("](")[1][:-2]
                res = requests.get(url,params=None,verify=False)
                imageFileName = "./Spring生命周期_image/img_" + str(count) + ".png"
                with open(imageFileName, "wb") as f1:
                    f1.write(res.content)
                print("下载图片完成:"  + imageFileName)
                line = line.replace(url, imageFileName)
                print(line)
            newLines.append(line)
    with open("NEW_"+fileName, "w+") as f:
        for line in newLines:
            f.write(line)

    print("总共图片数量:", count)



if __name__ == '__main__':
    parseFileAndReplace("../docs/src/sourcecode/Spring生命周期.md")