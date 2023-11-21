import pygame
import openpyxl as px
import time

pygame.init()

dsx = 1350
dsy = 650
display_screen = pygame.display.set_mode((dsx, dsy))
pygame.display.set_caption("Design and Analysis Algorithms Project")

t_color = (29, 52, 97)
bg_color = (191, 237, 239)
font = pygame.font.Font('freesansbold.ttf', 40)
font1 = pygame.font.Font('freesansbold.ttf', 32)
foph = pygame.font.Font('freesansbold.ttf', 50)
fopb = pygame.font.Font('freesansbold.ttf', 40)
finb = pygame.font.SysFont('calibri',20)
intro = [font.render('Design and Analysis of Algorithms Project', True, t_color),font1.render('Done By: Arooba Moin (20K-0213) & Sabah Mawani (20K-0393)', True, t_color)]
options = [foph.render('Options',True,t_color),fopb.render('a. Insertion Sort',True,t_color),fopb.render('b. Bubble Sort',True,t_color),fopb.render('c. Merge Sort',True,t_color),fopb.render('d. Heap Sort',True,t_color),fopb.render('e. Quick Sort',True,t_color),fopb.render('f. Radix Sort',True,t_color),fopb.render('g. Bucket Sort',True,t_color),fopb.render('h. Counting Sort',True,t_color),fopb.render('i. Quick Sort adaptation',True,t_color),fopb.render('j. Counting Sort adaptation',True,t_color)]
inputa = [foph.render('Insertion Sort Input Files: ',True,t_color),finb.render('1.[463, 123, 394, 467, 258, 99, 274, 312, 379, 433, 280, 218, 51, 446, 119, 164, 194, 105, 459, 477, 91, 493, 404, 52, 292]',True,t_color),finb.render('2.[109, 211, 27, 183, 283, 242, 36, 129, 155, 47, 193, 456, 44, 245, 421, 370, 208, 340, 131, 344, 342, 389, 142, 229, 386]',True,t_color),finb.render('3.[284, 440, 382, 375, 464, 199, 239, 113, 169, 497, 74, 203, 396, 369, 87, 76, 48, 28, 289, 173, 324, 366, 384, 173, 477]',True,t_color),finb.render('4.[65, 150, 318,265, 493, 387, 312, 140, 240, 326, 175, 224, 427, 314, 88, 432, 176, 447, 398, 66, 458, 208, 466, 191, 494]',True,t_color),finb.render('5.[119, 207, 144, 351, 474, 148, 50, 478, 278, 276, 299, 285, 218, 248, 97, 64, 466, 461, 305, 488, 367, 192, 128, 410, 414]',True,t_color)]
inputb = [foph.render('Bubble SortInput Files: ',True,t_color),finb.render('1.[223, 287, 66, 471, 128, 85, 270, 89, 50, 496, 339, 324, 51, 90, 41, 64, 11, 216, 54, 275, 280, 139, 390, 486, 281]',True,t_color),finb.render('2.[31, 437, 236, 303, 68, 437, 390, 55, 196, 234, 477, 48, 319, 68, 265, 375, 64, 53, 294, 344, 123,  348, 143, 202, 276]',True,t_color),finb.render('3.[182, 316, 145, 473, 18, 389, 388, 200, 477, 53, 322, 206, 404, 112, 485, 286, 205, 368, 375, 232, 279, 96, 307, 219, 215]',True,t_color),finb.render('4.[266, 417, 68, 228, 360, 218, 35, 376, 214, 231, 262, 120, 463, 222, 253, 10, 380, 224, 252, 259, 128, 174, 81, 258, 132]',True,t_color),finb.render('5.[475, 425, 58, 379, 152, 101, 358, 20, 366, 194, 497, 17, 252, 296, 338, 26, 73, 439, 258, 192, 97, 334, 186, 430, 395]',True,t_color)]
inputc = [foph.render('Merge Sort Input Files: ',True,t_color),finb.render('1.[155, 298, 22, 282, 129, 177, 145, 219, 277, 428, 122, 334, 402, 453, 234, 270, 253, 104, 218, 63, 206, 351, 477, 196, 423]',True,t_color),finb.render('2.[433, 209, 109, 180, 274, 117, 493, 134, 120, 25, 452, 382, 406, 138, 103, 230, 441, 275, 444, 443, 291, 146, 416, 245, 324]',True,t_color),finb.render('3.[247, 330, 387, 230, 47, 223, 354, 300, 52, 146, 15, 480, 465, 352, 146, 130, 253, 439, 269, 394, 13, 299, 341, 149, 299]',True,t_color),finb.render('4.[248, 201, 480, 207, 31, 137, 409, 45, 153, 306, 431, 417, 177, 255, 125, 225, 209, 173, 40, 486, 111, 216, 379, 486, 114]',True,t_color),finb.render('5.[86, 332, 65, 72, 393, 121, 36, 203, 351, 331, 338, 256, 167, 494, 179, 368, 297, 316, 200, 386, 248, 381, 308, 128, 292]',True,t_color)]
inputd = [foph.render('Heap Sort Input Files: ',True,t_color),finb.render('1.[84, 160, 391, 477, 409, 165, 256, 53, 229, 181, 197, 228, 382, 177, 444, 489, 254, 100, 244, 235, 347, 429, 126, 340, 274]',True,t_color),finb.render('2.[383, 492, 487, 333, 170, 367, 468, 431, 139, 405, 215, 391, 160, 53, 57, 116, 138, 44, 380, 417, 185, 218, 398, 482, 182]',True,t_color),finb.render('3.[33, 37, 230, 163, 241, 224, 85, 259, 153, 85, 63, 12, 148, 386, 335, 401, 173, 454, 133, 128, 168, 268, 481, 88, 158]',True,t_color),finb.render('4.[60, 88, 327, 293, 487, 192, 231, 305, 380, 462, 42, 443, 171, 89, 349, 331, 119, 476, 111, 219, 331, 247, 348, 112, 169]',True,t_color),finb.render('5.[237, 229, 298, 152, 326, 405, 129, 127, 402, 70, 415, 38, 172, 71, 443, 143, 201, 75, 221, 259, 426, 403, 397, 444, 107]',True,t_color)]
inpute = [foph.render('Quick Sort Input Files: ',True,t_color),finb.render('1.[46, 279, 77, 276, 423, 425, 418, 345, 172, 412, 425, 484, 165, 368, 53, 387, 91, 250, 345, 136, 37, 377, 63, 350, 294]',True,t_color),finb.render('2. [369, 440, 100, 70, 319, 443, 436, 86, 333, 27, 115, 50, 301, 215, 276, 65, 207, 492, 141, 394, 105, 323, 257, 430, 66]',True,t_color),finb.render('3.[272, 485, 68, 54, 399, 470, 372, 431, 19, 490, 122, 228, 329, 160, 282, 334, 44, 132, 306, 472, 238, 180, 417, 361, 429]',True,t_color),finb.render('4.[310, 97, 437, 153, 413, 409, 356, 373, 79, 481, 452, 491, 456, 425, 375, 247, 164, 115, 473, 68, 204, 266, 455, 23, 476]',True,t_color),finb.render('5.[93, 17, 18, 314, 13, 442, 339, 70, 293, 465, 452, 485, 422, 379, 141, 477, 120, 302, 13, 322, 419, 75, 221, 229, 342]',True,t_color)]
inputf = [foph.render('Radix Sort Input Files: ',True,t_color),finb.render('1.[447, 418, 357, 63, 498, 177, 83, 245, 301, 347, 221, 57, 85, 36, 337, 108, 242, 251, 152, 309, 325, 256, 219, 409, 111]',True,t_color),finb.render('2.[186, 211, 192, 316, 106, 391, 23, 150, 317, 325, 218, 157, 311, 431, 242, 321, 368, 22, 445, 351, 464, 457, 360, 289, 227]',True,t_color),finb.render('3.[216, 152, 157, 430, 488, 465, 90, 435, 65, 362, 143, 175, 170, 473, 286, 301, 483, 264, 19, 274, 155, 493, 421, 408, 352]',True,t_color),finb.render('4.[15, 23, 411, 176, 397, 47, 396, 67, 70, 168, 193, 110, 378, 266, 385, 365, 79, 191, 272, 126, 218, 192, 326, 327, 384]',True,t_color),finb.render('5.[454, 120, 346, 339, 100, 254, 176, 212, 379, 154, 128, 60, 419, 213, 126, 141, 34, 29, 469, 16, 496, 337, 358, 379, 452]',True,t_color)]
inputg = [foph.render('Bucket Sort Input Files: ',True,t_color),finb.render('1.[0.103, 0.452, 0.36, 0.111, 0.133, 0.134, 0.387, 0.146, 0.194, 0.054, 0.321, 0.081, 0.448, 0.232, 0.344, 0.227, 0.436,',True,t_color),finb.render('0.251, 0.104, 0.129, 0.343, 0.331, 0.103, 0.166, 0.325]',True,t_color),finb.render('2.[0.437, 0.118, 0.016, 0.093, 0.172,0.019, 0.243, 0.436, 0.007, 0.384, 0.006, 0.38, 0.105, 0.018, 0.262, 0.179, 0.464,', True,t_color),finb.render(' 0.154, 0.244, 0.25, 0.225, 0.458, 0.456, 0.234, 0.34]',True,t_color),finb.render('3.[0.182, 0.022, 0.284, 0.101, 0.286, 0.087, 0.481, 0.464, 0.322, 0.007, 0.25, 0.255, 0.216, 0.327, 0.293, 0.434, 0.127,', True, t_color) ,finb.render('0.451, 0.292, 0.315, 0.09, 0.158, 0.371, 0.098, 0.233]',True,t_color),finb.render('4.[0.238, 0.358, 0.035, 0.118, 0.5, 0.203, 0.13,0.119, 0.146, 0.445, 0.089, 0.333, 0.061, 0.445, 0.463, 0.402, 0.339,',True,t_color),finb.render('0.245, 0.39, 0.123, 0.436, 0.198, 0.253, 0.351, 0.448]',True,t_color),finb.render('5.[0.052, 0.07, 0.429, 0.325, 0.127, 0.004, 0.395, 0.167, 0.238, 0.434, 0.071, 0.081, 0.365, 0.418, 0.165, 0.452,',True,t_color), finb.render('0.208, 0.28, 0.365, 0.188, 0.389, 0.498, 0.318, 0.44, 0.332]',True,t_color)]
inputh = [foph.render('Counting Sort Input Files: ',True,t_color),finb.render('1.[239, 102, 195, 44, 150, 457,492, 318, 425, 80, 407, 244, 11, 39, 435,  444, 72, 364, 302,30, 239, 384, 378, 215, 180]',True,t_color),finb.render('2.[465, 383, 452, 168, 120, 179, 459, 325, 322, 403, 21, 383, 338, 492, 470, 72, 337, 21, 87, 448, 157, 383, 10, 218, 439]',True,t_color),finb.render('3.[72, 413, 442, 93, 424, 183,54, 330,389, 194,304, 119, 492, 279, 193, 261, 58, 394, 72, 288, 239, 112, 254, 444, 316]',True,t_color),finb.render('4.[237, 34, 312, 493, 63, 22,469, 218, 264,233, 350, 480, 266, 354, 164, 453,219, 451, 142, 149, 362, 112, 202, 275, 458]',True,t_color),finb.render('5.[321, 434, 257, 348, 353, 220, 18, 340, 363, 452, 463, 347, 226, 108, 154, 235, 263, 50, 275, 253, 438, 263, 25, 167, 369]',True,t_color)]
inputi = [foph.render('Quick Sort Adaptation Input Files: ',True,t_color),finb.render('1.[351, 411, 45, 43, 319, 161, 175, 386, 361, 424, 448, 349, 343, 154, 89,209, 17, 289, 473, 324, 163, 12, 31, 480, 489]',True,t_color),finb.render('2.[288, 486, 464, 443, 498, 263, 11, 473, 303, 50, 403, 282, 51, 47, 375, 74, 138, 136, 435, 191,217, 127, 109, 178, 43]',True,t_color),finb.render('3.[278, 254, 328, 318, 286, 389, 495, 248, 234, 217, 379, 298, 274, 317, 176, 346, 107,429, 348, 11, 409, 31, 131, 56, 354]',True,t_color),finb.render('4.[177, 81, 340, 203, 32, 21,54, 366, 220, 192, 12, 234, 144, 335, 208, 257, 189, 30, 358, 374, 201, 337, 278, 184, 292]',True,t_color),finb.render('5.[81, 404, 399, 369, 258, 449, 38, 20, 391, 211, 479, 487, 128, 123, 324, 454, 500, 496, 257, 129, 224, 411, 326, 328, 108]',True,t_color)]
inputj = [foph.render('Counting Sort Adaptation Input Files: ',True,t_color),finb.render('1.[278, 153, 330, 416, 56, 218, 253, 244, 101, 237, 115, 385, 263, 101, 270, 448, 425, 106, 68, 138, 19, 400, 124, 129, 420]',True,t_color),finb.render('2.[355, 446, 76, 191,496, 295, 495, 92, 447, 56, 21, 391, 329,122, 273, 314, 59, 143, 402, 299, 39, 61, 142, 142, 187]',True,t_color),finb.render('3.[291, 212, 345, 26, 282, 439, 141, 305, 357, 139, 400, 499, 215, 129, 66, 449, 424, 445, 324, 443, 391, 32, 237, 413, 40]',True,t_color),finb.render('4.[482, 337, 105, 37, 44, 268, 65, 246, 241, 434, 119,124, 140, 392, 312, 32, 146, 408, 259, 146, 133, 41, 398, 468, 500]',True,t_color),finb.render('5.[311, 265, 369, 183, 289, 149, 461, 319, 233, 342, 66, 145, 396, 252, 168, 241, 286, 456,347, 435, 48, 86, 163, 436, 466]',True,t_color)]

