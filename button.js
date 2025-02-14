const butao = document.querySelector('.botao');

butao.addEventListener('click', function(){
    document.body.classList.toggle("dark");
    document.body.classList.toggle("light");
});