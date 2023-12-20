from PIL import Image, ImageDraw
import matplotlib.pyplot as plt


def greyval(pixel):
    return (pixel[0] + pixel[1] + pixel[2]) // 3


image = Image.open("./images/Unequalized_Hawkes_Bay_NZ.jpg")
pix = image.load()

H = [0 for i in range(256)]

for i in range(image.size[0]):
    for j in range(image.size[1]):
        H[greyval(pix[i, j])] += 1

CH = [0 for i in range(256)]

CH[0] = H[0]
for i in range(1, 256):
    CH[i] = CH[i-1] + H[i]

T = [0 for i in range(256)]
for i in range(256):
    T[i] = round((255*CH[i])/(image.size[0]*image.size[1]))

new = Image.new("RGB", image.size)
draw = ImageDraw.Draw(new)
for i in range(image.size[0]):
    for j in range(image.size[1]):
        current_pix_grey_val = T[greyval(pix[i, j])]
        draw.point((i, j), (current_pix_grey_val,
                            current_pix_grey_val, current_pix_grey_val))

new.save("new.jpg", "JPEG")

pix = new.load()
newH = [0 for i in range(256)]
for i in range(image.size[0]):
    for j in range(image.size[1]):
        newH[greyval(pix[i, j])] += 1

fig, (ax1, ax2) = plt.subplots(
    nrows=1, ncols=2,
    figsize=(16, 8)
)
ax1.bar(range(1, 257), H, color='blue')
ax1.set_title('Гистограмма изображения до эквализации')
ax2.bar(range(1, 257), newH, color='green')
ax2.set_title('Гистограмма изображения после эквализации')
plt.show()
