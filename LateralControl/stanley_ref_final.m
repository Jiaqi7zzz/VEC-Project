
path=[cx',cy'];

figure(1)
plot(cx,cy,'LineWidth',2)

ref_x=cx;
ref_y=cy;

dif_x=diff(ref_x);
dif_xxxx=[dif_x,dif_x(end)];

dif_y=diff(ref_y);
dif_yyyy=[dif_y,dif_y(end)];

r_yaw = atan2(dif_yyyy , dif_xxxx);

figure(2)
plot(cx,r_yaw )
