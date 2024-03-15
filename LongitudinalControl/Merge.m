v2=[v,vbr];
a2=[a,abr];
br2=[tr,br];
F=scatteredInterpolant(v2',a2',br2');%转成列向量
vumer=0:0.05:50;
aumer=-8:0.05:5;
tablemer=zeros(length(vumer),length(aumer));
for i=1:length(vumer)
    for j=1:length(aumer)
        tablemer(i,j)=F(vumer(i),aumer(j));
    end
end