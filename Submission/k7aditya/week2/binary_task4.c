#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void print_flag() {
   printf("Flag: opencode{l34rn_buff3r_0ve3rf10w}\n");
}

void vulnerable_function(char *input) {
 char buffer[10];
 strcpy(buffer, input);
 
 // Check if the buffer overflow has occurred
 if (strlen(buffer) > sizeof(buffer)) {
   print_flag();
 } else {
   printf("You entered: %s\n", buffer);
 }
}

int main() {
 char input[100];
scanf("%s", input);
 vulnerable_function(input);
 return 0;
} 
