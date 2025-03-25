// Função para atualizar os gráficos
function atualizarGraficos() {
    let pedidos = JSON.parse(localStorage.getItem("pedidos")) || [];

    let statusCounts = { "Em Análise": 0, "Em Andamento": 0, "Concluído": 0 };
    let tipoCounts = { "Montagem": 0, "Conserto": 0, "Upgrade": 0 };

    pedidos.forEach(pedido => {
        statusCounts[pedido.status]++;
        tipoCounts[pedido.tipo]++;
    });

    // Criar gráfico de status dos pedidos
    new Chart(document.getElementById("graficoStatus"), {
        type: "pie",
        data: {
            labels: ["Em Análise", "Em Andamento", "Concluído"],
            datasets: [{
                data: Object.values(statusCounts),
                backgroundColor: ["#f39c12", "#3498db", "#2ecc71"]
            }]
        }
    });

    // Criar gráfico de tipo de serviço
    new Chart(document.getElementById("graficoTipoServico"), {
        type: "bar",
        data: {
            labels: ["Montagem", "Conserto", "Upgrade"],
            datasets: [{
                data: Object.values(tipoCounts),
                backgroundColor: ["#9b59b6", "#e74c3c", "#2ecc71"]
            }]
        },
        options: {
            scales: { y: { beginAtZero: true } }
        }
    });
}

