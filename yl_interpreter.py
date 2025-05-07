import sys
import re

s = {}
w = {}

#grids for objects and letters
OBJECTS = {
    'FLOWER':  [
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,1,1,1,0,0,3,3,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,1,1,2,2,1,1,0,3,3,0,0,0,0,0,0,0,0,0],
                [0,0,0,1,2,2,2,2,2,1,3,3,1,1,1,0,0,0,0,0,0,0],
                [0,0,0,1,2,2,2,2,2,3,3,1,1,2,2,1,0,0,0,0,0,0],
                [0,0,0,1,1,2,2,2,1,3,3,1,2,2,2,1,0,0,0,0,0,0],
                [0,0,0,0,1,1,2,1,1,3,3,1,1,2,2,1,5,5,0,0,0,0],
                [0,0,1,1,1,1,1,1,1,3,3,1,2,2,1,5,6,6,6,6,0,0],
                [0,1,2,2,2,2,2,1,1,3,1,1,1,1,1,1,5,5,5,6,5,0],
                [0,1,2,2,2,1,1,1,1,1,1,1,1,2,2,1,1,5,6,5,0,0],
                [0,1,2,2,2,2,2,1,2,1,2,1,2,2,2,2,1,5,5,0,0,0],
                [0,1,2,2,2,1,1,2,2,1,2,1,1,2,2,2,1,0,0,0,0,0],
                [0,1,2,2,1,1,1,2,2,2,2,1,1,1,1,1,0,0,0,0,0,0],
                [0,0,1,1,1,0,1,2,2,2,2,2,1,5,5,5,0,0,0,0,0,0],
                [0,0,0,0,0,0,1,2,2,2,2,1,1,5,5,6,5,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,1,1,5,5,6,5,6,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,5,6,6,6,6,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,5,5,5,5,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ],
    'BOW':     [
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0],
                [0,0,0,1,2,2,2,2,1,0,1,1,0,1,2,2,2,2,1,0,0,0],
                [0,0,0,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,1,0,0,0],
                [0,0,0,1,2,2,2,1,1,1,2,2,1,1,1,2,2,2,1,0,0,0],
                [0,0,0,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,1,0,0,0],
                [0,0,0,1,2,2,2,2,1,2,1,1,2,1,2,2,2,2,1,0,0,0],
                [0,0,0,0,1,1,1,1,2,1,0,0,1,2,1,1,1,1,0,0,0,0],
                [0,0,0,0,0,1,2,2,2,1,0,0,1,2,2,2,1,0,0,0,0,0],
                [0,0,0,0,1,2,2,2,1,0,0,0,0,1,2,2,2,1,0,0,0,0],
                [0,0,0,1,2,2,2,2,1,0,0,0,0,1,2,2,2,2,1,0,0,0],
                [0,0,0,0,1,1,2,1,0,0,0,0,0,0,1,2,1,1,0,0,0,0],
                [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ],
    'STAR': [
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0,0,0,0],
                [0,0,0,0,0,0,0,0,1,2,2,1,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,1,2,2,1,0,0,0,0,0,0,0,0],
                [0,0,0,0,1,1,1,1,2,2,2,2,1,1,1,1,0,0,0,0],
                [0,0,0,0,1,2,2,2,2,2,2,2,2,2,2,1,0,0,0,0],
                [0,0,0,0,0,1,2,2,2,2,2,2,2,2,1,0,0,0,0,0],
                [0,0,0,0,0,0,1,2,2,2,2,2,2,1,0,0,0,0,0,0],
                [0,0,0,0,0,0,1,2,2,2,2,2,2,1,0,0,0,0,0,0],
                [0,0,0,0,0,1,2,2,2,2,2,2,2,2,1,0,0,0,0,0],
                [0,0,0,1,0,1,2,2,2,1,1,2,2,2,1,0,0,0,0,0],
                [0,0,0,0,0,1,2,2,1,0,0,1,2,2,1,0,0,0,0,0],
                [0,0,1,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0],
                [0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ],
    'BUTTERFLY': [
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
                [0,0,0,1,2,2,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,2,2,1,0,0,0],
                [0,0,0,0,1,2,2,2,1,0,0,0,0,0,0,0,0,0,1,2,2,2,1,0,0,0,0],
                [0,0,0,0,1,2,3,3,2,1,0,0,0,0,0,0,0,1,2,3,3,2,1,0,0,0,0],
                [0,0,0,0,0,1,2,3,3,2,1,0,0,0,0,0,1,2,3,3,2,1,0,0,0,0,0],
                [0,0,0,0,0,1,2,3,3,3,2,1,0,0,0,1,2,3,3,3,2,1,0,0,0,0,0],
                [0,0,0,0,0,1,2,3,3,3,3,1,0,1,0,1,3,3,3,3,2,1,0,0,0,0,0],
                [0,0,0,0,0,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0],
                [0,0,0,0,0,0,1,2,3,3,3,2,1,0,1,2,3,3,3,2,1,0,0,0,0,0,0],
                [0,0,0,0,0,1,2,3,3,0,0,0,1,0,1,0,0,0,3,3,2,1,0,0,0,0,0],
                [0,0,0,0,0,1,2,3,0,0,0,0,1,1,1,0,0,0,0,3,2,1,0,0,0,0,0],
                [0,0,0,0,0,1,2,0,0,0,0,1,0,1,0,1,0,0,0,0,2,1,0,0,0,0,0],
                [0,0,0,0,0,1,2,0,0,2,2,1,0,1,0,1,2,2,0,0,2,1,0,0,0,0,0],
                [0,0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ]
}
LETTERS = {
   'A': [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,1,1,1,0,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,0,0,0,0,0,0,0,0,0],
],
	'B': [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,1,1,1,1,1,0,0],
        [0,1,1,1,1,1,1,1,0,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0],
], 
	'C': [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,0,0,0,0,0,0,0],
        [0,1,1,0,0,0,0,0,0,0],
        [0,1,1,0,0,0,0,0,0,0],
        [0,1,1,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,0,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0],
],
	'D': [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,1,1,1,1,1,0,0],
        [0,1,1,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0],
], 
	'E': [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0],
],
	'F': [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,0,0,0,0,0,0,0],
        [0,1,1,0,0,0,0,0,0,0],
        [0,1,1,0,0,0,0,0,0,0],   
        [0,0,0,0,0,0,0,0,0,0],
],
	
	'G': [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,1,1,1,0,0],
        [0,1,1,1,1,1,1,1,0,0],
        [0,1,1,0,0,0,0,0,0,0],
        [0,1,1,0,0,0,0,0,0,0],
        [0,1,1,0,0,1,1,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,0,1,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0],
],
	'H': [
        [0,0,0,0,0,0,0,0,0,0],
	    [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,0,0,0,0,0,0,0,0,0],
],
	'I': [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0],
],
	'J': [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,1,1,0,1,1,0,0,0,0],
        [0,1,1,1,1,1,0,0,0,0],
        [0,0,1,1,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
],
	'K': [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,1,1,0,0],
        [0,1,1,0,0,1,1,0,0,0],
        [0,1,1,1,1,1,0,0,0,0],
        [0,1,1,1,1,1,0,0,0,0],
        [0,1,1,0,0,1,1,0,0,0],
        [0,1,1,0,0,0,1,1,0,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,0,0,0,0,0,0,0,0,0],
],
	'L': [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,1,0,0,0,0,0,0,0],
        [0,1,1,0,0,0,0,0,0,0],
        [0,1,1,0,0,0,0,0,0,0],
        [0,1,1,0,0,0,0,0,0,0],
        [0,1,1,0,0,0,0,0,0,0],
        [0,1,1,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0],
],
    'M': [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,1,0,0,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,0,1,1,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,0,0,0,0,0,0,0,0,0],
],
    'N': [
        [0,0,0,0,0,0,0,0,0,0],
	    [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,1,0,0,0,1,1,0],
        [0,1,1,1,1,0,0,1,1,0],
        [0,1,1,0,1,1,0,1,1,0],
        [0,1,1,0,0,1,1,1,1,0],
        [0,1,1,0,0,0,1,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,0,0,0,0,0,0,0,0,0],
],
	'O': [
        [0,0,0,0,0,0,0,0,0,0],
	    [0,0,0,1,1,1,1,0,0,0],
        [0,0,1,1,1,1,1,1,0,0],
        [0,1,1,1,0,0,1,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,1,0,0,1,1,1,0],
        [0,0,1,1,1,1,1,1,0,0],
        [0,0,0,1,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
],
	'P': [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,0,0,0],
        [0,1,1,1,1,1,1,1,0,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,0,0],
        [0,1,1,0,0,0,0,0,0,0],
        [0,1,1,0,0,0,0,0,0,0],
        [0,1,1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0], 
],
	'Q': [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,1,1,1,0,0,0],
        [0,0,1,1,1,1,1,1,0,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,1,1,0,0,1,1,0],
        [0,0,1,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,1,1,0],
        [0,0,0,0,0,0,0,0,0,0],
],
	'R': [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,1,1,1,1,1,0,0],
        [0,1,1,1,1,1,1,0,0,0],
        [0,1,1,0,0,1,1,0,0,0],
        [0,1,1,0,0,0,1,1,0,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,0,0,0,0,0,0,0,0,0],
],
    'S': [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,0,0],
        [0,0,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0],
],
	'T': [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
], 
	'U': [
        [0,0,0,0,0,0,0,0,0,0],
	    [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,0,1,1,1,1,1,1,0,0],
        [0,0,0,1,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
], 
	'V': [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,0,1,1,1,1,1,1,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
],
	'W': [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,1,1,0,1,1,0],
        [0,1,1,0,1,1,0,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,0,1,1,0,0,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0],
],
	'X': [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,0,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,0,1,1,0,0,1,1,0,0],
        [0,0,0,1,1,1,1,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,1,1,1,1,0,0,0],
        [0,0,1,1,0,0,1,1,0,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,0,0,0,0,0,0,0,0,0],
],
    'Y': [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,0,1,1,1,1,1,1,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
],
	'Z': [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,1,1,0,0],
        [0,0,0,0,0,1,1,0,0,0],
        [0,0,0,1,1,1,0,0,0,0],
        [0,0,1,1,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0],
],
}

