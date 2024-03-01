% 纯速度实现PD控制
% 后续需对油门和刹车进行标定，根据车辆的error确定油门、刹车位置的大小，将dt后的输出传递给speed，实现油门刹车的控制
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
xlabel('时间 (s)');
ylabel('速度 (m/s)');
title('汽车速度随时间变化曲线');
grid on;



