brake=0;% 初始化刹车
for i=1:80

    sim('Throttle.slx');
    v_temp1(:,i) = ans.Vx(:,2);
    a_temp1(:,i) = ans.Ax(:,2);
    brake_temp1(:,i)=ones(length(ans.Vx(:,2)),1)*brake;
    brake=brake-0.1;% 刹车从0开始，每次增加0.1，一直增加到8
    % 消除奇异性
    for j = 1:length(v_temp1(:,i))
        if v_temp1(j,i)<0.001
            brake_temp1(j,i) = 0;
        end
    end
end


% 合并，一定要转成行向量再合并，否则会导致合并失败
vbr=v_temp1(:,1)';
abr=a_temp1(:,1)';
br=brake_temp1(:,1)';
for i=2:80
    vbr=[vbr,v_temp1(:,i)'];
    abr=[abr,a_temp1(:,i)'];
    br=[br,brake_temp1(:,i)'];
end
% 拟合
% F=scatteredInterpolant(vbr',abr',br');%转成列向量
% vubr=0:0.05:50;%虽然是减速，但是matlab需要单调递增
% aubr=-8:0.05:0;%加速度从负开始
% tablebr=zeros(length(vubr),length(aubr));
% for i=1:length(vubr)
%     for j=1:length(aubr)
%         tablebr(i,j)=F(vubr(i),aubr(j));
%     end
% end