x = 40
y = 40
width = 40

run = True

def show(height,z,t):
	for i in range(len(height)):
		if i == z:
			pygame.draw.rect(display_screen, (29, 52, 97), (x + 51 * i, y, width, height[i]))
		elif i==t:
			pygame.draw.rect(display_screen, (139, 38, 53), (x + 51 * i, y, width, height[i]))
		else:
			pygame.draw.rect(display_screen, (66, 106, 90), (x + 51 * i, y, width, height[i]))
   
def show1(height,z,t):
	for i in range(len(height)):
		if i == z:
			pygame.draw.rect(display_screen, (29, 52, 97), (x + 51 * i, y, width, height[i]*1000))
		elif i==t:
			pygame.draw.rect(display_screen, (139, 38, 53), (x + 51 * i, y, width, height[i]*1000))
		else:
			pygame.draw.rect(display_screen, (66, 106, 90), (x + 51 * i, y, width, height[i]*1000))

def show2(height,z,t,s):

	for i in range(len(height)):
		if i == z:
			pygame.draw.rect(display_screen, (29, 52, 97), (x + 51 * i, y, width, height[i]))
		elif i==t:
			pygame.draw.rect(display_screen, (139, 38, 53), (x + 51 * i, y, width, height[i]))
		elif i == s:
			pygame.draw.rect(display_screen, (0,0,0), (x + 51 * i, y, width, height[i]))
		else:
			pygame.draw.rect(display_screen, (66, 106, 90), (x + 51 * i, y, width, height[i]))

