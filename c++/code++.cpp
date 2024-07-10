#include <iostream>
// Biblioteca que tem muita coisa(principalmente Output and Input, std)
// Pre prosser - Acontece antes de tudo acontecer

namespace one
{
    // namespace são luagres onde variavis são armazenadas, podem ter nomes iguais mas com valores diferentes da função originaria
    int age = 1;
}

// Tudo é função
int helloworld()
{
    /*
std - Standart
cout - C-out, character output ou Output de Characteres
<< - Output
*/
    // BASIC
    std::cout << "hello world" << '\n';
    std::cout << "Vai se foder c++" << '\n';

    // VARIABLES
    int age = 16;                  // int - variavel de numero (4 bites)
    double pi = 3.14;              // double - variavel dos Racionais (R)
    char initial = 'H';            // char - apenas um character
    bool power = true;             // boolean - True/False (1 bit)
    std::string name = "Henrique"; // std::string - Texto

    std::cout << age << " anos" << '\n';
    std::cout << "hello " << name << '\n';

    // BASIC MATH
    const double DESCONTO = 0.10; // const - não pode ser mais modificada, "read-only"
    int price = 50;
    double finalprice = price - (price * DESCONTO);
    std::cout << finalprice << " reais" << '\n'; // 45 reais

    // NAMESPACE
    std::cout << age << '\n';      // 16
    std::cout << one::age << '\n'; // 1

    return 0; // Se coloca return 0 para saber se o codigo esta dando certo, se não estiver seria "1"
}

void basicmath(int a, int b)
{
    // a = a + b;
    // a+= 1
    // a++;

    std::cout << "adição: " << a + b << '\n';

    // a--;
    // a-=b
    // a = a - b;

    std::cout << "subtração: " << a - b << '\n';

    // a = a * b;
    // a *= b;

    std::cout << "multiplicação: " << a * b << '\n';

    // a = a / b;
    // a /= b;

    std::cout << "divisão: " << a / b << '\n';

    // int restante = a % b;

    std::cout << "Se dividirmos " << a << " por " << b << " teriamos " << a % b << " restantes" << '\n';
}

int usingthat()
{
    // Using
    using namespace one; // using namespace - coloca como padrão as variaveis do namespace one
    using std::cout;     // using std::count - coloca como padrão o std::cout, assim, podendo diminuir codigo
    using string = std::string;

    cout << age << '\n';

    string name = "Abbot";

    cout << name << '\n';

    // Type Conversion

    int totalquestao = 50;
    int certaquestao = 37;

    std::cout << totalquestao / certaquestao << '\n';

    int valororiginal = 10000;
    double juros = 0.05;
    std::cout << valororiginal + ((double)valororiginal * juros * 12) << "Valor Total com Juros" << '\n'; // 16000

    return 0;
}

int prompt()
{

    std::cout << '\n'
              << "Enter" << '\n';

    std::string prompt;
    std::getline(std::cin >> std::ws, prompt); // cin >> - character input
    // getline - aprova espaços em branco
    std::cout << "hello world " << prompt << '\n';

    int age;
    std::cout << "Quantos Anos? " << '\n';
    std::cin >> age;
    if (age < 18)
    {
        std::cout << "Menor de Idade";
    }
    else
    {
        std::cout << "Maior de Idade";
    }

    return 0;
}

int garbage()
{
    // Garbage - Feito para funções que não realmente fazem falta / tem melhores
    std::cout << "Lixo Eletronico";

    // colocar fora de garbage -

    // typedef std::string string; //typedef - faz um "tipo" de data, utilizando outros tipos, usado para encurtar codigo, melhor usar using

    return 0;
}

// void log(const char *message);

// static int multiply(int a, int b)
// {
//     log("multiply");
//     return a * b;
// }


int cherno()
{
    std::cout << std::endl << sizeof(double) << std::endl;
    std::cin.get();
}

int main()
{
    // int main() - é a função principal do codigo,é nescessaria para o codigo rodar, e é o "esqueleto" do codigo

    // helloworld();
    // basicmath(10, 2);
    // usingthat();
    // prompt();
    cherno();
}