# CheckPoint 1 - Dynamic Programming
Aluno: Lucca  
RM: 560731  

---

## Resumo do Trabalho

Este projeto implementa algoritmos de ordenação com foco em **Merge Sort** e **Quick Sort**, aplicados em dois contextos:

1. **Ordenação de pontos pela distância de Manhattan**  
   - Os pontos foram armazenados em uma **tupla** (estrutura imutável).  
   - Um **dicionário** foi usado para mapear cada ponto à sua distância calculada.  
   - A ordenação foi feita de forma **recursiva**, implementando tanto o **Merge Sort** quanto o **Quick Sort**.  
   - Também foi utilizada **list comprehension** para reestruturar os dados (ex.: gerar lista de `(ponto, distância)`).

2. **Ordenação de palavras por prioridade de caracteres**  
   - Foi fornecido um dicionário de prioridades (`'a':1, 'b':2, ...`).  
   - Cada palavra foi convertida em um **vetor de prioridades** para permitir comparação.  
   - **Hipótese adotada**: normalização de acentos (ex.: "melaço" → "melaco") para que as letras se encaixassem no dicionário.  
   - Implementação recursiva de **Merge Sort** e **Quick Sort** aplicada às palavras.

3. **Comparação de desempenho (análise conceitual)**  
   - **Merge Sort**: sempre `O(n log n)` no pior caso, **estável**, mas usa mais memória por criar listas auxiliares.  
   - **Quick Sort**: na média também `O(n log n)`, porém no **pior caso pode ser O(n²)**. Em listas pequenas (como as do exercício), a diferença prática de tempo/memória é mínima.  
   - Conclusão: **Merge Sort é previsível e estável**, enquanto **Quick Sort é mais rápido em média**, mas arriscado em casos desfavoráveis.

---

## Conclusões Gerais

- A ordenação de pontos mostrou como aplicar funções matemáticas simples (distância de Manhattan) dentro de algoritmos recursivos.  
- A ordenação de palavras destacou a importância de **transformar dados em vetores comparáveis** para seguir uma lógica personalizada.  
- O uso de **list comprehension** e **dicionários** foi essencial para tornar o código mais limpo e eficiente.  
- As comparações entre Merge e Quick demonstram como **diferentes algoritmos resolvem o mesmo problema de formas distintas**, cada um com suas vantagens e limitações.  
