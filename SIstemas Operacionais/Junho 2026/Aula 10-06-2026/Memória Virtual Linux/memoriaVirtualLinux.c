#include <stdio.h>
#include <stdint.h>
#include <unistd.h>

int main(){

    int minhaVariavel = 12345;
    uintptr_t enderecoVirtual = (uintptr_t)&minhaVariavel;

    printf("[INFO] ID do Processo (PID): %d\n", getpid());
    printf("[1] Endereco VIRTUAL da variavel (A ilusao): 0x%lx\n", enderecoVirtual);
    printf("    Valor guardado nela: %d\n\n", minhaVariavel);
    printf("[TENTATIVA] Tentando ler o arquivo /proc/self/pagemap...\n");

    //Tentando abrir o arquivo de paginação física do próprio processo
    FILE *pagemap = fopen("/proc/self/pagemap", "rb");

    if(pagemap == NULL){
        printf("❌ ERRO: Permissao Negada! Voce e um usuario comum."
               "O SO te barrou.\n");
        printf("Abstracao de memoria ativa e protegendo o hardware!\n");
        return 1;
    }

    //Código de tradução (Apenas executado se for Root)
    //Calcula o deslocamento dentro do arquivo pagemap
    uint64_t informacaoPagina;
    unsigned long tamanhoPagina = sysconf(_SC_PAGESIZE);
    unsigned long indicePagina = enderecoVirtual / tamanhoPagina;

    fseek(pagemap, indicePagina * sizeof(uint64_t), SEEK_SET);
    fread(&informacaoPagina, sizeof(uint64_t), 1, pagemap);
    fclose(pagemap);

    //Verifica se a página está presente na RAM física
    if(informacaoPagina & (1ULL << 63)){

        //Extrai o PFN (Page Frame Number) - bits 0 a 54
        uint64_t pfn =
            informacaoPagina & 0x7FFFFFFFFFFFFF00ULL;

        uintptr_t enderecoFisico =
            pfn + (enderecoVirtual % tamanhoPagina);

        printf("🔓 SUCESSO: Voce burlou a barreira como ROOT!\n");
        printf("[2] Endereco FISICO real na memoria RAM: 0x%lx\n", enderecoFisico);
    }else{
        printf("⚠️ A pagina de memoria foi movida para o Swap (Disco/SSD)!\n");
    }

    return 0;

}
