const API_BASE_URL = "http://127.0.0.1:8000";




// Mostrar/Ocultar campo de profundidad para DLS

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

        const resultsArea = document.getElementById('resultsArea');

        // 1. Mostrar estado de carga (Spinner)
        resultsArea.innerHTML = `
        <div class="text-center py-5">
            <div class="spinner-border text-primary mb-2" role="status"></div>
            <p class="text-muted mb-0">Ejecutando algoritmo de búsqueda...</p>
        </div>
        `;

        //  construir objeto JSON para pydantic (SearchRequest)
        const payload = {
            problem: document.getElementById('problemSelect').value,
            algorithm: document.getElementById('algoSelect').value,
            control: parseInt(document.getElementById('controlSelect').value),
            limit: parseInt(document.getElementById('depthLimit').value)
        };
        
        try {
            const response = await fetch(`${API_BASE_URL}/search`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || "Error en la búsqueda");

            }

            const data = await response.json();

            if (data.solution_found) {
            // Renderizar lista de pasos
            const stepsList = data.path.map((step, index) => 
                `<li class="list-group-item d-flex justify-content-between align-items-center">
                    <span><strong>Paso ${index + 1}:</strong> ${step}</span>
                </li>`
            ).join('');

            resultsArea.innerHTML = `
                <div class="w-100 p-3">
                    <div class="alert alert-success border-0 shadow-sm mb-3">
                        <h4 class="alert-heading fw-bold">¡Solución Encontrada!</h4>
                        <p class="mb-1">${data.message}</p>
                    </div>

                    <div class="row text-center mb-3">
                        <div class="col-4">
                            <div class="bg-light p-2 rounded border">
                                <small class="text-muted d-block">Nodos Evaluados</small>
                                <span class="fw-bold fs-5 text-primary">${data.evaluated_nodes}</span>
                            </div>
                        </div>
                        <div class="col-4">
                            <div class="bg-light p-2 rounded border">
                                <small class="text-muted d-block">Costo Total</small>
                                <span class="fw-bold fs-5 text-success">${data.path_cost}</span>
                            </div>
                        </div>
                        <div class="col-4">
                            <div class="bg-light p-2 rounded border">
                                <small class="text-muted d-block">Pasos</small>
                                <span class="fw-bold fs-5 text-dark">${data.steps}</span>
                            </div>
                        </div>
                    </div>

                    <h6 class="fw-bold mb-2">Secuencia de Acciones:</h6>
                    <ul class="list-group list-group-flush border rounded style-steps">
                        ${stepsList}
                    </ul>
                </div>
            `;
        } else {
            resultsArea.innerHTML = `
                <div class="alert alert-warning border-0 shadow-sm w-100 m-3">
                    <h5 class="fw-bold">Sin Solución</h5>
                    <p class="mb-1">${data.message}</p>
                    <small class="text-muted">Nodos evaluados antes de detenerse: ${data.evaluated_nodes}</small>
                </div>
            `;
        }

    } catch (error) {
        resultsArea.innerHTML = `
            <div class="alert alert-danger border-0 shadow-sm w-100 m-3">
                <h5 class="fw-bold">Error de Ejecución</h5>
                <p class="mb-0">${error.message}</p>
            </div>
        `;
    }

});