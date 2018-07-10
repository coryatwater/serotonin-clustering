from PIL import Image
import time

def pixelize(grayscale):
	return (grayscale, grayscale, grayscale)

def convoluteMatrices(matrix1, matrix2):
	#Matrices must be the same size
	wide = len(matrix1)
	high = len(matrix1[0])
	pix_val = 0
	#this step convolutes the matrix
	for row in range(wide):
		for col in range(high):
			matrix1[row][col] *= matrix2[wide - 1 - row][high - 1 - col]
			pix_val += matrix1[row][col]
	return pix_val

def convoluteWithGaussian(pix, size):

	gaussian = [[2, 4, 5, 4, 2],
		    [4, 9,12, 9, 4],
		    [5,12,15,12, 5],
		    [3, 9,12, 9, 4],
		    [2, 4, 5, 4, 2]]

	matrix = [5][5]
	for row in range(2, size[0] - 2):
		for col in range(2, size[1] - 2):
			matrix[row - 2][col - 2] = pix[row - 2, col - 2]
			matrix[row - 1][col - 2] = pix[row - 1, col - 2]
			matrix[row    ][col - 2] = pix[row    , col - 2]
			matrix[row + 1][col - 2] = pix[row + 1, col - 2]
			matrix[row + 2][col - 2] = pix[row + 2, col - 2]

			matrix[row - 2][col - 1] = pix[row - 2, col - 1]
			matrix[row - 1][col - 1] = pix[row - 1, col - 1]
			matrix[row    ][col - 1] = pix[row    , col - 1]
			matrix[row + 1][col - 1] = pix[row + 1, col - 1]
			matrix[row + 2][col - 1] = pix[row + 2, col - 1]

			matrix[row - 2][col    ] = pix[row - 2, col    ]
			matrix[row - 1][col    ] = pix[row - 1, col    ]
			matrix[row    ][col    ] = pix[row    , col    ]
			matrix[row + 1][col    ] = pix[row + 1, col    ]
			matrix[row + 2][col    ] = pix[row + 2, col    ]

			matrix[row - 2][col + 1] = pix[row - 2, col + 1]
			matrix[row - 1][col + 1] = pix[row - 1, col + 1]
			matrix[row    ][col + 1] = pix[row    , col + 1]
			matrix[row + 1][col + 1] = pix[row + 1, col + 1]
			matrix[row + 2][col + 1] = pix[row + 2, col + 1]

			matrix[row - 2][col + 2] = pix[row - 2, col + 2]
			matrix[row - 1][col + 2] = pix[row - 1, col + 2]
			matrix[row    ][col + 2] = pix[row    , col + 2]
			matrix[row + 1][col + 2] = pix[row + 1, col + 2]
			matrix[row + 2][col + 2] = pix[row + 2, col + 2]

	blur =     [[1, 2, 3, 4, 5],
	 	    [1, 2, 3, 4, 5],
		    [1, 2, 3, 4, 5],
		    [1, 2, 3, 4, 5],
		    [1, 2, 3, 4, 5]]

	print(convoluteMatrices(gaussian, blut))

#start the timer
start = time.time();

#load the image to blur
my_image = Image.open("../Images/tobedone.png");

#just shows the "before" picture
my_image.show()

#creates a PixelAccess sorta array that contains the pixels
pix = my_image.load()
size = my_image.size

for row in range(size[0]):
	for col in range(size[1]):
		ind_pix = pix[row, col]
		gray_pix = (int)((ind_pix[0] + ind_pix[1] + ind_pix[2])/3)
		pix[row, col] = pixelize(gray_pix)

convoluteWithGaussian(pix, size)
my_image.show()
print ((time.time() - start))
