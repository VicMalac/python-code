function consultarPedido() {
    let pedidoId = document.getElementById("pedidoId").value;
    let pedidos = JSON.parse(localStorage.getItem("pedidos")) || [];
    let pedido = pedidos.find(p => p.id === pedidoId);

    if (pedido) {
        let dataEntrada = new Date(pedido.dataEntrada);
        let dataExpiracao = new Date(dataEntrada);
        dataExpiracao.setDate(dataExpiracao.getDate() + parseInt(pedido.garantia));

        let detalhes = `
            <p><strong>Nome:</strong> ${pedido.nome}</p>
            <p><strong>Tipo de Serviço:</strong> ${pedido.tipo}</p>
            <p><strong>Descrição:</strong> ${pedido.descricao}</p>
            <p><strong>Status:</strong> ${pedido.status}</p>
            <p><strong>Data de Entrada:</strong> ${pedido.dataEntrada}</p>
            <p><strong>Garantia:</strong> ${pedido.garantia} dias (Expira em ${dataExpiracao.toLocaleDateString()})</p>
        `;

        document.getElementById("detalhesPedido").innerHTML = detalhes;
    } else {
        document.getElementById("detalhesPedido").innerHTML = "<p>Pedido não encontrado.</p>";
    }
}
document.getElementById("folderSelect").addEventListener("change", function() {
    var selectedPage = this.value;
    if (selectedPage) {
        window.location.href = selectedPage;
    }
});