#include <stdio.h>
#include <unistd.h>

int main(){

    int meuDado;

    printf("PID do processo: %d\n", getpid());
    printf("Endereco virtual: %p\n", (void*)&meuDado);

    printf("Digite um numero para este processo: ");
    scanf("%d", &meuDado);

    printf("Valor guardado: %d\n", meuDado);
    printf("Pressione Ctrl+C para fechar.\n");

    while(1){
        sleep(1);
    }

    return 0;

}
