% ���ٶ�ʵ��PD����
% ����������ź�ɲ�����б궨�����ݳ�����errorȷ�����š�ɲ��λ�õĴ�С����dt���������ݸ�speed��ʵ������ɲ���Ŀ���
clear;
target_speed = 30;
K_p = 0.5;
K_d = 0.2;
dt = 0.1;
total_time = 10;
time = 0:dt:total_time;
prev_error = 0;
speed = zeros(size(time));
speed(1) = 0; 

for i = 2:length(time)
    error = target_speed - speed(i-1);
    output = K_p * error + K_d * (error - prev_error)/dt;
    speed(i) = speed(i-1) + output * dt;
    prev_error = error;
end

figure;
plot(time, speed);
xlabel('ʱ�� (s)');
ylabel('�ٶ� (m/s)');
title('�����ٶ���ʱ��仯����');
grid on;