def dispinput(schar):
    if schar == 'a':
        display_screen.fill(bg_color)
        display_screen.blit(inputa[0], (50,200))
        display_screen.blit(inputa[1],(50,300))
        display_screen.blit(inputa[2],(50,350))
        display_screen.blit(inputa[3],(50,400))
        display_screen.blit(inputa[4],(50,450))
        display_screen.blit(inputa[5],(50,500))
        pygame.display.update()
        pygame.time.delay(10)
    if schar == 'b':
        display_screen.fill(bg_color)
        display_screen.blit(inputb[0], (50,200))
        display_screen.blit(inputb[1],(50,300))
        display_screen.blit(inputb[2],(50,350))
        display_screen.blit(inputb[3],(50,400))
        display_screen.blit(inputb[4],(50,450))
        display_screen.blit(inputb[5],(50,500))
        pygame.display.update()
        pygame.time.delay(10)
    if schar == 'c':
        display_screen.fill(bg_color)
        display_screen.blit(inputc[0], (50,200))
        display_screen.blit(inputc[1],(50,300))
        display_screen.blit(inputc[2],(50,350))
        display_screen.blit(inputc[3],(50,400))
        display_screen.blit(inputc[4],(50,450))
        display_screen.blit(inputc[5],(50,500))
        pygame.display.update()
        pygame.time.delay(10)
    if schar == 'd':
        display_screen.fill(bg_color)
        display_screen.blit(inputd[0], (50,200))
        display_screen.blit(inputd[1],(50,300))
        display_screen.blit(inputd[2],(50,350))
        display_screen.blit(inputd[3],(50,400))
        display_screen.blit(inputd[4],(50,450))
        display_screen.blit(inputd[5],(50,500))
        pygame.display.update()
        pygame.time.delay(10)
    if schar == 'e':
        display_screen.fill(bg_color)
        display_screen.blit(inpute[0], (50,200))
        display_screen.blit(inpute[1],(50,300))
        display_screen.blit(inpute[2],(50,350))
        display_screen.blit(inpute[3],(50,400))
        display_screen.blit(inpute[4],(50,450))
        display_screen.blit(inpute[5],(50,500))
        pygame.display.update()
        pygame.time.delay(10)
    if schar == 'f':
        display_screen.fill(bg_color)
        display_screen.blit(inputf[0], (50,200))
        display_screen.blit(inputf[1],(50,300))
        display_screen.blit(inputf[2],(50,350))
        display_screen.blit(inputf[3],(50,400))
        display_screen.blit(inputf[4],(50,450))
        display_screen.blit(inputf[5],(50,500))
        pygame.display.update()
        pygame.time.delay(10)
    if schar == 'g':
        display_screen.fill(bg_color)
        display_screen.blit(inputg[0], (50,100))
        display_screen.blit(inputg[1],(50,200))
        display_screen.blit(inputg[2],(50,225))
        display_screen.blit(inputg[3],(50,275))
        display_screen.blit(inputg[4],(50,300))
        display_screen.blit(inputg[5],(50,350))
        display_screen.blit(inputg[6],(50,375))
        display_screen.blit(inputg[7],(50,425))
        display_screen.blit(inputg[8],(50,450))
        display_screen.blit(inputg[9],(50,500))
        display_screen.blit(inputg[10],(50,525))
        pygame.display.update()
        pygame.time.delay(10)
    if schar == 'h':
        display_screen.fill(bg_color)
        display_screen.blit(inputh[0], (50,200))
        display_screen.blit(inputh[1],(50,300))
        display_screen.blit(inputh[2],(50,350))
        display_screen.blit(inputh[3],(50,400))
        display_screen.blit(inputh[4],(50,450))
        display_screen.blit(inputh[5],(50,500))
        pygame.display.update()
        pygame.time.delay(10)
    if schar == 'i':
        display_screen.fill(bg_color)
        display_screen.blit(inputi[0], (50,200))
        display_screen.blit(inputi[1],(50,300))
        display_screen.blit(inputi[2],(50,350))
        display_screen.blit(inputi[3],(50,400))
        display_screen.blit(inputi[4],(50,450))
        display_screen.blit(inputi[5],(50,500))
        pygame.display.update()
        pygame.time.delay(10)
    if schar == 'j':
        display_screen.fill(bg_color)
        display_screen.blit(inputj[0], (50,200))
        display_screen.blit(inputj[1],(50,300))
        display_screen.blit(inputj[2],(50,350))
        display_screen.blit(inputj[3],(50,400))
        display_screen.blit(inputj[4],(50,450))
        display_screen.blit(inputj[5],(50,500))
        pygame.display.update()
        pygame.time.delay(10)
    choice = True
    while choice:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                choice = False
            elif keys[pygame.K_1]:
                return 'A'
            elif keys[pygame.K_2]:
                return 'B'
            elif keys[pygame.K_3]:
                return 'C'
            elif keys[pygame.K_4]:
                return 'D'
            elif keys[pygame.K_5]:
                return 'E'
 
