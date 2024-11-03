// Función para agregar producto
async function addProduct() {
    const name = document.getElementById("name").value;
    const price = parseFloat(document.getElementById("price").value);
    
    const product = { name, price };
    
    const response = await fetch('/add_product', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(product)
    });
    
    const data = await response.json();
    alert(data.message);
}

// Función para buscar producto
async function searchProduct() {
    const price = parseFloat(document.getElementById("searchPrice").value);
    const response = await fetch(`/search_product?price=${price}`);
    
    if (response.ok) {
        const product = await response.json();
        document.getElementById("result").innerText = `Producto encontrado: ${product.name} - $${product.price}`;
    } else {
        const data = await response.json();
        document.getElementById("result").innerText = data.message;
    }
}

async function getSortedProducts() {
    const response = await fetch('/products_sorted');
    const products = await response.json();
    let resultText = 'Productos ordenados por precio:\n';
    products.forEach(product => {
        resultText += `${product.name} - $${product.price}\n`;
    });
    document.getElementById("result").innerText = resultText;
}
