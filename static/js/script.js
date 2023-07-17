const addItemBtn = document.querySelector('#add-item')
const submitBtn = document.querySelector('#submit')
const closeBtn = document.querySelector('#close')
const exibirBtn = document.querySelector('#exibir') 

const form = document.querySelector('form')
const addItemText = document.querySelector('p')
const inputs = [...document.querySelectorAll('input[type="text"]')]
const table = document.querySelector('table')
const tableBody = document.querySelector('tbody')
const tableHead = document.querySelector('thead')

addItemBtn.addEventListener('click', () => {
    form.style.display = 'flex'
    addItemText.style.display = 'none'
})

closeBtn.addEventListener('click', () => {
    form.style.display = 'none'
    addItemText.style.display = 'block'

    form.reset()
    }
)

submitBtn.addEventListener('click', (e) => {
    form.submit()
    e.preventDefault()
})

exibirBtn.addEventListener('click', () => {
    if (table.style.display != 'none') {
        table.style.display = 'none'
        exibirBtn.innerHTML = 'Exibir Músicas'
    } else if (table.style.display == 'none'){
        table.style.display = 'block'
        exibirBtn.innerHTML = 'Esconder Músicas'
    }
})