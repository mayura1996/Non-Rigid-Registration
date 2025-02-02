# import tkinter.filedialog

# import numpy as np
# from mayavi import mlab


# def model2xyz(model):
#     return model[:, 0], model[:, 1], model[:, 2]


# def model2xyzs(model):
#     return model[:, 0], model[:, 1], model[:, 2], model[:, -1]

# def main():
#     while True:
#         fns = tkinter.filedialog.askopenfilenames(title='选择文件', filetypes=[('所有文件', '.*'), ('文本文件', '.txt')])
#         print(fns)
#         if len(fns) == 0: exit(0)
#         for fn in fns:
#             model1 = np.loadtxt(fn, delimiter=',')
#             model1 = model1[:512]
#             # without labels
#             x, y, z = model2xyz(model1)
#             figure = mlab.figure(bgcolor=(1, 1, 1))
#             mlab.points3d(x, y, z, color=(0.3, 0.3, 1), figure=figure, scale_factor=0.05)

#         # with labels
#         # x,y,z,s=model2xyzs(model1)
#         # figure = mlab.figure(bgcolor=(1,1,1))
#         # mlab.points3d(x,y,z,s,figure=figure,scale_mode="none",scale_factor=0.06)
#         # # mlab.savefig(str(fn).split('.')[0]+".jpg",figure=figure)
#         # mlab.show()
#         mlab.show()

# if __name__ == '__main__':
#     main()



import tkinter.filedialog
import numpy as np
from mayavi import mlab

# Function to extract x, y, z coordinates from the model
def model2xyz(model):
    return model[:, 0], model[:, 1], model[:, 2]

# Function to extract x, y, z coordinates and another property from the model
def model2xyzs(model):
    return model[:, 0], model[:, 1], model[:, 2], model[:, -1]

def main():
    while True:
        # Open a file dialog to select files
        fns = tkinter.filedialog.askopenfilenames(title='Choose Files', filetypes=[('All Files', '.*'), ('Text Files', '.txt')])
        print(fns)
        if len(fns) == 0: exit(0)  # Exit if no files are selected
        for fn in fns:
            model1 = np.loadtxt(fn, delimiter=',')  # Load the data from the file
            model1 = model1[:512]  # Limit to the first 512 rows
            # Without labels
            x, y, z = model2xyz(model1)
            figure = mlab.figure(bgcolor=(1, 1, 1))  # Create a white background figure
            mlab.points3d(x, y, z, color=(0.3, 0.3, 1), figure=figure, scale_factor=0.05)  # Plot the points in blue

        # Uncomment the following lines to include labels in the visualization
        # x, y, z, s = model2xyzs(model1)
        # figure = mlab.figure(bgcolor=(1, 1, 1))
        # mlab.points3d(x, y, z, s, figure=figure, scale_mode="none", scale_factor=0.06)
        # mlab.savefig(str(fn).split('.')[0]+".jpg", figure=figure)
        # mlab.show()

        mlab.show()  # Show the plot

if __name__ == '__main__':
    main()  # Run the main function
