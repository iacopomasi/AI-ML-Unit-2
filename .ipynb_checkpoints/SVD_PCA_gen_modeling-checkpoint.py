import numpy as np
import cv2
import matplotlib.pyplot as plt

# Reproducibility stuff
import random
np.random.seed(42)  # initialize NumPy's RNG
random.seed(0)      # initialize Python's built-in RNG


from matplotlib.colors import ListedColormap
cmap = ListedColormap(['green', 'white', 'red'])
im = np.array([[1,]*50+[2,]*50+[3,]*50 for _ in range(100)]) # 100 x 150
plt.imshow(im, cmap=cmap, interpolation='nearest')
plt.axis('off')
# plt.show() # show the flag

# NOW perform SVD on "im". How many positive singular values you have?
U, S, V = np.linalg.svd(im)


# plot U S and V
fig, axs = plt.subplots(1,3)
axs[0].imshow(U)
axs[1].imshow(np.diag(S))
axs[2].imshow(V)
#plt.show()

# Now write the italian flag as ita = sig*u*v.T, where u = U[:,0], v = V[0,:] and sig = S[0]
# REMEMBER THAT u * v.T is the OUTER PRODUCT between u and v
sig = S[0]
u = U[:,0]
v = V[0,:]
new_ita = sig * (np.outer(u, v))
plt.imshow(new_ita)
#plt.imshow(new_ita, cmap=cmap, interpolation='nearest')    # why does this show the correct colors, but plt.imshow(new_ita) does not?  -> because of the color map!
#plt.show()

# Can you rewrite this for loop : im = np.array([[1,]*50+[2,]*50+[3,]*50 for _ in range(100)]) as an outer product between two vectors?
colors = [[1,]*50+[2,]*50+[3,]*50]
ones = [[1] * 100]
new_ita2 = np.outer(ones, colors)
plt.imshow(new_ita2, cmap=cmap, interpolation='nearest')
plt.show()
