from typing import Optional

class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

def binary_search_tree(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    """
    Realiza uma busca binária em uma árvore binária para encontrar o nó que contém o valor alvo.

    :param root: A raiz da árvore binária.
    :param target: O valor a ser buscado na árvore.
    :return: O nó que contém o valor, ou None se o valor não for encontrado.
    """
    if root is None:
        return None

    if root.value == target:
        return root
    elif target < root.value:
        return binary_search_tree(root.left, target)
    else:
        return binary_search_tree(root.right, target)

def insert(root: Optional[TreeNode], value: int) -> TreeNode:
    """
    Insere um valor na árvore binária.

    :param root: A raiz da árvore binária.
    :param value: O valor a ser inserido.
    :return: A raiz da árvore binária após a inserção.
    """
    if root is None:
        return TreeNode(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root

def main() -> None:
    """
    Função principal para testar a busca binária em uma árvore binária.
    """
    try:
        # Criando a árvore binária
        root = None
        values = [7, 3, 10, 1, 5, 9, 12]
        
        for value in values:
            root = insert(root, value)

        # Realizando a busca binária
        target = 9
        result = binary_search_tree(root, target)
        
        if result is not None:
            print(f"Elemento {result.value} encontrado na árvore.")
        else:
            print("Elemento não encontrado.")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