def colors(color):
    #remove any white space
    color = color.strip()
    #color = color.replace(" ", "")
    #lowercase
    color = color.lower()
    
    #assign code for given color
    if color == "black":
        code = '\033[30m'
    elif color == "red":
        code = '\033[31m'
    elif color == "green":
        code = '\033[32m'
    elif color == "yellow":
        code  = '\033[33m'
    elif color == "blue":
        code  = '\033[34m'
    elif color == "magenta":
        code  = '\033[35m'
    elif color == "cyan":
        code  = '\033[36m'
    elif color == "light gray":
        code  = '\033[37m'
    elif color == "dark gray":
        code  = '\033[90m'
    elif color == "bright red":
        code = '\033[91m'
    elif color == "bright green":
        code = '\033[92m'
    elif color == "bright yellow":
        code = '\033[93m'
    elif color == "bright blue":
        code = '\033[94m'
    elif color == "brightmagenta":
        code = '\033[95m'
    elif color == "bright cyan":
        code = '\033[96m'  
    elif color == "white":
        code = '\033[97m'
    else: #throws error if color isn't available
        raise Exception(f"Can't make that color yet")
    return code

def print_instructions(project, output, row_counts=None):
    #instructions before starting
    print("Single crochet stitches are represented by its symbol x")
    print("Tapestry rows alternate from right to left, left to right, etc.")
    
    if project == "word":
        print("Instructions start at the bottom and end at the top")
    print("\n")
    print(f"Tapestry Length: {(output[0].count("x"))} stitches")
    print(f"Rows: {len(output)}")
    
    for row in output:
        print(row)
    if project == "word":
        rows = len(output)
        j = 0
        for i in range(rows,0,-1):
            print(f"\033[31mrow:{i}\033[0m")
            if i == 1:
                print(f"To start first chain the length!")
            print(row_counts[j])
            j += 1
    print("\n")
    return None

