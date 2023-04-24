from scipy.optimize import linprog
from graphics import draw_graphs

obj= [-1, -1]

lhs_ineq = [[ -1,  -1], [1,  -2], [-3,  2], [3,  -1], [-1,  3]]

rhs_ineq = [-16, 8, 16, 16, 48]

bnd = [(0, 32), (0, 24)]

opt = linprog(c=obj,A_ub=lhs_ineq,b_ub=rhs_ineq,bounds=bnd,method='highs')

print("(", round(opt.x[0]), ", ", round(opt.x[1]), ")", sep='')

draw_graphs(opt)


