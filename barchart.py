from matplotlib import pyplot as plt

ax,ax1=plt.figure()
x=["Jan","Feb",'Mar','Apr','May','Jun']
y=[5000,8000,11000,6000,3000,9000]

ax.bar(x,height=y)
ax.xlabel("Month")
ax.ylabel("Sales")
ax.show();

x1=["Express",'Superfast','Rajdhani','Humsafar']
y1=[3.5,2.1,2.9,1.8]

ax1.bar(x1,height=y)
ax1.xlabel("Train Category")
ax1.ylabel("Passengers ferried")
ax1.show();

