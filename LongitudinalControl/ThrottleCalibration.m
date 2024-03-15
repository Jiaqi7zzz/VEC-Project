clear;

% 初始化油门开度
thr= 0 ;

for i = 1:21
    sim('Throttle.slx');

    v_temp(:,i) = ans.Vx(:,2);
    a_temp(:,i) = ans.Ax(:,2);
    thr_temp(:,i)=ones(length(ans.Vx(:,2)),1)*thr;
    thr = thr + 0.05;
end

% 修整不合理的数据
v_temp(:,1) = 0;
a_temp(:,1) = 0;

v=v_temp(:,1)';
a=a_temp(:,1)';
tr=thr_temp(:,1)';

for i=2:11
    v=[v,v_temp(:,i)'];
    a=[a,a_temp(:,i)'];
    tr=[tr,thr_temp(:,i)'];
end 
%拟合
% F=scatteredInterpolant(v',a',tr');
% vu=0:0.1:50;
% au=0:0.1:5;
% table=zeros(length(vu),length(au));
% for i=1:length(vu)
%     for j=1:length(au)
%         table(i,j)=F(vu(i),au(j));
%     end
% end
