#!/usr/bin/env wolframscript
(* ::Package:: *)

graph1=Row[Table[Plot[{n,n^2,n^3,Exp[n],Factorial[n]},{n,0,10^2},PlotRange->{0,2.5*10^a},AspectRatio->2/1,PlotLabels->"Expressions",PlotLabel->"Complexity O to 100"],{a,{1,3.25,10}}]];

graph2=Plot[{Log2[n],n,n^2,n^3,Exp[n],Factorial[n]},{n,0,100},
PlotRange->{0,5*10^3},AxesOrigin->{0,0},
PlotLabel->"Complexity O(n)",PlotLabels->"Expressions",AxesLabel->{n,N},Epilog->{Inset[Plot[{Log[n],n,n^2,n^3,Exp[n],Factorial[n]},{n,0,10},AspectRatio->0.75,Frame->True,Axes->False,ImageSize->Small],{50,500},ImageScaled[{0,0}]]},
Frame->True,AspectRatio->1]