def inputFile (schar):
    arr = []
    sheets=['Insertion','Bubble','Merge','Heap','Quick','Radix','Bucket','Counting','Qadap','Cadap']
    choices=['a','b','c','d','e','f','g','h','i','j']
    for i in range (10):
        if schar == choices[i]:
            char = dispinput(schar)
            book = px.load_workbook('input.xlsx')
            sheet = book[sheets[i]]
            for j in range (1,26):
                index = str(j)
                cell = char+index
                if schar=='g':
                    arr.append(float(sheet[cell].value))
                else:
                    arr.append(int(sheet[cell].value))
    return arr

def callinsert():
    start=time.time()
    arr = inputFile('a')
    insertionSort(arr)
    display_screen.fill((191, 237, 239))
    show(arr,-1,-1)
    pygame.time.delay(50)
    pygame.display.update()
    end=time.time()
    print("Time taken by insertion sort: ",end-start)

def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while j >=0 and temp < arr[j] :
            arr[j+1] = arr[j]
            j-=1
            arr[j+1] = temp
            display_screen.fill((191, 237, 239))
            show(arr,i,j)
            pygame.time.delay(50)
            pygame.display.update()

def mergecall():
    start=time.time()
    arr = inputFile('c')
    mergeSort(arr,0,len(arr)-1)
    display_screen.fill((191, 237, 239))
    show(arr,-1,-1)
    pygame.time.delay(50)
    pygame.display.update()
    end=time.time()
    print("Time taken by merge sort: ",end-start)

