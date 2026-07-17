#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

//Aluna: Maria Rita Campana Peixoto

// O que esse código faz?


int main(){
    pid_t pid = fork(); 

    if(pid == 0){
        execlp("ls", "ls", "-l", NULL);
    }else{
        wait(NULL);
        printf("Filho terminou\n");
    }

    return 0;
}
