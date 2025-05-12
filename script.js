document.getElementById('formAgendamento').addEventListener('submit', function (e) {
  e.preventDefault();

  const agendamento = {
    cliente: document.getElementById('cliente').value,
    data: document.getElementById('data').value,
    hora: document.getElementById('hora').value,
    servico: document.getElementById('servico').value,
    cor1: document.getElementById('cor1').value,
    cor2: document.getElementById('cor2').value,
    valor: document.getElementById('valor').value,
    pagamento: document.getElementById('pagamento').value,
    status: document.getElementById('status').value,
    obs: document.getElementById('obs').value
  };

  const agendamentos = JSON.parse(localStorage.getItem('agendamentos') || '[]');
  agendamentos.push(agendamento);
  localStorage.setItem('agendamentos', JSON.stringify(agendamentos));

  this.reset();
  mostrarTela('agenda');
  carregarAgenda();
});

function carregarAgenda() {
  const lista = document.getElementById('listaAgenda');
  lista.innerHTML = '';
  const agendamentos = JSON.parse(localStorage.getItem('agendamentos') || '[]');
  const hoje = new Date().toISOString().split('T')[0];

  agendamentos
    .filter(a => a.data === hoje)
    .sort((a, b) => a.hora.localeCompare(b.hora))
    .forEach(a => {
      const card = document.createElement('div');
      card.className = 'card-agendamento';
      card.innerHTML = `
        <strong>${a.hora} - ${a.cliente}</strong><br>
        Serviço: ${a.servico}<br>
        Valor: R$ ${a.valor} | ${a.pagamento}<br>
        Status: ${a.status}<br>
        Cores: <span style="background:${a.cor1};width:15px;height:15px;display:inline-block;border:1px solid #000;"></span>
               <span style="background:${a.cor2};width:15px;height:15px;display:inline-block;border:1px solid #000;"></span><br>
        Obs: ${a.obs}
      `;
      lista.appendChild(card);
    });
}

function carregarClientes() {
  const lista = document.getElementById('listaClientes');
  lista.innerHTML = '';
  const agendamentos = JSON.parse(localStorage.getItem('agendamentos') || '[]');
  const agrupado = {};

  agendamentos.forEach(a => {
    if (!agrupado[a.cliente]) agrupado[a.cliente] = [];
    agrupado[a.cliente].push(a);
  });

  Object.entries(agrupado).forEach(([cliente, registros]) => {
    const card = document.createElement('div');
    card.className = 'card-agendamento';
    card.innerHTML = `
      <strong>${cliente}</strong><br>
      Total de agendamentos: ${registros.length}<br>
      Último serviço: ${registros[registros.length - 1].servico}<br>
      Total gasto: R$ ${registros.reduce((s, r) => s + parseFloat(r.valor || 0), 0).toFixed(2)}
    `;
    lista.appendChild(card);
  });
}

function mostrarTela(tela) {
  document.getElementById('tela-agenda').style.display = 'none';
  document.getElementById('tela-novo').style.display = 'none';
  document.getElementById('tela-clientes').style.display = 'none';

  if (tela === 'agenda') carregarAgenda();
  if (tela === 'clientes') carregarClientes();

  document.getElementById('tela-' + tela).style.display = 'block';

  document.querySelectorAll('.nav-link').forEach(link => link.classList.remove('active'));
  document.querySelectorAll('.nav-link').forEach(link => {
    if (link.textContent.toLowerCase().includes(tela)) link.classList.add('active');
  });
}

window.onload = () => {
  mostrarTela('agenda');
};