def mergeSort(arr,low,high):
    if low>=high:
        return
    mid = (low+high)//2
    mergeSort(arr,low,mid)
    mergeSort(arr,mid+1,high)
    merge(arr,low,mid,high)
    
def merge(arr,low,mid,high):
    subarr1 = mid-low+1
    subarr2 = high-mid
    larr=[0]*subarr1
    rarr=[0]*subarr2
    for i in range (subarr1):
        larr[i] = arr[low+i]
        display_screen.fill((191, 237, 239))
        show(arr,low+i,-1)
        pygame.time.delay(50)
        pygame.display.update()
    for j in range (subarr2):
        rarr[j] = arr[mid+1+j]
        display_screen.fill((191, 237, 239))
        show(arr,mid+1+j,-1)
        pygame.time.delay(50)
        pygame.display.update()
    index1 = 0
    index2 = 0
    m_index = low
    while index1<subarr1 and index2<subarr2:
        if larr[index1] <= rarr[index2]:
            arr[m_index] = larr[index1]
            index1 += 1
            display_screen.fill((191, 237, 239))
            show(arr,-1,m_index)
            pygame.time.delay(50)
            pygame.display.update()
        else:
            arr[m_index] = rarr[index2]
            index2 += 1
            display_screen.fill((191, 237, 239))
            show(arr,-1,m_index)
            pygame.time.delay(50)
            pygame.display.update()
        m_index += 1
        
    while index1 < subarr1:
        arr[m_index] = larr[index1]
        index1 += 1
        display_screen.fill((191, 237, 239))
        show(arr,-1,m_index)
        pygame.time.delay(50)
        pygame.display.update()
        m_index += 1
    while index2 < subarr2:
        arr[m_index] = rarr[index2]
        index2 += 1
        display_screen.fill((191, 237, 239))
        show(arr,-1,m_index)
        pygame.time.delay(50)
        pygame.display.update()
        m_index += 1

