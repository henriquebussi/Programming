#include <iostream>
// Biblioteca que tem muita coisa(principalmente Output and Input, std)


namespace one{ 
    // namespace são luagres onde variavis são armazenadas, podem ter nomes iguais mas com valores diferentes da função originaria
    int age = 1;
}

int helloworld(){
        /*
    std - Standart
    cout - C-out, character output ou Output de Characteres
    << - Output
    */
//BASIC   
    std::cout << "hello world" << '\n';
    std::cout << "Vai se foder c++" << '\n';

//VARIABLES
    int age = 16; // int - variavel de inteiros (Z)
    double pi = 3.14; // double - variavel dos Racionais (R)
    char initial = 'H'; // char - apenas um character
    bool power = true; // boolean - True/False
    std::string name = "Henrique"; // std::string - Texto 

    std::cout << age << " anos" << '\n'; 
    std::cout << "hello " << name << '\n';

// MATH
    const double DESCONTO = 0.10; // const - não pode ser mais modificada, "read-only"
    double price = 50;
    double finalprice = price-price*DESCONTO;

    std::cout << finalprice << " reais" << '\n';

//NAMESPACE
    std::cout << age << '\n'; // 16
    std::cout << one::age << '\n'; // 1

    return 0; // Se coloca return 0 para saber se o codigo esta dando certo, se não estiver seria "1"
}


int garbage(){
    // Garbage - Feito para funções que não realmente fazem falta / tem melhores
    std::cout << "Lixo Eletronico";

    // colocar forac de garbage - 

    // typedef std::string string; //typedef - faz um "tipo" de data, utilizando outros tipos, usado para encurtar codigo, melhor usar using

    return 0;

}

int teste(){
    using namespace one; // using namespace - coloca como padrão as variaveis do namespace one
    using std::cout; // using std::count - coloca como padrão o std::cout, assim, podendo diminuir codigo
    using string = std::string;

    cout << age << '\n'; 

    string name = "Abbot";

    cout << name << '\n';

    return 0;
}

// int main() - é a função principal do codigo,é nescessaria para o codigo rodar, e é o "esqueleto" do codigo
int main(){
    // helloworld();
    teste();

}