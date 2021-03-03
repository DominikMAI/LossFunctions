import sympy as sy
from sympy.plotting import plot
from sympy.plotting import plot3d,plot3d_parametric_surface
from sympy.abc import i, k, m, n, x

x = sym.Symbol('x')
y = sym.Symbol('y')

f = sy.Function('f')(x,y)

y, yp, N = sym.symbols('y_i, y^p_i, N')

MSE =  1/n * sy.Sum((y - yp)**2, (i, 1 , n))
MSE

sy.Derivative(MSE, y, yp, 1)

MSE =  1/n * sy.summation((y-yp)**2, (i, 1 , n))
MSE

MSE_diff = sy.diff((y**2 + yp**2)**0.5, y,yp, 1)
MSE_diff

plt.ion()
p1 = plot3d(sy.diff((y**2 + yp**2)**0.5 , y,yp, 1), (y, -5, 5), (yp, -5, 5))
fg, ax = p1._backend.fig, p1._backend.ax
plt.rcParams["figure.figsize"] = (20,10)
ax[0].axis('tight')
#ax[0].set_aspect('auto') # 'auto', 'equal' or a positive integer is allowed
ax[0].grid(True)
ax[0].view_init(100, 150)
plt.draw()
plt.ion()
plt.show()