def getmax(arr):
	max=0
	for i in range (len(arr)):
		if arr[i]>max:
			max=arr[i]
	return max

def binsertionSort(arr,lower,upper):
    for i in range(lower + 1, upper+1):
        temp = arr[i]
        j = i-1
        while j >=lower and temp < arr[j] :
            arr[j+1] = arr[j]
            j-=1
            arr[j+1] = temp
            display_screen.fill((191, 237, 239))
            show1(arr,i,j)
            pygame.time.delay(50)
            pygame.display.update()
        
def bucketSort():
    start=time.time()
    arr = inputFile('g')
    temp = []
    
    for i in range (10):
        temp.append([])
        
    for i in range (len(arr)):
        temp[int(arr[i]*10)].append(arr[i])
        display_screen.fill((191, 237, 239))
        show1(arr,i,-1)
        pygame.time.delay(50)
        pygame.display.update()
    
    index = 0
    lower = 0
    upper = 0
    for i in range(10):
        j=0
        for j in range(len(temp[i])):
            arr[index] = temp[i][j]
            index += 1
        if j != 0:
            upper = index-1
            binsertionSort(arr,lower,upper)
            lower = j-1
    display_screen.fill((191, 237, 239))
    show1(arr,-1,-1)
    pygame.time.delay(50)
    pygame.display.update()
    end=time.time()
    print("Time taken by bucket sort: ",end-start)
            
