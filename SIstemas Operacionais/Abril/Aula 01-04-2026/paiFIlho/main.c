#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

//Aluna: Maria Rita Campana Peixoto

int value = 5;

int main(){
    pid_t pid;
    pid = fork();

    if(pid == 0){ /*processo-filho*/
        value += 15;
        return 0;
    }else if (pid > 0){ /*processo-pai*/
        wait(NULL);
        printf("%d", value); /*LINHA A*/
        return 0;
    }
}
