#include <stdio.h>
#include <unistd.h>

/* Aluna: Maria Rita Campana Peixoto
Código sem Threads */

int main(){

    int numero; // Variável para armazenar o número digitado pelo usuário

    printf("Execucao:\n\n");

    // Leitura de dados (entrada do usuário)
    printf("Digite um numero: ");
    scanf("%d", &numero);

    // Processamento: cálculo do dobro do número
    printf("Dobro: %d\n\n", numero * 2);

    // Processamento fixo: contagem decrescente de 10 até 1
    for(int i = 100000; i >= 1; i--){
        printf("Decrescente: %d\n", i); // Exibe o valor atual

        usleep(100000); // Pausa de 100000 microssegundos (0,1 segundo)
    }

    return 0; // Finaliza o programa
}
