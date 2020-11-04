perfect(N) :- not(N < 2), (0 is mod(N, 2)), factorChecker(N, 2, 1).

factorChecker(N, Div, Sum) :- not(Div > (N // 2)) -> 
                              (0 is mod(N, Div) -> 
                              (NewDiv is Div+1, NewSum is Sum+Div, 
                              factorChecker(N, NewDiv, NewSum));
                              modulusReject(N, Div, Sum));
                              equal(N, Sum).

modulusReject(N, Div, Sum) :- not(Div > (N // 2)),
                               NewDiv is Div+1, 
                               factorChecker(N, NewDiv, Sum).

equal(N, Sum) :- Sum = N.
