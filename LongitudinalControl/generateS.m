
t(1) = 0;
s(1) = 0;

for i = 1:99
    l = sqrt((Path(i+1,1)-Path(i,1))^2+(Path(i+1,2)-Path(i,2))^2);
    s(i+1) = s(i) + l;
    t(i+1) = t(i) + l/v_ref(i);

end
