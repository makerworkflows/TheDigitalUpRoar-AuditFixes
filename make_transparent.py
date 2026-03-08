from PIL import Image

def make_transparent(filename):
    try:
        img = Image.open(filename)
        img = img.convert("RGBA")
        datas = img.getdata()
        
        newData = []
        for item in datas:
            # Check if pixel is white or very close to white
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                newData.append((255, 255, 255, 0)) # transparent
            else:
                newData.append(item)
                
        img.putdata(newData)
        img.save(filename, "PNG")
        print(f"Made {filename} transparent.")
    except Exception as e:
        print(f"Error on {filename}: {e}")

make_transparent("50eggs.png")
