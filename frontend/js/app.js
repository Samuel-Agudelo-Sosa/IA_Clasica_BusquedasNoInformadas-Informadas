// Detectar cambios en el selector de algoritmos para mostrar parámestros extra

document.getElementById("algoSelect").addEventListener('change', function(e){
    const extraParams = document.getElementById('extraParams');
    if (e.target.value == 'DLS'){
        extraParams.style.display = 'block';
    }
    else {
        extraParams.style.display = 'none';
    }

});

// Intercepción envío formulario

document.getElementById('searchForm').addEventListener('submit', async function(e) {

        e.preventDefault(); // evita que la página recargue

        // Recolección datos del formulario
        const payload = {
            problem: document.getElementById('problemSelect').value,
            algorithm: document.getElementById('algoSelect').value,
            control: parseInt(document.getElementById('controlSelect').value),
            limit: parseInt(document.getElementById('depthLimit').value)
        };

        const resultsArea = document.getElementById('resultsArea');
        resultsArea.innerHTML = `<div class="spinner-border text-primary" role="status"><span class="visually-hidden">Cargando...</span></div>`;

        // 2. Aquí haremos el fetch() a FastAPI más adelante
        console.log("Enviando a FastAPI:", payload);
    
        // Simulación temporal de respuesta
        setTimeout(() => {
            resultsArea.innerHTML = `
                <div class="alert alert-success text-start w-100">
                    <h4 class="alert-heading">¡Solución Encontrada!</h4>
                    <p><strong>Nodos Evaluados:</strong> 150</p>
                    <p><strong>Costo Total:</strong> 11</p>
                    <hr>
                    <p class="mb-0">Aquí renderizaremos el camino paso a paso.</p>
                </div>
            `;
        }, 1000);

});