def word_tapestry(word, style = "x", color1 = "black", color2 = "white"):
    #color codes
    color1_code = colors(color1) 
    color2_code = colors(color2)
    
    #make word upper case and remove leading/trailing whitespace
    word = word.strip()
    word = word.upper()
    #remove any whitespace in between for multiple words
    word = word.replace(" ","")
    
    #number of rows from a grid
    rows = len(next(iter(LETTERS.values())))
    
    result = ['' for _ in range(rows)]
    row_counts = ['' for _ in range(rows)]
    
    #iterates through each character in the word
    for char in word: 
        #raise error for non letters
        if char not in LETTERS:
            raise Exception(f"must be a letter")
        
        #letter grid for character 
        grid = LETTERS[char]
        
        for i in range(rows):
            line = ''
            line_counts = ''
            
            #used to keep track of counts for both colors
            count_1 = 0
            count_2 = 0
            
            for bit in grid[i]:
                #assigns main colors when bit is 1
                if bit == 1:
                    if count_2 != 0:
                        line_counts += f"{color2}{count_2},"
                        count_2 = 0
                    count_1 += 1
                    line += f"{color1_code}{style}"
                #background colors
                else:
                    if count_1 != 0:
                        line_counts += f"{color1}{count_1},"
                        count_1 = 0
                    count_2 += 1
                    line += f"{color2_code}{style}"
            #prints last counts that didn't print in for loop
            if count_1 != 0:
                line_counts += f"{color1}{count_1},"
            elif count_2 != 0:
                line_counts += f"{color2}{count_2},"
            
            #stores result and row counts
            result[i] += line
            row_counts[i] += line_counts
            
    return result, row_counts

