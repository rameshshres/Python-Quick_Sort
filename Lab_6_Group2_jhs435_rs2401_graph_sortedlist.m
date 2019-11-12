n = [5000, 10000, 15000,20000,25000];

# Set vectors for the results of each algorithm

exp_time1_lm=[0.00523,0.0205,0.0496,0.0864,0.134];
exp_time1_bo3=[0.00508,0.0206,0.0464, 0.0841,0.130];
exp_time1_ninther=[0.0503,0.0201,0.0485,0.0831,0.128]; 
exp_time1_insort=[0.00071,0.0029,0.00613,0.01096,0.0179];

% Estimated theoretical C values based on an average of experimental values.

C_1_lm=0.0000000002146;
C_1_bo3=0.000000000208;
C_1_ninther=0.0000000002064;
C_1_insort=0.00000000002812;

% Theoretical Run Times

theory_lm=C_1_lm* n .^2;
theory_bo3=C_1_bo3*n .^2;
theory_ninther=C_1_ninther*n .^2;
theory_insort=C_1_insort*n .^2;

% Plot all the trends
figure(1)
clf
plot( n, exp_time1_lm, 'ro' )

hold on
plot( n, exp_time1_bo3, 'bo')
plot( n, exp_time1_ninther, 'mo' )
plot( n, exp_time1_insort, 'ko' )
plot( n, theory_lm, 'k-')
plot( n, theory_bo3, 'b-')
plot( n, theory_ninther, 'r-')
plot( n, theory_insort, 'y-')

hold off

% Make a legend for the trends
legend( 'experimental left most', 'experimental best of 3', 'experimental ninther', 'experimental insertion sort','theory lm', 
'theory bo3', 'theory ninther', 'theory insertion sort','Location', 'northwest' )

% Format axes and title
xlabel( ' list length n ' )
ylabel( 'run time f(n) in sec' )
title( 'Comparison between Quick sort and Insertion sort of Sorted list  ' )

set( gcf, 'Color', [ 1 1 1 ] )

% Plot all the trends on a loglog plot.
figure(2)
clf
loglog( n, exp_time1_lm, 'bo' )

hold on
loglog( n, exp_time1_bo3, 'ro')
loglog( n, exp_time1_ninther, 'go' )
loglog( n, exp_time1_insort, 'ko' )
loglog( n, theory_lm, 'k-')
loglog( n, theory_bo3, 'b-')
loglog( n, theory_ninther, 'g-')
loglog( n, theory_insort, 'r-')
hold off
%set axis label
xlabel('log(n)')
ylabel('log(f(n))')
%set axis title
title('Compare Quicksort and insertion sort of sorted list in log-log Axes ')
%set axis legend

legend( 'experimental left most', 'experimental best of 3', 'experimental ninther', 'experimental insertion sort','theory lm', 
'theory bo3', 'theory ninther', 'theory insertion sort','Location', 'northwest' )

axis tight