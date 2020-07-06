---
title: Sweep Line
author: Ren Zhang
date: June-26-2020
---  

# Sweep Line  

## Remarks 
+ It is more of a way of approaching problems than an algorithm.
+ It generally means that We will process data in some kind of order, and once we processed one piece of data, we won't go back anymore. 
+ Sweep a line across problem space, events of interest popsup, keep track of these events.
+ Deal with the events at the line and be done with it. 
+ The information about past events can be summarized in various format to handle new events. Example can be past min/max etc for single reference, a monotone stack or a priority queue for multi past events. 
+ Given a problem, there might be more than one way to define what is a event, which can lead to different solutions.  

## Common Problems  
+ Segment intersection. 1D
+ Rectangle intersection. 2D