def countSort():
    start=time.time()
    arr = inputFile('h')
    max=getmax(arr)
    count=[0]*(max+1)
    output=[0]*len(arr)
    for i in range (len(arr)):
        count[arr[i]] += 1
        display_screen.fill((191, 237, 239))
        show(arr,i,-1)
        pygame.time.delay(50)
        pygame.display.update()
    for i in range (1,max+1):
        count[i] += count[i-1]
    for i in range (len(arr)-1,-1,-1):
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
    for i in range (len(arr)):
        arr[i] = output[i]
        display_screen.fill((191, 237, 239))
        show(arr,-1,i)
        pygame.time.delay(50)
        pygame.display.update()
    display_screen.fill((191, 237, 239))
    show(arr,-1,-1)
    pygame.time.delay(50)
    pygame.display.update()
    end=time.time()
    print("Time taken by count sort: ",end-start)

def countSortadap():
    start=time.time()
    arr = inputFile('j')
    max=getmax(arr)
    count=[0]*(max+1)
    outputa=[0]*len(arr)
    for i in range (len(arr)):
        count[arr[i]] += 1
        display_screen.fill((191, 237, 239))
        show(arr,i,-1)
        pygame.time.delay(50)
        pygame.display.update()
    display_screen.fill((191, 237, 239))
    show(arr,-1,-1)
    pygame.time.delay(50)
    pygame.display.update()
    for i in range (1,max+1):
        count[i] += count[i-1]
    num1=0
    num2=0
    num1=int(input("Enter lower bound: "))
    num2=int(input("Enter upper bound: "))
    while num2>max:
        num2=int(input("Enter valid upper bound: "))
    string1=str(count[num2]-count[num1])
    cadap=fopb.render(string1,True,t_color)
    display_screen.blit(cadap, (50,500))
    pygame.display.flip()
    pygame.time.delay(50)
    end=time.time()
    print("Time taken by count sort adaptation: ",end-start)

def bubbleSort(): 
    start=time.time()
    num = inputFile('b')
    indexing_length = len(num)-1
    sorted= False

    while not sorted: 
        sorted = True 
        for i in range(0,indexing_length): 
            display_screen.fill((191, 237, 239))
            show(num,i,i+1)
            pygame.time.delay(50)
            pygame.display.update()
            if num[i] > num[i+1]: 
                sorted = False 
                num[i],num[i+1]=num[i+1],num[i]
                display_screen.fill((191, 237, 239))
                show(num,i,i+1)
                pygame.time.delay(50)
                pygame.display.update()
        indexing_length -=1
    display_screen.fill((191, 237, 239))
    show(num,-1,-1)
    pygame.time.delay(50)
    pygame.display.update()
    end=time.time()
    print("Time taken by bubble sort: ",end-start)

def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range (low,high):
        display_screen.fill((191, 237, 239))
        show2(arr,i,j,high)
        pygame.time.delay(250)
        pygame.display.update()
        if arr[j] < pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
            display_screen.fill((191, 237, 239))
            show2(arr,i,j,high)
            pygame.time.delay(250)
            pygame.display.update()
    display_screen.fill((191, 237, 239))
    show2(arr,i+1,high,-1)
    pygame.time.delay(50)
    pygame.display.update()
    arr[i+1],arr[high]=arr[high],arr[i+1]
    display_screen.fill((191, 237, 239))
    show2(arr,i+1,high,-1)
    pygame.time.delay(50)
    pygame.display.update()
    return i+1

def quickSort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)

def quickcall():
    start=time.time()
    arr = inputFile('e')
    quickSort(arr,0,len(arr)-1)
    display_screen.fill((191, 237, 239))
    show2(arr,-1,-1,-1)
    pygame.time.delay(50)
    pygame.display.update()
    end=time.time()
    print("Time taken by quick sort: ",end-start)

def heapify(arr, n, i): 
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        display_screen.fill((191, 237, 239))
        show(arr,i,largest)
        pygame.time.delay(150)
        pygame.display.update()
        arr[i], arr[largest] = arr[largest], arr[i]
        display_screen.fill((191, 237, 239))
        show(arr,i,largest)
        pygame.time.delay(150)
        pygame.display.update()
        heapify(arr, n, largest)  
  
