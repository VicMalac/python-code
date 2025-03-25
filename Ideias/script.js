document.getElementById("pedidoForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let nome = document.getElementById("nome").value;
    let tipoServico = document.getElementById("tipoServico").value;
    let descricao = document.getElementById("descricao").value;
    let dataEntrada = new Date().toLocaleDateString();
    let garantia = tipoServico === "Montagem" ? 30 : 60; // 30 dias para montagem, 
    // 90 para conserto

    let pedidoId = Math.floor(10000 + Math.random() * 90000);

    let novoPedido = {
        id: pedidoId.toString(),
        nome,
        tipo: tipoServico,
        descricao,
        status: "Em Análise",
        dataEntrada,
        garantia
    };

    // Salvar no localStorage
    let pedidos = JSON.parse(localStorage.getItem("pedidos")) || [];
    pedidos.push(novoPedido);
    localStorage.setItem("pedidos", JSON.stringify(pedidos));

    let tabela = document.getElementById("listaPedidos");
    let novaLinha = tabela.insertRow();

    novaLinha.innerHTML = `
        <td>${nome}</td>
        <td>${tipoServico}</td>
        <td>${descricao}</td>
        <td>Em Análise</td>
        <td>
            <strong>${pedidoId}</strong>
            <button onclick="atualizarStatus(this, '${pedidoId}')">Atualizar Status</button>
        </td>
    `;

    document.getElementById("pedidoForm").reset();
});

function atualizarStatus(botao, pedidoId) {
    let linha = botao.parentNode.parentNode;
    let statusCell = linha.cells[3];

    let pedidos = JSON.parse(localStorage.getItem("pedidos")) || [];
    let pedido = pedidos.find(p => p.id === pedidoId);

    if (pedido) {
        if (pedido.status === "Em Análise") {
            pedido.status = "Em Andamento";
        } else if (pedido.status === "Em Andamento") {
            pedido.status = "Concluído";
        } else {
            alert("O pedido já foi concluído.");
            return;
        }

        statusCell.innerText = pedido.status;
        localStorage.setItem("pedidos", JSON.stringify(pedidos));
    }
}
document.getElementById("folderSelect").addEventListener("change", function() {
    var selectedPage = this.value;
    if (selectedPage) {
        window.location.href = selectedPage;
    }
});
document.addEventListener("DOMContentLoaded", function () {
    carregarPedidos();
    atualizarGraficos(); // Garante que os gráficos sejam carregados ao abrir a página
});

function carregarPedidos() {
    let pedidos = JSON.parse(localStorage.getItem("pedidos")) || [];
    let tabela = document.getElementById("listaPedidos").getElementsByTagName('tbody')[0];

    tabela.innerHTML = ""; // Limpa a tabela antes de adicionar os pedidos salvos

    pedidos.forEach(pedido => {
        let novaLinha = tabela.insertRow();

        novaLinha.innerHTML = `
            <td>${pedido.nome}</td>
            <td>${pedido.tipo}</td>
            <td>${pedido.descricao}</td>
            <td>${pedido.status}</td>
            <td>
                <strong>${pedido.id}</strong>
                <button onclick="atualizarStatus(this, '${pedido.id}')">Atualizar Status</button>
                <button onclick="excluirPedido('${pedido.id}')">🗑 Excluir</button>
            </td>
        `;
    });

    atualizarGraficos(); // Atualiza os gráficos sempre que a lista de pedidos for carregada
}

function excluirPedido(pedidoId) {
    let pedidos = JSON.parse(localStorage.getItem("pedidos")) || [];

    // Filtra a lista de pedidos removendo o pedido com o ID correspondente
    pedidos = pedidos.filter(p => p.id !== pedidoId);

    // Atualiza o localStorage
    localStorage.setItem("pedidos", JSON.stringify(pedidos));

    // Recarrega a tabela e atualiza os gráficos
    carregarPedidos();
}
