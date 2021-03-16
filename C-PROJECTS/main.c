/*
  <--------project-1------------>
  <--------NUMBER GUESSING GAME!!!!------------>
*/

/*
 DESCRIPTION :   write a pgm that generates random number and asks the player guess it
*/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main()
{
     int number , guess , n_guesses=1;
     srand(time(0));
     number = random()%100 + 1; // Generates a random number b/w 1 and 100
    //  printf("The number is %d \n", number);
     // keep running the loop until number is guessed
     do
     {
         printf("Guess the number between 1 to 100\n");
         scanf("%d",&guess);
         if(guess>number){
             printf("Lower number please!!!!\n");
         }
         else if(guess<number){
             printf("Higher number please!!!!\n");
         }
         else{
             printf("You guessed it in %d attempts!!!\n",n_guesses);
         }
         n_guesses++;
     } while (guess!=number);
     
     return 0;
}