def object_tapestry(word, style = "x", main_color = "black", main_color2 = "white"):
    #make word upper case and remove whitespace
    word = word.strip()
    word = word.upper()
    #assign codes for main colors 
    color1_code = colors(main_color) 
    color2_code = colors(main_color2)
    
    #colors used for objects 
    yellow = '\033[33m'
    red = '\033[31m'
    green = '\033[32m'
    bright_green = '\033[92m'
    white = '\033[97m'
    black = '\033[30m'
    reset = '\033[0m]'
    
    #number of rows from object grid
    rows = len(OBJECTS[word])
    result = ['' for _ in range(rows)]
    
    #assign grid based on object
    grid = OBJECTS[word]
    
    #create tapestry
    if word == "FLOWER":
        for i in range(rows):
            line = ''
            for num in grid[i]:
                #assign stitch colors based on numbers in grid
                if num == 0:
                    line += f"{white}{style}"
                elif num == 1:
                    line += f"{color2_code}{style}"
                elif num == 2:
                    line += f"{color1_code}{style}"
                elif num == 3:
                    line += f"{yellow}{style}"
                elif num == 4:
                    line += f"{red}{style}"
                elif num == 5:
                    line += f"{green}{style}"
                elif num == 6:
                    line += f"{bright_green}{style}"
            result[i] += line 
    elif word == "BOW":
        for i in range(rows):
            line = ''
            for num in grid[i]:
                if num == 0:
                    line += f"{white}{style}"
                elif num == 1:
                    line += f"{color2_code}{style}"
                elif num == 2:
                    line += f"{color1_code}{style}"
            result[i] += line
    elif word == "STAR":
        for i in range(rows):
            line = ''
            for num in grid[i]:
                if num == 0:
                    line += f"{white}{style}"
                elif num == 1:
                    line += f"{color1_code}{style}"
                elif num == 2:
                    line += f"{color2_code}{style}"
            result[i] += line
    elif word == "BUTTERFLY":
        for i in range(rows):
            line = ''
            for num in grid[i]:
                if num == 0:
                    line += f"{white}{style}"
                elif num == 1:
                    line += f"{black}{style}"
                elif num == 2:
                    line += f"{color1_code}{style}"
                elif num == 3:
                    line += f"{color2_code}{style}"
            result[i] += line
    
    return result

#default 1-100 if numbers not given
def FizzBuzz(num_1=1, num_2=100):
    for i in range(num_1, num_2+1):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    return None

def tokenize(expr):
    token_pattern = r'[a-zA-Z_][a-zA-z0-9_]*|\d+|[+*/()%\-]'
    tokens = re.findall(token_pattern, expr)
    return tokens

def precedence(output, op):
    #give lower precedence to add or subtract
    if op == '+' or op == '-':
        return 1
    #give higher precedence to mult, div, modulo
    elif op == '*' or op == '/' or op == '%':
        return 2
    else:
        return 0
                      
