#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(){
    pid_t pid;
    int i;
    pid = fork();

    if(pid < 0){
        fprintf(stderr, "falhou\n");
    }else if(pid == 0){
        for(i = 0; i < 5; i++){
            printf("%d\n", i);
        }

        exit(0);
        }else{
            wait(NULL);
            printf("\n");
            printf("Eu sou seu paii!");
        }
            return 0;

    }