def heapSort():
    start=time.time()
    arr = inputFile('d')
    n = len(arr)
    display_screen.fill((191, 237, 239))
    show(arr,-1,-1)
    pygame.time.delay(150)
    pygame.display.update()
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        display_screen.fill((191, 237, 239))
        show(arr,i,0)
        pygame.time.delay(150)
        pygame.display.update()
        arr[i], arr[0] = arr[0], arr[i]
        display_screen.fill((191, 237, 239))
        show(arr,i,0)
        pygame.time.delay(150)
        pygame.display.update()
        heapify(arr, i, 0)
    display_screen.fill((191, 237, 239))
    show(arr,-1,-1)
    pygame.time.delay(150)
    pygame.display.update()
    end=time.time()
    print("Time taken by heap sort: ",end-start)

def countingSort(arr,place):
    k=max(arr)
    count=[0]*(k+1)
    output=[0]*len(arr)
    for i in range (len(arr)):
        count[(arr[i]//place)%10] += 1
        display_screen.fill((191, 237, 239))
        show(arr,i,-1)
        pygame.time.delay(50)
        pygame.display.update()
    for i in range (1,k+1):
        count[i] += count[i-1]
    for i in range (len(arr)-1,-1,-1):
        output[count[(arr[i]//place)%10]-1] = arr[i]
        count[(arr[i]//place)%10] -= 1
    for i in range (len(arr)):
        arr[i] = output[i]
        display_screen.fill((191, 237, 239))
        show(arr,-1,i)
        pygame.time.delay(50)
        pygame.display.update()
    return

def radixSort():
    start=time.time()
    array = inputFile('f')
    max_element = max(array)
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10
    display_screen.fill((191, 237, 239))
    show(array,-1,-1)
    pygame.time.delay(50)
    pygame.display.update()
    end=time.time()
    print("Time taken by radix sort: ",end-start)

def callnewquick():
    start=time.time()
    arr=inputFile('i')
    new_quickSort(arr,0,len(arr)-1)
    display_screen.fill((191, 237, 239))
    show2(arr,-1,-1,-1)
    pygame.time.delay(50)
    pygame.display.update()
    end=time.time()
    print("Time taken by quick sort adaptation: ",end-start)
    

def new_quickSort(arr,low,high):
    while low<high:
        if high-low + 1<10:
            insertionSort(arr)
            break
        else:
            pi=partition(arr,low,high)
            if pi-low<high-pi:
                new_quickSort(arr,low,pi-1)
                low=pi+1
            else: 
                new_quickSort(arr,pi+1,high)
                high=pi-1


display_screen.fill(bg_color)
display_screen.blit(intro[0], (200,250))
display_screen.blit(intro[1],(150,300))
pygame.display.update()
pygame.time.delay(2000)
 
while run:
	execute = False
	op = True
	keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		else:
			display_screen.fill(bg_color)
			display_screen.blit(options[0], (500,50))
			display_screen.blit(options[1],(150,200))
			display_screen.blit(options[2],(150,250))
			display_screen.blit(options[3],(150,300))
			display_screen.blit(options[4],(150,350))
			display_screen.blit(options[5],(150,400))
			display_screen.blit(options[6],(650,200))
			display_screen.blit(options[7],(650,250))
			display_screen.blit(options[8],(650,300))
			display_screen.blit(options[9],(650,350))
			display_screen.blit(options[10],(650,400))
			pygame.display.update()
			pygame.time.delay(10)
			while op:
				wait = False
				key = pygame.key.get_pressed()
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						run = False
						op = False
					if key[pygame.K_a]:
						callinsert()
						wait = True
					if key[pygame.K_b]:
						bubbleSort()
						wait = True
					if key[pygame.K_c]:
						mergecall()
						wait = True
					if key[pygame.K_d]:
						heapSort()
						wait = True
					if key[pygame.K_e]:
						quickcall()
						wait = True
					if key[pygame.K_f]:
						radixSort()
						wait = True
					if key[pygame.K_g]:
						bucketSort()
						wait = True
					if key[pygame.K_h]:
						countSort()
						wait = True
					if key[pygame.K_i]:
						callnewquick()
						wait = True
					if key[pygame.K_j]:
						countSortadap()
						wait = True
					while wait:
						pygame.display.flip()
						key2 = pygame.key.get_pressed()
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								run = False
								op = False
								wait = False
							if key2[pygame.K_q]:
								op = False
								wait = False
pygame.quit()
