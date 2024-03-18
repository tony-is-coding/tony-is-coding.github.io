import requests
import os


def parseFileAndReplace(fileName):
    count = 0
    newLines = []

    out_file = "./out/"
    abs_image_path = fileName.split('.')[0] + "/"
    if not os.path.exists(out_file + abs_image_path):
        os.makedirs(out_file + abs_image_path)

    with open(fileName, "r") as f:
        lines = f.readlines()
        for line in lines:
            if (line.startswith("![")):
                count += 1
                url = line.split("](")[1][:-2]
                print("url:", url)
                res = requests.get(url, params=None, verify=False)
                imageFileName = abs_image_path + "img_" + str(count) + ".png"
                with open(out_file + imageFileName, "wb") as f1:
                    f1.write(res.content)
                print("下载图片完成:" + imageFileName)
                line = line.replace(url, imageFileName)
                print(line)
            newLines.append(line)
    with open(out_file + fileName, "w+") as f:
        for line in newLines:
            f.write(line)
    print("完成输出总共图片数量:", count)


if __name__ == '__main__':
    parseFileAndReplace("NoSuchMethodError 常见原因及解决方法.md")
    parseFileAndReplace("OutOfMemoryError 常见原因及解决方法.md")
    parseFileAndReplace("StackOverFlowError 常见原因及解决方法.md")
