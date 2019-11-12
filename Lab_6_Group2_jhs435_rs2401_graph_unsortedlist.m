n = [5000, 10000, 15000,20000,25000];

# Set vectors for the results of each algorithm


exp_time1_bo3=[0.005144,0.0209,0.0478, 0.08279, 0.1306];
exp_time1_bubble_sort=[0.000949, 0.00288,0.00539,0.01085,0.01226]; 
exp_time1_insort=[0.00176,0.00695,0.0157,0.0277, 0.0451];

% Estimated theoretical C values based on an average of experimental values.


C_1_bo3=0.00000000020678;
C_1_bubble_sort=0.0000000000274;
C_1_insort=0.00000000007025;

% Theoretical Run Times

theory_lm=C_1_bubble_sort* n.^2;
theory_bo3=C_1_bo3*n.^2;
theory_insort=C_1_insort*n.^2;

% Plot all the trends
figure(1)
clf
plot( n, exp_time1_bubble_sort, 'bo')

hold on

plot( n, exp_time1_bo3, 'mo' )
plot( n, exp_time1_insort, 'ko' )

plot( n, theory_bubble_sort, 'b-')


hold off

% Make a legend for the trends
legend(  'experimental best of 3', 'experimental bubble sort', 'experimental insertion sort', 
'theory bo3', 'theory bubble sort', 'theory insertion sort','Location', 'northwest' )
axis tight