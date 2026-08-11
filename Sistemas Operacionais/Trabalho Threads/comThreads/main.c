#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

/* Aluna: Maria Rita Campana Peixoto
Código com Threads */

// THREAD 1 → leitura + processamento (dobro)
void* lerEDobro(void* arg){
    int numero;

    // Solicita ao usuário que digite um número
    printf("Digite um numero: \n");
    scanf("%d", &numero);

    // Calcula e imprime o dobro do número digitado
    printf("Dobro: %d\n", numero * 2);

    return NULL; // Finaliza a thread
}

// THREAD 2 → processamento fixo (decrescente)
void* contarDecrescente(void* arg){
    printf("Contagem decrescente iniciando\n");

    // Loop que faz uma contagem de 100000 até 1
    for(int i = 100000; i >= 1; i--){
        // usleep(100000); poderia ser usado para atrasar a execução
    }

    // Indica que a contagem terminou
    printf("Contagem decrescente concluida\n");

    return NULL; // Finaliza a thread
}

int main(){

    pthread_t t1, t2; // Declara duas variáveis para armazenar as threads

    printf("Execucao:\n\n");

    // Cria a thread t1 que executa a função lerEDobro
    pthread_create(&t1, NULL, lerEDobro, NULL);

    // Cria a thread t2 que executa a função contarDecrescente
    pthread_create(&t2, NULL, contarDecrescente, NULL);

    // Aguarda a finalização da thread t1
    pthread_join(t1, NULL);

    // Aguarda a finalização da thread t2
    pthread_join(t2, NULL);

    return 0; // Finaliza o programa
}