def eval_expr(expr):
        
    #stack for evaluating expression
    output = []
    operators = []
    tokens = tokenize(expr)
    ops = set(['+', '-', '*', '/', '%'])
    
    def op_application():
        if len(output) < 2:
            raise Exception("Invalid expression")
        #pop second operand
        op2 = output.pop()
        #pop first operand
        op1 = output.pop()
        #gets operator
        op = operators.pop()
            
        #do operation based on sign
        if op == '+':
            output.append(op1 + op2)
        elif op == '-': 
            output.append(op1 - op2)
        elif op == '*':
            output.append(op1 * op2)
        elif op == '/':
            output.append(op1 / op2)
        elif op == '%':
            output.append(op1 % op2)

    #if only number return number
    if expr.isdigit():
        return int(expr)
    #if variable return number stored in variable
    if expr in s:
        return s[expr]    

    
    for token in tokens:
        #check if number
        if token.isdigit():
            output.append(float(token))
        #check if token is variable
        elif token in s:
            output.append((s[token]))
        #token is an operation symbol
        elif token in ops:
            while(operators and operators[-1] != '(' and
                precedence([], operators[-1]) >= precedence([], token)):
                op_application()
            operators.append(token)
        elif token == '(':
            operators.append(token)
        #does calculations in parentheses 
        elif token == ')':
            while operators and operators[-1] != '(':
                op_application()
            if operators:
                operators.pop()
        else:
            raise Exception(f"Invalid token: {token}")
    
    while operators:
        op_application()
    
    #return final value
    if len(output) == 1:
        return output[0]
    else:
        raise Exception("Invalid expression")
    
def varmap(var, s):
    return s[var]

def wordmap(word, w):
    return w[word]

def eval_var(var, s):
    if var in s:
        return varmap(var, s)
    else:
        raise Exception(f"Variable '{var}' not defined")
    
def main():
    #read file from arguments 
    arg_file = sys.argv[1]
    #open file and read lines
    file = open(arg_file)
    lines = file.readlines()
    word = ""
    rules = []
    project = ""
    
    #parser
    for line in lines:
        if line.startswith("make:"):
            line = line.strip()
            try:  
                make, project = line.split(':')
                line = line.replace(f"make:{project}", (f"Let's make a{project}!"))
                print(line)   
            except:
                raise Exception(f"need a project to make")
        #extract word 
        elif line.startswith("word:"):
            try:
                line = line.strip()
                _, word_phrase = line.split("word:")
                project = "word"
            except:
                raise Exception(f"need a word")
        #if not word then extract object 
        elif line.startswith("object:"):
            try:
                line = line.strip()
                _, obj_phrase = line.split("object:")
                project = "object"
            except:
                raise Exception(f"error")
        #extract colors if given
        elif line.startswith("colors:"):
            line = line.strip()
            _, call = line.split("colors:") 
            if ',' in line:
                color1, color2 = call.split(",")
                if project == "word":
                    output, instructions = word_tapestry(word=word_phrase, color1 =color1, color2=color2)
                    print_instructions(project, output, instructions)
                elif project == "object":
                    output = object_tapestry(word=obj_phrase, main_color=color1, main_color2=color2)
                    print_instructions(project, output)
            #assume no colors are given
            else:
                if project == "word":
                    output, instructions = word_tapestry(word=word_phrase)
                    print_instructions(project, output, instructions)
                elif project == "object":
                    output = object_tapestry(word=obj_phrase)
                    print_instructions(project, output)
    
        elif line.startswith("print("):
            _, call = line.split("print(")
            val, _ = call.split(")")
            if val.startswith('"'): # print string
                mystr = val.split('"')[1]
                print(mystr)
            elif val.isdigit():
                print(val)
            else: # identifier
                print(eval_var(val, s))
        elif line.startswith("FizzBuzz:"):
            line.strip()
            if ',' in line:
                _, call = line.split("FizzBuzz:")
                call.strip()
                num_1, num_2 = call.split(",")
                FizzBuzz(int(num_1), int(num_2))
            #assume user gives no values and use default 1-100 
            else:
                FizzBuzz()
        elif '=' in line: # assume variable
            line = line.strip()
            try:
                var, expr = line.split('=')
                s[var] = eval_expr(expr)
            except:
                raise Exception(f"error")
        else:
            raise Exception(f"Invalid Statement")

if __name__ == "__main__":
    main()