function [ selectedsamplenumbers, remainingsamplenumbers] = kennardstonealgorithm( X, k)
% select samples using Kennard-Stone algorithm
%
% --- input ---
% X : dataset of X-variables (samples x variables)
% k : number of samples to be selected
%
% --- output ---
% selectedsamplenumbers : selected sample numbers (training data)
% remainingsamplenumbers : remaining sample numbers (test data)
% 
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

selectedsamplenumbers = zeros( 1, k);
remainingsamplenumbers = 1 : size( X, 1);
originalX = X;

[~, selectedsamplenumbers(1) ] = max(pdist2(X, mean(X)));
X( selectedsamplenumbers(1), :) = [];
remainingsamplenumbers(selectedsamplenumbers(1)) = [];

for iteration = 1 : k-1
    if iteration == 1
        [~, selectedsamplenumber] = max( pdist2( originalX(selectedsamplenumbers(1:iteration),:), X) );
    else
        [~, selectedsamplenumber] = max( min( pdist2( originalX(selectedsamplenumbers(1:iteration),:), X) ) );
    end
	selectedsamplenumbers(iteration+1) = remainingsamplenumbers(selectedsamplenumber);
    X( selectedsamplenumber, :) = [];
    remainingsamplenumbers(selectedsamplenumber) = [];
end
