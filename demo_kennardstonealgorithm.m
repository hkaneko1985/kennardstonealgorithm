% demonstration of Kennard-Stone algorighm

clear; close all;

numberofsamples = 50;
numberofselectedsamples = 20;

rng default

% generate samples of X-variables for demonstration
X = rand( numberofsamples, 2 );

% select samples using Kennard-Stone algorithm
[ selectedsamplenumbers, remainingsamplenumbers] = kennardstonealgorithm( X, numberofselectedsamples);
disp( 'selected sample numbers' );
disp( selectedsamplenumbers );
disp( '---' );
disp( 'remaining sample numbers' );
disp( remainingsamplenumbers );

% plot samples 
figure;
plot( X(:,1), X(:,2), 'b.', 'markersize', 10 );
hold on;
plot( X(selectedsamplenumbers,1), X(selectedsamplenumbers,2), 'ro', 'markersize', 8 );
hold off;
ylabel( 'x_2' ,  'FontSize' , 20 , 'FontName','Meiryo UI');
xlabel( 'x_1' ,  'FontSize' , 20 , 'FontName','Meiryo UI');
set(gcf, 'Color' , 'w' ); 
set(gca, 'FontSize' , 20);
set(gca, 'FontName','Meiryo UI');
% legend('all samples', 'selected samples','Location', 'northoutside');
legend('all samples', 'selected samples');
