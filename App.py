from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

#Árbol binario
class Node:
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, product):
        new_node = Node(product)
        if self.root is None:
            self.root = new_node
        else:
            self.insert_node(self.root, new_node)

    def insert_node(self, node, new_node):
        if new_node.product['price'] < node.product['price']:
            if node.left is None:
                node.left = new_node
            else:
                self.insert_node(node.left, new_node)
        else:
            if node.right is None:
                node.right = new_node
            else:
                self.insert_node(node.right, new_node)

    def search(self, price):
        return self.search_node(self.root, price)

    def search_node(self, node, price):
        if node is None:
            return None
        if price < node.product['price']:
            return self.search_node(node.left, price)
        elif price > node.product['price']:
            return self.search_node(node.right, price)
        else:
            return node.product

    # Método para obtener productos ordenados
    def in_order_traversal(self):
        products = []
        self.in_order(self.root, products)
        return products

    def in_order(self, node, products):
        if node is not None:
            self.in_order(node.left, products)
            products.append(node.product)
            self.in_order(node.right, products)

#Crer la instancia del árbol
bst = BinarySearchTree()


#RUTAS PARA INTERACTUAR CON LA PARTE DE FRONT
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_product', methods=['POST'])
def add_product():
    product = request.json
    bst.insert(product)
    return jsonify({"message": "Product added successfully"})

@app.route('/search_product', methods=['GET'])
def search_product():
    price = float(request.args.get('price'))
    product = bst.search(price)
    if product:
        return jsonify(product)
    else:
        return jsonify({"message": "Product not found"}), 404

# Nueva ruta para productos ordenados
@app.route('/products_sorted', methods=['GET'])
def products_sorted():
    sorted_products = bst.in_order_traversal()
    return jsonify(sorted_products)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
