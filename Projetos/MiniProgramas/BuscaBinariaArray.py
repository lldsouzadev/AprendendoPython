from typing import List, Optional

def binary_search(arr: List[int], target: int) -> Optional[int]:
    """
    Realiza uma busca binária em uma lista ordenada para encontrar o índice de um elemento.

    :param arr: Lista de inteiros ordenada.
    :param target: O valor a ser buscado na lista.
    :return: O índice do elemento se encontrado, caso contrário None.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

def main() -> None:
    """
    Função principal para testar a busca binária.
    """
    try:
        arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        target = 19
        result = binary_search(arr, target)
        
        if result is not None:
            print(f"Elemento encontrado no índice {result}.")
        else:
            print("Elemento não encontrado.")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
