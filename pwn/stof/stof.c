#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<unistd.h>

void write_note(char buff[]) {
	printf ("Enter your Notes : ");
	fflush (stdout);
	read (0, buff, 79);
	printf ("\n");
}


void read_note(char buff[])
{
	int len;
	len = strlen(buff);
	write (1, buff, len);
	printf ("\n");
}

void main()
{ 
   int option;
   char buff[50];
   printf("+++++++++++++++++ Secure Secret Notes ++++++++++++++++++++\n \n");
   printf("[1] Write ur dirty secret\n");
   printf("[2] Read  ur Notes\n");
   printf("[3] Exit \n");
   printf("\n");
   printf("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n \n");
 
  while(1)
 {
   printf("Enter your option: ");
   scanf("%d",&option);
   switch(option)
    {
        case 1:
            write_note(buff);
            break;
        case 2 :
            read_note(buff);
            break ;
        case 3 :
            printf("\n good bye ...\n");
            exit(0);
    }
  }
}
